import json
import re

SRC = "data/raw/draft_examples.md"
OUT = "data/raw/dataset.jsonl"

text = open(SRC, encoding="utf-8").read()

pattern = re.compile(
    r"\*\*Intent:\*\*\s*\n(.+?)\n\s*\*\*Spec:\*\*\s*\n```\n(.+?)\n```",
    re.DOTALL,
)

pairs = [
    {"intent": intent.strip(), "spec": spec.rstrip()}
    for intent, spec in pattern.findall(text)
]

with open(OUT, "w", encoding="utf-8") as f:
    for pair in pairs:
        f.write(json.dumps(pair, ensure_ascii=False) + "\n")

print(f"Wrote {len(pairs)} pairs to {OUT}")
