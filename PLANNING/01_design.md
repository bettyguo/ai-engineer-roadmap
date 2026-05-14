# Phase 1 — DESIGN

**Builds on:** `PLANNING/00_think.md`.
**Date:** 2026-05-14.
**Note on `frontend-design` skill:** The Phase 0 master prompt asks me to read `/mnt/skills/public/frontend-design/SKILL.md` before any UI work. That skill is **not present in this environment** (Windows, no `/mnt/skills/`). I will substitute explicit aesthetic-direction constraints (§4) and flag this in `docs/LAUNCH.md` so the maintainer can re-run the renderer phase under that skill if available later.

---

## 1. The roadmap taxonomy

12 stages, 96 nodes. Every node is reachable along a directed acyclic dependency graph rooted at Stage 1. Stages = visual clusters in the diagram. Nodes within a stage are mostly siblings; some have intra-stage dependencies.

> Status legend (drives the visual grammar): **core** = essential, study this. **recommended** = study this if your role/specialization touches it. **optional** = depth detour.

### Stage 1 — Prerequisites & Math (8 nodes)
- `math-linear-algebra` (core)
- `math-calculus` (core)
- `math-probability-statistics` (core)
- `math-information-theory` (recommended)
- `math-numerical-floating-point` (recommended)
- `math-optimization` (core)
- `math-discrete` (optional)
- `math-how-much-is-enough` (core) — meta-node addressing the most common anxiety

### Stage 2 — Programming & Tooling for AI (8 nodes)
- `tool-python` (core)
- `tool-numpy-scientific-stack` (core)
- `tool-pytorch` (core)
- `tool-git` (core)
- `tool-linux-shell` (core)
- `tool-docker` (recommended)
- `tool-gpu-cuda-basics` (recommended)
- `tool-data-formats` (recommended) — parquet, arrow, datasets

### Stage 3 — Machine Learning Fundamentals (10 nodes)
- `ml-supervised-loop` (core)
- `ml-linear-regression` (core)
- `ml-logistic-regression` (core)
- `ml-trees-forests` (core)
- `ml-gradient-boosting` (recommended)
- `ml-kmeans-clustering` (recommended)
- `ml-dimensionality-reduction` (recommended)
- `ml-train-val-test` (core)
- `ml-bias-variance-regularization` (core)
- `ml-evaluation-metrics` (core)

### Stage 4 — Deep Learning Fundamentals (10 nodes)
- `dl-neural-net-computational-graph` (core)
- `dl-backprop` (core)
- `dl-optimizers` (core)
- `dl-init-normalization` (core)
- `dl-activations-losses` (core)
- `dl-cnns` (recommended)
- `dl-rnns-lstms` (optional) — historical context, mostly
- `dl-embeddings-representations` (core)
- `dl-attention-history` (recommended) — pre-transformer attention
- `dl-generative-overview` (recommended) — AE, VAE, GAN, diffusion (overview only)

### Stage 5 — Transformers & LLM Internals (8 nodes)
- `tx-architecture` (core)
- `tx-self-attention` (core)
- `tx-multi-head-attention` (core)
- `tx-tokenization` (core)
- `tx-positional-encoding-rope` (recommended)
- `tx-pretraining-objectives` (core)
- `tx-scaling-laws` (recommended)
- `tx-model-anatomy` (core) — what a 2026 LLM actually contains

### Stage 6 — Training & Fine-tuning (10 nodes)
- `train-pretraining-pipeline` (recommended)
- `train-data-curation` (core)
- `train-sft` (core)
- `train-instruction-tuning` (core)
- `train-rlhf` (recommended)
- `train-dpo-preference` (core)
- `train-lora-qlora-adapters` (core)
- `train-distillation-compression` (recommended)
- `train-eval-during-training` (core)
- `train-distributed-infra` (recommended)

