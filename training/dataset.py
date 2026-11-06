import torch
from torch.utils.data import DataLoader, Dataset

IGNORE_INDEX = -100  # cross-entropy skips targets with this value


class SpecDataset(Dataset):
    """Loads one processed split (e.g. data/processed/train.pt)."""

    def __init__(self, path):
        self.examples = torch.load(path)

    def __len__(self):
        return len(self.examples)

    def __getitem__(self, i):
        e = self.examples[i]
        ids = e["ids"]

        # Next-token prediction: input is every token except the last,
        # target is every token except the first (shifted by one).
        x = ids[:-1]
        y = ids[1:].clone()

        # Loss mask: don't learn to predict the intent, only the spec.
        # y[t] is the token at position t + 1, so targets before
        # spec_start - 1 belong to the intent part.
        y[: e["spec_start"] - 1] = IGNORE_INDEX
        return x, y


def make_collate(pad_id):
    def collate(batch):
        # Pad every sequence in the batch to the longest one in the batch
        max_len = max(len(x) for x, _ in batch)
        xs = torch.full((len(batch), max_len), pad_id, dtype=torch.long)
        ys = torch.full((len(batch), max_len), IGNORE_INDEX, dtype=torch.long)
        for i, (x, y) in enumerate(batch):
            xs[i, : len(x)] = x
            ys[i, : len(y)] = y
        return xs, ys

    return collate


def make_loader(path, pad_id, batch_size, shuffle):
    return DataLoader(
        SpecDataset(path),
        batch_size=batch_size,
        shuffle=shuffle,
        collate_fn=make_collate(pad_id),
    )
