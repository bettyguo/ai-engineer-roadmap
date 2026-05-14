# Launch playbook

The drafts below are designed to be opened in tabs, lightly edited (links and
dates), and posted in this exact order on launch day. The diagram screenshot
in `assets/diagram-hero.png` is the asset that travels — every post leads
with it.

## Pre-launch checklist (run the morning of)

- [ ] `python tools/validate_data.py` is green.
- [ ] `python tools/linkcheck.py` is green.
- [ ] `npm run build` in `site/` succeeds.
- [ ] The hosted site at `https://bettyguo.github.io/ai-engineer-roadmap/` opens, pans, zooms, and clicking a random node opens its resource panel.
- [ ] `assets/diagram-hero.png` and `assets/social-card-1200x630.png` exist and look distinctive at thumbnail size (see `assets/MAKE_BANNER.md` if not).
- [ ] `CHANGELOG.md` has the `0.1.0` entry with today's date.
- [ ] `roadmap-data/manifest.json` `lastUpdated` is today's date.
- [ ] README's last-updated badge is today's date.
- [ ] Add the live site URL to the repo description on GitHub.

## Show HN

**Title** (Show HN titles are short — under 80 chars):

```
Show HN: ai-engineer-roadmap – an interactive roadmap for becoming an AI engineer
```

**Body** (keep the first paragraph dense; HN readers decide whether to read on in 5 seconds):

```
Hi HN — I've been keeping a personal roadmap of what an AI engineer needs to
know, end to end, and finally turned it into an interactive site:

  https://bettyguo.github.io/ai-engineer-roadmap/

It's 12 stages and ~106 nodes from math and tooling through transformers,
training, inference, RAG, agents, eval, and the safety / frontier edge.
Every node has 2–4 curated resources with a one-line "why this one"
annotation. Every link is automatically link-checked weekly.

I built this because there's no canonical, single-curator, end-to-end answer
to "how do I become or grow as an AI engineer?" There's roadmap.sh's
applied-AI page (scoped narrower), a few stale markdown lists on GitHub, and
a lot of paywalled Medium posts — but no single thing I'd send a friend
asking the question.

I am a final-year PhD candidate in CS at HKU (advised by Prof. Siu-Ming
Yiu); the curatorial picks reflect what I actually read and recommend. I'd
love feedback on the resource choices — especially on Stages 5–9 (the LLM
internals through agents stack), where the field moves fastest.

Source: https://github.com/bettyguo/ai-engineer-roadmap
Content CC BY 4.0, code MIT, contributions welcome (PR template enforces
verification + annotations).

The interactive diagram is built with Vite + React + React Flow; the data
model is plain JSON so the renderer and the content are decoupled. There's
also a static markdown fallback view in /content for SEO and accessibility.
```

**Etiquette:** post once. Reply to every top-level comment within the first 4 hours. No paid promotion.

## X / Twitter thread

Lead tweet — image is the hero diagram screenshot:

```
Spent the last several months building this:

an interactive roadmap for becoming — and growing as — an AI engineer.

12 stages, ~106 nodes, end-to-end from math to the frontier.
Every node has curated, link-verified resources.

→ https://bettyguo.github.io/ai-engineer-roadmap/
```

Follow-ups (one per tweet):

```
2/ The shape: the whole career path as a single navigable graph.

Pan, zoom, click any node for the 2–4 best resources for that topic, with
a one-line "why this one" annotation.

I’d send the screenshot to a friend asking "where do I start?"
```

```
3/ Stage 9 is Agents & Harnesses — a deliberate summary.

For the depth dive on building harnesses end to end, there's a peer
roadmap:

→ harness-engineer-roadmap

The two are siblings, not parent-and-child.
```

```
4/ It is single-curator on purpose.

The whole point is editorial coherence — one person who reads the field
behind the picks. If you disagree with a resource choice, the "why this
one" annotation is what to argue with.

Source + contribution template: github.com/bettyguo/ai-engineer-roadmap
```

```
5/ I'm a final-year PhD at HKU CS, advised by Prof. Siu-Ming Yiu. I work in
AI — this roadmap is the curriculum I wish I'd had when I started, kept
current.

Monthly pulse + weekly auto link-check, so it stays alive.

Feedback very welcome.
```

## r/MachineLearning

**Title:** `[P] I made an interactive end-to-end roadmap for AI engineers — curated by an active researcher`

**Body:** roughly the Show HN body, with the second paragraph reworked to acknowledge the existing landscape (r/ML is more sensitive to "another roadmap" framing — name them).

