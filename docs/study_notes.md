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

### Step 03: Build the tokenizer

- Built a BPE tokenizer from scratch: 3,000 tokens + 5 special = **3,005**.
- Trained on `train.jsonl` only, saved to `tokenizer/bpe_3000.json`, with 11 unit tests.
- Details: see **Tokenization (BPE)** below.

### Step 04: Prepare the training data

- Measured sequence lengths and chose `max_len = 512` (no pair is cut off).
- Tokenized all pairs and saved them to `data/processed/` (`train.pt`, `val.pt`, `test.pt`).
- Built a PyTorch `Dataset` and `DataLoader` with input/target shift, padding and a loss mask.
- Details: see **Data preparation** below.

### Step 05: Build the model

- Built a GPT-style Transformer from scratch: **11,998,080 parameters** (about 12M).
- 6 blocks, 6 attention heads, 384-number vectors, context of 512 tokens.
- 9 unit tests (shapes, causal mask, loss mask, gradients, memorizing one batch).
- Details: see **The model (Transformer)** below.

### Step 06: Train the model (done)

- Sanity check: the model memorized 5 examples (loss 8.04 -> 0.02) and reproduced one spec exactly.
- Full training: 800 pairs, 20 epochs, 71.5 minutes on CPU.
- Best val loss 3.2768 at epoch 19 (from 8.06 at the start). Saved to `checkpoints/best.pt`.
- Details: see **Training** below.

### Next: Step 07, generate specs

- Load `checkpoints/best.pt` and write a spec for a new intent, one token at a time.

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

### Part B: training the tokenizer (`train()`)

- **Pre-splitting (`SPLIT_PATTERN`):** before BPE, the text is cut into chunks (words, numbers, punctuation, whitespace).
  `"Type:       Web application"` -> `["Type", ":", "      ", " Web", " application"]`
  Merges only happen inside a chunk, so a token never glues a word to punctuation (no `"e: W"` tokens). GPT-2 does the same.
- **Count unique chunks (speed):** `" application"` appears hundreds of times but is stored once with its count. Pair counts are weighted by that count. Same result, about 30 seconds instead of hours.
- **The loop:** count pairs -> pick the most frequent -> merge it everywhere -> record it.
  - `self.merges[(a, b)] = new_id`: the rule (used by `encode`)
  - `self.vocab[new_id] = bytes_a + bytes_b`: what the token means (used by `decode`)
- **Result on our data:** 665,289 characters, 2,744 merges, about 27 seconds.
  - First merges are runs of spaces (from the column-13 padding), then common pieces (`er`, ` a`, `in`).
  - `"\n           "` (newline + 11 spaces) became one token: our continuation-line indent.
  - Last merges are whole words seen only about 13 times. With 8,000 tokens, many would be seen only 2-3 times, which is why we chose 3,000.

### Part C: `encode()` and `decode()`

- **`encode(text)`:** split into chunks -> bytes -> apply merges. When several pairs could merge, take the one **learned earliest** (lowest ID). This repeats the training order, so the same text always gives the same IDs.
- **`decode(ids)`:** look up each ID's bytes, join them, turn them into text. `errors="replace"` shows a bad byte sequence as `�` instead of crashing.

Results:

| Result | Meaning |
|--------|---------|
| 27 characters -> 5 tokens | `Type`, `:`, padding, ` Web`, ` application` |
| Round trip OK on train, val and test | `decode(encode(x)) == x` for every pair. Nothing is lost, even for text the tokenizer never saw (it falls back to bytes). |
| About 3.65 characters per token | Compression: sequences are about 3.65x shorter than raw characters, so training is faster. Val/test are almost the same as train, so the vocabulary generalizes. |

### Part D: special tokens, `save()` and `load()`

- Special tokens get IDs **after** the normal tokens: `<pad>` 3000, `<bos>` 3001, `<eos>` 3002, `<intent>` 3003, `<spec>` 3004.
- **Full vocabulary = 3,005.** The model needs this number (step 05).
- `encode(text)` never produces special IDs, so a user typing `"<eos>"` cannot break anything.
- **`encode_pair()`** builds one training sequence:
  ```
  <bos> <intent> ...intent... <spec> ...spec... <eos>
  ```
  - `<intent>` / `<spec>` mark which part is which.
  - `<eos>` teaches the model when to stop. Generation stops when the model outputs 3002.
  - Without a spec, it stops after `<spec>`. That is the **prompt** used when generating: "here is the intent, now write the spec".
