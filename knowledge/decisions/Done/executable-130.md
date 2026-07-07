# Lessons Forge — Route-Field QA Correction (supersedes plan 128 QA row 1)
**Date:** 2026-07-06 | **Tier:** Small | **Dispatch Mode:** bellows | **Test Scope:** targeted | **Execution:** Step 1 (QA) | **qa_steps:** 1 | **pause_for_verdict:** always

## CEO Context

Plan 128 (route column on `lesson_proposals`, commit `643e9e7`) halted at its QA step by CEO decision: verification row 1 presented a fresh-`init_db` PRAGMA as canonical-DB evidence, undisclosed, while the canonical `lessons-forge.db` does not yet have the `route` column. The column absence is CORRECT behavior — the guarded migration fires when `init_db()` next runs against the canonical DB (cycle start), and nothing writes routes before a cycle — but the record must say so accurately. This plan re-issues the verification with the canonical check done properly via absolute-path read-only URI. The dev deliverable is landed and is NOT re-worked here; the original QA report stays on disk as history. This plan is READ-ONLY on the canonical DB — the only writes are the QA report deposit and its commit.

## How to Run This Plan

Paste the bootstrap prompt into Claude Code. Single-step plan — the agent executes Step 1 and the daemon pauses for verdict at completion.

**Bootstrap prompt:**
```
Read the plan at lessons-forge/knowledge/decisions/executable-route-field-qa-correction-2026-07-06.md. Execute Step 1. Do NOT move the plan to Done until Step 1 is fully complete.
```

---
---

## STEP 1 — QA

---

> **FIRST — before any reads or work: post a short visible message to chat (1-2 sentences) confirming you are starting this plan and stating your immediate next action.** Do NOT rename the plan file.
>
> You are Lessons Forge QA. Read your specialist file at `lessons-forge/agents/FORGE_LESSONS_AGENT.md` first. All commands run from `/Users/marklehn/Developer/GitHub/lessons-forge`.
>
> **Rule 20 self-check is gate-enforced on this step.** Your QA report MUST include the byte-exact banner `Rule 20 — QA Self-Check Results` and a `PASSED — SELF-CHECK PASSED` line; the verification table below does NOT by itself satisfy the gate — end with a self-grep confirming the banner is present in your deposited report.
>
> **Scope:**
> - `knowledge/qa/route-field-lesson-proposals-qa-v2-2026-07-06.md`
>
> **Evidence-source rule for this step:** every PRAGMA/SQL row in your table MUST state which DB it ran against (canonical absolute path vs throwaway temp). The canonical DB is reachable from ANY working directory via `sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" "<query>"` — a worktree having no local DB copy is never a reason to substitute.
>
> Produce a verification table, one row per claim: (1) canonical DB via the absolute-path read-only URI: `PRAGMA table_info(lesson_proposals)` — quote the output and state the EXPECTED finding explicitly: the `route` column is ABSENT because the guarded migration fires at the next `init_db()` run against this DB (cycle start); nothing writes routes before a cycle, so absent-now is correct behavior, not a defect. If the column IS present, report that too (an init_db ran since 2026-07-06 19:49) — either state passes; what matters is the accurate canonical reading. (2) Fresh throwaway temp DB via `init_db()`: PRAGMA shows the `route` column with the CHECK constraint — DDL + migration-path proof, labeled as temp-DB evidence. (3) Migration tests `test_migration_idempotence_double_init` and `test_migration_adds_route_to_pre_existing_db` pass in isolation. (4) Full suite green: `timeout 600 python3 -m pytest src/ -v` to an explicit pass/fail, show the tail. If any row fails, report it and halt — do not pass a broken deliverable.
>
> **Deposit:** `lessons-forge/knowledge/qa/route-field-lesson-proposals-qa-v2-2026-07-06.md` — open with one paragraph stating this report supersedes verification row 1 of `knowledge/qa/route-field-lesson-proposals-qa-2026-07-06.md` (which presented fresh-init_db evidence as canonical; original retained as history), then the verification table, full-suite tail, the Rule 20 self-check block, and an Output Receipt with status. Commit the QA report. In `### Ledger Updates` include: `#### Project Status` — one corrective paragraph: route-column verification corrected 2026-07-06; canonical DB migrates at next init_db (cycle start) by design; deliverable (commit 643e9e7) confirmed sound; `#### Prompt Feedback` — standard.
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/route-field-lesson-proposals-qa-v2-2026-07-06.md`
>
> On full completion, move the plan file to `lessons-forge/knowledge/decisions/Done/` as the absolute last operation.