```
Posting here because this audience has the strongest opinions on what
"AI engineer" should mean, and I want pushback before this gets seen
widely.

  https://bettyguo.github.io/ai-engineer-roadmap/

What it is: an interactive, single-curator roadmap that covers the whole
career path. 12 stages, 106 nodes, 227 link-verified resources. The first
half (math → ML → DL → transformer internals → training) is research-flavor;
the second half (inference → RAG → agents → eval → deployment → safety) is
production-flavor.

What it isn't:
- A repeat of roadmap.sh/ai-engineer (which is scoped to applied AI only
  and is platform-flavored).
- A markdown link dump. Every resource has a "why this one" annotation
  in ≤25 words. Hard cap of 8 resources per node — curatorial judgment is
  the whole point.
- A bootcamp or a syllabus. It's a map, not a curriculum.

What I'd specifically like feedback on:
1. Stage 5 (Transformers & LLM Internals) and Stage 6 (Training & Fine-
   tuning) — these are the parts that need the sharpest picks.
2. Stage 9 (Agents & Harnesses) — deliberately summarized; the depth
   dive lives in the peer roadmap harness-engineer-roadmap.
3. Anything I'm missing on Stage 12 (frontier).

I'm a final-year PhD at HKU. The curatorial bias reflects what I read.
PR template enforces link verification; weekly automated link-check.
```

## r/learnmachinelearning and r/cscareerquestions

Same content, slightly different lede. r/learnmachinelearning wants "where do I start?" framing; r/cscareerquestions wants "how do I not fall behind?" framing.

```
[r/learnmachinelearning lede]
I made this for myself a few months ago when I kept getting asked
"where do I start with AI?" and didn't have a single link to send.
Sharing in case it's useful to anyone else:

  https://bettyguo.github.io/ai-engineer-roadmap/
```

```
[r/cscareerquestions lede]
The most common question I see in this sub right now is "am I learning the
right things to not fall behind on AI?" I tried to answer it as a single
visual map with curated resources:

  https://bettyguo.github.io/ai-engineer-roadmap/
```

## Newsletter outreach

Three short, personalized pitches. Send in this order over the launch week:

### To AlphaSignal (daily AI newsletter, large audience)
```
Subject: New: interactive AI-engineer roadmap, single-curator, ~250 verified resources

Hi AlphaSignal team —

I'm Betty Guo, final-year CS PhD at HKU. I just launched an interactive
roadmap covering the AI-engineer career path end to end — 12 stages, 106
nodes, with curated and link-verified resources on each:

  https://bettyguo.github.io/ai-engineer-roadmap/

Built because there's no canonical single-curator answer to "how do I
become / grow as an AI engineer?" — your daily readership is exactly who
this is for.

Feel free to feature, fork, or ignore. Hero image and one-paragraph
summary attached below in case it's easier.

— Betty
```

### To Sebastian Raschka's "Ahead of AI"
```
Subject: An end-to-end AI-engineer roadmap that's mostly your readers' shape

Hi Sebastian —

Long-time reader. I built an interactive roadmap covering the AI-engineer
career path end to end — and the picks lean heavily on writing of yours
(your model-annotation series shows up four times across Stages 4–6).

  https://bettyguo.github.io/ai-engineer-roadmap/

If it's worth a mention in a future issue, I'd be grateful. Either way,
thank you for the writing — it raises the field's standard for what
serious educational content looks like.

— Betty
```

### To Latent Space (swyx / Alessio)
```
Subject: AI-engineer roadmap — single-curator, interactive, link-verified

Hi Latent Space —

Long-time listener. I built an interactive roadmap of the AI-engineer
career path end to end, single-curator, with curated and link-verified
resources on every node. 227 resources, 12 stages:

  https://bettyguo.github.io/ai-engineer-roadmap/

If it fits a future newsletter or a guest-segment slot, I'd love that.
Either way, thank you for the work you do.

— Betty
```

## Day-after

- Post on LinkedIn (the diagram + 3 paragraphs of the Show HN body).
- Add `docs/PROFILE_SNIPPET.md` content to `bettyguo`'s GitHub profile README.
- Add the live URL and a "what's new" line to the next monthly pulse on the
  schedule documented in `docs/MAINTENANCE.md`.

## Anti-patterns to avoid on launch day

- **Do not** post to all subreddits simultaneously. Stagger them across 24 hours so each can build its own discussion thread.
- **Do not** reply to negative comments defensively. The honest "this is contested noun territory, here's how I'm framing it" answer is in `PLANNING/00_think.md` §1.
- **Do not** mass-tag people on X. The diagram speaks for itself — let it travel naturally.
- **Do not** ship a thin first impression. If anything on the launch checklist isn't ✅, delay a day.
