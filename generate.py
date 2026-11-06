"""Generate a spec from an intent with the trained model.

Usage:
    python generate.py "I want an app that ..."
    python generate.py "I want an app that ..." --temperature 0.8 --top-k 50
"""

import argparse

import torch
import torch.nn.functional as F

from model.gpt import GPT, GPTConfig
from tokenizer.bpe import BPETokenizer

CHECKPOINT = "checkpoints/best.pt"
TOKENIZER = "tokenizer/bpe_3000.json"


def load(device):
    ckpt = torch.load(CHECKPOINT, map_location=device)
    model = GPT(GPTConfig(**ckpt["config"]))
    model.load_state_dict(ckpt["model"])
    model.to(device).eval()  # eval: turn dropout off
    tok = BPETokenizer.load(TOKENIZER)
    return model, tok


@torch.no_grad()
def generate(model, tok, intent, max_new_tokens=400, temperature=0.0, top_k=None, top_p=None):
    """Intent in, spec out. temperature 0 = greedy (always pick the top token)."""
    device = next(model.parameters()).device
    eos_id = tok.special["<eos>"]
    context_len = model.cfg.context_len

    ids = tok.encode_pair(intent)  # <bos> <intent> ... <spec>
    idx = torch.tensor([ids], dtype=torch.long, device=device)
    prompt_len = idx.size(1)

    for _ in range(max_new_tokens):
        if idx.size(1) >= context_len:
            break
        logits, _ = model(idx)
        logits = logits[:, -1, :]  # only the last position predicts the next token

        if temperature == 0:
            next_id = logits.argmax(dim=-1, keepdim=True)
        else:
            logits = logits / temperature
            if top_k is not None:
                # keep the k highest logits, drop the rest
                kth = torch.topk(logits, top_k).values[:, -1, None]
                logits[logits < kth] = float("-inf")
            probs = F.softmax(logits, dim=-1)
            if top_p is not None:
                # keep the smallest set of tokens whose probabilities add up to top_p
                sorted_probs, sorted_ids = torch.sort(probs, descending=True)
                cum = sorted_probs.cumsum(dim=-1)
                sorted_probs[cum - sorted_probs > top_p] = 0
                probs = torch.zeros_like(probs).scatter(-1, sorted_ids, sorted_probs)
                probs = probs / probs.sum(dim=-1, keepdim=True)
            next_id = torch.multinomial(probs, num_samples=1)

        if next_id.item() == eos_id:
            break
        idx = torch.cat([idx, next_id], dim=1)

    return tok.decode(idx[0, prompt_len:].tolist())


def main():
    parser = argparse.ArgumentParser(description="Intent -> spec")
    parser.add_argument("intent", help="what you want to build, in plain English")
    parser.add_argument("--temperature", type=float, default=0.0, help="0 = greedy")
    parser.add_argument("--top-k", type=int, default=None)
    parser.add_argument("--top-p", type=float, default=None)
    parser.add_argument("--max-new-tokens", type=int, default=400)
    parser.add_argument("--seed", type=int, default=None)
    args = parser.parse_args()

    if args.seed is not None:
        torch.manual_seed(args.seed)

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model, tok = load(device)
    spec = generate(model, tok, args.intent, args.max_new_tokens,
                    args.temperature, args.top_k, args.top_p)
    print(spec)


if __name__ == "__main__":
    main()
