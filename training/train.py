import csv
import math
import os
import time
from dataclasses import asdict

import torch

from model.gpt import GPT, GPTConfig
from tokenizer.bpe import BPETokenizer
from training.dataset import IGNORE_INDEX, make_loader

# ---- Settings ----
BATCH_SIZE = 16
EPOCHS = 20
LR = 3e-4            # peak learning rate
MIN_LR = 3e-5        # learning rate at the end
WARMUP_STEPS = 50    # steps to ramp up from 0 to LR
WEIGHT_DECAY = 0.1
GRAD_CLIP = 1.0
DROPOUT = 0.1
PATIENCE = 4         # stop if val loss has not improved for this many epochs
SEED = 42

CHECKPOINT = "checkpoints/best.pt"
LOG_FILE = "experiements/train_log.csv"


def lr_at(step, total_steps):
    """Linear warm-up, then cosine decay from LR down to MIN_LR."""
    if step < WARMUP_STEPS:
        return LR * (step + 1) / WARMUP_STEPS
    progress = (step - WARMUP_STEPS) / max(1, total_steps - WARMUP_STEPS)
    return MIN_LR + 0.5 * (LR - MIN_LR) * (1 + math.cos(math.pi * progress))


@torch.no_grad()
def evaluate(model, loader, device):
    """Average loss per spec token over a whole split."""
    model.eval()
    total_loss, total_tokens = 0.0, 0
    for x, y in loader:
        x, y = x.to(device), y.to(device)
        _, loss = model(x, y)
        n = int((y != IGNORE_INDEX).sum())
        total_loss += loss.item() * n
        total_tokens += n
    model.train()
    return total_loss / total_tokens


def main():
    torch.manual_seed(SEED)
    device = "cuda" if torch.cuda.is_available() else "cpu"

    tok = BPETokenizer.load("tokenizer/bpe_3000.json")
    pad_id = tok.special["<pad>"]
    train_loader = make_loader("data/processed/train.pt", pad_id, BATCH_SIZE, shuffle=True)
    val_loader = make_loader("data/processed/val.pt", pad_id, BATCH_SIZE, shuffle=False)

    cfg = GPTConfig(vocab_size=len(tok), dropout=DROPOUT)
    model = GPT(cfg).to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=LR, betas=(0.9, 0.95), weight_decay=WEIGHT_DECAY)

    total_steps = EPOCHS * len(train_loader)
    n_params = sum(p.numel() for p in model.parameters())
    print(f"device: {device} | parameters: {n_params:,} | {len(train_loader)} steps/epoch, {total_steps} total")

    os.makedirs(os.path.dirname(CHECKPOINT), exist_ok=True)
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "w", newline="") as f:
        csv.writer(f).writerow(["epoch", "train_loss", "val_loss", "lr", "seconds"])

    best_val = float("inf")
    epochs_without_improvement = 0
    step = 0
    start = time.time()

    for epoch in range(1, EPOCHS + 1):
        epoch_loss, epoch_tokens = 0.0, 0
        for x, y in train_loader:
            x, y = x.to(device), y.to(device)

            lr = lr_at(step, total_steps)
            for group in optimizer.param_groups:
                group["lr"] = lr

            _, loss = model(x, y)
            optimizer.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), GRAD_CLIP)
            optimizer.step()

            n = int((y != IGNORE_INDEX).sum())
            epoch_loss += loss.item() * n
            epoch_tokens += n
            step += 1
            if step % 10 == 0:
                print(f"  step {step}/{total_steps}  loss {loss.item():.3f}  lr {lr:.2e}")

        train_loss = epoch_loss / epoch_tokens
        val_loss = evaluate(model, val_loader, device)
        seconds = time.time() - start

        marker = ""
        if val_loss < best_val:
            best_val = val_loss
            epochs_without_improvement = 0
            torch.save({
                "model": model.state_dict(),
                "config": asdict(cfg),
                "epoch": epoch,
                "val_loss": val_loss,
            }, CHECKPOINT)
            marker = "  <- best, saved"
        else:
            epochs_without_improvement += 1

        print(f"epoch {epoch:2d} | train {train_loss:.4f} | val {val_loss:.4f} | {seconds / 60:.1f} min{marker}")
        with open(LOG_FILE, "a", newline="") as f:
            csv.writer(f).writerow([epoch, f"{train_loss:.4f}", f"{val_loss:.4f}", f"{lr:.2e}", f"{seconds:.0f}"])

        if epochs_without_improvement >= PATIENCE:
            print(f"val loss has not improved for {PATIENCE} epochs, stopping early")
            break

    print(f"best val loss: {best_val:.4f} -> {CHECKPOINT}")


if __name__ == "__main__":
    main()
