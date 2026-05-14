#!/usr/bin/env python3
"""Build derived artifacts from the roadmap data model.

Reads `roadmap-data/` and emits:

  1. `content/<NN>-<slug>.md` — a static Markdown view of each stage,
     used as the JS-disabled / SEO-friendly fallback.
  2. `site/src/data.generated.ts` — a typed bundle of the data, ready
     for the React renderer to import.

Idempotent: pure function of the data. Stdlib-only.

Run from the repo root:
    python tools/build.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DATA_ROOT = REPO_ROOT / "roadmap-data"
STAGES_DIR = DATA_ROOT / "stages"
CONTENT_DIR = REPO_ROOT / "content"
SITE_DATA_PATH = REPO_ROOT / "site" / "src" / "data.generated.ts"


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

    print("Building site/src/data.generated.ts …")
    stages_in_order = [stages[sid] for sid in manifest.get("stages", []) if sid in stages]
    _emit_site_data(manifest, stages_in_order, peers, edges)

    print("Done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
