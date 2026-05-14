# Phase 4 — Verification log

**Date:** 2026-05-14.
**Status at sign-off:** 12 stages, 106 nodes, **227 unique resource URLs verified** (`python tools/linkcheck.py` — all 2xx/3xx).

## Method

For each node in `roadmap-data/stages/*.json`:

1. The curator selected 2–5 resources per node, drawn from a pool of canonical
   references in the field. The aim is curatorial judgment — not breadth.
2. Major canonical resources (Karpathy, 3Blue1Brown, Goodfellow, Vaswani et
   al., Stanford CS336, fast.ai, Hugging Face course, Anthropic / OpenAI
   docs, Eugene Yan / Lilian Weng / Sebastian Raschka writing, vLLM / TGI
   / SGLang / llama.cpp repos, the canonical arxiv papers for each
   subfield) were web-searched first to confirm the URL, author, and year
   currently in use.
3. Less-canonical resources (smaller blogs, niche tools) — when used at
   all — were spot-checked.
4. After population, `python tools/linkcheck.py` ran across the data and
   the curator triaged every 4xx/5xx response.
5. Failed URLs were either replaced with a working alternative (when the
   original page had moved or been removed), or added to
   `tools/.linkcheck-ignore` with documented justification (anti-bot
   blockers and rate-limiters that nonetheless serve real content to
   real browsers, plus pre-launch self-references to peer repos that
   don't exist yet).

## Resource counts (per stage at sign-off)

| Stage | Nodes | Resources |
|---|---|---|
| 01 Prerequisites & Math | 8 | 19 |
| 02 Programming & Tooling for AI | 8 | 23 |
| 03 Machine Learning Fundamentals | 10 | 22 |
| 04 Deep Learning Fundamentals | 10 | 23 |
| 05 Transformers & LLM Internals | 8 | 19 |
| 06 Training & Fine-tuning | 10 | 22 |
| 07 Inference & Serving | 10 | 28 |
| 08 Retrieval & RAG | 10 | 23 |
| 09 Agents & Harnesses | 8 | 18 |
| 10 Evaluation & Observability | 8 | 18 |
| 11 Deployment & Production | 8 | 19 |
| 12 Safety, Alignment & Frontier | 8 | 19 |
| **Total** | **106** | **~253 resource entries** *(227 unique URLs after dedup; many resources are referenced by multiple nodes)* |

## Replacements made during triage

| Original URL | Replaced with | Reason |
|---|---|---|
| `https://www.3blue1brown.com/topics/linear-algebra` | `https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab` | 3Blue1Brown site moved to a `?topic=` query-parameter scheme; YouTube playlist is the resilient canonical URL. |
| `https://www.3blue1brown.com/topics/calculus` | `https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr` | Same as above. |
| `https://projects.iq.harvard.edu/stat110` | `https://projects.iq.harvard.edu/stat110/about` | The bare path 403s; `/about` is the canonical landing page (and is also bot-blocked, so the path was added to the ignore list separately). |
| `https://karpathy.medium.com/yes-you-should-understand-backprop-…` | `https://medium.com/@karpathy/yes-you-should-understand-backprop-…` | The `karpathy.medium.com` subdomain form 403s; the `medium.com/@karpathy/` canonical form also 403s but is the right URL, so the medium.com prefix is in the ignore list. |
| `https://www.biostat.wisc.edu/~page/rocpr.pdf` | `https://mark.goadrich.com/articles/davisgoadrichcamera2.pdf` | Original author page moved; co-author's site hosts the canonical PDF. |
| `https://kipp.ly/transformer-inference-arithmetic/` | `https://kipp.ly/transformer-inference-arithmetic` *(no trailing slash)* | Trailing slash 404s on kipp.ly. The host blocks `HEAD` from the linkcheck UA so the prefix is also in the ignore list; the URL serves content fine in a browser, confirmed via WebFetch. |
| `https://aws.amazon.com/blogs/database/best-practices-for-multi-tenant-saas-applications…` | `https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/silo-pool-and-bridge-models.html` | Original AWS blog post 404'd; the SaaS Lens whitepaper is the better canonical reference. |

## URLs in `tools/.linkcheck-ignore`

Bot-blockers and rate-limiters whose content is real but the linkcheck UA can't fetch. All of these were verified manually (browser or WebFetch) to confirm the content exists at the listed URL:

- `https://medium.com/@karpathy/` — Medium 403s bots.
- `https://platform.openai.com/docs` — OpenAI's docs site 403s bots.
- `https://openai.com/index/` — OpenAI's news / blog 403s bots.
- `https://www.neelnanda.io/` — Rate-limits aggressively (429).
- `https://projects.iq.harvard.edu/` — 403s bots.
- `https://dl.acm.org/` — ACM Digital Library 403s bots.
- `https://kipp.ly/` — Server returns 404 to `HEAD` requests for paths that serve normally on `GET` in a browser.

Pre-launch self-references (these resolve once the repos are created; remove them from `.linkcheck-ignore` after the bettyguo account is set up):

- `https://github.com/bettyguo/ai-engineer-roadmap`
- `https://github.com/bettyguo/harness-engineer-roadmap`
- `https://github.com/bettyguo/llm-interview-prep`
- `https://github.com/bettyguo/build-your-own-ai`
- `https://bettyguo.github.io/ai-engineer-roadmap/`

## Schema $id fix

The JSON Schema files originally used HTTP `$id`s like
`https://github.com/bettyguo/ai-engineer-roadmap/roadmap-data/schema/resource.schema.json`.
The link-checker walker picked these up as URLs to verify, but they are
identifiers, not URLs to fetch. Changed all three `$id`s to URN form
(`urn:ai-engineer-roadmap:schema:resource` etc.), which is valid per JSON
Schema and no longer pulled into the linkcheck walk.

## What is *not* in this verification log

- **Resource *quality* judgments.** That's curatorial work, not link-check
  work. Each resource has an `annotation` field that documents the
  curator's "why this one" reasoning; the PR template requires the same
  from contributors.
- **Whether the resource teaches the topic well.** A returning-200 URL is
  not the same as a useful resource. Sample reads will happen during
  Phase 6's hostile-reviewer pass.
- **Currency.** Resources go stale on a months-to-years timescale.
  `docs/MAINTENANCE.md` describes the monthly pulse + weekly automated
  linkcheck that keeps this verification live.
