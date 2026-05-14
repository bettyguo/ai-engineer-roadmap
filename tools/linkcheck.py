#!/usr/bin/env python3
"""Check that every resource URL in the data model resolves.

Stdlib-only HTTP client (urllib). For each unique URL in
`roadmap-data/`, issues a HEAD (fallback GET on 405/501) with a
sensible UA and a short timeout. Writes a Markdown report to
`tools/_linkcheck_report.md`. Exits 0 if every URL is 2xx or 3xx; 1
otherwise.

Run from the repo root:
    python tools/linkcheck.py            # check all URLs
    python tools/linkcheck.py --only-changed  # check only URLs added since last commit

Used by CI on every push and weekly via the linkcheck-schedule workflow.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Iterable


REPO_ROOT = Path(__file__).resolve().parents[1]
DATA_ROOT = REPO_ROOT / "roadmap-data"
REPORT_PATH = REPO_ROOT / "tools" / "_linkcheck_report.md"

UA = (
    "Mozilla/5.0 (compatible; ai-engineer-roadmap-linkcheck/1.0; "
    "+https://github.com/bettyguo/ai-engineer-roadmap)"
)
TIMEOUT_SECONDS = 12
MAX_RETRIES = 1
MAX_WORKERS = 8


def _collect_urls() -> dict[str, list[str]]:
    """Walk every JSON under roadmap-data/ and collect URLs → list of source files."""
    urls: dict[str, list[str]] = {}

    def _walk(value, path: Path) -> None:
        if isinstance(value, dict):
            for v in value.values():
                _walk(v, path)
        elif isinstance(value, list):
            for v in value:
                _walk(v, path)
        elif isinstance(value, str) and value.startswith(("http://", "https://")):
            urls.setdefault(value, []).append(str(path.relative_to(REPO_ROOT)))

    for jf in DATA_ROOT.rglob("*.json"):
        try:
            with jf.open("r", encoding="utf-8") as f:
                data = json.load(f)
        except (OSError, json.JSONDecodeError):
            continue
        _walk(data, jf)
    return urls


def _changed_files_since_main() -> set[Path]:
    """Return JSON files in roadmap-data/ changed vs origin/main (or HEAD~1)."""
    candidates = ["origin/main...HEAD", "HEAD~1...HEAD"]
    for spec in candidates:
        try:
            out = subprocess.check_output(
                ["git", "diff", "--name-only", spec],
                cwd=REPO_ROOT,
                stderr=subprocess.DEVNULL,
            ).decode()
            paths: set[Path] = set()
            for line in out.splitlines():
                p = REPO_ROOT / line.strip()
                if p.exists() and p.suffix == ".json" and "roadmap-data" in p.parts:
                    paths.add(p)
            return paths
        except subprocess.CalledProcessError:
            continue
    return set()


def _filter_urls_to_changed(urls: dict[str, list[str]]) -> dict[str, list[str]]:
    changed = _changed_files_since_main()
    if not changed:
        return urls
    changed_rel = {str(p.relative_to(REPO_ROOT)) for p in changed}
    return {u: src for u, src in urls.items() if any(s in changed_rel for s in src)}


def _check_one(url: str) -> tuple[str, int | None, str]:
    """Return (url, status_code_or_None, message)."""
    last_err = ""
    for attempt in range(MAX_RETRIES + 1):
        for method in ("HEAD", "GET"):
            req = urllib.request.Request(url, method=method, headers={"User-Agent": UA})
            try:
                with urllib.request.urlopen(req, timeout=TIMEOUT_SECONDS) as resp:
                    return url, resp.status, "ok"
            except urllib.error.HTTPError as e:
                if e.code in (405, 501) and method == "HEAD":
                    continue
                return url, e.code, str(e.reason) if e.reason else "http error"
            except urllib.error.URLError as e:
                last_err = str(e.reason)
            except (TimeoutError, OSError) as e:
                last_err = str(e)
        if attempt < MAX_RETRIES:
            time.sleep(1.0)
    return url, None, last_err or "unreachable"


def _format_report(results: list[tuple[str, int | None, str, list[str]]]) -> str:
    ok = [r for r in results if r[1] and 200 <= r[1] < 400]
    bad = [r for r in results if not (r[1] and 200 <= r[1] < 400)]

    out: list[str] = []
    out.append("# Link-check report")
    out.append("")
    out.append(f"- Checked: **{len(results)}**")
    out.append(f"- OK (2xx/3xx): **{len(ok)}**")
    out.append(f"- Failed: **{len(bad)}**")
    out.append("")
    if bad:
        out.append("## Failed URLs")
        out.append("")
        out.append("| Status | URL | Source | Message |")
        out.append("|---|---|---|---|")
        for url, status, msg, sources in bad:
            s = "—" if status is None else str(status)
            out.append(f"| {s} | <{url}> | {', '.join(sources)} | {msg} |")
        out.append("")
    out.append("## All URLs")
    out.append("")
    out.append("| Status | URL | Source |")
    out.append("|---|---|---|")
    for url, status, _msg, sources in results:
        s = "—" if status is None else str(status)
        out.append(f"| {s} | <{url}> | {', '.join(sources)} |")
    out.append("")
    return "\n".join(out)


def run(only_changed: bool = False) -> int:
    urls = _collect_urls()
    if only_changed:
        urls = _filter_urls_to_changed(urls)

    if not urls:
        print("No URLs to check. (Empty data model, or --only-changed with no changes.)")
        REPORT_PATH.write_text("# Link-check report\n\nNo URLs to check.\n", encoding="utf-8")
        return 0

    print(f"Checking {len(urls)} unique URL(s)...")
    results: list[tuple[str, int | None, str, list[str]]] = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        future_to_url = {pool.submit(_check_one, url): url for url in urls}
        for fut in as_completed(future_to_url):
            url, status, msg = fut.result()
            sources = urls[url]
            results.append((url, status, msg, sources))
            mark = "OK " if status and 200 <= status < 400 else "FAIL"
            print(f"  {mark}  {status if status is not None else '---'}  {url}")

    REPORT_PATH.write_text(_format_report(results), encoding="utf-8")

    bad_count = sum(1 for _u, s, _m, _src in results if not (s and 200 <= s < 400))
    if bad_count == 0:
        print(f"\nAll {len(results)} URLs OK. Report: {REPORT_PATH.relative_to(REPO_ROOT)}")
        return 0
    print(
        f"\n{bad_count} of {len(results)} URLs failed. "
        f"Report: {REPORT_PATH.relative_to(REPO_ROOT)}"
    )
    return 1


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--only-changed",
        action="store_true",
        help="Check only URLs in JSON files changed since origin/main (or HEAD~1).",
    )
    args = parser.parse_args(list(argv) if argv is not None else None)
    return run(only_changed=args.only_changed)


if __name__ == "__main__":
    sys.exit(main())
