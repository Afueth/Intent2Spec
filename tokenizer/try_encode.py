import json

from tokenizer.bpe import BPETokenizer

with open("data/raw/train.jsonl", encoding="utf-8") as f:
    train = [json.loads(line) for line in f if line.strip()]
text = "\n".join(p["intent"] + "\n" + p["spec"] for p in train)

tok = BPETokenizer()
tok.train(text, 3000)

# 1. Encode and decode one example
sample = "Type:       Web application"
ids = tok.encode(sample)
print(f"{sample!r}")
print(f"  ids:    {ids}")
print(f"  tokens: {[tok.decode([i]) for i in ids]}")
print(f"  decode: {tok.decode(ids)!r}")

# 2. Round trip on every pair in every split
for path in ["data/raw/train.jsonl", "data/raw/val.jsonl", "data/evaluation/test.jsonl"]:
    with open(path, encoding="utf-8") as f:
        pairs = [json.loads(line) for line in f if line.strip()]
    ok = all(tok.decode(tok.encode(p[k])) == p[k] for p in pairs for k in ("intent", "spec"))
    chars = sum(len(p["intent"]) + len(p["spec"]) for p in pairs)
    tokens = sum(len(tok.encode(p["intent"])) + len(tok.encode(p["spec"])) for p in pairs)
    print(f"{path}: round trip {'OK' if ok else 'FAILED'}, {chars / tokens:.2f} characters per token")
