# Banner & social card — how to make them

Image generation isn't available in the environment this repo was scaffolded
in, so the marketing visuals are left as a deliberate to-do for the
maintainer. They are the highest-leverage manual launch step — the
diagram screenshot is the asset every Show HN post, LinkedIn share, and
X thread will lead with.

## What to produce

1. **`assets/diagram-hero.png`** — referenced from the README and Twitter
   card. **1600 × 1000 px** (will display at ~900 px wide on GitHub).
2. **`assets/social-card-1200x630.png`** — referenced from `site/index.html`
   as the Open Graph image. **1200 × 630 px** (the LinkedIn / Twitter
   recommendation).
3. **`site/public/og-card.png`** — copy of the social card placed where the
   live site can serve it.

## How (the literal step-by-step)

1. Build and deploy the site (or run it locally — `npm run dev`).
2. Open the live site in a real browser. Maximize the window.
3. Zoom the diagram out (use the React Flow controls in the lower-left)
   so the full 12-stage stack is visible.
4. Take a screenshot of the **diagram area only** (not the chrome / top
   bar / footer).
   - macOS: `Cmd+Shift+4` then drag.
   - Windows: Snipping Tool, rectangle mode.
   - Linux: Flameshot or `gnome-screenshot --interactive`.
5. Save as `assets/diagram-hero.png`.
6. Crop a 1200×630 region of the same screenshot — the part that includes
   the title row plus the top 2–3 stages, so the picture looks
   "in motion" at thumbnail size. Save as both
   `assets/social-card-1200x630.png` and `site/public/og-card.png`.
7. Commit the three files.

## Why a manual screenshot rather than an SVG export

A flat SVG export of the React Flow canvas would also work, but a PNG
screenshot has two advantages: (a) it reads identically on GitHub, LinkedIn,
X, and previewers that don't render SVG OG cards reliably; (b) it captures
the dark editorial canvas plus the React Flow grid/controls texture, which
is part of what makes the visual distinctive at thumbnail size.

## If you want a designed banner above the README screenshot

Optional, but high-leverage: a wordmark / banner. Suggested spec:
**1600 × 480 px**, dark canvas (`#050505`), the title `AI Engineer Roadmap`
in Source Serif Pro 600 white-cream (`#F8F7F4`), with a single
hand-drawn-feeling underline (the `signature-underline` motif from
`site/src/styles/theme.css`). Below in JetBrains Mono uppercase:
`CURATED · BETTY GUO · HKU · CC BY 4.0`. Save to
`assets/banner.png` and add it above the diagram in the README.

## Tested with

Confirm at thumbnail size:

- Does it read as **distinctively designed** rather than generic-AI-slop?
  (Goal of `PLANNING/01_design.md` §4.)
- Can a stranger glance at the thumbnail and infer "this is a roadmap"?
- Is the title legible at 1/8 size (Twitter card thumbnail)?

If yes to all three, ship it.
