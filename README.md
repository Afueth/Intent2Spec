```console
 _       _             _   ____  ____
(_)_ __ | |_ ___ _ __ | |_|___ \/ ___| _ __   ___  ___
| | '_ \| __/ _ \ '_ \| __| __) \___ \| '_ \ / _ \/ __|
| | | | | ||  __/ | | | |_ / __/ ___) | |_) |  __/ (__
|_|_| |_|\__\___|_| |_|\__|_____|____/| .__/ \___|\___|
                                      |_|
   plain words in  ->  technical spec out          v0.0.1
```

```console
$ intent2spec --help

USAGE
  intent2spec <command>

COMMANDS
  --about        What this project is and why it exists
  --demo         See an example: intent in, spec out
  --pipeline     How the model turns words into a spec
  --progress     Show the status of every step
  --roadmap      Open the step-by-step checklist
  --tree         Show the project folders
  --concepts     Things to learn along the way
  --stack        Tools and libraries used
```

---

## `$ intent2spec --about`

```console
$ intent2spec --about

PROJECT     Intent2Spec
TYPE        Study project: small language model (SLM)
TASK        Natural-language intent  ->  structured technical spec

PROBLEM
  Many people know WHAT they want to build, but not the technical
  words to describe it.

SOLUTION
  The user writes an everyday description (the "intent").
  The model rewrites it as a clear spec with the correct technical
  terms, ready for a developer or an AI coding tool.

PHASES
  phase 1   Build from scratch
            Own tokenizer + small GPT-style Transformer (~15M params)
            Learn: how a language model works inside

  phase 2   Fine-tune T5
            Teach a pretrained Flan-T5 the same task, then compare
            Learn: transfer learning, the encoder-decoder design
```

---

## `$ intent2spec --demo`

```console
$ intent2spec "I want a website where people can sign up and save their favourite recipes."

> reading intent ......................................... done
> generating spec ........................................ done

Type        Web application (CRUD)
Auth        User registration and login
            (email + password, hashed with bcrypt)
Data model  User(id, email, password_hash)
            Recipe(id, user_id -> User, title, ingredients,
                   steps, is_favourite)
Features    Create / read / update / delete recipes
            Mark recipes as favourite
API         REST
            POST /signup         POST /login
            GET  /recipes        POST /recipes
            PUT  /recipes/{id}   DELETE /recipes/{id}
Storage     SQLite (development), PostgreSQL (production)
```

---

## `$ intent2spec --pipeline`

```console
$ intent2spec --pipeline

  "I want a website..."                         plain words
          |
          v
  +----------------+
  |   TOKENIZER    |   text   -> tokens          BPE, 8k vocab
  +----------------+
          |
          v
  +----------------+
  |     MODEL      |   tokens -> next token      Transformer
  +----------------+
          |
          v
  +----------------+
  |    DECODER     |   tokens -> text
  +----------------+
          |
          v
  Type: Web application (CRUD) ...              technical spec


$ intent2spec --pipeline --journey

  00 setup --> 01 format --> 02 dataset --> 03 tokenizer --> 04 prep
                                 ^                              |
                                 |                              v
                          weak results         05 model --> 06 train
                                 |                              |
                                 |                              v
  10 share <-- 09 fine-tune T5 <-+--------- 08 evaluate <-- 07 generate

  [ phase 1: steps 01-08 ]   [ phase 2: steps 09-10 ]
```

---

## `$ intent2spec --progress`

```console
$ intent2spec --progress

  STEP  NAME                      PHASE   PROGRESS
  ----  ------------------------  -----   ---------------------------
  00    Environment setup         setup   [######----]   4/7   RUNNING
  01    Define the spec format    1       [----------]   0/5   QUEUED
  02    Build the dataset         1       [----------]   0/7   QUEUED
  03    Build the tokenizer       1       [----------]   0/7   QUEUED
  04    Prepare training data     1       [----------]   0/5   QUEUED
  05    Build the model           1       [----------]   0/3   QUEUED
  06    Train the model           1       [----------]   0/6   QUEUED
  07    Generate specs            1       [----------]   0/4   QUEUED
  08    Evaluate the model        1       [----------]   0/4   QUEUED
  09    Fine-tune T5              2       [----------]   0/6   QUEUED
  10    Share and document        2       [----------]   0/3   QUEUED

  STATUS   RUNNING = in progress   QUEUED = not started   DONE = finished
  CURRENT  step 00, environment setup
```

