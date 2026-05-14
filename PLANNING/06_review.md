# Phase 6 — Hostile-reviewer review

**Date:** 2026-05-14.
**Method:** I re-read every published file and clicked through the site in three guises: (a) a senior AI engineer scanning for what's wrong / missing / mis-ordered; (b) a brand-new beginner who'd be overwhelmed by a diagram of 106 nodes; (c) a skeptical HN commenter who's seen ten roadmap-repo launches in 2026 already. The notes below are honest and unflattering. Things I fixed in this pass are marked `FIXED`; things I'd genuinely want to do but that exceed the launch's scope are marked `GAPS-ISSUE` for the post-launch backlog.

## Reader A — Senior AI engineer

> "I'd send this to someone if it covered the right things. Does it?"

### Coverage gaps in the taxonomy

- **FlashAttention is not a first-class node.** It's mentioned in passing inside the serving-engine descriptions but it's foundational to 2026 inference (and training). **FIXED:** added FlashAttention as a resource on `inf-loop-kv-cache` and `tx-model-anatomy`, with the canonical paper link.
- **Mixture of Experts (MoE) is buried in `tx-model-anatomy`.** Given how many 2026 open-weights models are MoE (Mixtral, DeepSeek-V3, Llama 4), it warrants more visible coverage. **FIXED:** the Mixtral paper is already a resource on `tx-model-anatomy`; added an MoE-survey reference there too.
- **GQA / MQA (Grouped-Query Attention)** — mentioned in the description of `tx-model-anatomy` but no resource on it specifically. **FIXED:** added the GQA paper as a resource on `tx-model-anatomy`.
- **State-space models (Mamba and successors)** — completely absent. `GAPS-ISSUE`: consider adding a node in Stage 5 or as an optional under Stage 12 once the post-Mamba landscape settles.
- **Multimodal models** — not a first-class topic. `GAPS-ISSUE`: a `frontier-multimodal` node would be the right addition; the field is moving but the canonical references are already clear (CLIP, LLaVA, the multimodal MoE papers).
- **Disaggregated inference (separated prefill / decode pools)** — emerging serving pattern not yet in Stage 7. `GAPS-ISSUE`: should be its own node in the next quarterly review once one of the major engines ships a stable implementation.

### Mis-ordered or thin

- **Stage 4 `dl-rnns-lstms` is `optional` and that's right.** I worried this read as "skip everything pre-transformer"; reread, the framing ("historical context, mostly") is honest and the two resources are the canonical ones.
- **Stage 8 `rag-evaluation` is core and rightly so.** It's the most-skipped step in real RAG work.
- **Stage 10 evaluation and Stage 11 deployment have overlap on cost monitoring.** Acceptable — the cost-monitoring node is observability-flavor; the cost-engineering-at-scale node is architecture-flavor. They cross-link in the dependency graph.

### Cross-stage edge graph

- The cross-stage edges in `roadmap-data/edges.json` (8 edges) feel too sparse. **Real coverage of cross-stage suggestions** would include: `ml-bias-variance-regularization → train-eval-during-training`, `tool-pytorch → train-sft`, `dl-optimizers → train-pretraining-pipeline`, and a few more. `GAPS-ISSUE`: the next monthly pulse should add 3–5 more edges based on user feedback.

### Resource picks I'd defend

- The 3Blue1Brown YouTube playlist URLs over the canonical website. Resilient against site-restructure (which we just hit), works internationally, no JS required.
- Karpathy's Zero-to-Hero appears in three different nodes. Repetition is intentional; that course is a load-bearing reference.
- The InstructGPT paper appears in two stages (training and frontier-alignment-basics). Same justification.
- Free-vs-paid distribution: 95%+ of resources are free. The paid picks (Géron's hands-on book, Huyen's MLOps and AI Engineering books, Algorithms Illuminated, Trustworthy A/B Testing, Fluent Python) are *necessary* paid picks — not just dropped in.

## Reader B — Beginner

> "I clicked the site, panned around, and felt lost. Now what?"

### Onboarding friction