### Stage 7 — Inference & Serving (10 nodes)
- `inf-loop-kv-cache` (core)
- `inf-quantization` (core)
- `inf-batching` (recommended)
- `inf-speculative-decoding` (recommended)
- `inf-latency-throughput` (core)
- `inf-engines-vllm-tgi-sglang` (core)
- `inf-model-apis` (core)
- `inf-structured-output` (core)
- `inf-prompt-engineering-craft` (core)
- `inf-cost-engineering` (core)

### Stage 8 — Retrieval & RAG (10 nodes)
- `rag-embeddings` (core)
- `rag-vector-stores` (core)
- `rag-hybrid-search` (core)
- `rag-reranking` (core)
- `rag-chunking` (core)
- `rag-document-parsing` (recommended)
- `rag-query-reformulation` (recommended)
- `rag-architecture-patterns` (core)
- `rag-advanced-contextual-graph` (recommended)
- `rag-evaluation` (core)

### Stage 9 — Agents & Harnesses (SUMMARY) (8 nodes + sideways hand-off)
- `agent-tool-use` (core)
- `agent-function-calling-mcp` (core)
- `agent-planning-patterns` (core)
- `agent-memory-context` (core)
- `agent-multi-agent` (recommended)
- `agent-harnesses-scaffolds` (core) — the concept; deep dive lives in `harness-engineer-roadmap`
- `agent-evaluation` (core)
- `agent-safety` (core)
- **Sideways:** `→ harness-engineer-roadmap` (depth peer)

### Stage 10 — Evaluation & Observability (8 nodes)
- `eval-task-benchmarks` (core)
- `eval-llm-as-judge` (core)
- `eval-golden-datasets` (core)
- `eval-ab-testing` (recommended)
- `eval-tracing-observability` (core)
- `eval-harnesses` (recommended)
- `eval-cost-monitoring` (recommended)
- `eval-continuous-production` (core)

### Stage 11 — Deployment & Production (8 nodes)
- `prod-api-design` (core)
- `prod-latency-slos` (core)
- `prod-caching` (core)
- `prod-rate-limit-fallback` (core)
- `prod-secrets-access` (core)
- `prod-multi-tenant` (recommended)
- `prod-mlops-llmops` (recommended)
- `prod-cost-engineering-at-scale` (core)

### Stage 12 — Safety, Alignment & Frontier (8 nodes)
- `frontier-alignment-basics` (core)
- `frontier-jailbreaks-prompt-injection` (core)
- `frontier-red-teaming` (recommended)
- `frontier-mech-interp` (recommended)
- `frontier-reasoning-models` (core)
- `frontier-long-context` (recommended)
- `frontier-open-research` (recommended)
- `frontier-career-community` (core) — peer link to `llm-interview-prep`; staying current; contributing

**Totals:** 12 stages, 96 nodes. About 60 core + 30 recommended + 6 optional.

### Dependency edges (high-level)
- Stage forward dependency: each stage depends on the previous one's core nodes (a single forward edge between stages in the visual layout to keep the diagram clean).
- Within-stage dependencies: explicit when meaningful (e.g., `tx-self-attention → tx-multi-head-attention → tx-architecture`).
- Cross-stage dependencies: kept minimal and **dotted** in the diagram to avoid edge spaghetti. Example: `dl-embeddings-representations` (Stage 4) feeds `rag-embeddings` (Stage 8); shown as one dotted edge.

The exact edge list is materialized in `roadmap-data/` in Phase 2.

---

## 2. The structured data model (source of truth)

**Format:** JSON. (Universally toolable; validatable with a JSON Schema; no YAML indentation foot-guns; trivially diffable in PRs.)

