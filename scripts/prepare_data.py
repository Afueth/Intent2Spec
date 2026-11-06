import json
import os

import torch

from tokenizer.bpe import BPETokenizer

TOKENIZER = "tokenizer/bpe_3000.json"
MAX_LEN = 512
OUT_DIR = "data/processed"
SPLITS = {
    "train": "data/raw/train.jsonl",
    "val": "data/raw/val.jsonl",
    "test": "data/evaluation/test.jsonl",
}

tok = BPETokenizer.load(TOKENIZER)
spec_id = tok.special["<spec>"]
os.makedirs(OUT_DIR, exist_ok=True)

for name, path in SPLITS.items():
    with open(path, encoding="utf-8") as f:
        pairs = [json.loads(line) for line in f if line.strip()]

    examples = []
    for p in pairs:
        ids = tok.encode_pair(p["intent"], p["spec"])
        assert len(ids) <= MAX_LEN, f"sequence too long ({len(ids)} tokens): {p['intent'][:50]}"
        examples.append({
            "ids": torch.tensor(ids, dtype=torch.long),
            "spec_start": ids.index(spec_id) + 1,  # first token of the spec text
        })

    out = os.path.join(OUT_DIR, f"{name}.pt")
    torch.save(examples, out)
    total = sum(len(e["ids"]) for e in examples)
    print(f"{out}: {len(examples)} sequences, {total:,} tokens")
