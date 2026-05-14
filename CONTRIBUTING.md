# Contributing

This is a curated knowledge artifact, not a free-for-all link dump. PRs
that follow the rules below land quickly. PRs that don't will be asked to
revise, even from well-meaning contributors.

## What kinds of contributions are most useful

In rough order of value:

1. **A better resource for an existing node** — the existing pick is
   stale, paywalled, was deprecated, or there is genuinely something
   better. PR welcome.
2. **A broken link, wrong author, wrong year, wrong title** — fix it,
   either directly via PR or via the `fix-resource` issue template.
3. **A missing node** — something the roadmap doesn't cover but should.
   Open the `add-node` issue first; the curator triages before a PR.
4. **A new stage** — rare. Open an issue with a substantial rationale.
5. **Renderer / tooling improvements** — see the `bug` issue template.

## The hard rules (enforced by `tools/validate_data.py` in CI)

Every resource entry must have:

- A `url` that resolves (`linkcheck.py` enforces this).
- An `annotation` — a one-line "why this one" in ≤25 words. **No annotation,
  no merge.** The annotation is what separates this roadmap from a link
  list.
- `addedAt` and `verifiedAt` as ISO dates (`YYYY-MM-DD`) ≤ today.
- A `type` from the enum (`paper`, `course`, `repo`, `book`, `video`,
  `blog`, `tool`, `official`, `interactive`).
- A `difficulty` from the enum (`intro`, `intermediate`, `advanced`).
- A `free` boolean (true if the resource is free to access; false if
  paywalled). Free is not required, but the marker is.

Every node has a **maximum of 8 resources.** This cap is the single most
important rule. If you're adding a 9th, you must propose one to remove.
The cap is what forces curatorial judgment instead of link-dump drift.

## How to add a resource (the common case)

1. Fork the repo.
2. Edit `roadmap-data/stages/<NN>-<slug>.json` and add an entry to the
   relevant node's `resources` array.
3. From the repo root: `python tools/validate_data.py` (must pass) and
   `python tools/linkcheck.py --only-changed` (must pass).
4. Add a line to `CHANGELOG.md` under the `## Unreleased` heading.
5. Open the PR. CI re-runs both checks. The curator reviews for
   curatorial fit.

## How to propose a new node

1. Open an issue with the `add-node` template. Include:
   - Proposed stage and a 1-paragraph rationale (why this belongs here).
   - 1–3 candidate resources with annotations.
   - What the node's "done when" criterion would be.
2. The curator triages within a week. If accepted, you (or the curator)
   open a PR that adds the node, its edges, and its position in the
   stage's grid.

## Local development

Tooling (Python):

```
python tools/validate_data.py            # validate the data model
python tools/linkcheck.py                # check every resource URL
python tools/build.py                    # generate content/ and site data
```

Site (Vite + React; Node 20+ and pnpm):

```
cd site
pnpm install
pnpm dev          # local dev server
pnpm build        # production build to site/dist
```

## Code of conduct

Be respectful. Disagreement about resources or ordering is the entire
point of this repo and is welcome; personal attacks aren't. The curator
has final editorial say on what ships.

## Editorial bias is visible on purpose

Every resource has an annotation explaining *why this one*. That makes the
curator's bias legible and reviewable. If you disagree with a pick, the
"why this one" line is the right thing to argue against in a PR.
