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

## What we have done so far

### Step 00: Environment setup

- Created the project folders and a Python virtual environment (`.venv`), so this project's packages stay separate from the rest of the computer.
- Installed PyTorch, NumPy, pandas, scikit-learn, matplotlib and JupyterLab.
- `requirements.txt` lists only the packages we chose. A full `pip freeze` broke on Windows, because it also listed Linux-only GPU packages.
- Set up git, and a `.gitignore` for files that should not be saved (`.venv/`, checkpoints, processed data).
- Git identity: GitHub links commits to an account by **email**. This project uses its own email, set with `git config` (no `--global`), so commits show the right account.

### Step 01: Define the spec format

- The model learns by copying the pattern in its training outputs. If the outputs are inconsistent, the model learns the inconsistency.
- So we fixed one exact format before writing any data: `docs/spec_format.md`.
- Fields, always in this order: `Type`, `Auth`, `Data model`, `Features`, `Input`, `API`, `Storage`, `Tech stack`.
- Required: `Type`, `Features`, `Tech stack`. The rest are optional.
- Main rule: if a field does not apply, **leave it out** (never write `None`).
- Wrote 10 hand-made "gold" examples (web, mobile, script, API, game, data analysis, extension, chatbot, dashboard, desktop) to test the format.

### Step 02: Build the dataset

**How much data?**
- A ~15M-parameter model trained from scratch knows no English, so it must learn the language, the technical concepts and the format from our pairs alone.
- About 1,000 pairs teaches the format; about 5,000 gives useful results; 10,000+ is better.
- Plan: 1,000 now to get the whole pipeline working, then grow to 5,000 based on what the model gets wrong.
- Variety and correctness matter more than raw count.

**How the data was made:**
- Generated 990 pairs with a large LLM, in 10 categories of 99 (web, mobile, scripts, APIs, data/ML, games, extensions/desktop/CLI, bots/AI, dashboards/IoT, small business).
- Mixed writing styles in the intents: casual, short and vague, long, typos, non-native English.
- Checked: every pair valid, no duplicate intents.

**Scripts (in `scripts/`):**

| Script | What it does |
|--------|--------------|
| `draft_to_jsonl.py` | Reads `draft_examples.md`, writes `dataset.jsonl` (one pair per line) |
| `validate_specs.py` | Checks every spec follows `spec_format.md`: field names, order, required fields, no `None`, `- ` bullets, alignment |
| `split_dataset.py` | Shuffles and splits the dataset into train / validation / test |

- Always edit `draft_examples.md`, then re-run `draft_to_jsonl.py` and `validate_specs.py`. Edits made directly in `dataset.jsonl` get overwritten.
- A JSONL file looks like "one line" in the editor because each line is very long. Turn word wrap on or off with `Alt + Z`.

**Train / validation / test split:**

| File | Pairs | Purpose |
|------|-------|---------|
| `data/raw/train.jsonl` | 800 | The model learns from these |
| `data/raw/val.jsonl` | 100 | Checked during training to detect overfitting and choose the best checkpoint |
| `data/evaluation/test.jsonl` | 100 | Used once at the end, for the final honest score |

- **Why split:** testing on data the model trained on only measures memorization. It must be tested on unseen data.
- **Overfitting:** training loss keeps going down but validation loss starts going up. The model is memorizing, not learning. Keep the checkpoint with the lowest validation loss.
- **Why test is separate from validation:** many decisions are made using validation results, so the model becomes slightly tuned to it. The test set is never used for decisions, so its score is unbiased.
- **Shuffle before splitting:** the dataset is ordered by category; without shuffling, the test set would contain only one category.
- **Fixed seed (`42`):** the same shuffle every run, so the split is reproducible.

### Next: Step 03, build the tokenizer

- Watch Karpathy's "Let's build the GPT Tokenizer" first.

---

## Key ML terms

### Data and the model

| Term | Meaning |
|------|---------|
| **Token** | A small piece of text (a word or part of a word) that the model reads as a number |
| **Vocabulary** | The full list of tokens the tokenizer knows (we plan about 8,000) |
| **Parameters / weights** | The numbers inside the model that training adjusts. Our model has about 15 million. |
| **Next-token prediction** | The model's only job: given the tokens so far, predict the next one. A full spec is generated one token at a time. |
| **Training from scratch** | Starting with random weights; the model knows nothing, not even English |
| **Pretrained model** | A model already trained on huge amounts of text (like Flan-T5); it already knows the language |
| **Fine-tuning** | Training a pretrained model a little more on our task (phase 2) |

### Training

| Term | Meaning |
|------|---------|
| **Batch** | A small group of examples processed together (e.g. 16 pairs) |
| **Step** | One weight update, done after each batch |
| **Epoch** | One full pass through all the training data |
| **Optimizer** | The algorithm that updates the weights to reduce the loss (we use AdamW) |
| **Learning rate** | How big each weight update is. Too high: training is unstable. Too low: training is very slow. |
| **Backpropagation** | The method that works out how much each weight contributed to the error, so it can be adjusted |
| **Checkpoint** | A saved copy of the model's weights at some point in training |

