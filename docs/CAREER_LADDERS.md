# Career ladders

The roadmap is a map of the field, not a job description. This doc
projects it onto the four levels that AI-engineer compensation bands
typically use (junior / mid / senior / staff). Use it to self-locate,
to figure out what specific gap is between you and the next level, or
to interview a candidate against a calibrated bar.

The framing is honest, opinionated, and US-2026-flavored.
Compensation numbers are medians from public sources (levels.fyi,
Glassdoor, leaked offer letters) and will be wrong in two years.

---

## L1 — Junior AI Engineer (≤2 yrs, ~$130k–$180k US base)

**The bar:** Can implement against an API, can read a paper with help,
can ship a feature behind a senior's design.

### Must own (cores)

- Stage 2 (Programming & Tooling) — full
- Stage 3 (ML Fundamentals) — `ml-supervised-loop` through
  `ml-evaluation-metrics`
- Stage 4 (DL Fundamentals) — through `dl-embeddings-representations`
- Stage 5 (Transformers & LLM Internals) — `tx-self-attention`,
  `tx-architecture`, `tx-tokenization`, `tx-model-anatomy`
- Stage 7 (Inference & Serving) — `inf-model-apis`,
  `inf-prompt-engineering-craft`, `inf-structured-output`
- Stage 8 (Retrieval & RAG) — at least the four core nodes
- Stage 10 (Evaluation) — `eval-llm-as-judge`, `eval-golden-datasets`
- Stage 11 (Deployment) — `prod-api-design`, `prod-secrets-access`

### Optional at this level
- Most of Stage 6 (training), Stage 9 (agents), Stage 12 (frontier).
  You should *recognize* these topics but not be on the hook for them.

### Portfolio evidence the hiring manager wants
- One working LLM project shipped to real users (yours, your team's,
  or open source).
- A working RAG over a corpus you care about.
- A `git log` that reads like a software engineer's, not a notebook
  user's.

### Common pitfalls
- "I've trained models in class" but no production code in git.
- "I've used the API" but cannot articulate the cost of one request.
- A README that says "powered by AI" without a numbers table.

---

## L2 — Mid AI Engineer (2–5 yrs, ~$180k–$280k US base)

**The bar:** Owns features end-to-end. Picks the model, designs the
retrieval / agent flow, ships the eval suite, watches the cost. Can
mentor an L1. Reads papers without help.

### Must own (cores)

- Everything from L1.
- Stage 6 (Training & Fine-tuning) — `train-sft`,
  `train-instruction-tuning`, `train-dpo-preference`,
  `train-lora-qlora-adapters`, `train-eval-during-training`,
  `train-synthetic-data`. **Has actually run a fine-tune end-to-end,
  not just read about it.**
- Stage 7 (Inference & Serving) — all 12 nodes. Knows enough to pick
  between vLLM/TGI/SGLang for a deployment and to debug an OOM at 2am.
- Stage 8 (Retrieval & RAG) — all 10 nodes. Has personally tuned a
  retrieval pipeline against a real eval set.
- Stage 9 (Agents & Harnesses) — `agent-tool-use`,
  `agent-function-calling-mcp`, `agent-planning-patterns`,
  `agent-memory-context`, `agent-evaluation`, `agent-safety`.
- Stage 10 (Evaluation) — all 9 nodes. Has built a continuous-eval
  pipeline in production.
- Stage 11 (Deployment) — all 8 nodes including
  `prod-cost-engineering-at-scale` and `prod-rate-limit-fallback`.
- Stage 12 (Safety) — at minimum `frontier-jailbreaks-prompt-injection`
  and `frontier-red-teaming`.

### Portfolio evidence
- An LLM feature that's been in production long enough for the cost
  curve and the eval curve to be visible.
- A LoRA fine-tune they shipped (or a documented reason they chose
  not to).
- Incidents they've responded to: a model regression, a prompt
  injection, a cost spike, a latency issue.

### Common pitfalls
- Can build a RAG demo but not measure it.
- Has read about agents but never shipped one with a real safety
  review.
- Knows DPO exists but has never actually run one.

---

## L3 — Senior AI Engineer (5–8 yrs, ~$280k–$450k+ US base)

**The bar:** Designs systems. Picks what *not* to build. Owns
multi-quarter technical bets. Mentors L1s and L2s. Knows the limits
of every component well enough to pick the right one without
prototyping all three.

### Must own (cores)

- Everything from L2.
- Stage 5 (Transformers & LLM Internals) — all 8 nodes, including
  `tx-scaling-laws` and `tx-pretraining-objectives`. Can read a paper
  and judge whether the new technique would help their stack.
