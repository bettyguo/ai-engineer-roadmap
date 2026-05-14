#!/usr/bin/env python3
"""Build derived artifacts from the roadmap data model.

Reads `roadmap-data/` and emits:

  1. `content/<NN>-<slug>.md` — a static Markdown view of each stage,
     used as the JS-disabled / SEO-friendly fallback.
  2. `content/RECENTLY_ADDED.md` — a chronological view of resources
     added in the last 90 days, sorted newest-first.
  3. `site/src/data.generated.ts` — a typed bundle of the data, ready
     for the React renderer to import.
  4. `site/public/sitemap.xml` — one entry per node so search engines
     can index the hash-link deep URLs.

Idempotent: pure function of the data. Stdlib-only.

Run from the repo root:
    python tools/build.py
"""

from __future__ import annotations

import json
import sys
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DATA_ROOT = REPO_ROOT / "roadmap-data"
STAGES_DIR = DATA_ROOT / "stages"
CONTENT_DIR = REPO_ROOT / "content"
SITE_DATA_PATH = REPO_ROOT / "site" / "src" / "data.generated.ts"
SITE_PUBLIC_DIR = REPO_ROOT / "site" / "public"

RECENTLY_ADDED_WINDOW_DAYS = 90


def _load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _render_resource(res: dict[str, Any]) -> str:
    parts: list[str] = []
    title = res.get("title", "Untitled")
    url = res.get("url", "")
    author = res.get("author")
    year = res.get("year")
    annotation = res.get("annotation", "")
    type_ = res.get("type", "")
    free = res.get("free")
    diff = res.get("difficulty", "")

    head = f"[{title}]({url})"
    if author:
        head += f" — {author}"
    if year:
        head += f" ({year})"

    tags: list[str] = []
    if type_:
        tags.append(f"`{type_}`")
    if diff:
        tags.append(f"`{diff}`")
    if free is True:
        tags.append("`free`")
    elif free is False:
        tags.append("`paid`")
    tag_str = " ".join(tags)

    parts.append(f"- {head} {tag_str}".rstrip())
    if annotation:
        parts.append(f"  - {annotation}")
    return "\n".join(parts)


def _render_node_md(node: dict[str, Any]) -> str:
    out: list[str] = []
    label = node.get("label", node.get("id", "?"))
    status = node.get("status", "")
    out.append(f"### {label}  `{status}`")
    out.append("")
    desc = node.get("description", "")
    if desc:
        out.append(desc)
        out.append("")
    done = node.get("doneWhen", "")
    if done:
        out.append(f"**Done when:** {done}")
        out.append("")
    deps = node.get("dependsOn", [])
    cross = node.get("crossStageDependsOn", [])
    if deps or cross:
        line_parts = []
        if deps:
            line_parts.append("depends on " + ", ".join(f"`{d}`" for d in deps))
        if cross:
            line_parts.append("cross-stage: " + ", ".join(f"`{d}`" for d in cross))
        out.append("*" + "; ".join(line_parts) + "*")
        out.append("")
    resources = node.get("resources", [])
    if resources:
        out.append("**Resources**")
        out.append("")
        for r in resources:
            out.append(_render_resource(r))
        out.append("")
    else:
        out.append("*Resources: to be curated.*")
        out.append("")
    return "\n".join(out)


def _render_stage_md(stage: dict[str, Any], peers: dict[str, Any]) -> str:
    out: list[str] = []
    n = stage.get("stageNumber", "?")
    title = stage.get("title", stage.get("id", "?"))
    blurb = stage.get("blurb", "")
    out.append(f"# Stage {n} — {title}")
    out.append("")
    if blurb:
        out.append(blurb)
        out.append("")

    for node in stage.get("nodes", []):
        out.append(_render_node_md(node))

    sideways = stage.get("sidewaysLinks", [])
    if sideways:
        out.append("---")
        out.append("")
        out.append("## Going sideways")
        out.append("")
        for sl in sideways:
            label = sl.get("label", "Sideways link")
            url = sl.get("url", "")
            blurb_sl = sl.get("blurb", "")
            out.append(f"### [{label}]({url})")
            out.append("")
            if blurb_sl:
                out.append(blurb_sl)
                out.append("")
    return "\n".join(out)


