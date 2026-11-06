# Tokenizer
# Author : Afueth
# Date : 06:11:2026

"""Byte Pair Encoding (BPE) tokenizer, written from scratch."""

import json
import re
from collections import Counter

# Split text into chunks before BPE: words, numbers, punctuation, whitespace.
# Merges never cross a chunk boundary, so "Type:" and "Web" stay separate pieces.
SPLIT_PATTERN = re.compile(r" ?[^\W\d_]+| ?\d+| ?[^\w\s]+|_+|\s+(?!\S)|\s+")


def get_stats(ids, counts=None):
    """Count how often each adjacent pair of token IDs appears.

    Example: [1, 2, 3, 1, 2] -> {(1, 2): 2, (2, 3): 1, (3, 1): 1}
    """
    counts = {} if counts is None else counts
    for pair in zip(ids, ids[1:]):
        counts[pair] = counts.get(pair, 0) + 1
    return counts


def merge(ids, pair, new_id):
    """Replace every occurrence of `pair` in `ids` with `new_id`.

    Example: merge([1, 2, 3, 1, 2], (1, 2), 99) -> [99, 3, 99]
    """
    out = []
    i = 0
    while i < len(ids):
        if i < len(ids) - 1 and ids[i] == pair[0] and ids[i + 1] == pair[1]:
            out.append(new_id)
            i += 2
        else:
            out.append(ids[i])
            i += 1
    return out


class BPETokenizer:
    def __init__(self):
        self.merges = {}                                  # (id, id) -> new id
        self.vocab = {i: bytes([i]) for i in range(256)}  # id -> bytes
        self.special = {}                                 # "<eos>" -> id

    def train(self, text, vocab_size, verbose=False):
        assert vocab_size >= 256
        num_merges = vocab_size - 256

        # Count each unique chunk once, with how often it appears.
        # This is much faster than running BPE over the whole text.
        chunk_counts = Counter(SPLIT_PATTERN.findall(text))
        words = [(list(chunk.encode("utf-8")), n) for chunk, n in chunk_counts.items()]

        for i in range(num_merges):
            # Count pairs across all chunks, weighted by chunk frequency
            stats = {}
            for ids, n in words:
                for pair in zip(ids, ids[1:]):
                    stats[pair] = stats.get(pair, 0) + n
            if not stats:
                break  # nothing left to merge

            pair = max(stats, key=stats.get)
            new_id = 256 + i
            words = [(merge(ids, pair, new_id), n) for ids, n in words]

            self.merges[pair] = new_id
            self.vocab[new_id] = self.vocab[pair[0]] + self.vocab[pair[1]]

            if verbose and (i + 1) % 100 == 0:
                print(f"merge {i + 1}/{num_merges}: {self.vocab[new_id]!r} (seen {stats[pair]} times)")

    def _encode_chunk(self, chunk_bytes):
        ids = list(chunk_bytes)
        while len(ids) >= 2:
            # Of the pairs present, pick the one that was learned earliest
            stats = get_stats(ids)
            pair = min(stats, key=lambda p: self.merges.get(p, float("inf")))
            if pair not in self.merges:
                break  # no more merges apply
            ids = merge(ids, pair, self.merges[pair])
        return ids

    def encode(self, text):
        ids = []
        for chunk in SPLIT_PATTERN.findall(text):
            ids.extend(self._encode_chunk(chunk.encode("utf-8")))
        return ids

    def decode(self, ids):
        id_to_special = {i: name for name, i in self.special.items()}
        parts = []
        for i in ids:
            if i in id_to_special:
                parts.append(id_to_special[i].encode("utf-8"))
            else:
                parts.append(self.vocab[i])
        return b"".join(parts).decode("utf-8", errors="replace")

    def add_special_tokens(self, names):
        # Special tokens get IDs after all normal tokens
        for name in names:
            if name not in self.special:
                self.special[name] = len(self.vocab) + len(self.special)

    def __len__(self):
        return len(self.vocab) + len(self.special)

    def encode_pair(self, intent, spec=None):
        """<bos> <intent> intent <spec> spec <eos>

        Without a spec (when generating), stops after <spec> so the model writes the rest.
        """
        ids = [self.special["<bos>"], self.special["<intent>"]]
        ids += self.encode(intent)
        ids.append(self.special["<spec>"])
        if spec is not None:
            ids += self.encode(spec)
            ids.append(self.special["<eos>"])
        return ids

    def save(self, path):
        data = {
            "merges": [[a, b] for (a, b) in self.merges],  # in the order they were learned
            "special": self.special,
        }
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f)

    @classmethod
    def load(cls, path):
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        tok = cls()
        for a, b in data["merges"]:
            new_id = len(tok.vocab)
            tok.merges[(a, b)] = new_id
            tok.vocab[new_id] = tok.vocab[a] + tok.vocab[b]
        tok.special = data["special"]
        return tok
