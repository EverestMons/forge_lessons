# Lessons Forge — Learning-Loop Routing & Cadence Audit
**Date:** 2026-07-06 | **Tier:** Small | **Dispatch Mode:** bellows | **Test Scope:** targeted | **Execution:** Step 1 (SA) | **pause_for_verdict:** always

## CEO Context

CEO observation (2026-07-06): the shop runs heavy plan/execute volume but the learning loop surfaces feedback irregularly, and captured lessons have only two fates — codified into PLANNER_TEMPLATE at a cycle, or nothing. Proposal 129 (routed by hand to the bellows BACKLOG) exposed the missing third and fourth routes: action-item and reference-grade knowledge. Two candidate fixes are on the table: (1) a capture-time route field per LESSONS entry (`codify | backlog | reference`), and (2) an evidence-count trigger that nudges a cycle when unclassified entries or closed plans cross a threshold. Per diagnostic-first discipline, this plan enumerates current state before either fix is designed. Prompt Forge corpus plateau is established (cycle #16, shop baton 2026-07-03) and is OUT OF SCOPE; Anvil is not yet live and is OUT OF SCOPE. This diagnostic is READ-ONLY — no code changes, no DB writes, no commits except the deposit.

## How to Run This Plan

Paste the bootstrap prompt into Claude Code. Single-step plan — the agent executes Step 1 and the daemon pauses for verdict at completion.

**Bootstrap prompt:**
```
Read the plan at lessons-forge/knowledge/decisions/diagnostic-learning-loop-routing-audit-2026-07-06.md. Execute Step 1. Do NOT move the plan to Done until Step 1 is fully complete.
```

---
---

## STEP 1 — SA

---

> **FIRST — before any reads or work: post a short visible message to chat (1-2 sentences) confirming you are starting this plan and stating your immediate next action.** Do NOT rename the plan file.
>
> You are the Lessons Forge agent. Read your specialist file at `lessons-forge/agents/FORGE_LESSONS_AGENT.md` first. All commands run from `/Users/marklehn/Developer/GitHub/lessons-forge`. **READ-ONLY: no code changes, no DB writes, no commits except the deposit.** All DB reads use the read-only URI form: `sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" "<query>"`.
>
> **Scope:**
> - `knowledge/research/learning-loop-routing-audit-2026-07-06.md`
>
> **Task 1 — channel state.** Quantify the current Lessons Forge backlog: (a) total `lesson_entries`; (b) the unclassified work list via `get_unclassified_entries(conn)` (invoke the helper itself from `src/lessons_forge.py`, per Orchestration Rule #47 — do not hand-copy SQL) — report count, entry dates, and tags; (c) date of the most recent classification/cycle activity in the DB, and days elapsed since. This establishes how much captured-but-unprocessed learning exists right now and how stale the loop is.
>
> **Task 2 — routing outcomes.** For all rows in `lesson_proposals`, report the status breakdown (implemented / superseded / rejected / stale / proposed / accepted). Then, for the `implemented` set, determine the DESTINATION of each: PLANNER_TEMPLATE edit, BACKLOG route (e.g. proposal 129), or other. State explicitly whether the schema records destination as a column or whether it must be reconstructed from Gate 2 records, reports in `reports/`, and batons — if the schema does not record it, that absence is itself a finding. Separately, enumerate the per-entry classification schema the classifier emits (columns on `lesson_entries` and any classification tables): could an existing field carry a route value (`codify | backlog | reference`) without a schema migration, or would one be required? Cite column names from `src/db.py`.
>
> **Task 3 — trigger inventory.** Enumerate the counters and trigger mechanics that already exist which a cycle-nudge could reuse, with file:line citations: (a) the `get_unclassified_entries(conn)` count; (b) a plans-closed-since-timestamp query against `bellows/lifecycle.db` (read-only URI; confirm the table/columns that support it); (c) the `timeline.md` trigger mechanics at governance root (calendar backstop / evidence-count threshold — cite where the trigger logic lives, or state that it is convention-only with no code); (d) candidate hook points for a nudge: the Bellows daemon loop + `notifier.py` Pushover path vs a Phase 1.5 session-start check. For each option state what exists, what is missing, and rough cost. Do NOT decide between them — enumerate only.
>
> **Task 4 — Gap Assessment table.** End the deposit with the required table for change-proposing diagnostics: one row per candidate change (route field; evidence trigger; destination column if Task 2 finds it missing) with columns: candidate change | current behavior | gap | evidence (file:line or DB query) | affected components.
>
> **Deposit:** `knowledge/research/learning-loop-routing-audit-2026-07-06.md` — Tasks 1-4 findings, the Gap Assessment table, and an Output Receipt with status. Use the canonical Python file-write pattern — no heredoc. Commit the deposit: `git add knowledge/research/learning-loop-routing-audit-2026-07-06.md && git commit -m "docs(lessons-forge): learning-loop routing and cadence audit"`. In `### Ledger Updates` include `#### Prompt Feedback` only (no Project Status — diagnostic).
>
> **Deposits:**
> - `lessons-forge/knowledge/research/learning-loop-routing-audit-2026-07-06.md`
>
> On full completion, move the plan file to `lessons-forge/knowledge/decisions/Done/` as the absolute last operation.
