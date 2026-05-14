# Changelog

All notable changes to this roadmap are recorded here. The roadmap follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) conventions, with a
monthly "pulse" entry that summarizes resource additions, revisions, and
removals.

## [Unreleased]

### Added (third enhancement pass, late 2026-05)
- **Six more new nodes** covering identified gaps:
  - `dl-vision-transformers` (Stage 4, core) — ViT as a first-class
    node, the bridge from transformers to multimodal. 3 verified
    resources (Dosovitskiy et al. paper, lucidrains/vit-pytorch,
    google/vit-base-patch16-224 model card).
  - `train-synthetic-data` (Stage 6, core) — the biggest post-training
    shift of 2025. 4 verified resources (Self-Instruct paper, Tülu 3
    paper, yizhongw/self-instruct repo, tatsu-lab/stanford_alpaca).
  - `inf-flashattention` (Stage 7, core) — was mentioned as a resource
    on multiple other nodes; promoted to its own. 4 verified resources
    (FlashAttention 1/2/3 papers + the Dao-AILab repo).
  - `agent-coding-agents` (Stage 9, recommended) — Claude Code, Aider,
    SWE-bench. 3 verified resources.
  - `eval-arena-elo` (Stage 10, recommended) — the Chatbot Arena
    pattern, pairwise crowdsourced preference with Bradley-Terry. 3
    verified resources (Chatbot Arena paper, LMSYS launch blog,
    lm-sys/FastChat).
  - `frontier-test-time-compute` (Stage 12, recommended) — distinct
    from `frontier-reasoning-models`; the underlying scaling-law
    paradigm. 3 verified resources (Snell et al., Lightman et al.,
    DeepSeek-R1).
- **Three more new docs:**
  - `docs/SUGGESTED_PROJECTS.md` — one concrete project per stage,
    ~1-3 days each, designed so completing all twelve assembles into
    a coherent portfolio.
  - `docs/CAREER_LADDERS.md` — maps the roadmap onto L1/L2/L3/L4
    AI-engineer levels with comp-band context, hiring-loop framing,
    and the "PhD or not" question addressed honestly.
  - `docs/WHAT_CHANGED.md` — the monthly-pulse changelog template, with
    the launch-month entry as the first row.
- **Two governance files:**
  - `SECURITY.md` — vulnerability and abuse reporting policy.
    Defines what counts as a security issue for a content artifact
    (malicious URLs, doxxing in PRs, supply-chain attacks on the
    renderer) vs. ordinary maintenance.
  - `MAINTAINERS.md` — single-curator model rationale, decision rules,
    COI disclosure norms, and the soft + hard succession protocol.
- **New tool: `tools/stats.py`** — canonical count source. Emits
  stages / nodes / resources / unique URLs / status breakdown /
  type breakdown / difficulty / free-paid / per-stage rollup. Used to
  keep the README, SVGs, and CHANGELOG count claims from drifting
  apart.

### Fixed
- Broken `eugeneyan.com/writing/shadow-mode/` URL on
  `prod-canary-shadow-rollout` swapped for the verified Christopher
  Samiullah writeup of the same pattern.

### Changed
- Node count 110 → 122 (six explicit additions + six from concurrent
  curation in stages 2, 8, 9, 10, 11).
- Auto-verified URL count 245 → 276.
- Total resources in the data 272 → 317.
- README opening framing updated; `122 nodes, 276 link-verified
  resources`. Reading-paths section now also links the new docs.
- SVG hero and social card counts updated and re-synced into
  `site/public/og-card.svg`.

### Added (second enhancement pass, 2026-05-14)
- **Four new nodes** closing Phase 6 GAPS-ISSUE items #1, #2, #3, plus
  one not previously on the backlog:
  - `frontier-state-space-models` (Stage 12) — Mamba and the SSD
    framework. 4 resources (Mamba paper, Mamba-2, the canonical repo,
    Maarten Grootendorst's visual guide).
  - `frontier-multimodal` (Stage 12) — vision-language models. 4
    resources (CLIP, LLaVA, LLaVA-1.5, the LLaVA project page).
  - `inf-disaggregated` (Stage 7) — disaggregated prefill/decode
    serving. 3 resources (DistServe paper, Splitwise paper,
    DistServe reference implementation).
  - `agent-computer-use` (Stage 9) — computer-use agents. 3 resources
    (Anthropic's Computer Use announcement, the API docs, Simon
    Willison's day-one exploration).
- **Three new docs** the README already referenced but did not previously
  carry:
  - `docs/READING_PATHS.md` — three concrete reader-shaped subsets of
    the map with node-by-node order, honest time budgets, and "one
    project to lock it in" per path.
  - `docs/FAQ.md` — the questions every roadmap reader asks. How long
    does it take, do I need a PhD, can I skip math, why not roadmap.sh,
    how the maintenance posture works.
  - `docs/GLOSSARY.md` — A–Z terminology lookup, each term pointing to
    the node where it's developed. ~60 entries.

### Changed
- Node count 106 → 110; verified resource count 231 → 245.
- `tools/validate_data.py` EXPECTED_STAGES updated for the new node counts
  (Stage 7: 10→11, Stage 9: 8→9, Stage 12: 8→10).
- README opening framing updated (`110 nodes, 245 link-verified resources`)
  and reading-path section now links the new docs.
- `assets/diagram-hero.svg` and `assets/social-card-1200x630.svg` updated
  to reflect the new counts; the OG-card SVG was re-synced.

## [0.1.0] — 2026-05-14

### Added
- Initial release: the full 12-stage / 96-node taxonomy of the AI-engineer
  career path.
- Structured data model in `roadmap-data/` with JSON Schemas for stages,
  nodes, and resources.
- Tooling: `tools/validate_data.py`, `tools/linkcheck.py`,
  `tools/build.py`.
- CI: data validation on every push, link-check on every push and on a
  weekly cron.
- Interactive site: Vite + React + React Flow renderer with pan, zoom,
  click-for-resources, search, and a dark/paper-warm theme.
- README, CONTRIBUTING, CITATION.cff, dual licensing (content CC-BY-4.0
  / code MIT).
- Curated and link-verified resource entries on every node.
- Constellation peer-link block to `harness-engineer-roadmap`,
  `llm-interview-prep`, `build-your-own-ai`.
- Sideways hand-off card from the Agents & Harnesses stage to
  `harness-engineer-roadmap` for the depth dive.