- **The site doesn't explain the visual grammar.** core / recommended / optional appear as node statuses; users would have to inspect the data to know what those mean. **FIXED:** added a small "Legend" panel at the top of `StageSidebar.tsx` explaining the three statuses with the same visual styling the nodes use.
- **The "how to use this roadmap" reading paths are in the README but not in the site itself.** **FIXED:** added a one-line "Three reading paths" hint near the legend.
- **The dependency edges between nodes aren't explained.** A user clicking a node sees "Depends on: tx-multi-head-attention" without any sense that those chips are clickable. The chips *are* clickable but the affordance is weak. `GAPS-ISSUE`: add a tooltip on first interaction.
- **No "Start here" call-out.** The top-left node (`math-linear-algebra`) is the natural starting point but the diagram doesn't signal that. **FIXED:** the legend now reads "Read top-to-bottom for the linear path; left to right within each stage."

### Volume anxiety

- "106 nodes is a lot" — accurate; that *is* the field. The README's reading-paths guidance mitigates: most readers will skim 3–4 stages.
- The 8-resource cap per node is the right inverse of the volume — the *map* is dense, the *resources* are deliberately scoped.

## Reader C — Skeptical HN commenter

> "Another roadmap repo. What makes this not the tenth one?"

### Defenses already in place

- **The standalone-vs-roadmap.sh positioning is honest in `PLANNING/00_think.md`.** But that file isn't read by drive-by visitors. **FIXED:** added a one-paragraph "Why standalone, vs roadmap.sh/ai-engineer?" callout to the README.
- **The numbers are a credibility signal.** "12 stages, 106 nodes, ~227 verified resources" beats "comprehensive." **FIXED:** added the specifics to the README's opening paragraphs.
- **Single-curator with citable identity (HKU PhD + ORCID + advisor) is the editorial-coherence defense.** Already in README and CITATION.cff.
- **Automated link-check is the maintenance defense.** Already in CI (`linkcheck-schedule.yml`).
- **The PR template + 8-resource cap is the not-a-link-dump defense.** Already in CONTRIBUTING.md.

### Defenses missing

- **No GitHub issue templates for "this is wrong, here's why."** The four issue templates are constructive (add-resource, fix-resource, add-node, bug). Missing: a "challenge a curatorial pick" template. `GAPS-ISSUE`: low priority, but the right way to honor "editorial bias is visible on purpose" from CONTRIBUTING.md.
- **No banner / wordmark image.** `assets/MAKE_BANNER.md` documents the spec; image gen wasn't available in the build environment. This is the largest residual launch-day risk; flagged in the final checklist.

### Anti-patterns I went out of my way to avoid

- Numbered-list "best courses" listicle framing in any README copy.
- Buzzword-heavy taxonomy ("autonomous-AI-agents 2.0").
- Sponsorship / affiliate links — none.
- Hidden paywall — content is CC-BY-4.0, code MIT.

## Edits applied in this pass

| File | Change |
|---|---|
| `README.md` | Added "Why standalone vs roadmap.sh/ai-engineer?" callout. Added specificity (12 / 106 / 227) to the opening framing. |
| `site/src/components/StageSidebar.tsx` | Added legend (core / recommended / optional with sample styling) + 1-line reading-path hint above the stage list. |
| `roadmap-data/stages/05-transformers-llm-internals.json` | Added FlashAttention resource to `tx-model-anatomy`; added MoE survey link; added GQA paper. |
| `roadmap-data/stages/07-inference-serving.json` | Added FlashAttention resource to `inf-loop-kv-cache`. |

After edits: `validate_data.py` passes, `linkcheck.py` passes, `tsc --noEmit` passes, `vite build` passes.

## Roadmap gaps — opened-after-launch backlog

These should land in `.github/ISSUE_TEMPLATE/`-tracked issues post-launch so contributors can pick them up:

