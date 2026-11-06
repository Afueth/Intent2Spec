"""Evaluate the trained model on the test set.

Usage:
    python -m scripts.evaluate              # all 100 test pairs
    python -m scripts.evaluate --limit 10   # quick run on the first 10
"""

import argparse
import json
import re
import time

import torch

from generate import generate, load
from scripts.validate_specs import FIELDS, validate
from training.dataset import make_loader
from training.train import evaluate as eval_loss

TEST_JSONL = "data/evaluation/test.jsonl"
TEST_PT = "data/processed/test.pt"
OUT_FILE = "experiements/eval_results.jsonl"

field_line = re.compile(r"^([A-Za-z][A-Za-z ]*):\s*(.*)$")


def parse_fields(spec):
    """Spec text -> {field name: [value lines]}."""
    fields, current = {}, None
    for line in spec.split("\n"):
        m = field_line.match(line)
        if m and m.group(1) in FIELDS:
            current = m.group(1)
            fields[current] = [m.group(2).strip()]
        elif current is not None and line.strip():
            fields[current].append(line.strip())
    return fields


def f1(pred, ref):
    """F1 between two sets: 2 * precision * recall / (precision + recall)."""
    if not pred and not ref:
        return 1.0
    common = len(pred & ref)
    if common == 0:
        return 0.0
    precision, recall = common / len(pred), common / len(ref)
    return 2 * precision * recall / (precision + recall)


def terms(fields):
    """Tech terms from Storage and Tech stack: 'PostgreSQL (orders), S3' -> {'postgresql', 's3'}."""
    out = set()
    for name in ("Storage", "Tech stack"):
        for part in ", ".join(fields.get(name, [])).split(","):
            part = re.sub(r"\(.*?\)", "", part).strip().lower()
            if part:
                out.add(part)
    return out


def rouge_l(pred, ref):
    """ROUGE-L F1: longest common subsequence of words."""
    a, b = pred.split(), ref.split()
    if not a or not b:
        return 0.0
    prev = [0] * (len(b) + 1)
    for x in a:
        cur = [0]
        for j, y in enumerate(b):
            cur.append(prev[j] + 1 if x == y else max(prev[j + 1], cur[j]))
        prev = cur
    lcs = prev[-1]
    if lcs == 0:
        return 0.0
    precision, recall = lcs / len(a), lcs / len(b)
    return 2 * precision * recall / (precision + recall)


def repetition(spec):
    """Share of lines that are exact repeats of an earlier line."""
    lines = [l.strip() for l in spec.split("\n") if l.strip()]
    return 1 - len(set(lines)) / len(lines) if lines else 0.0


def score(pred, ref):
    p, r = parse_fields(pred), parse_fields(ref)
    p_type = p.get("Type", [""])[0].lower()
    r_type = r.get("Type", [""])[0].lower()
    return {
        "format_ok": not validate(pred),
        # compare only the main type, before any "(...)"
        "type_ok": p_type.split("(")[0].strip() == r_type.split("(")[0].strip(),
        "fields_f1": f1(set(p), set(r)),
        "terms_f1": f1(terms(p), terms(r)),
        "rouge_l": rouge_l(pred, ref),
        "repetition": repetition(pred),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=None, help="only the first N test pairs")
    args = parser.parse_args()

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model, tok = load(device)

    # 1. Test loss: same measure as val loss during training
    loader = make_loader(TEST_PT, tok.special["<pad>"], batch_size=16, shuffle=False)
    test_loss = eval_loss(model, loader, device)
    print(f"test loss {test_loss:.4f} | perplexity {torch.tensor(test_loss).exp():.1f}")

    # 2. Generate a spec for every test intent and score it
    with open(TEST_JSONL, encoding="utf-8") as f:
        pairs = [json.loads(line) for line in f if line.strip()]
    pairs = pairs[: args.limit]

    results = []
    t0 = time.time()
    for i, pair in enumerate(pairs, start=1):
        pred = generate(model, tok, pair["intent"])  # greedy
        s = score(pred, pair["spec"])
        results.append({"intent": pair["intent"], "reference": pair["spec"],
                        "generated": pred, **s, "human": ""})
        print(f"[{i}/{len(pairs)}] format {'OK ' if s['format_ok'] else 'BAD'} | "
              f"type {'OK ' if s['type_ok'] else 'BAD'} | rouge-l {s['rouge_l']:.2f} | "
              f"{time.time() - t0:.0f}s")

    with open(OUT_FILE, "w", encoding="utf-8") as f:
        for r in results:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    # 3. Summary
    n = len(results)
    avg = lambda key: sum(r[key] for r in results) / n
    print(f"\n=== {n} test pairs ===")
    print(f"format valid   {avg('format_ok'):6.1%}   follows docs/spec_format.md")
    print(f"type correct   {avg('type_ok'):6.1%}   main Type matches the reference")
    print(f"fields F1      {avg('fields_f1'):6.3f}   right set of fields")
    print(f"terms F1       {avg('terms_f1'):6.3f}   Storage + Tech stack items")
    print(f"ROUGE-L F1     {avg('rouge_l'):6.3f}   word overlap with the reference")
    print(f"repeated lines {avg('repetition'):6.1%}   lower is better")
    print(f"saved -> {OUT_FILE}")


if __name__ == "__main__":
    main()