---

## `$ intent2spec --roadmap`

Click a step to open its checklist. To mark a task done, change `[ ]` to `[x]`.

<details>
<summary><code>$ intent2spec step 00   # environment setup          [RUNNING]</code></summary>

```console
$ intent2spec step 00

  [x] Create the folder structure
  [x] Create a Python virtual environment (.venv, Python 3.13)
  [x] Install PyTorch, NumPy, pandas, scikit-learn, matplotlib,
      JupyterLab
  [x] Install git
  [ ] Run `git init` and add a .gitignore
      (leave out .venv/, checkpoints/, large files in data/)
  [ ] Add a requirements.txt so the environment can be rebuilt
  [ ] Check whether a GPU is available:
      $ python -c "import torch; print(torch.cuda.is_available())"
```

</details>

<details>
<summary><code>$ intent2spec step 01   # define the spec format     [QUEUED]</code></summary>

```console
$ intent2spec step 01

  NOTE  Decide exactly what a "spec" looks like BEFORE collecting
        data. Every training example must follow the same format.

  [ ] Choose the sections every spec has
      (Type, Auth, Data model, Features, API, Storage, Tech stack)
  [ ] Decide which sections are optional and which are required
  [ ] Write a glossary of technical terms the model should use
      (CRUD, REST, authentication, schema, endpoint, ...)
  [ ] Write 10 example pairs by hand as the "gold standard"
  [ ] Document the format in docs/spec_format.md
```

</details>

<details>
<summary><code>$ intent2spec step 02   # build the dataset          [QUEUED]</code></summary>

```console
$ intent2spec step 02

  NOTE  Most important step. Model quality depends mostly on
        data quality.

  [ ] Choose a file format for the pairs, e.g. JSONL:
      {"intent": "I want an app that ...", "spec": "Type: ..."}
  [ ] Collect or write intent -> spec pairs in data/raw/
        - write them by hand
        - generate drafts with a larger AI model, then review and
          fix each one
        - vary the wording: casual, unclear, short, long, typos
  [ ] Cover many kinds of projects: websites, mobile apps, scripts,
      APIs, data analysis, automation, games
  [ ] Target size: 1,000+ pairs to start, 5,000+ for better results
  [ ] Clean the data: remove duplicates, fix formatting, check terms
  [ ] Split: 80% train / 10% validation / 10% test
      (test set goes in data/evaluation/)
  [ ] Write a script that checks every spec matches the step 01
      format
```

</details>

<details>
<summary><code>$ intent2spec step 03   # build the tokenizer        [QUEUED]</code></summary>

```console
$ intent2spec step 03

  NOTE  The tokenizer splits text into small pieces (tokens) that
        the model can read.

  [ ] Learn how Byte Pair Encoding (BPE) works
  [ ] Implement a simple BPE tokenizer in tokenizer/
      (or use the `tokenizers` library to compare)
  [ ] Add special tokens: <pad> <bos> <eos> <intent> <spec>
  [ ] Train the tokenizer on the training data ONLY
  [ ] Choose a vocabulary size (start with about 8,000 tokens)
  [ ] Save the vocabulary files in tokenizer/
  [ ] Test it: encode text, decode it back, confirm it matches
```

</details>

<details>
<summary><code>$ intent2spec step 04   # prepare training data      [QUEUED]</code></summary>

```console
$ intent2spec step 04

  [ ] Format each pair as one sequence:
      <bos> <intent> ...intent text... <spec> ...spec text... <eos>
  [ ] Tokenize all pairs and save them in data/processed/
  [ ] Choose a max sequence length (e.g. 512 tokens) and check how
      many examples are longer
  [ ] Write a PyTorch Dataset and DataLoader with padding and
      batching
  [ ] Mask the loss so the model learns only from the SPEC part,
      not the intent
```

</details>

<details>
<summary><code>$ intent2spec step 05   # build the model            [QUEUED]</code></summary>