def _emit_content(manifest: dict[str, Any], stages: dict[str, dict[str, Any]], peers: dict[str, Any]) -> None:
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    for sid in manifest.get("stages", []):
        stage = stages.get(sid)
        if stage is None:
            continue
        out_path = CONTENT_DIR / f"{sid}.md"
        out_path.write_text(_render_stage_md(stage, peers), encoding="utf-8")
        print(f"  wrote {out_path.relative_to(REPO_ROOT)}")

    index = ["# AI Engineer Roadmap — content view", ""]
    index.append(
        "This is the static Markdown view of the roadmap data model. The "
        "interactive view lives at the [live site](" +
        manifest.get("liveSite", "") + ")."
    )
    index.append("")
    index.append("- [Recently added](RECENTLY_ADDED.md) — what changed in the last 90 days")
    index.append("")
    for sid in manifest.get("stages", []):
        stage = stages.get(sid)
        if stage is None:
            continue
        index.append(f"- [Stage {stage.get('stageNumber')} — {stage.get('title')}]({sid}.md)")
    index.append("")
    if peers:
        index.append("## Peer roadmaps")
        index.append("")
        for p in peers.get("peers", []):
            index.append(f"- [{p.get('title')}]({p.get('url')}) — {p.get('blurb')}")
        index.append("")
    (CONTENT_DIR / "README.md").write_text("\n".join(index), encoding="utf-8")
    print(f"  wrote {(CONTENT_DIR / 'README.md').relative_to(REPO_ROOT)}")


def _emit_recently_added(manifest: dict[str, Any], stages: dict[str, dict[str, Any]]) -> None:
    """Emit content/RECENTLY_ADDED.md — resources added in the last N days.

    Sorted newest-first by `addedAt`. The README and FAQ promise a
    'recently added' view for the working-AI-engineer reading path;
    this is that artifact, regenerated whenever data changes.
    """
    cutoff = date.today() - timedelta(days=RECENTLY_ADDED_WINDOW_DAYS)
    rows: list[tuple[str, str, dict[str, Any], dict[str, Any]]] = []
    for sid, stage in stages.items():
        for node in stage.get("nodes", []):
            for r in node.get("resources", []):
                try:
                    added = datetime.strptime(r.get("addedAt", ""), "%Y-%m-%d").date()
                except ValueError:
                    continue
                if added >= cutoff:
                    rows.append((r.get("addedAt", ""), sid, node, r))
    rows.sort(key=lambda t: t[0], reverse=True)

    out: list[str] = []
    out.append("# Recently added")
    out.append("")
    out.append(
        f"Resources added in the last {RECENTLY_ADDED_WINDOW_DAYS} days, newest first. "
        f"Generated from `roadmap-data/`. The interactive view at "
        f"[{manifest.get('liveSite', '')}]({manifest.get('liveSite', '')}) "
        "renders the same data."
    )
    out.append("")
    out.append(f"Total: **{len(rows)}** resources across **{len({r[2]['id'] for r in rows})}** nodes.")
    out.append("")
    current_date = None
    for added, sid, node, r in rows:
        if added != current_date:
            out.append("")
            out.append(f"## {added}")
            out.append("")
            current_date = added
        title = r.get("title", "?")
        url = r.get("url", "")
        author = r.get("author")
        node_label = node.get("label", node.get("id", "?"))
        stage_num = stages[sid].get("stageNumber", "?")
        line = f"- **[{title}]({url})**"
        if author:
            line += f" — {author}"
        line += f" · Stage {stage_num} / *{node_label}*"
        out.append(line)
        ann = r.get("annotation", "")
        if ann:
            out.append(f"  - {ann}")
    out.append("")

    path = CONTENT_DIR / "RECENTLY_ADDED.md"
    path.write_text("\n".join(out), encoding="utf-8")
    print(f"  wrote {path.relative_to(REPO_ROOT)}")


