# What changed

The monthly pulse — what's been added to, revised in, or retired from
the roadmap. Read this if you've already worked through the map once
and want to know what to revisit. The full per-commit history lives in
[`CHANGELOG.md`](../CHANGELOG.md); this doc summarizes the
*reader-relevant* deltas in one place per month.

The pulse is published on or near the **1st of each month**. If
you're seeing this doc and the most recent entry is more than 8 weeks
old, something is wrong — open an issue.

---

## 2026-05 — Launch month

Launched the roadmap at 12 stages and grew it through three internal
enhancement passes during the same month. This first published pulse
records the net state at the end of the launch month.

### Added (new nodes)

In rough order of when they were added during the month:

| Stage | Node | Status | Why it's here |
|---|---|---|---|
| 7 | `inf-disaggregated` | recommended | Disaggregated prefill/decode serving. DistServe and Splitwise established the pattern; major engines have shipped enough support that it's now teachable as stable. |
| 9 | `agent-computer-use` | core | Computer-use agents (Anthropic Computer Use, OpenAI Operator). Not optional — they're a 2026 product category. |
| 12 | `frontier-state-space-models` | recommended | Mamba and the SSD framework. Coverage for "what's beyond transformers" without overclaiming. |
| 12 | `frontier-multimodal` | core | CLIP, LLaVA, vision-language models. Multimodal moved from frontier to product-expectation in 2026; ships as core. |
| 4 | `dl-vision-transformers` | core | ViT as a first-class node. The bridge from Stage 5 transformer mental model to Stage 12 multimodal. |
| 6 | `train-synthetic-data` | core | The biggest post-training shift of 2025 (Phi, Tülu 3, the persona-driven datasets). |
| 7 | `inf-flashattention` | core | FlashAttention 1/2/3 + the canonical repo. Was a resource on multiple other nodes; deserves its own. |
| 9 | `agent-coding-agents` | recommended | Claude Code, Aider, SWE-bench. The clearest commercial agentic-AI category in 2026. |
| 10 | `eval-arena-elo` | recommended | The Chatbot Arena pattern — pairwise crowdsourced preference scored by Bradley-Terry. Adopt for your own product. |
| 12 | `frontier-test-time-compute` | recommended | The 2024-2026 paradigm shift (Snell et al., DeepSeek-R1). Distinct from `frontier-reasoning-models` (the trained behavior); this is the underlying scaling law. |

Plus three nodes added by community / concurrent curation that
arrived during the month: a Stage 2 tool node, a Stage 8 RAG node,
and a Stage 9 deep-research agent node — see `git log` for the
specifics.

### Added (new docs)

| Doc | Why |
|---|---|
| [`docs/READING_PATHS.md`](READING_PATHS.md) | Three concrete reader-shaped subsets of the map; the README mentioned reading paths but didn't carry them as an artifact. |
| [`docs/FAQ.md`](FAQ.md) | The questions every reader asks, answered honestly. |
| [`docs/GLOSSARY.md`](GLOSSARY.md) | A–Z terminology lookup, each term linked to its canonical node. |
| [`docs/SUGGESTED_PROJECTS.md`](SUGGESTED_PROJECTS.md) | One concrete project per stage. ~1-3 days of work each; together they form a portfolio. |
| [`docs/CAREER_LADDERS.md`](CAREER_LADDERS.md) | Maps the roadmap to L1/L2/L3/L4 AI-engineer levels with comp-band context and hiring-loop framing. |
| `SECURITY.md`, `MAINTAINERS.md` | Standard governance hygiene for an OSS launch. |

### Added (new tooling)

| Tool | What it does |
|---|---|
| `tools/stats.py` | Canonical count source: stages, nodes, resources, unique URLs, status / type / difficulty / free-paid breakdowns. Eliminates manual count-maintenance drift in the README and SVG assets. |
| `tools/.linkcheck-ignore` | URL prefix allowlist for pre-launch peer-repo URLs and known bot-blockers. Documented; revisit when peer repos go live. |

### Visual updates

- `assets/diagram-hero.svg` and `assets/social-card-1200x630.svg`
  updated to reflect end-of-month counts.

### Field outlook for next pulse

What I'm watching that may land in next month's update:

- **Reasoning model open-weights wave.** DeepSeek-R1 was the opener;
  the next replications will probably move `frontier-test-time-compute`
  from recommended to core.
- **Computer-use safety incidents.** First serious-incident report
  on a computer-use agent will likely tighten the `agent-safety`
  node's resources.
- **MoE proliferation.** Mixtral-style MoE shipping in more open
  weights may justify pulling out `tx-moe` as its own node from
  inside `tx-model-anatomy`.
- **Long-context cost curves.** If 1M+ context becomes default-cheap,
  `rag-architecture-patterns` will need re-framing.

---

## Pulse template (for future months)

Maintainer note — when writing the next pulse, replicate this shape:

```markdown
## YYYY-MM — One-line headline of what this month was about

### Added
- (new nodes, new docs, new tooling — each with a one-line reason)

### Revised
- (existing nodes where resources were swapped, with the swap rationale)

### Retired
- (nodes or resources removed, with the reason)

### Visual updates
- (banner, SVG, README copy changes worth flagging)

### Field outlook for next pulse
- (what I'm watching that may shape next month)
```

Cadence: published on or near the **1st of each month**. If a pulse
slips by more than two weeks, post a one-liner on the issue tracker
explaining why.