```console
$ intent2spec step 05

  [ ] Learn the building blocks: embeddings, self-attention,
      feed-forward layers, layer norm, residual connections
  [ ] Implement in model/:
        [ ] token and position embeddings
        [ ] causal (masked) multi-head self-attention
        [ ] feed-forward block
        [ ] transformer block (attention + feed-forward + norm)
        [ ] full model with a next-token output layer
  [ ] Write tests in tests/ that check output shapes and that one
      batch runs forward and backward

$ cat config/model.yaml   # suggested starting point

  n_layers:     6
  n_heads:      6
  d_embed:      384
  context_len:  512
  vocab_size:   8000
  # parameters: ~15M
```

</details>

<details>
<summary><code>$ intent2spec step 06   # train the model            [QUEUED]</code></summary>

```console
$ intent2spec step 06

  [ ] Write the training loop in training/:
        [ ] loss: cross-entropy on next-token prediction
        [ ] optimizer: AdamW
        [ ] learning rate: warm-up, then cosine decay
        [ ] gradient clipping
  [ ] SANITY CHECK: train on ~10 examples and confirm the model
      can memorise them
  [ ] Train on the full training set
  [ ] Check validation loss regularly; save the best checkpoint
      to checkpoints/
  [ ] Plot training vs. validation loss to spot overfitting
  [ ] Record each experiment (settings + results) in experiements/
```

</details>

<details>
<summary><code>$ intent2spec step 07   # generate specs             [QUEUED]</code></summary>

```console
$ intent2spec step 07

  [ ] Write a generate() function: intent in, spec out
  [ ] Try decoding methods: greedy, temperature, top-k, top-p
  [ ] Stop generating at the <eos> token
  [ ] Build a small command-line tool:
      $ python generate.py "I want an app that ..."
```

</details>

<details>
<summary><code>$ intent2spec step 08   # evaluate the model         [QUEUED]</code></summary>

```console
$ intent2spec step 08

  [ ] Run the model on the test set in data/evaluation/
  [ ] Automatic checks:
        [ ] format score   does the output follow the spec format?
        [ ] term score     does it use the right glossary terms?
        [ ] similarity     compare with the reference (BLEU/ROUGE)
  [ ] Human check: read 30-50 outputs and rate each one
      CORRECT / PARTLY CORRECT / WRONG
  [ ] List common mistakes; fix them with more or better data
      (go back to step 02)
```

</details>

<details>
<summary><code>$ intent2spec step 09   # phase 2: fine-tune T5      [QUEUED]</code></summary>

```console
$ intent2spec step 09 --why

  After building the SLM from scratch (steps 01-08), fine-tune a
  pretrained T5 model on the same data.

  encoder-decoder   The encoder reads the whole intent, the decoder
                    writes the spec. Matches the task directly.
  both designs      Phase 1 is decoder-only (GPT-style). T5 adds
                    the encoder and cross-attention.
  fair comparison   Same dataset and test set, so you can measure
                    how much pretraining helps.

  NOTE  This is FINE-TUNING, not training an LLM from scratch.
        Google already pretrained T5 on a huge amount of text.
        We teach it one new task: intent -> spec.

$ intent2spec step 09 --models

  Start from Flan-T5: same design as T5, but also trained to follow
  instructions, so it learns new tasks faster.

  MODEL           PARAMS   HARDWARE
  flan-t5-small   60M      CPU or a small GPU
  flan-t5-base    220M     GPU with about 8 GB
  flan-t5-large   770M     16 GB+, or use LoRA
```