**Layout:**
```
roadmap-data/
  manifest.json                 # top-level metadata + stage order + curator info
  schema/
    stage.schema.json           # JSON Schema for stage files
    node.schema.json            # JSON Schema for node files (referenced by stages)
    resource.schema.json        # JSON Schema for resource entries
  stages/
    01-prerequisites-math.json
    02-programming-tooling.json
    03-ml-fundamentals.json
    04-dl-fundamentals.json
    05-transformers-llm-internals.json
    06-training-finetuning.json
    07-inference-serving.json
    08-retrieval-rag.json
    09-agents-harnesses.json
    10-evaluation-observability.json
    11-deployment-production.json
    12-safety-alignment-frontier.json
  edges.json                    # cross-stage edges only; within-stage edges live in node entries
  peers.json                    # the constellation: harness-engineer-roadmap, llm-interview-prep, build-your-own-ai
```

### `manifest.json` (shape)
```json
{
  "schemaVersion": "1.0",
  "title": "AI Engineer Roadmap",
  "tagline": "An interactive roadmap for becoming — and growing as — an AI engineer. Curated by an active AI researcher.",
  "curator": {
    "name": "Betty Guo (Dongxin Guo, 郭东欣)",
    "affiliation": "PhD candidate, Department of Computer Science, University of Hong Kong",
    "advisor": "Prof. Siu-Ming Yiu",
    "github": "bettyguo",
    "orcid": "0009-0000-2388-1072"
  },
  "license": { "content": "CC-BY-4.0", "code": "MIT" },
  "lastUpdated": "2026-05-14",
  "liveSite": "https://bettyguo.github.io/ai-engineer-roadmap/",
  "stages": [
    "01-prerequisites-math",
    "02-programming-tooling",
    "03-ml-fundamentals",
    "04-dl-fundamentals",
    "05-transformers-llm-internals",
    "06-training-finetuning",
    "07-inference-serving",
    "08-retrieval-rag",
    "09-agents-harnesses",
    "10-evaluation-observability",
    "11-deployment-production",
    "12-safety-alignment-frontier"
  ]
}
```

### `stages/<NN>-<slug>.json` (shape)
```json
{
  "id": "05-transformers-llm-internals",
  "stageNumber": 5,
  "title": "Transformers & LLM Internals",
  "blurb": "How a modern LLM is built, from self-attention up.",
  "color": "#7C3AED",       // assigned per stage from the palette in §4
  "nodes": [
    {
      "id": "tx-architecture",
      "label": "The Transformer architecture",
      "status": "core",                  // core | recommended | optional
      "description": "One paragraph: what the transformer is, why it won, what to study.",
      "doneWhen": "You can sketch a decoder-only transformer's forward pass on a whiteboard.",
      "position": { "x": 0, "y": 0 },     // hand-laid coordinates; see §4
      "dependsOn": ["tx-self-attention", "tx-multi-head-attention"],
      "crossStageDependsOn": [],          // node ids from other stages, rendered dotted
      "resources": [/* see Resource schema below */]
    }
  ],
  "sidewaysLinks": [                       // present on stage 9
    {
      "to": "harness-engineer-roadmap",
      "url": "https://github.com/bettyguo/harness-engineer-roadmap",
      "label": "Going deep on this stage",
      "blurb": "This stage summarizes agents and harnesses. For the depth dive on building harnesses end-to-end — scaffolds, control loops, eval, hardening — see the peer roadmap."
    }
  ]
}
```

### Resource entry schema
```json
{
  "title": "Attention Is All You Need",
  "author": "Vaswani et al.",
  "year": 2017,
  "type": "paper",
  "url": "https://arxiv.org/abs/1706.03762",
  "annotation": "The original transformer paper. Required reading.",
  "difficulty": "intermediate",
  "free": true,
  "addedAt": "2026-05-14",
  "verifiedAt": "2026-05-14",
  "verifiedBy": "curator"
}
```

**`type` enum:** `paper` | `course` | `repo` | `book` | `video` | `blog` | `tool` | `official` | `interactive`.
**`difficulty` enum:** `intro` | `intermediate` | `advanced`.
**`status` enum:** `core` | `recommended` | `optional`.

