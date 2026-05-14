# Suggested projects

Reading the roadmap is not the same as becoming an AI engineer. Building is.
This doc gives you **one concrete project per stage**, sized to ~1–3 days
of focused work, with clear deliverables. Each project locks in the
mental model of the stage; doing the project once is worth re-reading
the stage twice.

The projects are deliberately *small*. None of them is your portfolio
piece. They are exercises — the equivalent of the textbook problems
that turn passive reading into operational fluency.

For the bigger "portfolio piece" projects, see the peer companion
[**build-your-own-ai**](https://github.com/bettyguo/build-your-own-ai) —
that's where "build a transformer from scratch" lives.

---

## Stage 1 — Prerequisites & Math

**Project: SVD from scratch.**
Implement singular value decomposition on a small matrix using only
NumPy `dot`, `transpose`, and an eigendecomposition you write yourself
(or take from `np.linalg.eig`). Use it to compress a small grayscale
image (32×32) to rank-5 and rank-20. Plot the reconstruction.

**Done when:**
- You can explain what U, Σ, V do, why low-rank captures most of the
  image, and how this connects to LoRA in [`train-lora-qlora-adapters`](../roadmap-data/stages/06-training-finetuning.json).

---

## Stage 2 — Programming & Tooling

**Project: Reproducible Docker training environment.**
Take any small PyTorch model (an MLP on MNIST is fine), put it in a
git repo with a `Dockerfile` and a `Makefile`. `make train` should
build the image, run the training inside a container, and write
logs + a final checkpoint to a mounted volume.

**Done when:**
- A teammate could clone your repo and reproduce your training run with
  `make train`, no Python install required.

---

## Stage 3 — ML Fundamentals

**Project: Tabular classifier with an honest eval.**
Pick a small tabular dataset (Titanic, Adult Income, a Kaggle starter).
Build three models: logistic regression, random forest, gradient boosted
trees. Report accuracy, precision, recall, F1, and PR-AUC on a held-out
test set. Identify one source of data leakage you find and fix it.

**Done when:**
- You have a results table, *and* a written paragraph explaining why
  one metric matters more than another for your problem.

---

## Stage 4 — DL Fundamentals

**Project: A 2-layer MLP, forward and backward, in NumPy only.**
No PyTorch. Implement forward pass, cross-entropy loss, backward pass
(chain rule by hand), and SGD update. Train it on MNIST until it gets
≥90% test accuracy. Then re-implement it in PyTorch and verify the
gradients match.

**Done when:**
- You have two implementations, the gradients agree (within FP precision),
  and you understand exactly what `loss.backward()` is doing.

---

## Stage 5 — Transformers & LLM Internals

**Project: Tokenize, then read a model.**
Pick an open-weights model from Hugging Face (Llama 3.1 8B, Qwen 2.5,
Mistral). Use its tokenizer to tokenize three test strings of your
choice (an English paragraph, a code snippet, and a non-English
sentence). Then load the model with `transformers`, print the named
parameters with their shapes, and identify by name the embedding,
attention heads, MLP blocks, layer norms, and final logit head.

**Done when:**
- You can read a 2026 LLM's parameter list and explain every name. You
  know exactly how many tokens your three test strings became, and
  why.

---

## Stage 6 — Training & Fine-tuning

**Project: A LoRA fine-tune end-to-end.**
Pick a small open-weights model (≤8B params). Pick a small dataset
(<10k examples — Dolly, a slice of UltraChat, or a synthetic one you
generate with Self-Instruct). Run a LoRA fine-tune. Compare the
fine-tuned model and the base model on 20 held-out prompts. Write a
one-page eval doc.

**Done when:**
- You ran a real LoRA training pass on a real GPU, and you can speak
  to one observation about the fine-tune that surprised you. Keep
  the eval doc; it'll be useful in interviews.

---

## Stage 7 — Inference & Serving

**Project: vLLM throughput experiment.**
Stand up vLLM serving a small open-weights model. Send 1 / 4 / 16 /
64 concurrent requests with `wrk`, `vegeta`, or a custom asyncio
script. Plot tokens-per-second and TTFT against concurrency. Identify
the regime where the system saturates.

**Done when:**
- You have a real throughput-vs-concurrency curve for your hardware,
  and you can articulate where the bottleneck is (prefill, decode, KV
  cache, network).

---

## Stage 8 — Retrieval & RAG

**Project: A personal-corpus RAG.**
Take a corpus you actually have (notes, papers, company docs, your
Slack export). Build a RAG pipeline end-to-end: parse → chunk →
embed → vector store → hybrid search → reranker → LLM. Build a 20-
question eval set (questions whose answers are in the corpus) and
measure recall@5, faithfulness, and answer quality. Iterate three
times.

**Done when:**
- You have a working RAG over content you care about, an eval set,
  and three rounds of iteration logged. This is the single highest-
  leverage project in the roadmap; do not skip it.

---

## Stage 9 — Agents & Harnesses

**Project: A 3-tool agent with a real harness.**
Build an agent with three tools: a calculator, a search tool, and a
file-write tool. Implement the harness yourself (control loop,
message history, tool-call parsing, error handling). Run it on five
multi-step tasks. Add safety: tool calls require explicit permission
on first use of each tool.

**Done when:**
- The agent works on five tasks, and you can explain every line of the
  harness loop. For the deeper craft of building harnesses, sideways
  to the peer roadmap [**harness-engineer-roadmap**](https://github.com/bettyguo/harness-engineer-roadmap).

---

## Stage 10 — Evaluation & Observability

**Project: Build a golden eval suite for the RAG you built in Stage 8.**
Hand-write 100 prompt+expected-answer pairs as a JSONL file. Define a
4-point rubric (faithfulness, context relevance, completeness,
fluency). Score the rubric with an LLM-as-judge prompt, and validate
the judge against you on 20 samples (compute agreement). Add the eval
as a CI step that runs on every PR to your RAG repo.

**Done when:**
- You have a regression suite that catches a deliberate prompt
  regression in your RAG. The CI integration is the part that turns
  this into a habit.

---

## Stage 11 — Deployment & Production

**Project: Fallback policy end-to-end.**
Take your RAG or your agent. Wrap it behind an HTTP endpoint. Add a
primary→secondary model fallback (Anthropic→OpenAI or vice versa).
Add per-tenant rate limiting (token bucket). Add prompt caching with
Anthropic's cache control. Load-test it; verify the fallback fires
when you simulate a primary outage.

**Done when:**
- You have an endpoint with documented SLOs, a tested fallback path,
  a rate limiter that works, and a cost-per-1k-requests number.

---

## Stage 12 — Safety, Alignment & Frontier

**Project: Red-team your own RAG/agent.**
Spend half a day trying to break the system you built in Stages 8–11.
Specifically attempt: direct jailbreaks, indirect prompt injection
via uploaded documents, exfiltration via tool outputs, and over-trust
of LLM-judge calls. Write a one-page red-team report: vulnerabilities
found, severity, mitigations applied.

**Done when:**
- You found at least three real vulnerabilities in your own system
  and fixed two of them. The report is something you'd be comfortable
  sharing with a security reviewer.

---

## A note on portfolio shape

If you do all 12 of these (each takes 1–3 days), you'll have:

1. A repo containing the RAG, the agent, the eval suite, the
   deployment scaffolding, and the red-team report. **One coherent
   project** that touches every stage.
2. Six smaller artifacts (SVD, Docker scaffold, tabular classifier,
   NumPy MLP, model-anatomy notebook, LoRA fine-tune) that
   demonstrate breadth.

The big repo is your portfolio piece. The smaller ones are evidence
you understood the fundamentals, not just orchestrated APIs. Together
they cover the entire roadmap.