- Stage 6 (Training) — full coverage including
  `train-rlhf`, `train-distillation-compression`,
  `train-distributed-infra`. Has chosen between SFT, DPO, and
  full-RL for a real problem and defended the call.
- Stage 9 (Agents & Harnesses) — full coverage of the summary stage,
  plus enough of the depth peer
  ([**harness-engineer-roadmap**](https://github.com/bettyguo/harness-engineer-roadmap))
  to design a custom harness if needed.
- Stage 12 (Frontier) — all 11 nodes. Specifically, can reason about
  `frontier-reasoning-models`, `frontier-test-time-compute`,
  `frontier-state-space-models`, and `frontier-multimodal` well
  enough to advise the team on what to bet on next quarter.

### Beyond cores
- Cross-team work: has presented design decisions to non-AI leadership
  and won the argument *with evidence*.
- Has run at least one major hiring loop for AI engineers and
  calibrated other interviewers.
- Has either published, open-sourced a meaningful tool, or written
  a public technical post that other practitioners reference.

### Portfolio evidence
- One AI system that's been in production for a year. Numbers visible:
  cost, latency, quality, incident rate.
- A documented "we considered X, chose Y, here's why" decision that's
  held up after deployment.
- A junior engineer they trained who has since gone to L2.

### Common pitfalls
- Can build but cannot say no.
- Treats every new paper as table-stakes.
- Hasn't actually run a fine-tune in 18 months and has stopped
  noticing.

---

## L4 — Staff AI Engineer (8+ yrs, ~$450k–$700k+ US base in 2026)

**The bar:** Strategic. Multi-team. Picks the bets that matter at
company-scale. Is the person leadership asks "should we invest in
this?" — and is right.

### Must own

- Everything from L3.
- A point of view about how the field is moving — anchored in
  Stage 12's frontier nodes and re-evaluated quarterly. Specifically:
  reasoning-models, test-time compute, agent capabilities, multimodal,
  and the cost-curves around all four.
- Cost engineering at company scale (Stage 11
  `prod-cost-engineering-at-scale`). Has saved their company ≥$1M /
  year through a single architectural call.
- Cross-discipline fluency: product, design, security, legal. Can
  represent AI engineering in any of those rooms.

### Portfolio evidence at this level

There's no portfolio per se — there are *bets*. Bets that paid off.
Bets that didn't but were correctly framed at the time. Public talks,
papers, or systems that other staff engineers cite as reference.

### Common pitfalls

- Has stopped reading code.
- Has stopped reading papers.
- Forms strong opinions without doing the L2/L3 work to ground them.

---

## A note on titles vs. levels

Titles ("AI Engineer," "ML Engineer," "Applied Scientist," "MLE,"
"LLM Engineer," "Founding Engineer at AI startup") vary
chaotically in 2026. **Levels travel.** Two L3s at different
companies do roughly the same kind of work even if their titles
look nothing alike. Calibrate on the must-own list, not the title.

## A note on PhDs and credentials

This ladder is title-and-credential blind. The L3 bar is the same
whether the engineer has a PhD, a bootcamp certificate, or a CS
undergrad. The PhD has often (not always) compressed L1→L3, because
the skill of *reading the literature* — the part most non-PhD
engineers under-invest in — is exactly what the doctorate trains.

A non-PhD candidate clears the same bar by reading more papers.
Specifically: the resources tagged `advanced` in this roadmap.

## A note on staying current at each level

- **L1**: monthly Sebastian Raschka + weekly check of the Stage 12
  frontier nodes.
- **L2**: add quarterly re-read of Stages 6/7/8/9 cores. The field
  *will* move under you.
- **L3**: add a paper-a-week habit and an actual eval pulse on your
  systems.
- **L4**: add cross-discipline reading (product, security, compliance)
  and a strategic eye on the cost curves.

See the [Working AI Engineer path](READING_PATHS.md#path-c--the-working-ai-engineer-staying-current)
for the operationalized version of this.

---

## Interviewing against this ladder

A practical hiring-loop framing for AI-engineer roles, mapped to the
roadmap:

- **Coding round:** Stage 2 fluency, Stage 3 fundamentals.
- **LLM-systems-design round:** Stage 5, 7, 8 in conversation.
- **ML-fundamentals round:** Stage 3, 4 in conversation.
- **Behavioral / scope round:** evidence of L1/L2/L3 work.
- **Optional research-flavor round:** Stage 6 and Stage 12 reading.

For the depth of preparation aimed at each round, see the peer
companion [**llm-interview-prep**](https://github.com/bettyguo/llm-interview-prep).