With our data:
```
800 pairs / batch size 16 = 50 steps per epoch
20 epochs x 50 steps      = 1,000 weight updates
```

### Loss

- **Loss:** one number that says how wrong the model's predictions are. Lower is better.
- **Cross-entropy loss:** `loss = -log(probability the model gave to the correct token)`, averaged over all tokens.

| Probability given to the correct token | Loss |
|----------------------------------------|------|
| 0.99 | 0.01 (almost perfect) |
| 0.70 | 0.36 |
| 0.10 | 2.30 |
| 0.001 | 6.9 (very wrong) |

- Starting point: a random model with an 8,000-token vocabulary has a loss of about `ln(8000) ≈ 9.0`.

### Train loss vs. validation loss

| | Measured on | Model learns from it? |
|---|-------------|-----------------------|
| **Train loss** | `train.jsonl` (800) | Yes |
| **Val loss** | `val.jsonl` (100) | No, only measured |

- Train loss: how well the model fits the data it learns from.
- Val loss: how well it handles data it has never seen. **This is the one that matters.**

Example training log:
```
epoch   train loss   val loss
  1        6.5          6.6     just started
  5        2.1          2.3     learning
 10        0.9          1.2     still fine
 15        0.3          1.1     lowest val loss -> save this checkpoint
 20        0.1          1.5     val rising -> overfitting
```

| What you see | Meaning | What to do |
|--------------|---------|------------|
| Both falling | Learning well | Keep training |
| Train falling, val rising | **Overfitting** (memorizing) | Stop; use the checkpoint with the lowest val loss |
| Both stuck high | **Underfitting** (not learning enough) | Bigger model, tune the learning rate, train longer |

### Data size

- **Chinchilla rule of thumb:** a model needs about 20 training tokens per parameter.
  `15M params x 20 = 300M tokens ≈ 1.2 million pairs` (far more than we can make).
- So a from-scratch model will be limited by data. A pretrained model (phase 2) needs far fewer examples, because it already knows the language.
- **Random seed:** a fixed number that makes "random" operations (shuffling, weight initialization) give the same result every run, so experiments are reproducible.

---

## Tokenization (BPE)

### What a tokenizer does

The model only works with numbers. The tokenizer converts text to numbers and back:

```
"Type: Web application"  --encode-->  [412, 7, 1893, 655]
[412, 7, 1893, 655]      --decode-->  "Type: Web application"
```

### How BPE (Byte Pair Encoding) works

```
1. Start:  text -> bytes. Each byte (0-255) is one token.  vocab = 256
2. Count every adjacent pair of tokens in the training text.
3. Merge the most frequent pair into a new token (ID 256, 257, ...).
4. Repeat until the vocabulary reaches the target size.
```

- **Encoding:** apply the learned merges to new text, in the same order they were learned.
- **Decoding:** turn each ID back into its bytes and join them.
- **Starting from bytes means no unknown tokens:** any text (typos, emoji, other languages) can be encoded.
- Frequent pieces like `Type:`, `application` and `POST /` end up as single tokens, so the text gets shorter in tokens.

### The two core functions (`tokenizer/bpe.py`, part A)

| Function | What it does | Example |
|----------|--------------|---------|
| `get_stats(ids)` | Counts how often each neighbouring pair of IDs appears | `[1, 2, 3, 1, 2]` -> `{(1,2): 2, (2,3): 1, (3,1): 1}` |
| `merge(ids, pair, new_id)` | Replaces every occurrence of `pair` with `new_id` | `merge([1, 2, 3, 1, 2], (1, 2), 99)` -> `[99, 3, 99]` |

- `get_stats` uses `zip(ids, ids[1:])` to walk through every neighbouring pair.
- `merge` scans left to right. When it finds the pair, it writes the new ID and skips 2 positions; otherwise it copies the token and moves 1.

Full BPE training is these two functions in a loop:
```
repeat N times:
    stats = get_stats(ids)
    top   = most frequent pair
    ids   = merge(ids, top, next_new_id)
```

### First merge on our own spec text

Text: `"Type:       Web application"`

| Result | Meaning |
|--------|---------|
| 27 bytes: `[84, 121, 112, ...]` | Each character is one byte. `84` = `T`, `121` = `y`, `32` = space. |
| Most frequent pair: `(32, 32)`, 6 times | Space + space, because specs pad field names to column 13 |
| After the merge: 24 tokens | 7 spaces became `[256, 256, 256, 32]`: 3 merges, not 6, because a merged byte is not reused |

### Decisions for our tokenizer

- **Vocabulary size:** 2,000-4,000 (not 8,000), because our training text is small (about 700 KB). With too many tokens, many appear only a few times and the model cannot learn them well.
- **Train the tokenizer on `train.jsonl` only.** Using validation or test text would leak information from them.
- **Special tokens:**

| Token | Purpose |
|-------|---------|
| `<pad>` | Fills short sequences so all sequences in a batch have the same length |
| `<bos>` | Beginning of sequence |
| `<eos>` | End of sequence; tells the model when to stop |
| `<intent>` | Marks where the intent starts |
| `<spec>` | Marks where the spec starts |

---
