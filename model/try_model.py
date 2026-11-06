import math

import torch

from model.gpt import GPT, GPTConfig
from tokenizer.bpe import BPETokenizer
from training.dataset import make_loader

torch.manual_seed(0)
tok = BPETokenizer.load("tokenizer/bpe_3000.json")
cfg = GPTConfig(vocab_size=len(tok))
model = GPT(cfg)

n_params = sum(p.numel() for p in model.parameters())
print(f"parameters: {n_params:,}")

loader = make_loader("data/processed/train.pt", tok.special["<pad>"], batch_size=4, shuffle=True)
x, y = next(iter(loader))
logits, loss = model(x, y)
print("input  shape:", tuple(x.shape))
print("logits shape:", tuple(logits.shape))
print(f"loss: {loss.item():.3f}   (random guessing = ln({cfg.vocab_size}) = {math.log(cfg.vocab_size):.3f})")

loss.backward()
print("gradients computed:", model.emb.tok.weight.grad is not None)
