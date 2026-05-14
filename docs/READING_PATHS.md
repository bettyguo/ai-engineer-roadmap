# Reading paths

The roadmap has 122 nodes across 12 stages. Reading it linearly takes
many months. This doc collapses the map to **three concrete reader-
shaped subsets** so you can start without staring at the full graph.

Each path lists the core nodes in order, the recommended detours, and
how long honest commitment would take. Paths are not exclusive — you
can switch between them as you go. The interactive site at
<https://bettyguo.github.io/ai-engineer-roadmap/> is where the picks
actually live; this doc is the human-readable plan.

The site renders the same data with status colors: **filled** = core,
**outlined** = recommended, **muted** = optional. Stick to the cores
on a first pass.

---

## Path A — The CS student / new grad pivoting into AI

**Anxiety:** "I keep seeing 50-link threads and none of them agree.
What do I actually study so I don't waste 6 months?"

**Goal:** A grounded baseline in the whole field. Linear, end-to-end.

**Time, honest:** 6–10 months at 15 hours / week. Less if you already
know the math; more if you're starting from zero programming.

### The order

1. **Stage 1 — Prerequisites & Math** (all 8 core/recommended nodes).
   Pace: 4–6 weeks. The meta-node `math-how-much-is-enough` is the
   antidote to perfectionism here. Don't get stuck.

2. **Stage 2 — Programming & Tooling** (all 8 nodes). Pace: 3–4 weeks.
   `tool-python`, `tool-numpy-scientific-stack`, `tool-pytorch`, and
   `tool-git` are non-negotiable.

3. **Stage 3 — ML Fundamentals** (10 nodes). Pace: 4–6 weeks. Build
   linear and logistic regression from scratch in NumPy once. The
   `ml-bias-variance-regularization` and `ml-evaluation-metrics` nodes
   pay rent forever.

4. **Stage 4 — DL Fundamentals** (10 nodes). Pace: 4–6 weeks. Implement
   a 2-layer MLP's forward and backward pass by hand once. Take
   `dl-rnns-lstms` as an optional skim, not a deep dive.

5. **Stage 5 — Transformers & LLM Internals** (8 nodes). Pace: 3–4
   weeks. This is the pivot. `tx-self-attention` → `tx-architecture` →
   `tx-model-anatomy` is the spine of the stage.

6. **Stage 6 — Training & Fine-tuning** (10 nodes). Pace: 3–4 weeks.
   Do a real LoRA fine-tune on an open-weights model end-to-end before
   moving on. That single run teaches more than reading 5 papers.

7. **Stages 7–8 — Inference & RAG** (21 nodes total). Pace: 4–6 weeks.
   Build one production-shaped RAG system. The whole point.

8. **Stage 9 — Agents & Harnesses (summary)** (9 nodes). Pace: 2 weeks
   for the summary. If this is your direction, go sideways to
   `harness-engineer-roadmap` for the depth.

9. **Stage 10 — Evaluation** (8 nodes). Pace: 1–2 weeks. Most-skipped
   stage in real practice; do not skip.

10. **Stage 11 — Deployment** (8 nodes). Pace: 2 weeks. Will feel
    review-shaped if you've done web engineering before.

11. **Stage 12 — Frontier** (10 nodes). Pace: 2–4 weeks of light
    reading. `frontier-multimodal` and `frontier-reasoning-models` are
    now table-stakes; the rest is genuinely frontier.

### What to skip on a first pass

- `math-discrete` (optional). Come back if interviews want it.
- `dl-rnns-lstms` (optional). Historical context, don't dwell.
- The "recommended" status on most Stage 6/7/12 nodes — fine to skim,
  not skip entirely.

### One project to lock the path in

After Stage 8: build a working RAG system over a personal corpus (your
own notes, papers, or company docs). Wire eval (Stage 10) and a
deploy (Stage 11). That single artifact is the portfolio piece that
gets the first AI-engineer job.

---

## Path B — The working software engineer transitioning in

**Anxiety:** "I've shipped production systems for years. I don't know
which fundamentals I'm missing and I'm too embarrassed to start at
the beginning."

**Goal:** Self-locate, fill the specific gaps, get to RAG/agents/eval
fast.

**Time, honest:** 8–12 weeks at 10 hours / week.

### The order

1. **Skim Stages 1–4** in ~1 week. Use the `doneWhen` criteria as a
   self-test: read each one and decide if you can do it. If yes, mark
   the node mentally as done and move on. If no, study just that
   node's resources. You'll find 5–15 gaps.

2. **Stage 5 — Transformers & LLM Internals** (8 nodes). Pace: 2 weeks.
   Read top-to-bottom even if you've used LLMs in production. The
   mental model behind the box labeled "LLM" pays for itself.