```console
$ intent2spec step 09.1   # setup

  [ ] Install the libraries:
      $ pip install transformers datasets sentencepiece accelerate evaluate
  [ ] Add them to requirements.txt
  [ ] Load google/flan-t5-small and its tokenizer; run a quick test

$ intent2spec step 09.2   # learn the encoder-decoder design

  [ ] Study how the encoder and decoder work together
  [ ] Understand cross-attention (how the decoder looks at the
      encoder's output)
  [ ] Learn T5's "text-to-text" idea: every task is text in, text out
  [ ] Compare with the phase 1 model: what is the same, what differs?

$ intent2spec step 09.3   # prepare the data for T5

  [ ] Reuse the train / validation / test split from step 02
  [ ] Add a task prefix to each input:
      "convert intent to spec: I want a website where..."
  [ ] Tokenize with the T5 tokenizer (SentencePiece):
      intent -> input_ids,  spec -> labels
  [ ] Choose maximum lengths for the input and the output
  [ ] Save the processed data in data/processed/t5/

$ intent2spec step 09.4   # fine-tune

  [ ] Write the fine-tuning script in training/
      (Hugging Face Seq2SeqTrainer, or your own PyTorch loop)
  [ ] Starting settings:
        learning rate   3e-4   (try 1e-4 to 5e-4)
        batch size      8-16
        epochs          3-10
  [ ] SANITY CHECK: fine-tune on ~10 examples; confirm it learns them
  [ ] Fine-tune flan-t5-small on the full training set
  [ ] Track validation loss; save the best checkpoint to
      checkpoints/t5/
  [ ] Then try flan-t5-base and compare

$ intent2spec step 09.5   # evaluate and compare

  [ ] Run the same evaluation as step 08
  [ ] Fill in the comparison table:

      MODEL              PARAMS  FORMAT  TERMS  ROUGE  HUMAN
      phase 1 SLM        ~15M    --      --     --     --
      flan-t5-small      60M     --      --     --     --
      flan-t5-base       220M    --      --     --     --

  [ ] Write up what you learned in experiements/:
      why does pretraining help? where does each model fail?

$ intent2spec step 09.6   # optional: LoRA on a larger model

  [ ] Learn LoRA (Low-Rank Adaptation): train only small added
      layers instead of the whole model
  [ ] Install `peft` and fine-tune flan-t5-large with LoRA
  [ ] Compare results, training time and memory use with full
      fine-tuning
```

</details>

<details>
<summary><code>$ intent2spec step 10   # share and document         [QUEUED]</code></summary>

```console
$ intent2spec step 10

  [ ] Build a simple interface (web page or chat-style) where anyone
      can type an intent and see the spec
  [ ] Write docs/ pages: how the data was made, the model design,
      training results, what was learned
  [ ] Update this README with final results and example outputs
```

</details>

---

## `$ intent2spec --tree`

```console
$ tree Intent2Spec/

Intent2Spec/
|-- config/           settings for the model and training
|-- data/
|   |-- raw/          original intent -> spec pairs
|   |-- processed/    cleaned, tokenized data ready for training
|   `-- evaluation/   held-out pairs, used only for testing
|-- tokenizer/        tokenizer code and vocabulary files
|-- model/            Transformer model code
|-- training/         training loop and scripts
|-- checkpoints/      saved model weights
|-- experiements/     notebooks and experiment notes
|-- docs/             extra documentation
`-- tests/            unit tests for each part

10 directories
```

---

## `$ intent2spec --concepts`

```console
$ intent2spec --concepts --phase 1

  tokenization (BPE)        how text becomes numbers the model reads
  embeddings                how tokens become vectors with meaning
  self-attention            how the model relates words to each other
  transformer block         the repeated building block of the model
  next-token prediction     how the model learns and generates text
  loss + backpropagation    how the model improves during training
  overfitting               why validation data matters
  decoding strategies       how to get good outputs from the model

$ intent2spec --concepts --phase 2

  encoder-decoder           how T5 reads an input and writes an output
  cross-attention           how the decoder looks at the encoder
  transfer learning         reusing what a pretrained model knows
  fine-tune vs. scratch     why existing models are a better start
  LoRA                      fine-tuning large models with little memory
```

---

## `$ intent2spec --stack`

```console
$ intent2spec --stack

  language          python 3.13
  deep learning     torch 2.15
  phase 2 (T5)      transformers, datasets, sentencepiece,
                    accelerate, evaluate, peft
  data              pandas, numpy
  evaluation        scikit-learn
  plots             matplotlib
  experiments       jupyterlab
  version control   git 2.47
```

---

```console
$ intent2spec --status

  current step   00  environment setup
  next up        01  define the spec format
  purpose        study: build an SLM, then fine-tune T5

$ exit
```
