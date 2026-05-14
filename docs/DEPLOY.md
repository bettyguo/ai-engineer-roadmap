# Deploy guide

This is the tested recipe for deploying the interactive site. The default path
is GitHub Pages via the GitHub Actions workflow in
`.github/workflows/deploy.yml` — once Pages is enabled, every push to `main`
deploys automatically. The rest of this document is the manual fallback for
when Pages isn't available, plus the local-dev recipe.

## Local dev

Prereqs: **Python 3.11+** and **Node 20+** (npm comes with Node).

```bash
# from the repo root

# 1. Validate the data model
python tools/validate_data.py

# 2. Generate the static markdown view + the typed bundle the site imports
python tools/build.py

# 3. Install site deps
cd site
npm install

# 4. Run the dev server
npm run dev

# Opens at http://localhost:5173/
```

Re-run `python tools/build.py` from the repo root whenever you edit a file
under `roadmap-data/`. The site will hot-reload.

## Production build

```bash
# from the repo root

python tools/validate_data.py     # must pass
python tools/build.py              # regenerate site/src/data.generated.ts

cd site
npm install
npm run build
# Output is in site/dist/. Static files. Host anywhere.
```

Verified locally: produces ~30 KB CSS and ~390 KB JS (~125 KB gzipped).

## Path A — GitHub Pages (recommended)

This is what `.github/workflows/deploy.yml` does. One-time setup:

1. Push the repo to `https://github.com/bettyguo/ai-engineer-roadmap`.
2. Go to **Settings → Pages**. Under **Source**, choose **GitHub Actions**.
   (You do not need a `gh-pages` branch — the workflow uses the
   `actions/deploy-pages` action with an artifact upload.)
3. Push to `main` (or run the workflow manually from the **Actions** tab).
4. The workflow builds the site with `BASE_PATH=/ai-engineer-roadmap/`, uploads
   the artifact, and deploys it to
   `https://bettyguo.github.io/ai-engineer-roadmap/`.

If you want a custom domain, put it in **Settings → Pages → Custom domain**;
the workflow also serves the right base path if you set
`BASE_PATH=/` in `deploy.yml` for the apex case.

## Path B — Cloudflare Pages (fastest CDN, generous free tier)

If GitHub Pages is unavailable (private repo + free plan, org policy, etc.):

1. Push the repo to GitHub.
2. Sign in to [dash.cloudflare.com](https://dash.cloudflare.com) → **Workers &
   Pages → Create → Pages → Connect to Git**.
3. Pick the `ai-engineer-roadmap` repo.
4. Build settings:
   - **Framework preset:** None
   - **Build command:**
     ```
     pip install -q nothing && python tools/build.py && cd site && npm install && npm run build
     ```
     (the `pip install` is a no-op that ensures Python is provisioned; if you
     hit issues, switch to Cloudflare's build image v2 which has Python 3.11
     preinstalled)
   - **Build output directory:** `site/dist`
   - **Root directory:** `/` (leave empty)
   - **Environment variables:** `BASE_PATH=/`
5. Save. The first build takes ~2 minutes. Subsequent pushes auto-deploy.

## Path C — Netlify

Same idea as Cloudflare Pages.

1. Push the repo to GitHub.
2. Sign in to [app.netlify.com](https://app.netlify.com) → **Add new site →
   Import an existing project → GitHub**.
3. Pick the repo. Build settings:
   - **Base directory:** *(leave empty)*
   - **Build command:**
     `python tools/build.py && cd site && npm install && npm run build`
   - **Publish directory:** `site/dist`
   - **Environment variables:** `BASE_PATH=/`, `PYTHON_VERSION=3.11`,
     `NODE_VERSION=20`.
4. Deploy.

## Path D — Anywhere static (S3, Vercel, Fly, your own server)

`site/dist/` after `npm run build` is a plain static directory: `index.html`,
one CSS, one JS. Drop it anywhere that serves static files. Two things to set:

- `BASE_PATH` env var at build time — set to whatever subpath your host serves
  the site under (e.g. `/`, `/ai-roadmap/`).
- Browser-router rewrite: not required. The app only uses URL fragments
  (`#node-id`), not history routing.

## Updating the live site

Once deployed via any path, the maintenance loop is:

```bash
# edit roadmap-data/*.json
python tools/validate_data.py
python tools/linkcheck.py --only-changed
git commit -am "Add resource X on node Y"
git push origin main
# CI re-validates, re-link-checks, re-builds, re-deploys.
```

## Diagnostics

- **Build fails on `data.generated.ts`** → run `python tools/build.py` from
  the repo root first; the site imports a Python-generated TS file.
- **Site renders empty in production** → check the `BASE_PATH` you built
  with matches the path you're serving from.
- **Fonts don't load offline** → `index.html` loads Inter / Source Serif Pro
  / JetBrains Mono from Google Fonts. Replace those links with self-hosted
  copies if you need full offline support.
- **CI workflow uses `npm ci`** → that requires `site/package-lock.json` to
  be committed. It already is.