3. **Stage 7 — Inference & Serving** (11 nodes). Pace: 1–2 weeks. Many
   nodes here are software-engineering-shaped (`inf-cost-engineering`,
   `inf-model-apis`, `inf-prompt-engineering-craft`). The architectural
   ones (`inf-loop-kv-cache`, `inf-quantization`, `inf-disaggregated`)
   are where to slow down.

4. **Stage 8 — Retrieval & RAG** (10 nodes). Pace: 2–3 weeks. The
   single highest-leverage stage for someone with backend experience.

5. **Stage 9 — Agents & Harnesses** (9 nodes). Pace: 1–2 weeks. The
   summary fits a working engineer's reading speed; for deeper craft,
   `harness-engineer-roadmap` is the peer roadmap to open.

6. **Stage 10 — Evaluation & Observability** (8 nodes). Pace: 1 week.
   Software engineers tend to already be SLO-fluent; the LLM-eval
   wrinkles are where to focus.

7. **Stage 11 — Deployment** (8 nodes). Pace: 1 week. Review-shaped.

8. **Stage 6 — Training & Fine-tuning, selectively** (~5 nodes worth
   reading; the rest is "nice to have"). Pace: 1 week. Most working
   engineers don't train models day-to-day, but `train-sft`,
   `train-lora-qlora-adapters`, and `train-eval-during-training` come
   up often enough to matter.

9. **Stage 12 — Frontier, selectively** (~4 nodes). Pace: ongoing
   reading. `frontier-multimodal`, `frontier-reasoning-models`,
   `frontier-jailbreaks-prompt-injection`, `frontier-career-community`.

### What to skip

- Most of Stages 1–4, after the skim. Returning when an actual gap
  surfaces is fine.
- `train-pretraining-pipeline`, `train-distributed-infra` — unless
  you're going to pretrain.

### One project to lock the path in

A RAG + eval + deploy project that solves a real problem inside your
current company. Pair it with the `prod-cost-engineering-at-scale`
node — that's the framing that turns "I built a demo" into "I shipped
a feature."

---

## Path C — The working AI engineer staying current

**Anxiety:** "I shipped my first RAG/agent 18 months ago. I don't
know what's frontier anymore. Is my stack about to be obsolete?"

**Goal:** Frontier awareness on the minimum sustainable monthly
budget. Find the small handful of nodes where the field actually
moved.

**Time, honest:** 2–4 hours / week, indefinitely.

### Quarterly anchor reads

These are the four stages where 2026 has moved fast enough that even
practitioners need to refresh:

- **Stage 6 — Training & Fine-tuning.** Specifically `train-dpo-preference`
  (and successors), `train-distillation-compression`. Synthetic data
  reshaped the post-training stack — pay attention to what's
  replacing instruction-following datasets you used a year ago.

- **Stage 7 — Inference & Serving.** `inf-disaggregated` is new this
  quarter; `inf-engines-vllm-tgi-sglang` ships breaking changes every
  few months; `inf-speculative-decoding` is now standard.

- **Stage 8 — Retrieval & RAG.** `rag-advanced-contextual-graph` is
  where new patterns land (Contextual Retrieval, GraphRAG, late
  chunking). Reranking and embedding choices keep evolving.

- **Stage 9 — Agents & Harnesses.** `agent-computer-use`,
  `agent-function-calling-mcp`, and `agent-memory-context` are the
  three places agents got measurably better. For depth, the peer
  roadmap is `harness-engineer-roadmap`.

- **Stage 12 — Frontier.** `frontier-reasoning-models`,
  `frontier-multimodal`, `frontier-state-space-models`,
  `frontier-mech-interp`. The last is the one most likely to surprise
  practitioners.

### The sustainable monthly routine

1. **Once a month:** read the `CHANGELOG.md` of this roadmap (the
   pulse). Diff what's new since last month. Open the 2–3 nodes that
   changed.
2. **Once a week:** Sebastian Raschka's *Ahead of AI*, *Latent Space*
   podcast, *The Batch* — three sources, ~1 hour total.
3. **Once a quarter:** re-read the cores of one of the four anchor
   stages above. Pick the one nearest your day job; rotate.

### One project to keep yourself current

Ship one thing per quarter that uses a technique you didn't have a
year ago. The act of shipping it (eval, deploy, post-mortem) is the
forcing function; the technique is the excuse. The roadmap nodes are
the menu.

---

## A note on time budgets

The numbers above are honest medians for an engineer who can dedicate
the stated weekly hours. They are not aspirational. People finish in
half the time when they're already strong on math or programming.
People take twice as long when they're learning Python alongside
linear algebra alongside Pandas. Both are fine; the roadmap doesn't
care.

The thing that wastes time is jumping between paths every two weeks
because a Twitter thread said you were doing it wrong. Pick a path,
finish a project, then re-pick. The map will still be here.
