import json

from tokenizer.bpe import BPETokenizer

tok = BPETokenizer.load("tokenizer/bpe_3000.json")
print("vocab size:", len(tok))
print("special tokens:", tok.special)

with open("data/raw/train.jsonl", encoding="utf-8") as f:
    pair = json.loads(f.readline())

ids = tok.encode_pair(pair["intent"], pair["spec"])
print(f"\nfull pair: {len(ids)} tokens")
print("first 12 ids:", ids[:12])
print("decoded start:", repr(tok.decode(ids[:12])))
print("last id:", ids[-1], "=", tok.decode([ids[-1]]))

prompt = tok.encode_pair(pair["intent"])
print(f"\nprompt only (for generation): {len(prompt)} tokens, ends with {tok.decode(prompt[-1:])}")
