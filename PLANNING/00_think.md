# Phase 0 — THINK

**Project:** `ai-engineer-roadmap` — a canonical, single-curator, interactive visual roadmap for the AI-engineer career path.
**Curator:** Betty Guo (Dongxin Guo / 郭东欣), PhD candidate (final year), University of Hong Kong, advised by Prof. Siu-Ming Yiu. GitHub: `bettyguo`. ORCID: 0009-0000-2388-1072.
**Date written:** 2026-05-14.

---

## 1. Noun validation

**Verdict:** The noun "AI engineer roadmap" is **partially contested but not canonically owned by a single standalone repo.** The slot for *"the focused, single-curator, end-to-end, interactive, citable standalone roadmap"* is genuinely open. Proceed — but with eyes open about the incumbents.

### What exists today

| Player | Format | What it is | Why it does not own the noun |
|---|---|---|---|
| `roadmap.sh/ai-engineer` (kamranahmedse/developer-roadmap, 354k★) | Interactive node graph | The strongest single page on the SEO. Part of a giant 354k-star platform. | **Scope-narrowed to "applied AI" only** ("uses pre-trained models" — explicitly NOT training, fine-tuning, internals, research). Community-curated within a platform, not a focused single-curator standalone. Cannot be forked, cited, or branded independently. One of dozens of roadmaps on a multi-topic site — no editorial voice specific to AI. |
| `dswh/ai-engineer-roadmap` (~628★) | Markdown only | A README-style guide with 3 levels (beginner / intermediate / advanced). | Markdown, no interactive diagram. 14 total commits — effectively stale. Links rot. |
| `AgenticAiLabs/Ai-Engineering-Roadmap` (~487★) | Markdown only | OSSU-style curated curriculum across 4 stages. | `roadmap.png` is marked "coming soon." Lots of words, no diagram. Not interactive. |
| `Ch-Balaji/ai-engineer-roadmap` | Static site + markdown | A 26-week structured 2026 plan with a GitHub-Pages site. | Single-author bootcamp-style plan; not a comprehensive map of the field. Strong on agents / production track only. Aesthetic is generic. |
| `krishnaik06/Complete-RoadMap-To-Learn-AI`, `PrinceSinghhub/Ultimate-AI-Engineer-Roadmap-2026`, etc. | Markdown / notes | Mostly personal study notes. | Thin, idiosyncratic, generally low star counts. |
| Medium / Scaler / Dataquest / KDnuggets / Coursera / Udemy "roadmap 2026" posts | Blog posts / paywalled courses | High SEO traffic. | Not citable, not maintained, not interactive, not open. |

### What "canonical" therefore requires
1. **Interactive node graph** (not markdown). The visual is the artifact people screenshot, share, and remember. The thin GitHub repos lose against `roadmap.sh` on this axis alone.
2. **End-to-end scope.** Cover the *whole* career path — math/programming → ML → DL → transformer internals → training & fine-tuning → inference & serving → retrieval/RAG → agents & harnesses → eval → deployment → safety & frontier. `roadmap.sh/ai-engineer` deliberately leaves out the model-internals and training/research half. That is the breadth gap.
3. **Single-curator editorial voice.** "One person stands behind this and has read the field" is what `system-design-primer` has and `roadmap.sh` cannot have. Especially when that one person is an active AI researcher publishing in the field — the trust signal compounds.
4. **Citable identity.** A real name, an ORCID, an institutional affiliation. None of the incumbents has this.
5. **Visible maintenance.** A "last updated" badge + a stated monthly cadence. AI moves so fast that "stale" is the dominant failure mode of every existing roadmap.
6. **Aesthetic distinctiveness.** The screenshot must be the asset that travels on launch. Generic AI-slop UI is fatal here — the incumbents already look generic; that is exactly where to differentiate.
7. **Hosted live site.** Interactive only works if it is clickable on the web. A GitHub Pages deploy is mandatory, not optional.

### How this is positioned honestly
This repo is **not** trying to dethrone `roadmap.sh` on the SEO of "AI engineer roadmap" (that fight is unwinnable in the short term — they are a 354k-star platform). It is trying to be the **standalone reference** people cite, fork, embed, and screenshot — the AI-engineer analogue of `system-design-primer` (an authoritative single-curator knowledge artifact that coexists with `roadmap.sh/system-design`, and is more cited in academic / serious contexts). Different game, different win condition.

---

## 2. Audience and anxiety map