### Hard rules enforced by `tools/validate_data.py`
1. ≤8 resources per node (adopted from `developer-roadmap`).
2. Every resource has `title`, `url`, `type`, `annotation`, `addedAt`, `verifiedAt`.
3. Every `dependsOn` and `crossStageDependsOn` resolves to a real node id.
4. No orphan nodes (every node is reachable along a dependency chain or is a stage root).
5. Every node has a non-empty `description` and `doneWhen`.
6. Every `addedAt` and `verifiedAt` is an ISO date ≤ today.
7. The 12 stages and the node count match the taxonomy (§1) — guards against accidental drift.

---

## 3. The renderer architecture

### Stack
- **Vite + React + TypeScript** — minimal, fast, statically-buildable.
- **React Flow (xyflow.com)** — the canonical React node-graph library. Renders nodes as React components (so resource panels can be rich), supports pan/zoom/drag, has stable styling APIs.
- **Tailwind CSS** — speed of iteration; small bundle when purged.
- **No backend.** Everything is a static site; data is bundled at build time.

### Information architecture
- **Top bar:** title, curator credit, "last updated" badge, GitHub link, "Recently added" link.
- **Left sidebar:** stage list (12 entries, each a colored chip); clicking a stage scrolls the diagram to that cluster and dims the others.
- **Center:** the pannable / zoomable node graph.
- **Right panel (opens on node click):** node title, status chip, one-paragraph description, "done when" criteria, the ≤8 resource list with annotations and type icons.
- **Footer:** the constellation peer-link block (the four-repo set).

