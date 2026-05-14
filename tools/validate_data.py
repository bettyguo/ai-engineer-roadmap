#!/usr/bin/env python3
"""Validate the roadmap data model.

Reads every file under `roadmap-data/`, checks structural rules from
`PLANNING/01_design.md`, and exits 0 (pass) or 1 (fail). Prints a
numbered list of problems. Stdlib-only.

Run from the repo root:
    python tools/validate_data.py

Used by CI on every push and every PR.
"""

from __future__ import annotations

import json
import re
import sys
from datetime import date, datetime
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DATA_ROOT = REPO_ROOT / "roadmap-data"
STAGES_DIR = DATA_ROOT / "stages"

# Enums (kept in sync with the JSON Schemas in roadmap-data/schema/)
STATUS_ENUM = {"core", "recommended", "optional"}
TYPE_ENUM = {
    "paper",
    "course",
    "repo",
    "book",
    "video",
    "blog",
    "tool",
    "official",
    "interactive",
}
DIFFICULTY_ENUM = {"intro", "intermediate", "advanced"}

ID_PATTERN = re.compile(r"^[a-z0-9-]+$")
STAGE_ID_PATTERN = re.compile(r"^\d{2}-[a-z0-9-]+$")
HEX_COLOR_PATTERN = re.compile(r"^#[0-9A-Fa-f]{6}$")
DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")
URL_PATTERN = re.compile(r"^https?://[^\s]+$")

MAX_RESOURCES_PER_NODE = 8
MAX_ANNOTATION_LEN = 240
MIN_ANNOTATION_LEN = 4
MIN_DESCRIPTION_LEN = 20

# Expected taxonomy (guards against accidental drift). If the curator
# decides to change the spine, update this list deliberately.
EXPECTED_STAGES: list[tuple[str, int, int]] = [
    # (stage_id, stage_number, expected_node_count)
    ("01-prerequisites-math", 1, 8),
    ("02-programming-tooling", 2, 8),
    ("03-ml-fundamentals", 3, 10),
    ("04-dl-fundamentals", 4, 10),
    ("05-transformers-llm-internals", 5, 8),
    ("06-training-finetuning", 6, 10),
    ("07-inference-serving", 7, 10),
    ("08-retrieval-rag", 8, 10),
    ("09-agents-harnesses", 9, 8),
    ("10-evaluation-observability", 10, 8),
    ("11-deployment-production", 11, 8),
    ("12-safety-alignment-frontier", 12, 8),
]
EXPECTED_TOTAL_NODES = sum(n for (_, _, n) in EXPECTED_STAGES)  # 96


class Problems:
    """Accumulator for validation errors. Pretty-prints at the end."""

    def __init__(self) -> None:
        self.entries: list[str] = []

    def add(self, where: str, msg: str) -> None:
        self.entries.append(f"[{where}] {msg}")

    def ok(self) -> bool:
        return not self.entries

    def report(self) -> None:
        if not self.entries:
            return
        print(f"\nValidation failed with {len(self.entries)} problem(s):\n")
        for i, entry in enumerate(self.entries, 1):
            print(f"  {i:>3}. {entry}")
        print()


def _load_json(path: Path, problems: Problems) -> dict[str, Any] | None:
    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        problems.add(str(path), "file not found")
    except json.JSONDecodeError as e:
        problems.add(str(path), f"invalid JSON: {e}")
    return None


def _check_date(value: Any, where: str, field: str, problems: Problems) -> None:
    if not isinstance(value, str) or not DATE_PATTERN.match(value):
        problems.add(where, f"{field}: not an ISO date (YYYY-MM-DD): {value!r}")
        return
    try:
        d = datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError:
        problems.add(where, f"{field}: not a valid date: {value!r}")
        return
    if d > date.today():
        problems.add(where, f"{field}: date in the future: {value!r}")