The roadmap serves three readers. Each reader has a specific anxiety; the roadmap is the answer to that anxiety.

### Reader A — The CS student / new grad pivoting to AI
- **Anxiety:** "AI is moving so fast that whatever I learn in my degree will be obsolete. What do I actually study? I keep seeing 50-link Twitter threads and none of them agree."
- **What they need:** A trusted single source that says "study these things, in this order, and you will not be wasting your time." Wants the spine of the field plus the top one or two resources per node — not 20 alternatives.
- **Reading path:** Linear, stage-by-stage, top-to-bottom.

### Reader B — The working software engineer transitioning
- **Anxiety:** "I have shipped production systems for years but I do not know which AI fundamentals I am missing. I cannot tell which of the new tools (RAG, agents, MCP, vector DBs) are real and which are hype. I am embarrassed to start at the beginning."
- **What they need:** A map that lets them *self-locate* — "I already know these stages, I am weak on these stages, here is the missing piece." Heavy on tooling, eval, deployment, production patterns. Less time on math foundations.
- **Reading path:** Skip the early stages, zoom into the LLM / RAG / agents / deployment cluster.

### Reader C — The working AI engineer trying not to fall behind
- **Anxiety:** "I shipped my first RAG system 18 months ago and the field has moved twice since then. I do not know what 'frontier' means anymore. Is my stack about to be obsolete? What do I read this month?"
- **What they need:** Visible recency. A "recently added" / changelog. A "frontier" cluster that gets refreshed quarterly. Eval, safety, alignment, mech interp, RLHF/DPO, long-context, agent eval — the actively-evolving edge.
- **Reading path:** Goes straight to the "Recent additions" feed and the late-stage clusters.

**Implication for the artifact:** A roadmap that serves all three readers must be (a) linearly navigable for A, (b) skimmable / self-locatable for B, and (c) visibly fresh for C. The interactive node graph supports (a) and (b); the "last updated" badge and changelog support (c).

---

## 3. Competitive structural study

### Lesson from `kamranahmedse/developer-roadmap` (354k★)
- **The data is decoupled from the renderer.** Content lives as one-paragraph markdown files in `src/data/roadmaps/<slug>/content/<topic>.md`, with strict rules: a heading, a single explanatory paragraph, a `Visit the following resources to learn more:` section, ≤8 typed links per topic (`@official@`, `@article@`, `@course@`, etc.). The interactive editor renders against this.
- **Strict per-topic resource cap (≤8 links).** This is the most underrated rule in the whole project. Caps stop the roadmap from becoming a link dump and force curatorial judgment. We adopt the same rule.
- **Visual clustering by color + dotted vs solid edges.** Color codes status (core / recommended / optional). Dotted edges = optional. This is the *visual grammar* that makes the diagram readable at a glance. We adopt the same grammar.
- **The screenshot of the diagram is what travels.** Twitter threads, blog posts, LinkedIn — all use the diagram image. That image is the marketing asset. We design the diagram so its screenshot looks distinctive at thumbnail size.

### Lesson from `donnemartin/system-design-primer` (~290k★)
- **One curator's voice beats a platform.** People cite this README in interview prep as authoritative even though `roadmap.sh/system-design` also exists. Editorial coherence wins when the curator has real depth.
- **Definitive-on-day-one.** It launched with the full structure end to end. It did not grow into authority; it claimed it.

### Lesson from `codecrafters-io/build-your-own-x`
- **A long, complete list beats a curated short list when the topic is "I want to do X by hand."** Different shape from us — we are a *map*, not a *list of projects*. But the lesson stands: completeness signals authority.

### Recipe extracted
1. Open with the noun-as-title.
2. Anxiety-framed first two sentences in the README.
3. Diagram screenshot + live-site link prominently in the README (top fold).
4. ≤8 typed links per node, each with a one-line "why this one" annotation.
5. Visual grammar: stage = color cluster, status = node weight, dependency = edge, optional = dotted edge.
6. "Last updated" badge + maintenance cadence stated.
7. Curator attribution with citable identity.
8. PR template that makes contributions easy and force-checks link verification.

---

## 4. The scope partition (critical)

This repo and `harness-engineer-roadmap` are **standalone peers** — not flagship + companion, not parent + child. They must look like two different books on the same shelf, not one book and its appendix. The partition:

