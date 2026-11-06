import time

import torch

from model.gpt import GPT, GPTConfig
from tokenizer.bpe import BPETokenizer
from training.dataset import IGNORE_INDEX, SpecDataset, make_collate

N_EXAMPLES = 5
STEPS = 200
LR = 3e-4

torch.manual_seed(42)
tok = BPETokenizer.load("tokenizer/bpe_3000.json")
pad_id = tok.special["<pad>"]

# One fixed batch: the first 5 training examples
dataset = SpecDataset("data/processed/train.pt")
x, y = make_collate(pad_id)([dataset[i] for i in range(N_EXAMPLES)])
print(f"batch: {tuple(x.shape)}, tokens in loss: {int((y != IGNORE_INDEX).sum())}")

model = GPT(GPTConfig(vocab_size=len(tok), dropout=0.0))
optimizer = torch.optim.AdamW(model.parameters(), lr=LR)

start = time.time()
for step in range(STEPS + 1):
    _, loss = model(x, y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    if step % 10 == 0:
        print(f"step {step:3d}   loss {loss.item():.4f}   ({time.time() - start:.0f}s)")

# Can it reproduce example 0 from its intent alone?
model.eval()
e = dataset.examples[0]
ids = e["ids"][: e["spec_start"]].tolist()  # <bos> <intent> ... <spec>
with torch.no_grad():
    while len(ids) < 512:
        logits, _ = model(torch.tensor([ids]))
        next_id = int(logits[0, -1].argmax())
        ids.append(next_id)
        if next_id == tok.special["<eos>"]:
            break

generated = tok.decode(ids[e["spec_start"]:])
expected = tok.decode(e["ids"][e["spec_start"]:].tolist())
print("\nmemorised example 0 exactly:", generated == expected)
print(generated[:300])
