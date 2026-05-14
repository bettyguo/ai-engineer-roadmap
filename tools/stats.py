#!/usr/bin/env python3
"""Emit current roadmap counts.

A tiny, stdlib-only utility that walks `roadmap-data/` and prints the
numbers that the README, CHANGELOG, and SVG launch assets keep in
sync: stages, total nodes, per-stage nodes, total resources, unique
URLs, status breakdown, type breakdown.

Run from the repo root:
    python tools/stats.py            # human-readable summary
    python tools/stats.py --json     # machine-readable, for CI / scripts
    python tools/stats.py --md       # a markdown snippet you can paste

Used so README / SVG / CHANGELOG count claims do not drift from the
data. CI can wire `python tools/stats.py --json` into a future check
that fails when README claims diverge from reality; for now it's
manually invoked by the maintainer.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DATA_ROOT = REPO_ROOT / "roadmap-data"
STAGES_DIR = DATA_ROOT / "stages"


def _load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def compute_stats() -> dict[str, Any]:
    manifest = _load_json(DATA_ROOT / "manifest.json")
    stage_ids: list[str] = manifest.get("stages", [])

    per_stage: list[dict[str, Any]] = []
    total_nodes = 0
    total_resources = 0
    unique_urls: set[str] = set()
    status_counter: Counter[str] = Counter()
    type_counter: Counter[str] = Counter()
    difficulty_counter: Counter[str] = Counter()
    free_count = 0
    paid_count = 0
    nodes_with_zero_resources = 0

    for sid in stage_ids:
        stage = _load_json(STAGES_DIR / f"{sid}.json")
        nodes = stage.get("nodes", [])
        stage_resources = 0
        for n in nodes:
            status_counter[n.get("status", "?")] += 1
            resources = n.get("resources", [])
            if not resources:
                nodes_with_zero_resources += 1
            stage_resources += len(resources)
            for r in resources:
                unique_urls.add(r.get("url", ""))
                type_counter[r.get("type", "?")] += 1
                difficulty_counter[r.get("difficulty", "?")] += 1
                if r.get("free") is True:
                    free_count += 1
                elif r.get("free") is False:
                    paid_count += 1
        per_stage.append({
            "id": sid,
            "stageNumber": stage.get("stageNumber"),
            "title": stage.get("title"),
            "nodes": len(nodes),
            "resources": stage_resources,
        })
        total_nodes += len(nodes)
        total_resources += stage_resources

    return {
        "stages": len(stage_ids),
        "totalNodes": total_nodes,
        "totalResources": total_resources,
        "uniqueUrls": len(unique_urls),
        "nodesWithZeroResources": nodes_with_zero_resources,
        "byStatus": dict(status_counter),
        "byType": dict(type_counter),
        "byDifficulty": dict(difficulty_counter),
        "freePaid": {"free": free_count, "paid": paid_count},
        "perStage": per_stage,
        "lastUpdated": manifest.get("lastUpdated"),
    }


def render_human(stats: dict[str, Any]) -> str:
    out: list[str] = []
    out.append("AI Engineer Roadmap — stats")
    out.append("=" * 40)
    out.append(f"Last updated:   {stats['lastUpdated']}")
    out.append(f"Stages:         {stats['stages']}")
    out.append(f"Total nodes:    {stats['totalNodes']}")
    out.append(f"Resources:      {stats['totalResources']}")
    out.append(f"Unique URLs:    {stats['uniqueUrls']}")
    out.append(f"Nodes without any resource: {stats['nodesWithZeroResources']}")
    out.append("")
    out.append("By status:")
    for k, v in sorted(stats["byStatus"].items()):
        out.append(f"  {k:>12}: {v}")
    out.append("")
    out.append("By resource type:")
    for k, v in sorted(stats["byType"].items(), key=lambda kv: -kv[1]):
        out.append(f"  {k:>12}: {v}")
    out.append("")
    out.append("By difficulty:")
    for k, v in sorted(stats["byDifficulty"].items()):
        out.append(f"  {k:>12}: {v}")
    out.append("")
    fp = stats["freePaid"]
    out.append(f"Free / paid: {fp['free']} free, {fp['paid']} paid")
    out.append("")
    out.append("Per-stage node and resource counts:")
    for s in stats["perStage"]:
        out.append(f"  {s['stageNumber']:>2}. {s['id']:<36} {s['nodes']:>3} nodes  {s['resources']:>3} resources")
    return "\n".join(out)


def render_markdown(stats: dict[str, Any]) -> str:
    out: list[str] = []
    out.append(f"**{stats['stages']} stages · {stats['totalNodes']} nodes · "
               f"{stats['uniqueUrls']} link-verified resources** "
               f"(last updated {stats['lastUpdated']}).")
    out.append("")
    out.append("| # | Stage | Nodes | Resources |")
    out.append("|---|---|---:|---:|")
    for s in stats["perStage"]:
        out.append(f"| {s['stageNumber']} | {s['title']} | {s['nodes']} | {s['resources']} |")
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="emit JSON")
    parser.add_argument("--md", action="store_true", help="emit a markdown snippet for the README")
    args = parser.parse_args(argv)

    stats = compute_stats()
    if args.json:
        print(json.dumps(stats, indent=2))
    elif args.md:
        print(render_markdown(stats))
    else:
        print(render_human(stats))
    return 0


if __name__ == "__main__":
    sys.exit(main())