### `ai-engineer-roadmap` (THIS repo) — BREADTH
- The **entire** AI-engineer career path, end to end.
- ~10 stages, ~80–120 nodes total.
- Treats "Agents & Harnesses" as **ONE stage among ten**: covers it at a *summary* level — the concepts (tool use, planning, memory, multi-agent, eval, harness/scaffold concept), the canonical resources for each — and then *hands off sideways* to `harness-engineer-roadmap` for the depth dive.
- The home of the cross-stage view: math → frontier.
- ~8 nodes in the Agents & Harnesses stage. Not 40.

### `harness-engineer-roadmap` (PEER repo) — DEPTH
- A single craft: building agent harnesses / scaffolds.
- The depth dive that the breadth roadmap explicitly does NOT do.
- Lives at `bettyguo/harness-engineer-roadmap`, sibling URL in `bettyguo/`'s account.

### How they reference each other
- Symmetric, sideways. Never "see the parent" / "see the appendix."
- In **this** roadmap, the Agents & Harnesses stage has a prominent **"Going deep on this stage"** card pointing to `harness-engineer-roadmap`.
- In **that** roadmap, the "context" section has a **"This is one stage of the broader AI-engineer career path"** card pointing to `ai-engineer-roadmap`.
- README peer-link blocks use identical phrasing in both.

### What "summarized" means in the Agents & Harnesses stage of this repo
- ~8 nodes: tool use, function calling / MCP, planning patterns, memory & context engineering, multi-agent coordination, agent harnesses (the concept), agent evaluation, agent safety.
- Each node has 3–5 top resources.
- The stage closes with the sideways pointer.

### What this partition prevents
- Duplicated content drifting out of sync.
- Reader confusion ("which one do I open?"). Answer: open this one to see the whole field; open the other one when you decide to specialize in harness engineering.
- The two repos cannibalizing each other's stars. They serve different intents.

---

## 5. Interactive-format scoping

### Rendering approach
- **Stack:** Vite + React + React Flow (xyflow.com) + Tailwind. React Flow is the canonical library for pannable / zoomable / clickable node graphs in React; it renders nodes as real React components (so resource panels can be rich), supports custom edges and layouts, and is widely-deployed.
- **Why not Astro + custom editor like roadmap.sh:** roadmap.sh's custom editor is part of a monorepo with a private editing tool. We do not need editing-on-the-web; we need *viewing*-on-the-web. A static Vite SPA hosted on GitHub Pages is dramatically simpler and self-contained.
- **Why not Cytoscape / D3:** React Flow's node-as-React-component model is the right fit for "click a node → open a resource panel" interactions. Cytoscape is overkill and harder to style distinctively.
- **Why not custom SVG from scratch:** layout + interaction primitives (pan / zoom / drag) are nontrivial; we should not rebuild them.

### Data model drives rendering
- Source of truth: structured data files in `roadmap-data/` (one file per stage, JSON or YAML — decide in Phase 1).
- The renderer reads the data model and lays it out (manual coordinates per node, since auto-layout produces visually-mediocre roadmaps — every successful roadmap has been hand-laid).
- The data model is independently validatable (`tools/validate_data.py`) and link-checkable (`tools/linkcheck.py`) without running the renderer.

### Node-click interaction
- Click a node → side panel (or modal on mobile) opens with: node title, one-paragraph explanation, the resource list (≤8 typed links with annotations), the "done" criteria.
- Same content also generates a static markdown view (`build.py`) for SEO and JS-disabled accessibility.

### Hosting
- GitHub Pages (or Cloudflare Pages as fallback). CI builds and deploys on push to main.
- Live URL target: `https://bettyguo.github.io/ai-engineer-roadmap/`.
- The deploy step is automated; if blocked, a tested `docs/DEPLOY.md` recipe is the deliverable.

### Visual aesthetic direction (commit in Phase 1)
- Read `frontend-design` skill before any rendering work.
- Reject the default "boxes in a flowchart" aesthetic of every other AI-engineer roadmap. The screenshot must be distinctive at thumbnail size.

---

## 6. Constellation map

The standalone-equal peer set:
- **`bettyguo/harness-engineer-roadmap`** — the depth roadmap for the Agents & Harnesses stage. Sideways link from inside that stage and from the README footer.
- **`bettyguo/llm-interview-prep`** — a peer artifact for AI-engineer interview prep. Referenced from a "Preparing for AI engineer interviews" node in the late-stage cluster (around Deployment / Career).
- **`bettyguo/build-your-own-ai`** — a peer artifact for hands-on practice. Referenced from individual stage nodes where "build it yourself" is the right next step (e.g., "build your own transformer", "build your own RAG").

