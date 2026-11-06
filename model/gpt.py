import math
from dataclasses import dataclass

import torch
import torch.nn as nn
import torch.nn.functional as F


@dataclass
class GPTConfig:
    vocab_size: int = 3005   # 3000 BPE tokens + 5 special tokens
    context_len: int = 512   # longest sequence the model can see
    n_layers: int = 6        # number of transformer blocks
    n_heads: int = 6         # attention heads per block
    d_embed: int = 384       # size of each token's vector
    dropout: float = 0.1


class Embeddings(nn.Module):
    """Token IDs -> vectors, plus a vector for each position."""

    def __init__(self, cfg):
        super().__init__()
        self.tok = nn.Embedding(cfg.vocab_size, cfg.d_embed)
        self.pos = nn.Embedding(cfg.context_len, cfg.d_embed)
        self.drop = nn.Dropout(cfg.dropout)

    def forward(self, idx):
        B, T = idx.shape
        positions = torch.arange(T, device=idx.device)  # 0, 1, 2, ..., T-1
        return self.drop(self.tok(idx) + self.pos(positions))

class CausalSelfAttention(nn.Module):
    """Each token looks at itself and all earlier tokens, and mixes in their information."""

    def __init__(self, cfg):
        super().__init__()
        assert cfg.d_embed % cfg.n_heads == 0
        self.n_heads = cfg.n_heads
        self.qkv = nn.Linear(cfg.d_embed, 3 * cfg.d_embed)  # makes query, key, value at once
        self.proj = nn.Linear(cfg.d_embed, cfg.d_embed)     # combines the heads' outputs
        self.attn_drop = nn.Dropout(cfg.dropout)
        self.resid_drop = nn.Dropout(cfg.dropout)

        # Causal mask: lower-triangular matrix of ones.
        # Row t has ones up to column t, so token t can only see tokens 0..t.
        mask = torch.tril(torch.ones(cfg.context_len, cfg.context_len))
        self.register_buffer("mask", mask.view(1, 1, cfg.context_len, cfg.context_len), persistent=False)

    def forward(self, x):
        B, T, C = x.shape
        hd = C // self.n_heads  # size of each head (384 / 6 = 64)

        # 1. Query, key, value for every token
        q, k, v = self.qkv(x).split(C, dim=2)

        # 2. Split into heads: (B, T, C) -> (B, n_heads, T, hd)
        q = q.view(B, T, self.n_heads, hd).transpose(1, 2)
        k = k.view(B, T, self.n_heads, hd).transpose(1, 2)
        v = v.view(B, T, self.n_heads, hd).transpose(1, 2)

        # 3. Attention scores: how well each query matches each key
        att = (q @ k.transpose(-2, -1)) / math.sqrt(hd)       # (B, n_heads, T, T)

        # 4. Block the future: scores for later tokens become -infinity
        att = att.masked_fill(self.mask[:, :, :T, :T] == 0, float("-inf"))

        # 5. Scores -> weights that sum to 1 in each row
        att = F.softmax(att, dim=-1)
        att = self.attn_drop(att)

        # 6. Weighted sum of the values
        out = att @ v                                          # (B, n_heads, T, hd)

        # 7. Join the heads back together: -> (B, T, C)
        out = out.transpose(1, 2).contiguous().view(B, T, C)
        return self.resid_drop(self.proj(out))
class FeedForward(nn.Module):
    """Processes each token's vector on its own: expand 4x, apply GELU, shrink back."""

    def __init__(self, cfg):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(cfg.d_embed, 4 * cfg.d_embed),  # 384 -> 1536
            nn.GELU(),
            nn.Linear(4 * cfg.d_embed, cfg.d_embed),  # 1536 -> 384
            nn.Dropout(cfg.dropout),
        )

    def forward(self, x):
        return self.net(x)


class Block(nn.Module):
    """One transformer block: attention, then feed-forward, each with layer norm and a residual."""

    def __init__(self, cfg):
        super().__init__()
        self.ln1 = nn.LayerNorm(cfg.d_embed)
        self.attn = CausalSelfAttention(cfg)
        self.ln2 = nn.LayerNorm(cfg.d_embed)
        self.ff = FeedForward(cfg)

    def forward(self, x):
        x = x + self.attn(self.ln1(x))  # tokens exchange information
        x = x + self.ff(self.ln2(x))    # each token processes what it gathered
        return x

class GPT(nn.Module):
    def __init__(self, cfg):
        super().__init__()
        self.cfg = cfg
        self.emb = Embeddings(cfg)
        self.blocks = nn.ModuleList([Block(cfg) for _ in range(cfg.n_layers)])
        self.ln_f = nn.LayerNorm(cfg.d_embed)
        self.head = nn.Linear(cfg.d_embed, cfg.vocab_size, bias=False)

        # Weight tying: the output layer reuses the token embedding table
        self.head.weight = self.emb.tok.weight

        self.apply(self._init_weights)

    def _init_weights(self, m):
        # Small random starting weights keep early training stable
        if isinstance(m, (nn.Linear, nn.Embedding)):
            nn.init.normal_(m.weight, mean=0.0, std=0.02)
        if isinstance(m, nn.Linear) and m.bias is not None:
            nn.init.zeros_(m.bias)

    def forward(self, idx, targets=None):
        x = self.emb(idx)                  # (B, T) -> (B, T, C)
        for block in self.blocks:
            x = block(x)                   # 6 blocks, shape stays (B, T, C)
        logits = self.head(self.ln_f(x))   # (B, T, vocab_size): a score for every token

        loss = None
        if targets is not None:
            loss = F.cross_entropy(
                logits.view(-1, logits.size(-1)),  # (B*T, vocab_size)
                targets.view(-1),                  # (B*T,)
                ignore_index=-100,                 # skip intent and padding (the loss mask)
            )
        return logits, loss

