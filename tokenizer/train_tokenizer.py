import json
import time

from tokenizer.bpe import BPETokenizer

VOCAB_SIZE = 3000
SPECIAL_TOKENS = ["<pad>", "<bos>", "<eos>", "<intent>", "<spec>"]
OUT = "tokenizer/bpe_3000.json"

with open("data/raw/train.jsonl", encoding="utf-8") as f:
    pairs = [json.loads(line) for line in f if line.strip()]
text = "\n".join(p["intent"] + "\n" + p["spec"] for p in pairs)
print(f"training text: {len(text):,} characters from {len(pairs)} pairs")

start = time.time()
tok = BPETokenizer()
tok.train(text, VOCAB_SIZE, verbose=True)
tok.add_special_tokens(SPECIAL_TOKENS)
print(f"done in {time.time() - start:.1f}s, vocab size = {len(tok)} (incl. {len(tok.special)} special)")

tok.save(OUT)
print(f"saved to {OUT}")