def _validate_resource(
    res: dict[str, Any], where: str, problems: Problems
) -> None:
    required = ["title", "url", "type", "annotation", "difficulty", "free", "addedAt", "verifiedAt"]
    for field in required:
        if field not in res:
            problems.add(where, f"resource missing required field: {field!r}")

    if "title" in res and (not isinstance(res["title"], str) or len(res["title"]) < 2):
        problems.add(where, "resource.title: must be a string with length >= 2")

    if "url" in res:
        url = res["url"]
        if not isinstance(url, str) or not URL_PATTERN.match(url):
            problems.add(where, f"resource.url: must be http(s) URL, got {url!r}")

    if "type" in res and res["type"] not in TYPE_ENUM:
        problems.add(where, f"resource.type: not in enum: {res['type']!r}")

    if "annotation" in res:
        ann = res["annotation"]
        if not isinstance(ann, str):
            problems.add(where, "resource.annotation: must be a string")
        elif not (MIN_ANNOTATION_LEN <= len(ann) <= MAX_ANNOTATION_LEN):
            problems.add(
                where,
                f"resource.annotation: length {len(ann)} not in "
                f"[{MIN_ANNOTATION_LEN}, {MAX_ANNOTATION_LEN}]",
            )

    if "difficulty" in res and res["difficulty"] not in DIFFICULTY_ENUM:
        problems.add(where, f"resource.difficulty: not in enum: {res['difficulty']!r}")

    if "free" in res and not isinstance(res["free"], bool):
        problems.add(where, "resource.free: must be boolean")

    if "addedAt" in res:
        _check_date(res["addedAt"], where, "resource.addedAt", problems)
    if "verifiedAt" in res:
        _check_date(res["verifiedAt"], where, "resource.verifiedAt", problems)

    if "year" in res:
        y = res["year"]
        if not isinstance(y, int) or not (1950 <= y <= 2100):
            problems.add(where, f"resource.year: must be int in [1950, 2100], got {y!r}")

    allowed_keys = {
        "title", "author", "year", "type", "url", "annotation",
        "difficulty", "free", "addedAt", "verifiedAt", "verifiedBy",
    }
    extra = set(res.keys()) - allowed_keys
    if extra:
        problems.add(where, f"resource has unknown fields: {sorted(extra)}")


def _validate_node(
    node: dict[str, Any],
    stage_id: str,
    node_index: int,
    problems: Problems,
) -> str | None:
    where = f"{stage_id}/nodes[{node_index}]"
    nid = node.get("id")
    if not isinstance(nid, str) or not ID_PATTERN.match(nid):
        problems.add(where, f"id missing or invalid: {nid!r}")
        nid = None

    required = ["id", "label", "status", "description", "doneWhen", "position",
                "dependsOn", "crossStageDependsOn", "resources"]
    for field in required:
        if field not in node:
            problems.add(where, f"missing required field: {field!r}")

    if "label" in node and (not isinstance(node["label"], str) or len(node["label"]) < 2):
        problems.add(where, "label: must be a string with length >= 2")

    if "status" in node and node["status"] not in STATUS_ENUM:
        problems.add(where, f"status: not in enum: {node['status']!r}")

    if "description" in node:
        desc = node["description"]
        if not isinstance(desc, str) or len(desc) < MIN_DESCRIPTION_LEN:
            problems.add(
                where,
                f"description: must be a string of length >= {MIN_DESCRIPTION_LEN}",
            )

    if "doneWhen" in node and (not isinstance(node["doneWhen"], str) or len(node["doneWhen"]) < 6):
        problems.add(where, "doneWhen: must be a string of length >= 6")

    if "position" in node:
        pos = node["position"]
        if (
            not isinstance(pos, dict)
            or "x" not in pos
            or "y" not in pos
            or not isinstance(pos["x"], (int, float))
            or not isinstance(pos["y"], (int, float))
        ):
            problems.add(where, f"position: must be {{x: number, y: number}}, got {pos!r}")

    for ref_field in ("dependsOn", "crossStageDependsOn"):
        if ref_field in node:
            arr = node[ref_field]
            if not isinstance(arr, list):
                problems.add(where, f"{ref_field}: must be array")
            else:
                for ref in arr:
                    if not isinstance(ref, str) or not ID_PATTERN.match(ref):
                        problems.add(where, f"{ref_field}: invalid id {ref!r}")

    if "resources" in node:
        resources = node["resources"]
        if not isinstance(resources, list):
            problems.add(where, "resources: must be array")
        else:
            if len(resources) > MAX_RESOURCES_PER_NODE:
                problems.add(
                    where,
                    f"resources: {len(resources)} > {MAX_RESOURCES_PER_NODE} (hard cap)",
                )
            for ri, res in enumerate(resources):
                _validate_resource(res, f"{where}/resources[{ri}]", problems)

    return nid


