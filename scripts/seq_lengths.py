import json

from tokenizer.bpe import BPETokenizer

tok = BPETokenizer.load("tokenizer/bpe_3000.json")

for path in ["data/raw/train.jsonl", "data/raw/val.jsonl", "data/evaluation/test.jsonl"]:
    with open(path, encoding="utf-8") as f:
        pairs = [json.loads(line) for line in f if line.strip()]
    lengths = sorted(len(tok.encode_pair(p["intent"], p["spec"])) for p in pairs)
    n = len(lengths)
    print(f"{path}")
    print(f"  pairs: {n}")
    print(f"  min: {lengths[0]}   median: {lengths[n // 2]}   max: {lengths[-1]}")
    print(f"  95th percentile: {lengths[int(n * 0.95)]}   99th: {lengths[int(n * 0.99)]}")
    for limit in (256, 384, 512):
        over = sum(1 for x in lengths if x > limit)
        print(f"  longer than {limit}: {over}")
