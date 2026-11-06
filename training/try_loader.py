import torch

from tokenizer.bpe import BPETokenizer
from training.dataset import IGNORE_INDEX, make_loader

tok = BPETokenizer.load("tokenizer/bpe_3000.json")
pad_id = tok.special["<pad>"]

torch.manual_seed(0)
loader = make_loader("data/processed/train.pt", pad_id, batch_size=4, shuffle=True)
print("batches per epoch:", len(loader))

x, y = next(iter(loader))
print("x shape:", tuple(x.shape), "  y shape:", tuple(y.shape))

# Look at the first sequence in the batch
row_x, row_y = x[0], y[0]
learned = row_y != IGNORE_INDEX
print("\nfirst sequence:")
print("  real tokens:  ", int((row_x != pad_id).sum()))
print("  padding:      ", int((row_x == pad_id).sum()))
print("  tokens in loss:", int(learned.sum()))

first = int(learned.nonzero()[0])
print("\nfirst target the model is trained on:")
print("  input so far ends with:", repr(tok.decode(row_x[first - 3 : first + 1].tolist())))
print("  target (next token):   ", repr(tok.decode([int(row_y[first])])))

last = int(learned.nonzero()[-1])
print("last target:", repr(tok.decode([int(row_y[last])])))