All four sit in the same author profile (`bettyguo`) as a constellation of complementary canonical artifacts: roadmap (this) + craft-depth (harness) + interview (llm-interview-prep) + hands-on (build-your-own-ai). README peer-link blocks make this constellation visible without subordinating any one to the others.

---

## 7. Risk log

| # | Risk | Severity | Mitigation |
|---|---|---|---|
| R1 | Contested noun — `roadmap.sh/ai-engineer` is the SEO incumbent. | High | Compete on editorial coherence, end-to-end scope (vs their applied-only scope), single-curator authority, citable academic identity, frontier-awareness, and aesthetic distinctiveness. Be honest about positioning — we are the standalone, not the platform. |
| R2 | Thin-launch risk — graph half-empty on day 1 reads as "another half-finished roadmap." | High | Build the **complete** data-model skeleton (every stage, every node, every edge) in Phase 2 *before* curating resources. Day-1 verdict is "complete map, deep curation on every node." |
| R3 | Two-roadmap confusion with `harness-engineer-roadmap`. | Medium | Strict scope partition (§4). Symmetric sideways framing. Identical peer-link wording in both READMEs. |
| R4 | Abandonment risk under a real academic name. | High | Visible "last updated" badge + monthly cadence stated. Automated linkcheck on CI schedule. PR template designed to make community contributions low-friction so maintenance is shared. |
| R5 | Interactive build is bigger than markdown — could blow up the timeline. | Medium | Decouple. Build the data model first; even if the renderer is a v1, the data model alone is shippable as a static markdown fallback. Renderer is additive. |
| R6 | JS-required interactive site hurts SEO + accessibility. | Medium | `build.py` emits a static markdown view of the whole roadmap from the same data model. Crawlers and JS-disabled readers see the full content. Meta tags + Open Graph card + social-image PNG of the diagram. |
| R7 | "AI-slop" aesthetic — generic-looking roadmap loses to a thoughtful one. | High | Mandatory: read `frontend-design` skill before building UI. Commit to a distinctive aesthetic direction in Phase 1. The screenshot is the marketing asset. |
| R8 | Link rot in curated resources. | Medium | `tools/linkcheck.py` on CI schedule (weekly). PR template requires verification link for every new resource. Verification log (`PLANNING/04_verification_log.md`) records every resource's check status. |
| R9 | Frontier nodes go stale fast (the field changes monthly). | High | A "Recently added" / "Recently revised" view, driven by per-resource `addedAt` and `revisedAt` metadata in the data model. Quarterly frontier review on the maintenance cadence. |
| R10 | Curatorial bias — picking favorites in a field with many alternatives. | Low | The ≤8-link cap forces explicit pick-the-best judgment. The "why this one" annotation makes the bias visible and reviewable. PRs can challenge picks. |

---

## 8. Open questions

These would normally be checkpoint clarifications; per the autonomous-run directive, defaults are recorded so the run can proceed.

1. **Live URL.** Default: `https://bettyguo.github.io/ai-engineer-roadmap/` on GitHub Pages. (Alternative: Cloudflare Pages on a custom domain — left to the maintainer after launch.)
2. **Data-model file format.** Default: JSON (universally toolable, validatable with a JSON Schema, no YAML indentation foot-guns). Decided in Phase 1.
3. **"Agents & Harnesses" stage size.** Default: 8 nodes (tool use, function calling / MCP, planning, memory & context, multi-agent, harnesses/scaffolds, agent eval, agent safety) — summarized, sideways link to depth repo at stage close. Decided in Phase 1.
4. **Frontier stage aggressiveness.** Default: cover RLHF/DPO, mech interp, evals, alignment, long-context, reasoning/o-style, agent safety. Do NOT speculate about ASI or capability timelines. Decided in Phase 1.
5. **Diagram orientation.** Default: top-to-bottom scroll (matches the chronological "study path" mental model, matches `roadmap.sh`'s convention so the visual grammar is familiar). Decided in Phase 1.
6. **Color palette.** Default: a small, hand-picked palette per stage (10 distinguishable colors), dark background as primary. Confirmed against `frontend-design` skill in Phase 1.

---

## 9. Decision: proceed

The noun is open enough, the structural gap is real, the editorial differentiation is genuine, and the risks are mitigable. Proceed to Phase 1 — DESIGN.
