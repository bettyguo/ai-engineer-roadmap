# Maintenance cadence

The visible commitment in the README is **monthly pulse + weekly linkcheck**.
That cadence is small enough to be sustainable next to a PhD; it is also
enough to keep a roadmap from going stale in 2026.

## Monthly pulse (1st of each month)

A single 30–60 minute pass:

1. Skim the Frontier stage (Stage 12) — is anything in there now obsolete
   or has anything new arrived that belongs?
2. Skim the Recently-added view (`CHANGELOG.md`'s last month) — is anything
   already out of date?
3. Open the `linkcheck` issues that the weekly cron raised (if any) and
   fix them.
4. Open `gh pr list --state open` — triage outstanding PRs.
5. Bump `roadmap-data/manifest.json` `lastUpdated` to today's date.
6. Add a `## YYYY-MM-DD pulse` entry to `CHANGELOG.md` summarizing what
   changed.
7. Push. CI deploys automatically.

## Weekly linkcheck

Runs automatically on Mondays at 13:00 UTC via
`.github/workflows/linkcheck-schedule.yml`. If anything breaks, the workflow
opens an issue with a markdown report listing the failing URLs. Fix them
during the monthly pulse, or earlier if the breakage is widespread.

## Frontier reviews (quarterly)

Every three months, do a deeper pass on Stage 12 specifically. The frontier
moves quickly. A node that was a "core" research area in 2026 Q1 might be
saturated, deprecated, or commodified by 2026 Q3.

## Annual taxonomy review

Once a year, sit with `PLANNING/01_design.md` and ask whether the taxonomy
itself is still right. New stages, retired stages, renamed stages. Update
`tools/validate_data.py`'s `EXPECTED_STAGES` if you change the spine.

## Sharing maintenance with contributors

The PR template (`.github/PULL_REQUEST_TEMPLATE.md`) is designed so that a
well-formed PR is mergeable in minutes. The hard rules (verified URL,
annotation, the 8-resource cap, date fields) are CI-enforced; the
curatorial review is the only thing the curator does by hand.

When a contributor steps up consistently, add them to `CITATION.cff` as a
co-author of the roadmap content and to the CHANGELOG as a recognized
maintainer.