- A typical pair is about **164 tokens** (used to choose the max sequence length in step 04).
- **`save()`** stores only the merge list (in order) and the special tokens in `tokenizer/bpe_3000.json` (about 33 KB).
- **`load()`** rebuilds the vocabulary by replaying the merges.
- Train the tokenizer **once**; every later step just loads the file.

### Part E: unit tests (`tests/test_tokenizer.py`)

- **Why:** if `bpe.py` changes later and something breaks, the tests catch it immediately.
- **How `unittest` works:** each method starting with `test_` is one test. `assertEqual(a, b)` fails if `a != b`. `setUpClass` runs once before all tests.
- Run: `python -m unittest tests.test_tokenizer -v`

| Test | Checks that... |
|------|----------------|
| `get_stats`, `merge` | the core functions give correct results |
| merge does not overlap | `[5,5,5]` -> `[9,5]`, not `[9,9]` |
| vocab size | 3,005 tokens |
| special tokens | all 5 exist and decode to their names |
| edge cases | empty text, spaces, emoji, accents, typos survive encode -> decode |
| user text never becomes special | typing `"<eos>"` does not produce the real `<eos>` ID |
| all data round trip | all 1,000 pairs survive encode -> decode |
| `encode_pair` format | starts `<bos> <intent>`, ends `<eos>` |
| prompt | ends at `<spec>`, no `<eos>` |
| save / load | a reloaded tokenizer gives the same IDs |

### Tokenizer files

| File | What it is |
|------|------------|
| `tokenizer/bpe.py` | The tokenizer code (`BPETokenizer` class) |
| `tokenizer/train_tokenizer.py` | Trains on `train.jsonl` and saves the result. Run: `python -m tokenizer.train_tokenizer` |
| `tokenizer/bpe_3000.json` | The trained tokenizer (merges + special tokens) |
| `tokenizer/try_encode.py`, `try_special.py` | Small scripts to see the tokenizer working |
| `tests/test_tokenizer.py` | Unit tests |

- **Why `python -m tokenizer.train_tokenizer`:** `-m` runs the file as a module from the project root, so Python can find the `tokenizer` package for `from tokenizer.bpe import ...`.

---

## Data preparation (step 04)

### Part A: choosing the max sequence length

The model has a fixed **context length**: the most tokens it can see at once.

| Split | Median | Longest |
|-------|--------|---------|
| train | 226 tokens | 455 |
| val | 231 | 407 |
| test | 212 | 399 |

| Option | Pairs cut off (train) | Verdict |
|--------|-----------------------|---------|
| 256 | 250 of 800 | Too short |
| 384 | 13 | Close |
| **512** | **0** | **Chosen** |

- **Truncation is harmful:** a cut-off sequence loses the end of the spec and the `<eos>` token, so the model never learns to finish.
- **Longer is not free:** attention compares every token with every other token, so cost grows with **length²**.

### Part B: tokenize once, save to `data/processed/`

- `scripts/prepare_data.py` encodes every pair with `encode_pair()` and saves a list per split:

| Field | Example | Used for |
|-------|---------|----------|
| `ids` | `tensor([3001, 3003, 2762, ...])` | The sequence the model reads |
| `spec_start` | `28` | Where the spec begins (for the loss mask) |

- `dtype=torch.long`: the embedding layer needs token IDs as 64-bit integers.
- Training reads the data thousands of times, so encoding once is faster and keeps every run identical.
- `data/processed/` is not committed: it can be recreated with `python -m scripts.prepare_data`.
- **Training tokens: 183,153** (val 23,684, test 22,400).

### Part C: input and target (shift by one)

The model predicts the next token at every position at once:
```
ids: <bos> <intent> I  want ... <spec> Type  :  ... <eos>
x  : <bos> <intent> I  want ... <spec> Type  :  ...
y  : <intent> I  want  ... <spec> Type  :  ... <eos>
```
At position `t` the model sees `x[0..t]` and must predict `y[t]`.

### Part D: the loss mask

- Targets inside the intent part are set to **`-100`**. Cross-entropy **skips** any target equal to `-100`.
```
y:  -100 -100 ... -100  Type  :  ...  <eos>
    └─ intent: no loss ┘ └── spec: loss ──┘
```
- **Why:** the user writes the intent; the model only ever has to write the spec. Learning to predict the intent wastes capacity.
- First trained target is `Type` (right after `<spec>`); last is `<eos>`, so the model learns when to stop.

### Padding and batching (`collate`)

- A batch is one tensor, so all rows must have the same length. Short rows are filled:
  - `x` with `<pad>` (3000)
  - `y` with `-100`, so padding is never in the loss
