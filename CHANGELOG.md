# Changelog

All notable changes to this roadmap are recorded here. The roadmap follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) conventions, with a
monthly "pulse" entry that summarizes resource additions, revisions, and
removals.

## [Unreleased]

## [0.1.0] — 2026-05-14

### Added
- Initial release: the full 12-stage / 96-node taxonomy of the AI-engineer
  career path.
- Structured data model in `roadmap-data/` with JSON Schemas for stages,
  nodes, and resources.
- Tooling: `tools/validate_data.py`, `tools/linkcheck.py`,
  `tools/build.py`.
- CI: data validation on every push, link-check on every push and on a
  weekly cron.
- Interactive site: Vite + React + React Flow renderer with pan, zoom,
  click-for-resources, search, and a dark/paper-warm theme.
- README, CONTRIBUTING, CITATION.cff, dual licensing (content CC-BY-4.0
  / code MIT).
- Curated and link-verified resource entries on every node.
- Constellation peer-link block to `harness-engineer-roadmap`,
  `llm-interview-prep`, `build-your-own-ai`.
- Sideways hand-off card from the Agents & Harnesses stage to
  `harness-engineer-roadmap` for the depth dive.
