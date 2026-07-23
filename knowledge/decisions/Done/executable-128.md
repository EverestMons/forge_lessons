# Lessons Forge — Route Column on `lesson_proposals` (routing outcome capture)
**Date:** 2026-07-06 | **Tier:** Small | **Dispatch Mode:** bellows | **Test Scope:** both | **Execution:** Step 1 (DEV) → Step 2 (QA) | **qa_steps:** 2 | **pause_for_verdict:** always

## CEO Context

Implements Gap Assessment row 1 of diagnostic-127 (`knowledge/research/learning-loop-routing-audit-2026-07-06.md`). Finding: routing outcomes (codify to PLANNER_TEMPLATE vs route to a BACKLOG vs archive as reference) are not captured anywhere — `target_artifact` records the edit-target file only, 15/90 implemented proposals have it NULL, and proposal 129's hand-route to the Bellows BACKLOG left zero DB trace. No existing column can carry the value (subcategory is a Phase-2 taxonomy reservation; overloading it was rejected). This plan adds a nullable `route` column with a CHECK constraint, threads it through insert and disposition paths, and surfaces it in the report. Historical rows stay NULL (pre-route history) — NO backfill. The capture-time LESSONS.md convention and any Gate 1/Gate 2 workflow rules are OUT OF SCOPE — those are PLANNER_TEMPLATE edits that go through the normal Lessons Forge Gate 2 path, not this plan. Companion plan (independent, parallel): `bellows/knowledge/decisions/executable-cycle-nudge-trigger-2026-07-06.md`.

## How to Run This Plan

Paste the bootstrap prompt into Claude Code. The agent reads the full plan file and executes Step 1 ONLY. After completing Step 1, the agent STOPS and waits for CEO confirmation before proceeding to Step 2. The agent must never skip steps, auto-chain, or move the plan to Done without completing all steps including QA.

**Bootstrap prompt:**
```
Read the plan at lessons-forge/knowledge/decisions/executable-route-field-lesson-proposals-2026-07-06.md. Execute Step 1 ONLY. After completing Step 1, STOP and wait for my confirmation. Do NOT proceed to Step 2 or move the plan to Done.
```

---
---

## STEP 1 — DEV

---

> **FIRST — before any reads or work: post a short visible message to chat (1-2 sentences) confirming you are starting this plan and stating your immediate next action.** Do NOT rename the plan file.
>
> You are the Lessons Forge Developer. Read your specialist file at `lessons-forge/agents/FORGE_LESSONS_AGENT.md` first. All commands run from `/Users/marklehn/Developer/GitHub/lessons-forge`.
>
> **Scope:**
> - `src/db.py`
> - `src/lessons_forge.py`
> - `src/test_lessons_forge.py`
> - `knowledge/development/route-field-lesson-proposals-2026-07-06.md`
>
> **Change 1 — schema.** In `src/db.py:init_db()`, add `route TEXT CHECK(route IN ('codify', 'backlog', 'reference'))` (nullable, no default) to the `lesson_proposals` CREATE TABLE. Existing-DB migration: follow the migration pattern db.py already uses if one exists; if none exists, add a guarded `ALTER TABLE lesson_proposals ADD COLUMN ...` inside `init_db()` that fires only when `PRAGMA table_info(lesson_proposals)` shows the column absent. `init_db()` must remain idempotent — running it twice against the same DB must not error.
>
> **Change 2 — insert path.** `insert_proposal()` in `src/lessons_forge.py` gains an optional `route: str | None = None` parameter, validated against the three allowed values or None (raise `ValueError` on anything else — do not rely on the DB CHECK alone), written to the new column. All existing call sites remain valid unchanged (keyword-optional).
>
> **Change 3 — disposition path.** Inspect how proposal status is updated at disposition (the path that sets `status`/`status_updated_at`/`status_updated_by`). Extend the minimal-surface option: either add an optional `route` parameter to the existing update helper or add a small `set_proposal_route(conn, proposal_id, route)` — pick whichever is smaller given the actual code shape, state which and why in the dev log. Same three-value-or-None validation.
>
> **Change 4 — report.** `generate_lessons_report()` includes the route value on proposal rows where present (NULL rows render without it — no placeholder noise).
>
> **Change 5 — tests.** In `src/test_lessons_forge.py`, existing tests must pass UNCHANGED — if any fails, halt and report in the Output Receipt; do NOT rewrite assertions. Add new tests: (a) insert with each valid route value persists and reads back; (b) invalid route raises ValueError at the Python layer AND a direct SQL insert with an invalid value is rejected by the CHECK constraint; (c) migration idempotence — `init_db()` twice on one DB, then once against a DB created WITHOUT the column (simulating pre-migration state) and verify the column appears; (d) disposition-path route set persists.
>
> **Self-verify.** Run the FULL suite with `timeout 600 python3 -m pytest src/ -v` to an explicit pass/fail and READ THE TAIL — never infer green from a subset or collect count.
>
> **Commit** with a descriptive message (e.g. `feat(lessons-forge): route column on lesson_proposals — routing outcome capture (diagnostic-127 gap 1)`).
>
> **Deposit:** `lessons-forge/knowledge/development/route-field-lesson-proposals-2026-07-06.md` — dev log with: exact diff hunks (or verbatim old/new blocks), the migration approach chosen and why, the new test names + one-line rationale each, the full-suite tail verbatim, commit hash, and an Output Receipt with status. Use the canonical Python file-write pattern — no heredoc. In `### Ledger Updates` include `#### Prompt Feedback` (daemon-owned; do NOT edit any feedback file directly).
>
> **Deposits:**
> - `lessons-forge/knowledge/development/route-field-lesson-proposals-2026-07-06.md`
>
> **STOP. Do NOT proceed to Step 2. Do NOT move the plan to Done. Wait for CEO verdict before continuing.**