- **Dynamic padding:** pad to the longest sequence **in the batch** (e.g. 308), not to 512. Saves a lot of computation.
- **Padding cannot confuse the model:** attention is causal (tokens only see earlier tokens) and padding comes after the real tokens.
- `DataLoader`: `batch_size=16` gives 50 batches per epoch; `shuffle=True` for training only.

### Data preparation files

| File | What it is |
|------|------------|
| `scripts/seq_lengths.py` | Measures sequence lengths |
| `scripts/prepare_data.py` | Tokenizes all splits and saves `.pt` files |
| `training/dataset.py` | `SpecDataset`, `collate` (padding), `make_loader` |
| `training/try_loader.py` | Shows one batch and the loss mask |

- Git warning `CRLF will be replaced by LF`: harmless. Windows ends lines with CRLF, Linux with LF; `.gitattributes` stores files with LF.

---

## The model (Transformer, step 05)

### The full pipeline

```
token IDs (B, T)
  -> Embeddings          token + position vectors     (B, T, 384)
  -> Block x 6           attention + feed-forward     (B, T, 384)
  -> LayerNorm (ln_f)    final normalization          (B, T, 384)
  -> head (Linear)       a score for every token      (B, T, 3005)
  -> cross-entropy       compare with targets          one number: the loss
```

| Letter | Meaning |
|--------|---------|
| `B` | Batch size: sequences processed together |
| `T` | Sequence length in tokens |
| `C` | Vector size per token (`d_embed` = 384) |

### Settings (`GPTConfig`)

| Setting | Value | Meaning |
|---------|-------|---------|
| `vocab_size` | 3005 | Tokens the model knows |
| `context_len` | 512 | Longest sequence |
| `n_layers` | 6 | Transformer blocks |
| `n_heads` | 6 | Attention heads per block |
| `d_embed` | 384 | Numbers per token vector |
| `dropout` | 0.1 | Fraction of values randomly zeroed during training |

### Part A: embeddings

- **Token embedding** `nn.Embedding(3005, 384)`: a table with one row of 384 numbers per token. Training adjusts the rows so tokens with similar roles get similar vectors.
- **Position embedding** `nn.Embedding(512, 384)`: attention has no sense of order, so each position gets its own learned vector, **added** to the token vector.
- **Dropout:** during training, randomly zeroes 10% of values so the model cannot depend on any single one. Reduces overfitting. Off during generation.

### Part B: causal self-attention

How each token gathers information from earlier tokens.

| Vector | Question it answers |
|--------|---------------------|
| **Query** (q) | What am I looking for? |
| **Key** (k) | What do I contain? |
| **Value** (v) | What information do I pass on? |

1. `q @ kᵀ`: a score for every pair of tokens (how well a query matches a key).
2. Divide by `√64`: keeps scores small so softmax does not become extreme.
3. **Causal mask:** scores for future tokens become `-inf`, so they get **zero** weight.
   ```
           sees→ 0  1  2  3
   token 0:      1  0  0  0
   token 1:      1  1  0  0
   token 2:      1  1  1  0
   token 3:      1  1  1  1
   ```
   Why: during generation the future does not exist yet; if the model could peek in training, it would learn to copy the answer.
4. **Softmax:** each row of scores becomes weights that sum to 1.
5. `att @ v`: each token's output is a weighted average of the value vectors it attends to.
6. **Multi-head (6 heads of 64 numbers):** each head can learn a different relationship. `proj` combines them.

### Parts C and D: feed-forward and the block

- **Feed-forward:** `384 -> 1536 -> GELU -> 384`, applied to each token separately. Attention moves information **between** tokens; feed-forward **processes** it. About two-thirds of each block's parameters are here.
- **GELU:** a non-linear activation. Without it, stacked linear layers collapse into one and cannot learn complex patterns.
- **Block:**
  ```python
  x = x + self.attn(self.ln1(x))  # tokens exchange information
  x = x + self.ff(self.ln2(x))    # each token processes what it gathered
  ```
- **Residual connection (`x + ...`):** each layer adds a correction instead of replacing `x`. Gradients flow straight back through the `+`, so deep stacks still learn.
- **Layer norm:** rescales each token's vector to mean 0, variance 1. Keeps values stable through many layers.
- **Pre-norm:** layer norm **before** each sub-layer (modern GPT style); trains more stably.
- Input and output shapes are the same `(B, T, 384)`, which is why blocks can be stacked.

### Part E: the full GPT

