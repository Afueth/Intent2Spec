# Study Notes

My notes while learning AI/ML through the Intent2Spec project.

How to use this file:
- Add a dated entry to the **Learning log** each study session.
- Fill in the **Concept notes** as each topic becomes clear.
- Put open doubts in **Questions** and move them to the notes once answered.

---

## Project folders

| Folder | What it is, in simple words |
|--------|-----------------------------|
| `config/` | The settings file. Numbers like model size and learning rate live here, not in the code, so you can change them without touching any code. |
| `data/raw/` | The examples written by hand or collected, kept exactly as made. Each one is an intent and its correct spec. Never edit these; they are the original copy. |
| `data/processed/` | The same examples after cleaning and turning into numbers (tokens). This is what the model actually reads during training. |
| `data/evaluation/` | The "exam paper". Examples the model never sees while training, used only at the end to check how well it really learned. |
| `tokenizer/` | The code that cuts text into small pieces (tokens) and gives each piece a number, plus the saved list of all known pieces (the vocabulary). |
| `model/` | The "brain". Code for the Transformer that takes tokens in and predicts the next token. |
| `training/` | The code that teaches the model: show examples, measure the mistakes, adjust, repeat. |
| `checkpoints/` | Saved copies of the model's learned weights, like save points in a game. Lets you stop and resume, or keep the best version. |
| `experiements/` | A lab notebook. Jupyter notebooks and notes on each experiment: what you tried and what happened. |
| `docs/` | Written explanations, like the spec format and these study notes. |
| `tests/` | Small checks that each part works correctly, for example "does the tokenizer decode back to the same text?" |

---

## Dataset formats

### Text formats (you can open and read them)

| Format | What it is | Use it for |
|--------|------------|------------|
| CSV / TSV | Rows and columns, separated by commas or tabs | Simple tables. Bad for multi-line text. |
| JSON | One big list of objects | Small datasets and config files |
| JSONL | One JSON object per line | Text pairs for language models |
| TXT | Plain text, no structure | Raw text for pretraining |

### Binary formats (fast, but not human-readable)

| Format | What it is | Use it for |
|--------|------------|------------|
| Parquet | Compressed table | Large tables (pandas, Hugging Face) |
| Arrow | Fast in-memory table | Hugging Face `datasets` |
| .npy / .npz | NumPy array | Arrays of numbers, like token IDs |
| .pt | PyTorch tensor | Tensors saved with `torch.save` |
| .bin | Raw array of numbers | Token IDs; the fastest to load in training |
| HDF5 (.h5) | Large numeric arrays | Scientific data |
| TFRecord | TensorFlow format | TensorFlow only |

### In this project

```
draft_examples.md  -->  dataset.jsonl  -->  token IDs (.bin / .pt / .npy)
   (design)              (raw text)           (what the model trains on)
```

- **Raw data is JSONL:** each example has two fields (`intent`, `spec`), and the spec has many lines.
- **Processed data is binary:** the model only reads numbers.
- **Phase 2 (T5):** Hugging Face loads the same JSONL and turns it into Arrow by itself.

---
