# Banner & social card — status and how to refresh

## Current status

Two hand-authored SVG launch assets ship with this repo:

- **[`assets/diagram-hero.svg`](./diagram-hero.svg)** — 1600×1000 hero
  image referenced from the README. Distinctive, dark-canvas editorial
  style, 12 colored stage stripes, curator credit, live-URL.
- **[`assets/social-card-1200x630.svg`](./social-card-1200x630.svg)** —
  1200×630 social-card variant; a copy is also at
  `site/public/og-card.svg`.

These satisfy the README hero slot today (GitHub renders SVG in
`<img>` tags). They are the "launch plate" — structural overview,
curator credit, URL — not a screenshot of the interactive diagram.

## What's still on the human's to-do

**The OG card slot in `site/index.html` references `./og-card.png`**, not the
SVG, because Twitter / LinkedIn / Slack / iMessage previewers render PNG
reliably and SVG inconsistently. Until you produce the PNG, social shares
will show the default-preview fallback (page title + description).

Three ways to produce the PNG, in increasing order of effort:

### Option A — convert the SVG (5 minutes)

```bash
# Requires rsvg-convert (librsvg) or Inkscape
rsvg-convert -w 1200 -h 630 assets/social-card-1200x630.svg \
  > site/public/og-card.png

# or with Inkscape:
inkscape assets/social-card-1200x630.svg \
  --export-type=png --export-width=1200 --export-filename=site/public/og-card.png
```

Then delete `site/public/og-card.png.placeholder` and commit the PNG.

### Option B — screenshot the interactive diagram (10 minutes)

If you'd rather the social card *be* the interactive diagram (a
genuinely striking choice once the live site is up):

1. Deploy the site (`docs/DEPLOY.md`).
2. Open `https://bettyguo.github.io/ai-engineer-roadmap/` in a browser.
3. Zoom out until all 12 stages are visible.
4. Take a screenshot of the diagram area only — no chrome.
5. Crop to 1200×630.
6. Save as `site/public/og-card.png` and `assets/diagram-screenshot.png`.
7. Optionally update the README to use the screenshot instead of the SVG.

### Option C — commission designed visuals

If the maintainer wants designed launch assets — a wordmark, custom
illustration, branded social card — keep the SVGs as the v1 baseline
and replace at leisure. Nothing about the rest of the repo depends on
the visual.

## Why both an SVG and a PNG?

| Asset slot | Best format | Why |
|---|---|---|
| GitHub README hero | SVG | GitHub renders SVG cleanly; scales for retina; ~5 KB; no rasterization. |
| GitHub social preview (`og:image` for the repo) | PNG | GitHub specifically rasterizes a 1280×640 PNG for its OG card. SVG won't render in this slot. |
| Twitter / LinkedIn / Slack OG card | PNG | Most previewers don't render SVG. |
| The live site's social card | PNG | Same as above. |
| Internal documentation, dev preview | SVG | Crisper. |

So the canonical pairing: SVG in the repo, PNG exported from the SVG for
every OG-card consumer.

## Why the SVG layout looks the way it does

Each visual choice maps to a Phase 0 / Phase 1 decision:

- **Dark canvas (`#050505`).** Differentiates from every other roadmap
  in the field (all light-mode). High screenshot legibility.
  Editorial-not-productized direction from `PLANNING/01_design.md` §4.
- **12 colored stripes.** The structural shape of the artifact at
  thumbnail size. A reader skimming on Twitter sees the colors and
  immediately reads "structured, ordered, complete." Block colors
  survive aggressive thumbnailing better than fine detail.
- **The signature underline beneath the title.** The one signature
  flourish from `PLANNING/01_design.md` §4 — a single deliberate
  detail marks the artifact as curator-made.
- **Serif title + sans body + mono labels.** Same three-typeface
  system as the live site (`site/src/styles/theme.css`). The asset
  and the product agree on aesthetic.
- **Curator credit + ORCID at the bottom.** Citable identity is part
  of the editorial-coherence argument; visible on the launch asset,
  not just in the README.
- **Live URL bottom-right.** The post-clipboard test: someone who saves
  this image without the surrounding context can still find the site.