def _emit_site_data(manifest: dict[str, Any], stages_in_order: list[dict[str, Any]], peers: dict[str, Any], edges: dict[str, Any]) -> None:
    """Emit a TypeScript module the renderer can import."""
    SITE_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    body = {
        "manifest": manifest,
        "stages": stages_in_order,
        "peers": peers.get("peers", []),
        "crossStageEdges": edges.get("crossStageEdges", []),
    }
    js = json.dumps(body, ensure_ascii=False, indent=2)
    ts = (
        "// AUTO-GENERATED by tools/build.py. Do not edit by hand.\n"
        "// Source of truth: roadmap-data/*.json\n"
        "\n"
        "import type { RoadmapData } from \"./types\";\n"
        "\n"
        "export const ROADMAP: RoadmapData = " + js + " as RoadmapData;\n"
    )
    SITE_DATA_PATH.write_text(ts, encoding="utf-8")
    print(f"  wrote {SITE_DATA_PATH.relative_to(REPO_ROOT)}")


def _emit_sitemap(manifest: dict[str, Any], stages_in_order: list[dict[str, Any]]) -> None:
    """Emit site/public/sitemap.xml.

    One entry for the root, one for every node (via fragment URL).
    The fragment isn't strictly indexable everywhere, but Google and
    Bing both treat well-formed hash URLs as canonical when the page
    behind them serves matching content (we do, via the static
    markdown view and the SPA hash router).
    """
    SITE_PUBLIC_DIR.mkdir(parents=True, exist_ok=True)
    base_url = manifest.get("liveSite", "").rstrip("/")
    last_updated = manifest.get("lastUpdated", date.today().isoformat())

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    lines.append("  <url>")
    lines.append(f"    <loc>{base_url}/</loc>")
    lines.append(f"    <lastmod>{last_updated}</lastmod>")
    lines.append("    <changefreq>weekly</changefreq>")
    lines.append("    <priority>1.0</priority>")
    lines.append("  </url>")
    for stage in stages_in_order:
        for node in stage.get("nodes", []):
            nid = node.get("id", "")
            if not nid:
                continue
            lines.append("  <url>")
            lines.append(f"    <loc>{base_url}/#{nid}</loc>")
            lines.append(f"    <lastmod>{last_updated}</lastmod>")
            lines.append("    <changefreq>monthly</changefreq>")
            lines.append("    <priority>0.7</priority>")
            lines.append("  </url>")
    lines.append("</urlset>")
    out = SITE_PUBLIC_DIR / "sitemap.xml"
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"  wrote {out.relative_to(REPO_ROOT)}")


def main() -> int:
    manifest = _load_json(DATA_ROOT / "manifest.json")
    peers = _load_json(DATA_ROOT / "peers.json")
    edges = _load_json(DATA_ROOT / "edges.json")

    stages: dict[str, dict[str, Any]] = {}
    for sid in manifest.get("stages", []):
        path = STAGES_DIR / f"{sid}.json"
        stages[sid] = _load_json(path)

    print("Building content/ …")
    _emit_content(manifest, stages, peers)

    print("Building content/RECENTLY_ADDED.md …")
    _emit_recently_added(manifest, stages)

    print("Building site/src/data.generated.ts …")
    stages_in_order = [stages[sid] for sid in manifest.get("stages", []) if sid in stages]
    _emit_site_data(manifest, stages_in_order, peers, edges)

    print("Building site/public/sitemap.xml …")
    _emit_sitemap(manifest, stages_in_order)

    print("Done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
