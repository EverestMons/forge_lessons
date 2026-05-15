# Lessons Forge — Project Brief

## Purpose

Layer 2 governance improvement tool. Ingests Planner-side lesson observations from `LESSONS.md` at governance root (`/Users/marklehn/Developer/GitHub/LESSONS.md`), classifies them, and proposes ratifications for governance updates.

## Architecture

Source-of-truth design: `governance/adr/ADR-002-lessons-forge-design.md`.

## Pipeline

1. **Parse** — Segment `LESSONS.md` by dated headings, extract tags and content hashes.
2. **Ingest** — Upsert parsed entries into `lesson_entries` table with idempotency (content-hash dedup).
3. **Detect duplicates** — Compare against reference files via tag keyword overlap and heading substring matching.
4. **Classify** — Agent-driven categorization of lesson entries.
5. **Generate report** — Produce human-readable lessons report.
6. **Planner review** — Planner reviews proposals for ratification.

## Database

`lessons-forge.db` — SQLite database with two tables:
- `lesson_entries` — Ingested lesson observations.
- `lesson_proposals` — Classification and ratification proposals linked to entries.

## Specialist

`agents/FORGE_LESSONS_AGENT.md` — Agent specialist file for lessons classification and proposal generation.

## Reports

`reports/lessons-report-YYYY-MM-DD.md` — Cycle output deposited per run.

## Provenance

Extracted from `forge/` on 2026-05-16 per B2 carry-forward decision. See `governance/adr/ADR-002-lessons-forge-design.md` for original design.