def _validate_stage(path: Path, problems: Problems) -> dict[str, Any] | None:
    raw = _load_json(path, problems)
    if raw is None:
        return None

    where = path.name
    sid = raw.get("id")
    if not isinstance(sid, str) or not STAGE_ID_PATTERN.match(sid):
        problems.add(where, f"id missing or invalid: {sid!r}")

    if sid and sid != path.stem:
        problems.add(where, f"id {sid!r} does not match filename {path.stem!r}")

    if "stageNumber" in raw and not (isinstance(raw["stageNumber"], int) and 1 <= raw["stageNumber"] <= 99):
        problems.add(where, "stageNumber: must be int in [1, 99]")

    if "title" in raw and not (isinstance(raw["title"], str) and len(raw["title"]) >= 2):
        problems.add(where, "title: missing or too short")
    if "blurb" in raw and not (isinstance(raw["blurb"], str) and len(raw["blurb"]) >= 10):
        problems.add(where, "blurb: missing or too short")
    if "color" in raw and not (isinstance(raw["color"], str) and HEX_COLOR_PATTERN.match(raw["color"])):
        problems.add(where, f"color: not a hex code: {raw.get('color')!r}")

    nodes = raw.get("nodes")
    if not isinstance(nodes, list) or len(nodes) == 0:
        problems.add(where, "nodes: must be a non-empty array")
        return raw

    seen_local_ids: set[str] = set()
    for i, node in enumerate(nodes):
        nid = _validate_node(node, sid or path.stem, i, problems)
        if nid:
            if nid in seen_local_ids:
                problems.add(where, f"duplicate node id within stage: {nid!r}")
            seen_local_ids.add(nid)

    return raw


def _validate_manifest_and_peers(problems: Problems) -> tuple[dict[str, Any] | None, dict[str, Any] | None]:
    manifest = _load_json(DATA_ROOT / "manifest.json", problems)
    peers = _load_json(DATA_ROOT / "peers.json", problems)

    if manifest:
        for field in ("schemaVersion", "title", "tagline", "curator", "license", "lastUpdated", "liveSite", "stages", "palette"):
            if field not in manifest:
                problems.add("manifest.json", f"missing field: {field}")

        stages_in_manifest = manifest.get("stages", [])
        if [s for s, _, _ in EXPECTED_STAGES] != stages_in_manifest:
            problems.add(
                "manifest.json",
                "stages list does not match the expected taxonomy "
                "(EXPECTED_STAGES in tools/validate_data.py)",
            )

        if "lastUpdated" in manifest:
            _check_date(manifest["lastUpdated"], "manifest.json", "lastUpdated", problems)

        palette = manifest.get("palette", {})
        for sid in stages_in_manifest:
            if sid not in palette:
                problems.add("manifest.json", f"palette missing color for stage {sid!r}")

    if peers:
        peer_list = peers.get("peers", [])
        if not isinstance(peer_list, list) or len(peer_list) == 0:
            problems.add("peers.json", "peers: must be a non-empty array")
        else:
            for p in peer_list:
                for field in ("id", "title", "role", "blurb", "url", "openWhen"):
                    if field not in p:
                        problems.add("peers.json", f"peer entry missing field: {field}")
                if "url" in p and not URL_PATTERN.match(str(p["url"])):
                    problems.add("peers.json", f"peer.url not http(s): {p.get('url')!r}")

    return manifest, peers