---
---

## STEP 2 — QA

---

> **Before starting, read the Step 1 dev-log deposit at `lessons-forge/knowledge/development/route-field-lesson-proposals-2026-07-06.md` and check its Output Receipt status. If status is not Complete, halt and report the blocker before proceeding.**
>
> You are Lessons Forge QA. Read your specialist file at `lessons-forge/agents/FORGE_LESSONS_AGENT.md` first.
>
> **Rule 20 self-check is gate-enforced on this step.** Your QA report MUST include the byte-exact banner `Rule 20 — QA Self-Check Results` and a `PASSED — SELF-CHECK PASSED` line; the verification table below does NOT by itself satisfy the gate — end with a self-grep confirming the banner is present in your deposited report.
>
> **Scope:**
> - `knowledge/qa/route-field-lesson-proposals-qa-2026-07-06.md`
>
> Verify the route column. Produce a verification table, one row per claim: (1) `PRAGMA table_info(lesson_proposals)` against the canonical `lessons-forge.db` (read-only URI) shows the `route` column — quote the output; (2) the CHECK constraint rejects an invalid value — prove against a THROWAWAY temp DB created via `init_db()`, never the canonical DB; (3) `insert_proposal()` accepts `route` keyword and existing call sites are unchanged — cite the signature and a grep of call sites; (4) disposition-path route set exists per the dev log's chosen shape and its test passes in isolation; (5) migration idempotence test passes in isolation; (6) `generate_lessons_report()` renders route where present, no placeholder on NULL rows — quote the relevant code; (7) pre-existing tests pass with assertions untouched — verify via `git diff HEAD~1 -- src/test_lessons_forge.py` that no existing assertion lines were modified (additions only); (8) full suite green: re-run `timeout 600 python3 -m pytest src/ -v` to an explicit pass/fail and show the tail. If any row fails, report it and halt — do not pass a broken deliverable.
>
> **Deposit:** `lessons-forge/knowledge/qa/route-field-lesson-proposals-qa-2026-07-06.md` — verification table, full-suite tail, the Rule 20 self-check block, and an Output Receipt with status. Commit the QA report. In `### Ledger Updates` include: `#### Project Status` — one milestone paragraph: route column shipped 2026-07-06, routing outcomes (codify/backlog/reference) now capturable at insert and disposition, historical rows NULL by design; `#### Prompt Feedback` — standard.
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/route-field-lesson-proposals-qa-2026-07-06.md`
>
> On full completion, move the plan file to `lessons-forge/knowledge/decisions/Done/` as the absolute last operation.