- **`nn.ModuleList`:** a list of layers PyTorch tracks, so their parameters get trained.
- **Logits:** for every position, 3,005 scores (one per token). Highest score = best guess.
- **Weight tying:** the output layer reuses the token embedding table (`head.weight = emb.tok.weight`). Saves 1.15M parameters and helps on small data. GPT-2 does the same.
- **Weight init (`std=0.02`):** small random starting weights. Too large: outputs explode. All zero: every neuron learns the same thing.
- **Starting loss check:** an untrained model should give every token about 1/3005 probability, so loss ≈ `ln(3005) = 8.01`. Ours: **8.06**. A standard first sanity check.
- **`loss.backward()`:** backpropagation computes the gradient for all 12M weights.

### Model size

```
embeddings (shared with head):   1,350,528
6 blocks x 1,774,464:           10,646,784
   attention      591,360
   feed-forward 1,181,568
   2 layer norms    1,536
final layer norm:                      768
total:                          11,998,080
```

The README estimated about 15M; weight tying and the smaller vocabulary (3,005 instead of 8,000) made it about 12M.

### Part F: model tests (`tests/test_model.py`)

- Most tests use a **tiny model** (2 layers, 32 numbers, 50 tokens) so they run fast; the logic is the same.

| Test | Checks that... |
|------|----------------|
| output shapes | `(3, 10)` in gives `(3, 10, vocab)` out |
| full-size parameter count | exactly 11,998,080 |
| weight tying | output layer and embedding are the same matrix |
| initial loss | about `ln(vocab)` |
| ignored targets | `-100` targets are really skipped (loss mask works) |
| attention / model causal | changing future tokens does not change earlier outputs |
| backward | every weight gets a gradient |
| memorise one batch | 100 training steps cut the loss by more than 80% |

- Run all tests: `python -m unittest tests.test_tokenizer tests.test_model` (20 tests).

### Built is not trained

| | Status |
|---|--------|
| Architecture (`model/gpt.py`) | The structure: the code that defines the model |
| Weights | Random until training; `GPT(cfg)` always creates a new random model in memory |
| Trained model | Exists only after training, saved to `checkpoints/best.pt` |

---

## Training (step 06)

### The training loop

Every neural network is trained with these 4 lines, repeated:
```python
_, loss = model(x, y)      # 1. forward: predict and measure the loss
optimizer.zero_grad()      # 2. clear old gradients
loss.backward()            # 3. backpropagation: gradient for every weight
optimizer.step()           # 4. AdamW nudges every weight to reduce the loss
```

### Part A: sanity check (`training/sanity_check.py`)

- Train on **5 examples only** and check the model can **memorize** them. If it cannot, full training will fail too, and the problem is much faster to find here.
- Result: loss **8.04 -> 0.02** in 200 steps, and the model wrote example 0's spec **exactly**, stopping at `<eos>` by itself.

| Loss | Meaning |
|------|---------|
| 8.04 | Random guessing |
| 2.0 | Learned common patterns (field names, structure) |
| 0.4 | Most tokens right |
| 0.02 | Almost perfect (correct token gets about 98% probability) |

- **Lesson: learning rate matters.** With `1e-3` the loss got stuck around 5.6; with `3e-4` it learned. Too high a learning rate makes updates jump around instead of settling.
- This is **overfitting on purpose**, to prove the model can learn. Dropout is off (`0.0`) here because dropout fights memorization.
- **Greedy decoding** (preview of step 07): give the model `<bos> <intent> ... <spec>`, pick the highest-scoring token (`argmax`), add it, repeat until `<eos>`.

### Part B: full training (`training/train.py`)

| Feature | What it does | Why |
|---------|--------------|-----|
| Epochs (20) | All 800 pairs, 20 times | Learn from everything |
| Validation | Loss on the 100 val pairs after each epoch, no learning | Detect overfitting |
| Best checkpoint | Saved only when val loss improves | Keep the version that generalizes best |
| Early stopping (`PATIENCE = 4`) | Stop if val loss does not improve for 4 epochs | Do not waste time overfitting |
| Warm-up (50 steps) | Learning rate ramps from 0 to `3e-4` | Random weights + big updates = unstable start |
| Cosine decay | Learning rate falls smoothly to `3e-5` | Learn fast in the middle, fine-tune at the end |
| Gradient clipping (`1.0`) | Caps the size of one update | One bad batch cannot wreck the weights |
| Weight decay (`0.1`) | Gently pulls weights toward zero | Reduces overfitting |
| Dropout (`0.1`) | On again | Reduces overfitting |
| Log file | `experiements/train_log.csv` | For loss curves later |

