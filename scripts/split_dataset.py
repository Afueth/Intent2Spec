import json
import random

SRC = "data/raw/dataset.jsonl"
TRAIN = "data/raw/train.jsonl"
VAL = "data/raw/val.jsonl"
TEST = "data/evaluation/test.jsonl"

SEED = 42          
VAL_SIZE = 0.1
TEST_SIZE = 0.1

with open(SRC, encoding="utf-8") as f:
    pairs = [json.loads(line) for line in f if line.strip()]

random.Random(SEED).shuffle(pairs)

n_test = int(len(pairs) * TEST_SIZE)
n_val = int(len(pairs) * VAL_SIZE)
test = pairs[:n_test]
val = pairs[n_test:n_test + n_val]
train = pairs[n_test + n_val:]


def write(path, rows):
    with open(path, "w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"{path}: {len(rows)} pairs")


write(TRAIN, train)
write(VAL, val)
write(TEST, test)