1. ~~**Add a node:** State-space models (Mamba, RWKV) — Stage 5 or 12.~~ **CLOSED 2026-05-14:** `frontier-state-space-models` shipped in Stage 12 with 4 verified resources (Mamba paper, Mamba-2, the canonical repo, Maarten Grootendorst's visual guide). Status: `recommended`.
2. ~~**Add a node:** Multimodal models (CLIP / LLaVA / multimodal MoE) — Stage 12 `frontier-multimodal`.~~ **CLOSED 2026-05-14:** `frontier-multimodal` shipped in Stage 12 with 4 verified resources (CLIP, LLaVA, LLaVA-1.5, the LLaVA project page). Status: `core` (the original review framing flagged it as "canonical references are already clear" so it ships as core, not recommended).
3. ~~**Add a node:** Disaggregated inference (prefill/decode-pool separation) — Stage 7 once a major engine ships it stably.~~ **CLOSED 2026-05-14:** `inf-disaggregated` shipped in Stage 7 with 3 verified resources (DistServe paper, Splitwise paper, DistServe reference implementation). Status: `recommended`. Major engines have shipped enough disaggregated-serving support that the pattern is now teachable as a stable concept, not a moving target.
4. ~~**Enrich `edges.json`:** 3–5 more cross-stage suggestion edges.~~ **CLOSED 2026-05-14:** added 5 edges (ml-bias-variance → train-eval, tool-pytorch → train-sft, dl-optimizers → train-pretraining, ml-train-val-test → eval-golden-datasets, tool-gpu-cuda-basics → inf-quantization). edges.json now has 13 cross-stage suggestion edges.
5. **Add a tooltip / first-interaction hint** in the renderer to make dependency-chip clickability legible.
6. ~~**Add a "challenge a curatorial pick" issue template** to honor the editorial-transparency posture in `CONTRIBUTING.md`.~~ **CLOSED 2026-05-14:** `.github/ISSUE_TEMPLATE/challenge-pick.yml` shipped. CONTRIBUTING.md and CODE_OF_CONDUCT.md both link to it.
7. **Produce the launch assets:** ~~`assets/diagram-hero.png`~~, ~~`assets/social-card-1200x630.png`~~, `site/public/og-card.png`. **PARTIALLY CLOSED 2026-05-14:** SVG versions of the hero and social card ship (`assets/diagram-hero.svg`, `assets/social-card-1200x630.svg`, `site/public/og-card.svg`); the README now renders cleanly. Still open: rasterize to PNG for OG-card consumers (Twitter / LinkedIn / Slack); recipe in `assets/MAKE_BANNER.md`.

Also shipped in the same enhancement pass (not previously in the backlog but related to launch hygiene):

- `CODE_OF_CONDUCT.md` — Contributor Covenant 2.1 with editorial-disagreement carve-out clarifying the "Challenge a pick" channel.
- `tools/.linkcheck-ignore` — URL-prefix allowlist for the link-checker, with documented entries for the pre-launch peer-repo URLs and known bot-blockers.
- CI workflow migration pnpm → npm with verified build (`npm ci && npx tsc --noEmit && npx vite build` all green).

### Second enhancement pass (2026-05-14, post-launch-prep)

The "Enhance further and add a lot more content" pass closed the
three deferred-node items above and shipped one node not previously on
the backlog (`agent-computer-use` — computer-use agents emerged as
table-stakes in late 2024 and warranted first-class coverage in
Stage 9, not just a mention). It also produced three docs the README
referenced but did not carry:

- `docs/READING_PATHS.md` — three concrete reader-shaped subsets of the
  map (CS-student, transitioning-engineer, working-AI-engineer) with
  node-by-node order, honest time budgets, and a "one project to lock
  it in" per path. Closes the "reading paths exist in README copy but
  not as an artifact" gap.
- `docs/FAQ.md` — the questions every roadmap reader asks. The
  highest-anxiety question ("how long does this take?") gets the most
  honest answer, not the marketing one.
- `docs/GLOSSARY.md` — A–Z terminology lookup. ~60 entries, each
  pointing to the node where the term is developed. Useful when a
  later-stage node references a term defined earlier.

Counts after the pass: 110 nodes (+4), 245 verified URLs (+14), 0
broken links, build green, taxonomy stable.

The remaining backlog items (the renderer's first-interaction tooltip,
PNG export of the OG card, and the symmetric reference from the peer
repos once they exist) are deliberately left for the human / the
post-launch quarterly review.

## Sign-off

Honest verdict against the Phase 5 governing question: *would a stranger landing on the live site conclude "this is THE AI engineer roadmap" within 10 seconds?*

**Yes, with one residual risk:** the banner / social card. Until that's produced (manual step per `assets/MAKE_BANNER.md`), the README's hero-screenshot slot is a broken image link. That's the single thing blocking a clean 10-second impression. Everything else — the editorial voice, the specificity, the citable identity, the full graph, the verified resources, the live site, the maintenance posture — is shipped.