Learning-rate schedule:
```
LR
3e-4 |    /‾‾‾‾\
     |   /      ‾‾\
     |  /          ‾‾\__
3e-5 | /                ‾‾‾‾
     +----------------------- steps
      warm-up   cosine decay
```

- **`model.eval()` + `@torch.no_grad()` in `evaluate`:** dropout off and no gradient tracking, so validation is deterministic, faster and never changes the weights.
- **Validation loss is averaged per spec token**, so batches with longer specs count more, the same as in training.
- **Checkpoint contents:** weights (`state_dict`), model config, epoch, val loss. About 48 MB; not committed (`checkpoints/` is in `.gitignore`).

### Running on CPU

- No GPU (`torch 2.15.0+cpu`), so training runs on the CPU.
- One step: about 3-4 seconds. One epoch (50 steps + validation): about 3.5 minutes. 20 epochs: about **70 minutes**.
- `Ctrl + C` stops training; the best checkpoint so far is kept.

### First results (2-epoch test run)

```
epoch 1 | train 6.70 | val 5.39
epoch 2 | train 4.94 | val 4.73
```

### Full 20-epoch results

Run: `python -m training.train`, 1000 steps, 71.5 minutes on CPU. Log: `experiements/train_log.csv`.

| Epoch | Train loss | Val loss | Gap (val - train) | LR |
|---|---|---|---|---|
| 1 | 6.6952 | 5.3866 | -1.31 | 3.00e-04 |
| 2 | 4.8640 | 4.4739 | -0.39 | 2.98e-04 |
| 5 | 3.6789 | 3.7582 | 0.08 | 2.72e-04 |
| 10 | 2.9921 | 3.3964 | 0.40 | 1.77e-04 |
| 15 | 2.5866 | 3.2897 | 0.70 | 7.39e-05 |
| 18 | 2.4556 | 3.2808 | 0.83 | 3.75e-05 |
| **19** | **2.4262** | **3.2768** | 0.85 | 3.19e-05 |
| 20 | 2.4052 | 3.2787 | 0.87 | 3.00e-05 |

**Best checkpoint: epoch 19, val loss 3.2768.**

How to read it:

- **Epochs 1-2, val lower than train.** The train loss is the average over the whole epoch, including the bad early steps. Val is measured at the end of the epoch, when the model is already better. Dropout is also on during training and off during val.
- **Epochs 1-8, fast learning.** Val dropped from 5.39 to 3.49. The model learned the spec format: field names, their order, the 12-space indent, `- ` before features, and stopping at `<eos>`.
- **Epochs 9-20, slow learning.** Val dropped only 0.22 more. The format is learned. What is left is the content (which features or tech stack fit an intent), which is hard to learn from 800 examples.
- **The gap grew from 0.08 to 0.87.** Train loss kept going down, but val loss stopped. This is overfitting: the model is starting to memorize the training specs instead of learning general rules. It is mild here, because val did not go back up.
- **Epochs 18 and 20 did not save.** Their val loss was slightly worse than the best. Early stopping needs 4 epochs in a row without improvement, so it never triggered. All 20 epochs ran.
- **Low LR at the end.** The cosine schedule brought LR down to 3e-5, so the last epochs made only small, fine adjustments.

What the loss number means:

- Loss is the average of `-ln(probability of the correct next token)`.
- **Perplexity** = `e^loss`. It is roughly "how many tokens the model is choosing between" at each step.

| | Loss | Perplexity |
|---|---|---|
| Random start (3005 tokens) | 8.06 | about 3005 |
| Best val (epoch 19) | 3.28 | about 26 |
| Train (epoch 20) | 2.41 | about 11 |

- The model went from guessing among 3005 tokens to about 26.
- Most of the remaining loss comes from content tokens (feature wording, tool names), where many answers are correct. Format tokens (`Type:`, indent, `<eos>`) are almost certain now.
- The loss does not show if the specs are good. Step 07 (generation) and step 08 (evaluation) will show that.

Why val loss stopped at about 3.28:

- **Limited data.** 183k training tokens for 12M parameters. Chinchilla suggests about 20 tokens per parameter, which would be about 240M tokens. The model is data-limited, not size-limited.
- Ways to improve later: more data, a smaller model, higher dropout, or fine-tuning a pretrained model (phase 2, Flan-T5).

### Training files

| File | What it is |
|------|------------|
| `training/sanity_check.py` | Overfit 5 examples to prove the pipeline learns |
| `training/train.py` | Full training. Run: `python -m training.train` |
| `checkpoints/best.pt` | The trained model (best val loss) |
| `experiements/train_log.csv` | Train/val loss per epoch |

---