def _validate_edges(
    problems: Problems,
    all_node_ids: set[str],
) -> None:
    raw = _load_json(DATA_ROOT / "edges.json", problems)
    if not raw:
        return
    for ei, edge in enumerate(raw.get("crossStageEdges", [])):
        where = f"edges.json/crossStageEdges[{ei}]"
        for field in ("from", "to", "kind"):
            if field not in edge:
                problems.add(where, f"missing field {field!r}")
        if "from" in edge and edge["from"] not in all_node_ids:
            problems.add(where, f"`from` references unknown node id: {edge['from']!r}")
        if "to" in edge and edge["to"] not in all_node_ids:
            problems.add(where, f"`to` references unknown node id: {edge['to']!r}")


def main() -> int:
    problems = Problems()

    manifest, _ = _validate_manifest_and_peers(problems)

    stage_files = sorted(STAGES_DIR.glob("*.json"))
    if [p.stem for p in stage_files] != [s for s, _, _ in EXPECTED_STAGES]:
        problems.add(
            "roadmap-data/stages/",
            "stage files on disk do not match the expected taxonomy "
            "(check filenames and EXPECTED_STAGES)",
        )

    stages_data: dict[str, dict[str, Any]] = {}
    all_node_ids: set[str] = set()
    node_to_stage: dict[str, str] = {}

    for path in stage_files:
        data = _validate_stage(path, problems)
        if not data:
            continue
        sid = data.get("id") or path.stem
        stages_data[sid] = data
        for node in data.get("nodes", []):
            nid = node.get("id")
            if isinstance(nid, str):
                if nid in all_node_ids:
                    problems.add(path.name, f"duplicate node id across stages: {nid!r}")
                all_node_ids.add(nid)
                node_to_stage[nid] = sid

    # Count check
    total_nodes = len(all_node_ids)
    if total_nodes != EXPECTED_TOTAL_NODES:
        problems.add(
            "taxonomy",
            f"expected {EXPECTED_TOTAL_NODES} unique nodes, got {total_nodes}",
        )

    # Per-stage node-count check
    for sid, _snum, expected_count in EXPECTED_STAGES:
        data = stages_data.get(sid)
        if not data:
            continue
        actual = len(data.get("nodes", []))
        if actual != expected_count:
            problems.add(
                sid,
                f"expected {expected_count} nodes, got {actual} "
                "(update EXPECTED_STAGES if this is intentional)",
            )

    # Cross-reference checks: dependsOn within stage, crossStageDependsOn outside
    for sid, data in stages_data.items():
        local_ids = {n["id"] for n in data.get("nodes", []) if isinstance(n.get("id"), str)}
        for node in data.get("nodes", []):
            nid = node.get("id")
            where = f"{sid}/{nid}"
            for ref in node.get("dependsOn", []):
                if ref not in all_node_ids:
                    problems.add(where, f"dependsOn: unknown id {ref!r}")
                elif node_to_stage.get(ref) != sid:
                    problems.add(
                        where,
                        f"dependsOn: {ref!r} is in stage "
                        f"{node_to_stage.get(ref)!r}, not the same stage "
                        f"(use crossStageDependsOn for cross-stage edges)",
                    )
                elif ref == nid:
                    problems.add(where, f"dependsOn: self-loop {ref!r}")
            for ref in node.get("crossStageDependsOn", []):
                if ref not in all_node_ids:
                    problems.add(where, f"crossStageDependsOn: unknown id {ref!r}")
                elif node_to_stage.get(ref) == sid:
                    problems.add(
                        where,
                        f"crossStageDependsOn: {ref!r} is in the same stage "
                        "(use dependsOn for intra-stage edges)",
                    )

    _validate_edges(problems, all_node_ids)

    # Sideways-link sanity check on stage 9
    stage9 = stages_data.get("09-agents-harnesses")
    if stage9 is not None:
        sideways = stage9.get("sidewaysLinks", [])
        if not sideways:
            problems.add(
                "09-agents-harnesses",
                "Stage 9 must include a sidewaysLinks entry to harness-engineer-roadmap "
                "(scope-partition requirement from PLANNING/01_design.md)",
            )

    # Report
    if problems.ok():
        print(
            f"OK — {len(stages_data)} stages, {total_nodes} nodes, "
            f"all cross-references resolve, all rules pass."
        )
        return 0
    problems.report()
    return 1


if __name__ == "__main__":
    sys.exit(main())
