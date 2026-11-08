"""Append the new draft parts (data/raw/new/part_*.md) to data/raw/draft_examples.md.

New pairs are validated, de-duplicated and checked against the test set
(pairs too similar to a test intent are dropped), then appended as
"## Example 1001", "## Example 1002", ... in the same format.

Usage:  python -m scripts.merge_new_data
"""

import glob
import json
import re

from scripts.validate_specs import validate
from tokenizer.bpe import BPETokenizer

DRAFTS = "data/raw/draft_examples.md"
TEST = "data/evaluation/test.jsonl"
MAX_TOKENS = 500  # prepare_data.py allows 512

PATTERN = re.compile(r"\*\*Intent:\*\*\s*\n(.+?)\n\s*\*\*Spec:\*\*\s*\n```\n(.+?)\n```", re.DOTALL)


def words(text):
    return frozenset(re.sub(r"\W+", " ", text.lower()).split())


def jaccard(a, b):
    return len(a & b) / max(1, len(a | b))


def main():
    tok = BPETokenizer.load("tokenizer/bpe_3000.json")

    drafts = open(DRAFTS, encoding="utf-8").read()
    existing = [(i.strip(), s.rstrip()) for i, s in PATTERN.findall(drafts)]
    with open(TEST, encoding="utf-8") as f:
        test_sets = [words(json.loads(line)["intent"]) for line in f if line.strip()]

    seen_intents = {i.lower() for i, _ in existing}
    seen_word_sets = {words(i) for i, _ in existing}

    new, dropped = [], {"invalid": 0, "too long": 0, "duplicate": 0, "near test": 0}
    for path in sorted(glob.glob("data/raw/new/part_*.md")):
        for intent, spec in PATTERN.findall(open(path, encoding="utf-8").read()):
            intent, spec = intent.strip(), spec.rstrip()
            if "\n" in intent or validate(spec):
                dropped["invalid"] += 1
                continue
            if len(tok.encode_pair(intent, spec)) > MAX_TOKENS:
                dropped["too long"] += 1
                continue
            ws = words(intent)
            if intent.lower() in seen_intents or ws in seen_word_sets:
                dropped["duplicate"] += 1
                continue
            if len(ws) >= 4 and any(jaccard(ws, t) > 0.7 for t in test_sets):
                dropped["near test"] += 1
                continue
            seen_intents.add(intent.lower())
            seen_word_sets.add(ws)
            new.append((intent, spec))

    start = len(existing) + 1
    blocks = [
        f"## Example {n}\n\n**Intent:**\n{intent}\n\n**Spec:**\n```\n{spec}\n```\n"
        for n, (intent, spec) in enumerate(new, start=start)
    ]
    with open(DRAFTS, "a", encoding="utf-8") as f:
        for block in blocks:
            f.write("\n---\n\n" + block)

    print(f"existing examples: {len(existing)}")
    print(f"new examples appended: {len(new)}  (Example {start}..{start + len(new) - 1})")
    print(f"dropped: {dropped}")
    print(f"total in {DRAFTS}: {len(existing) + len(new)}")


if __name__ == "__main__":
    main()
