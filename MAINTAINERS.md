# Maintainers & governance

This roadmap is a **single-curator artifact**. That's deliberate — the
editorial coherence argument in `PLANNING/00_think.md` only holds if
one person stands behind the picks. This doc explains who that is,
what they're responsible for, what they're not, and what happens if
they go away.

## Current curator

**Betty Guo (Dongxin Guo, 郭东欣)**
PhD candidate (final year), Department of Computer Science,
University of Hong Kong, advised by Prof. Siu-Ming Yiu.

- GitHub: [`@bettyguo`](https://github.com/bettyguo)
- ORCID: [0009-0000-2388-1072](https://orcid.org/0009-0000-2388-1072)
- Academic email: `dongxin DOT guo AT cs.hku.hk`

## What the curator is responsible for

1. **Editorial decisions.** Which nodes exist, which resources are
   picked, what the annotations say. The "why this one" judgment
   that makes this roadmap not a link dump.
2. **The monthly pulse.** A `CHANGELOG.md` entry + a
   [`docs/WHAT_CHANGED.md`](docs/WHAT_CHANGED.md) entry, on or near
   the 1st of each month. Silence past 8 weeks counts as a maintenance
   gap; see "succession" below.
3. **Triaging issues.** First-pass triage within a week of filing,
   per [`docs/MAINTENANCE.md`](docs/MAINTENANCE.md)'s SLAs.
4. **Security & abuse reports.** Per [`SECURITY.md`](SECURITY.md).
5. **The peer-roadmap constellation.** Keeping the sideways links to
   `harness-engineer-roadmap`, `llm-interview-prep`, and
   `build-your-own-ai` accurate and symmetric as those repos evolve.

## What the curator is NOT responsible for

1. **Personal study assistance.** Comments asking the curator to
   evaluate someone's individual learning path or career situation
   will be redirected to [`docs/READING_PATHS.md`](docs/READING_PATHS.md)
   or closed.
2. **Job referrals or interview practice.** Outside the scope of this
   repo. The peer companion [`llm-interview-prep`](https://github.com/bettyguo/llm-interview-prep)
   exists for that.
3. **Disputes between contributors.** The Code of Conduct applies; the
   curator will enforce it but won't mediate substantive technical
   disputes that aren't about the roadmap's contents.

## Decision rules

| Decision | Who decides | How |
|---|---|---|
| Add a resource to an existing node | Curator | PR review. CI must pass. |
| Swap a resource on a full (8-resource) node | Curator | PR review with explicit displacement target in the PR body. |
| Add a new node | Curator | Issue first (`add-node` template); the curator approves before any PR. |
| Remove a node | Curator only | After at least 4 weeks' "intent to deprecate" notice in `docs/WHAT_CHANGED.md`. |
| Add a new stage | Curator only | Requires a `PLANNING/` design doc and a 4-week public comment window. |
| Rename / re-scope a stage | Curator only | Same as adding a stage. |
| Code-only changes in `site/` or `tools/` | Curator or a trusted contributor | PR review. Outside contributors welcome; merging requires a curator review. |

## Conflict of interest

The curator commits to disclosing relevant COIs in `CHANGELOG.md`
under any node where the COI applies. Categories of COI to watch:

- **Co-authorship** with the authors of a recommended paper.
- **Employment / consulting / equity** in a recommended tool or
  product company.
- **Active collaboration** with a recommended researcher.

As of the launch date, the curator's only research COI is being a
collaborator-of-collaborators of several authors of the
constitutional-AI paper line; the relationship is no closer than
typical academic distance and does not gate the recommendation.

## Succession & continuity

This is the failure mode that kills single-curator OSS artifacts.
The plan:

### Soft-failure ladder

- **Weeks 0–8 since last commit:** Normal. The curator may be in a
  paper-writing or conference-prep period; no action needed.
- **Weeks 8–16:** A `linkcheck` cron failure is unaddressed, or the
  monthly pulse has been skipped twice. An issue is opened
  automatically (the weekly linkcheck issue acts as a tripwire);
  contributors should not interpret this as abandonment yet.
- **Weeks 16–26:** If contact attempts at the academic email and the
  GitHub address fail, a banner is added to the README pointing
  readers at the most recent stable commit and noting the curator is
  out of contact.
- **Beyond 26 weeks:** See "hard succession" below.

### Hard succession

If the curator becomes permanently unavailable, the repo passes to a
named successor under the following rules:

1. **Repository ownership** transfers to a new GitHub account
   designated in the curator's institutional records (UHK CS dept).
2. **The single-curator model continues.** Two people don't get the
   keys; the named successor is the new curator, with the same
   editorial latitude.
3. **The dual licensing** (CC-BY-4.0 content, MIT code) is
   irrevocable; even an unmaintained fork remains usable.

This protocol is documented privately with the curator's PhD advisor
(Prof. Siu-Ming Yiu) and with one external trusted contact.

## Becoming a regular contributor

If you've landed three or more curatorial PRs (substantive resource
or node contributions, not just typo fixes) and would like to be
trusted with more, open an issue introducing yourself. The curator
may then add you as a code-trusted reviewer for the `site/` and
`tools/` directories. **The editorial decisions remain
single-curator.**

## Why single-curator?

See [`PLANNING/00_think.md`](PLANNING/00_think.md) §3 (the lesson
from `system-design-primer`) and [`docs/FAQ.md`](docs/FAQ.md) ("Why
not just use roadmap.sh/ai-engineer?"). The short version: editorial
coherence loses immediately under committee-curation. The trade-off
is a higher bus-factor risk, which the succession protocol above
mitigates.
