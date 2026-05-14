# FAQ

The questions every roadmap reader asks. Honest answers from the
curator.

---

## "How long does the full path take?"

**4–10 months end-to-end** at 15 hours / week from-scratch. **8–12
weeks** for an experienced software engineer who skims Stages 1–4
and focuses on 5–11. The realistic ranges are in [`READING_PATHS.md`](READING_PATHS.md).

Whatever number you saw in a YouTube thumbnail ("become an AI engineer
in 30 days") is marketing. Whatever number you saw in a research lab's
job posting ("5+ years of ML experience required") is also marketing.
Median engineers learn at median speeds.

---

## "Do I need a PhD?"

No. The roadmap is curated by a PhD candidate because that's who
wrote it, not because the field requires one. The vast majority of AI
engineering jobs in 2026 hire on demonstrated portfolio, not degree.

You need a PhD if you want to *do AI research* — push the frontier in
[Stage 12](../roadmap-data/stages/12-safety-alignment-frontier.json)'s
direction at a frontier lab or in academia. You do not need one to
ship AI products, design RAG systems, build agent harnesses, or earn
$150k–$300k.

---

## "Can I skip the math?"

You can skip the *proofs*. You cannot skip the *intuition*.

- You will not write a measure-theoretic proof of stochastic gradient
  descent's convergence.
- You will read a paper that says "we use a low-rank adaptation" and
  need to know what "rank" means.
- You will debug a model that won't train and need to know why
  normalization choices matter.

The [`math-how-much-is-enough`](../roadmap-data/stages/01-prerequisites-math.json)
node is the meta-answer; the rest of Stage 1 is the operational answer.
Practitioner-level fluency, not theorem-level.

---

## "Why not just use roadmap.sh/ai-engineer?"

That's a fine roadmap and it's part of a much bigger 354k-star
platform. Use it.

This roadmap is different in three deliberate ways:

1. **Scope.** `roadmap.sh/ai-engineer` is explicitly scoped to
   *applied AI* — using pre-trained models, not building or training
   them. This roadmap covers the whole career path including
   internals, training, and the research frontier.
2. **Voice.** This is a single curator with an editorial point of
   view and a citable academic identity. Disagreement with a pick
   has a place to land (the `Challenge a pick` issue template);
   community-curated roadmaps necessarily average toward the middle.
3. **Maintenance posture.** This repo has automated link-checking
   (weekly CI), a monthly pulse changelog, and a published `lastUpdated`
   date. The standard alternative for standalone roadmap repos is
   abandonment.

If you don't care about any of those three, `roadmap.sh/ai-engineer`
is great. Use both; they're complementary.

---

## "What about the other related repos?"

Three peer artifacts in the same author constellation, each a
standalone equal:

- **[harness-engineer-roadmap](https://github.com/bettyguo/harness-engineer-roadmap)**
  — the depth roadmap for the [Agents & Harnesses](../roadmap-data/stages/09-agents-harnesses.json)
  stage. Open it when you want to specialize.
- **[llm-interview-prep](https://github.com/bettyguo/llm-interview-prep)**
  — interview preparation. Open it when you're about to interview.
- **[build-your-own-ai](https://github.com/bettyguo/build-your-own-ai)**
  — hands-on "build it yourself" companion. Open it when reading
  isn't enough.

None is a child of another. They sit sideways to each other and to
this roadmap.

---

## "The 8-resource cap per node feels limiting. Why?"

Because that's the entire point.

Every AI-engineer roadmap that allows unlimited resources per topic
becomes a link dump within a year. A 200-link page is a search engine,
not a roadmap. The 8-resource cap forces every addition to displace
something — which forces an actual editorial judgment about whether
the new resource is better than what's there.

The `Challenge a pick` issue template
([template](../.github/ISSUE_TEMPLATE/challenge-pick.yml)) is the right
way to argue against a current pick. The curator reads every one.

---

## "How do I add a resource?"

Three paths in [CONTRIBUTING.md](../CONTRIBUTING.md):

1. **Direct PR** if the node has headroom under the 8-resource cap.
2. **PR with a swap** if you're proposing to displace an existing pick
   — say which one and why in the PR description.
3. **`Challenge a pick` issue** if you want to argue for the swap
   before doing the PR work.

CI runs `validate_data.py` and `linkcheck.py` on every PR; both must
pass before a human review.

---

## "Why JSON for the data model?"

Three reasons:

1. **Universally toolable.** Every language, every IDE, every diff
   viewer handles JSON cleanly.
2. **No indentation foot-guns.** YAML allows two valid documents that
   disagree because of whitespace. JSON does not.
3. **Strictly schema-validatable.** The JSON Schemas in
   [`roadmap-data/schema/`](../roadmap-data/schema/) define exactly
   what's allowed; `validate_data.py` enforces it.

A static site generator like Astro would have been the obvious choice
for a content-only site. We chose Vite + React + React Flow because the
interactive node graph is the product, and the graph is a real
interactive React component, not styled HTML.

---

## "What happens if a link rots?"

Three layers of defense:

1. **Pre-commit:** every contributor runs `tools/linkcheck.py --only-changed`
   before submitting a PR.
2. **CI on every PR:** `tools/linkcheck.py --only-changed` runs as a
   required check.
3. **Weekly cron:** `.github/workflows/linkcheck-schedule.yml` runs
   the full check every Monday at 13:00 UTC. Any failure auto-opens a
   GitHub issue labeled `linkcheck` with the broken URLs.

A `fix-resource` issue template
([template](../.github/ISSUE_TEMPLATE/fix-resource.yml)) is the right
channel for community link-rot reports.

---

## "Why does the diagram look the way it does?"

The visual choices are deliberate, not aesthetic preference. See
[PLANNING/01_design.md](../PLANNING/01_design.md) §4 for the full
direction; the short version:

- **Dark canvas.** Every other AI-engineer roadmap is light-mode-only.
  This is differentiation at thumbnail size.
- **Color = stage, weight = status, edge style = dependency type.**
  Three visual variables, three semantic axes. Anything more becomes
  noise.
- **Hand-laid coordinates, not auto-layout.** Every successful
  roadmap (developer-roadmap, system-design-primer's diagrams) is
  hand-positioned. Auto-layout produces visually-mediocre roadmaps.
- **One signature flourish.** The hand-drawn-feeling underline under
  the title is the only intentional ornament. The rest is restraint.

---

## "Is the roadmap actually maintained, or is this another launch-and-abandon?"

This is the honest one. The CI keeps the links honest. The
[`CHANGELOG.md`](../CHANGELOG.md) records every monthly pulse. The
[`MAINTENANCE.md`](MAINTENANCE.md) doc lays out the maintenance
cadence: weekly link-check (automated), monthly pulse (a PR with the
changelog entry), quarterly frontier review.

If two months pass without a pulse, open an issue. The maintainer
should be either pulsing or saying "I'm not." Silence is the failure
mode.

---

## "Why does this repo carry the curator's real name and academic affiliation?"

Two reasons.

1. **Editorial accountability.** A real name and an ORCID is the
   credibility signal that "another markdown roadmap" can't match.
   Citable identity is part of the standalone-vs-platform positioning.
2. **Editorial discipline.** Publishing under your real name in front
   of your advisor and your future hiring committee is a forcing
   function. The 8-resource cap, the "why this one" annotations, the
   refusal to fabricate resources — those discipline behaviors are
   easier when the byline is real.

---

## "I think a resource you picked is wrong. What do I do?"

Open a [`Challenge a curatorial pick` issue](https://github.com/bettyguo/ai-engineer-roadmap/issues/new?template=challenge-pick.yml).
Make the case: what's the current pick wrong about, what would replace
it, why is the replacement better.

Editorial bias here is intentional and visible — every resource has a
"why this one" annotation specifically so you have something concrete
to argue with. The right reaction to a pick you disagree with is
*argue better*, not *the curator is bad*.

---

## "I'm overwhelmed."

110 nodes is a lot. The whole point of [`READING_PATHS.md`](READING_PATHS.md)
is to collapse the map to a ~30-node subset that maps to your specific
goal. Pick a path, finish a project, then re-open the map.

The roadmap will still be here.