### Layout strategy: hand-laid positions, not auto-layout
- Auto-layout (dagre, elkjs) produces visually-mediocre roadmaps. Every successful roadmap (developer-roadmap, system-design-primer's diagrams) is hand-laid.
- Each node gets explicit `{x, y}` coordinates in its stage file. The renderer reads these and lays the graph deterministically.
- A spacing convention: stages are vertical columns (or rows, decided below); nodes within a stage are arranged in a 2- or 3-column local grid.

### Diagram orientation
- **Top-to-bottom, vertical-scrolling.** Matches the chronological "study path" mental model and the convention readers know from `developer-roadmap`. Stages stack downward.
- Within each stage, nodes flow left-to-right in a 2- or 3-column local grid.

### Visual grammar (drives readability)
- **Color = stage.** A 12-color palette (one per stage), chosen for distinguishability on both light and dark backgrounds.
- **Node weight = status.** Solid filled background = core. Outlined / tinted background = recommended. Hatched / muted = optional.
- **Edge style = dependency type.** Solid edge = required dependency. Dotted edge = optional / cross-stage suggestion.
- **Node shape = node type.** Rounded rectangle for content nodes; chevron/badge for stage-headers; pill for sideways-peer link cards.

### Interactions
- Pan & zoom (mouse drag + wheel; pinch on touch).
- Click node → right panel opens with resource list.
- Click resource link → opens in new tab.
- Keyboard: `/` focuses search; `?` opens shortcuts; arrow keys move panel selection.
- URL hash carries selected node id (`#tx-architecture`) so a clicked node is shareable.

### Performance
- All 96 node components rendered statically; React Flow virtualizes off-screen nodes for scroll perf.
- Resource panels are bundled — no runtime fetches.
- Diagram screenshot at high-res is exported at build time for use as the social card / README hero.

---

## 4. Aesthetic direction (substituting for the missing `frontend-design` skill)

Three explicit anti-patterns to reject (the field is full of all three):
1. **Generic "boxes on a flowchart" aesthetic.** Every existing AI roadmap looks like a brainstorm in a default whiteboard tool.
2. **AI-slop gradients + neon glow.** Pattern-matched as "made by AI in five minutes."
3. **Material/Bootstrap default styling.** Reads as a corporate dashboard, not a knowledge artifact.

Direction chosen:
- **Editorial, not productized.** It should look like a serious book's frontmatter, not a SaaS landing page.
- **Dark background as primary, with a paper-warm alternative.** Sets it apart from every other roadmap (all of which are light-mode-only). The diagram against a dark canvas with colored stage clusters has the highest screenshot legibility.
- **A single elegant sans-serif** (Inter or similar) for UI; a serif (e.g., Source Serif or IBM Plex Serif) for node titles to convey editorial weight.
- **Restrained, high-contrast palette.** 12 stage colors picked from a shared HSL ring with consistent saturation and luminance so they read as a *system*, not a parade.
- **Tight visual rhythm.** Consistent node sizes within a status class; consistent spacing; no decorative ornaments.
- **One signature flourish.** A subtle hand-drawn-feeling underline or chevron under stage titles to mark this as curator-made, not auto-generated. (A single deliberate detail differentiates more than ten tasteful ones.)

This direction will be confirmed by screenshot review in Phase 3 and revisable by the maintainer.

---

## 5. Repo architecture

```
ai-engineer-roadmap/
  README.md                       # noun-as-title + anxiety opener + hero diagram + live link
  LICENSE                         # MIT for code
  LICENSE-CONTENT                 # CC-BY-4.0 for the roadmap content
  CONTRIBUTING.md                 # PR rules: verification link + annotation required
  CITATION.cff                    # for academic citation
  CHANGELOG.md                    # human-readable "what changed when"
  .gitignore
  .gitattributes

  roadmap-data/                   # the STRUCTURED SOURCE OF TRUTH
    manifest.json
    edges.json
    peers.json
    schema/
      stage.schema.json
      node.schema.json
      resource.schema.json
    stages/
      01-prerequisites-math.json
      ...
      12-safety-alignment-frontier.json

  site/                           # the interactive renderer (Vite + React + React Flow)
    package.json
    pnpm-lock.yaml
    tsconfig.json
    vite.config.ts
    index.html
    public/
      og-card.png                 # social card
      favicon.svg
    src/
      main.tsx
      App.tsx
      data.ts                     # imports roadmap-data/*.json
      components/
        Diagram.tsx               # the React Flow canvas
        NodeCard.tsx
        StageHeader.tsx
        ResourcePanel.tsx
        TopBar.tsx
        StageSidebar.tsx
        PeerFooter.tsx
        SearchPalette.tsx
      styles/
        theme.css

  content/                        # generated: static markdown fallback view (one file per stage)
    01-prerequisites-math.md
    ...

  tools/
    linkcheck.py                  # GET every resource URL; flag non-200s
    validate_data.py              # JSON-Schema + cross-ref validation
    build.py                      # data -> static markdown content/; copy data into site/src/data
    export_diagram.py             # post-build: take a high-res screenshot of the live diagram for hero/og-card

  assets/
    diagram-hero.png              # the marketing screenshot (referenced from README)
    diagram-hero.svg              # editable vector source (when available)
    social-card-1200x630.png
    MAKE_BANNER.md                # if image generation is unavailable, exact spec lives here

  docs/
    DEPLOY.md                     # the human-runnable deploy recipe (mandatory fallback)
    LAUNCH.md                     # show-HN, X, Reddit, newsletter drafts
    MAINTENANCE.md                # monthly cadence + linkcheck schedule
    PROFILE_SNIPPET.md            # snippet for the bettyguo profile README

  .github/
    workflows/
      ci.yml                      # lint + validate_data + linkcheck + build
      deploy.yml                  # build the site, deploy to gh-pages
      linkcheck-schedule.yml      # weekly cron: run linkcheck on main, open an issue if rot
    PULL_REQUEST_TEMPLATE.md
    ISSUE_TEMPLATE/
      add-resource.yml
      fix-resource.yml
      add-node.yml
      bug.yml

  PLANNING/                       # the planning trail (THINK + DESIGN + verification log + review)
    00_think.md
    01_design.md
    04_verification_log.md
    06_review.md
```

Single-file size limit: **no source file > 500 lines**, including JSON data files. (If a stage file approaches this limit, split nodes into a sub-folder of node files referenced from the stage manifest.)

---

## 6. README wireframe

```
# AI Engineer Roadmap

> An interactive roadmap for becoming — and growing as — an AI engineer.
> The whole career path, from math and programming to the research frontier,
> with curated and verified resources on every node. Curated by an active AI researcher.

[![Last updated: 2026-05-14](badge)] [![License CC-BY-4.0 / MIT](badge)] [![Star History](badge)]

[![Diagram screenshot](assets/diagram-hero.png)](https://bettyguo.github.io/ai-engineer-roadmap/)

→ **[Open the interactive roadmap →](https://bettyguo.github.io/ai-engineer-roadmap/)**

## Why this exists

AI engineering moves so fast that no single course, blog, or thread holds the
whole picture. This roadmap is the picture: every stage, every required idea,
the best one or two resources for each, kept current.

## How to use this roadmap

- **CS student / new grad:** read top-to-bottom.
- **Working engineer pivoting in:** skim Stages 1–4, focus on 5–11.
- **Working AI engineer:** the **Recently added** view, the **Frontier** stage.

## Scope

Breadth: the whole AI-engineer career path. Stage 9 (Agents & Harnesses)
deliberately summarizes — for the depth dive on harness engineering,
see the peer roadmap **harness-engineer-roadmap**.

## The constellation (peer roadmaps & artifacts)

- **harness-engineer-roadmap** — the depth roadmap for the Agents & Harnesses stage.
- **llm-interview-prep** — interview preparation for AI engineer roles.
- **build-your-own-ai** — hands-on "build it yourself" companion.

Each is a standalone equal; this roadmap points sideways to them, not down.

## How this roadmap is maintained

- Monthly pulse: a CHANGELOG entry + a frontier review.
- Weekly: automated link-check (CI cron), broken links opened as issues.
- PRs welcome — see CONTRIBUTING.md.

## Curator

**Betty Guo (Dongxin Guo, 郭东欣)** — PhD candidate (final year),
Department of Computer Science, University of Hong Kong, advised by
Prof. Siu-Ming Yiu.
GitHub: [@bettyguo](https://github.com/bettyguo) · ORCID: [0009-0000-2388-1072](https://orcid.org/0009-0000-2388-1072)

## License

Content: CC-BY-4.0. Code: MIT.

## Citation

If you use this roadmap in academic or educational work, see CITATION.cff.

[Star history embed]
```

---

## 7. Hosting plan

- **Live URL target:** `https://bettyguo.github.io/ai-engineer-roadmap/`.
- **Mechanism:** GitHub Actions builds `site/` with Vite (`pnpm install && pnpm build`), uploads `site/dist/` as a Pages artifact, deploys via `actions/deploy-pages`.
- **Branch:** Pages is sourced from GitHub Actions, not a `gh-pages` branch.
- **Fallback:** if Pages cannot be enabled (private repo / org policy), `docs/DEPLOY.md` provides a 5-step manual deploy recipe to Cloudflare Pages or Netlify (both are zero-config for static sites; the `site/dist/` output is portable).
- **The fallback recipe is mandatory and tested**, not optional — the live site is what makes "interactive" real.

---

## 8. Tooling design

All scripts stdlib-first where possible. Python 3.11+.

### `tools/validate_data.py`
- Loads `roadmap-data/manifest.json` and every `stages/*.json`.
- Validates each against the JSON Schema files in `roadmap-data/schema/`.
- Enforces the hard rules from §2 (resource cap, required fields, ID resolution, no orphans, date sanity, taxonomy stability).
- Exit code 0 on pass, 1 on fail. Prints a numbered error list.
- Used by CI on every push and by the PR template's checklist.

### `tools/linkcheck.py`
- Walks every resource URL in `roadmap-data/`.
- Issues a HEAD (fallback GET) with a sensible UA + 10s timeout + 1 retry.
- Whitelist: arxiv.org, github.com, well-known publishers.
- Output: a Markdown report with status code per URL.
- Exit 0 if all 2xx/3xx; exit 1 on any 4xx/5xx (configurable severity).
- CI runs it weekly via `linkcheck-schedule.yml`; failures open an issue with the failing URL list.

### `tools/build.py`
- Reads `roadmap-data/` and emits:
  - `content/<NN>-<slug>.md` — one human-readable markdown view per stage (SEO + JS-disabled fallback).
  - `site/src/data.generated.ts` — a typed import wrapping the data for the renderer (this keeps the renderer build-time-safe; if validation fails, build fails).
- Idempotent. Pure function of the data.
- CI builds the site only after `validate_data.py` and `build.py` both succeed.

### `tools/export_diagram.py`
- Optional, run post-deploy: uses Playwright to screenshot the live diagram at 1920×1080 and 1200×630 for the social card.
- Output: `assets/diagram-hero.png` and `assets/social-card-1200x630.png`.

---

## 9. Contribution flow

`CONTRIBUTING.md` rules:
1. **New resource on an existing node** — submit a PR that adds the resource entry to the relevant `stages/*.json`. Required: `url` that resolves, `annotation` (the "why this one" line), `addedAt`, `verifiedAt`. CI runs `validate_data.py` and `linkcheck.py`.
2. **New node** — open an Issue first (`.github/ISSUE_TEMPLATE/add-node.yml`) with the rationale + proposed stage + 1–3 candidate resources. Curator triages before PR.
3. **Fixing a broken/wrong resource** — direct PR or use the `fix-resource.yml` issue template.

PR template (`.github/PULL_REQUEST_TEMPLATE.md`) is a checklist:
- [ ] `validate_data.py` passes locally
- [ ] `linkcheck.py` passes for any URL added
- [ ] Every new resource has an `annotation` ("why this one" in ≤25 words)
- [ ] No node exceeds the 8-resource cap
- [ ] CHANGELOG.md updated under "Unreleased"

---

## 10. Test / verification plan

| Check | Mechanism | When |
|---|---|---|
| Data validity (schema + hard rules) | `tools/validate_data.py` | every push, every PR |
| Link health | `tools/linkcheck.py` | every push, every PR; weekly cron |
| Build reproducibility | `pnpm build` in site/ | every push |
| Site renders | Playwright smoke test (1 test: open the deployed page, assert diagram canvas present) | every deploy |
| Interactive behavior | Manual: pan, zoom, click 5 random nodes, check resource links open | Phase 3, Phase 5, Phase 6 |
| Resource correctness (existence + author + year accuracy) | Manual curator pass logged in `PLANNING/04_verification_log.md` | Phase 4 |
| Aesthetic — "is this distinctive?" | Manual review against §4; screenshot at thumbnail size and ask "does it look generic-AI?" | Phase 3, Phase 5, Phase 6 |

---

## 11. Decisions confirmed (overriding Phase 0 defaults)

- Live URL: `https://bettyguo.github.io/ai-engineer-roadmap/` ✓
- Data format: JSON ✓
- Agents & Harnesses stage: 8 nodes + sideways pointer to depth peer ✓
- Frontier scope: alignment, jailbreaks, red-teaming, mech interp, reasoning models, long context, open research; no ASI speculation ✓
- Diagram orientation: top-to-bottom ✓
- Palette: 12 stage colors on a dark canvas (primary), paper-warm alternative as the secondary theme ✓
- Stack: Vite + React + TypeScript + React Flow + Tailwind ✓
- Hosting: GitHub Pages via Actions; documented fallback to Cloudflare Pages / Netlify ✓

Proceed to Phase 2.
