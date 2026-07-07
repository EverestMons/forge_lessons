# Lessons Forge — Gate 1 Route Disposition (cycle 2026-07-06)
**Date:** 2026-07-06 | **Tier:** Small | **Dispatch Mode:** bellows | **Test Scope:** targeted | **Execution:** Step 1 (DEV) → Step 2 (QA) | **qa_steps:** 1 | **pause_for_verdict:** always

## CEO Context

First Gate 1 with route assignment, dispositioning the 15 proposals from cycle 2026-07-06 (plan 131). CEO dispositions are final and embedded below: 13 codify, 2 reference, 0 backlog. Cluster-1 consolidation (entries 125/126/129/135 → one umbrella rule) is a Gate 2 authoring decision — routes here are recorded per-proposal. Entries 132/133 route reference because their fixes already shipped (plan 62/63, FORWARD canaries verified). Entry 136's codify target is the EXISTING `forge/agents/FORGE_QA.md` (created 2026-06-12, plan 8) — the "file does not exist" classifier flag was stale. Writes to the canonical `lessons-forge.db` go through the shipped module API `set_proposal_route()` (commit `643e9e7`) — this plan is its first live exercise. Proposal `status` values are NOT changed here; status transitions happen at Gate 2.

**Disposition table (authoritative for both steps):**

| Entry | Route |
|---|---|
| 123 | codify |
| 124 | codify |
| 125 | codify |
| 126 | codify |
| 127 | codify |
| 128 | codify |
| 129 | codify |
| 130 | codify |
| 131 | codify |
| 132 | reference |
| 133 | reference |
| 134 | codify |
| 135 | codify |
| 136 | codify |
| 137 | codify |

## How to Run This Plan

Paste the bootstrap prompt into Claude Code.

**Bootstrap prompt:**
```
Read the plan at lessons-forge/knowledge/decisions/executable-gate1-route-disposition-2026-07-06.md. Execute Step 1, then Step 2. Do NOT move the plan to Done until both steps are fully complete.
```

---
---

## STEP 1 — DEV

---

> **FIRST — before any reads or work: post a short visible message to chat (1-2 sentences) confirming you are starting this plan and stating your immediate next action.** Do NOT rename the plan file.
>
> You are Lessons Forge DEV. Read your specialist file at `lessons-forge/agents/FORGE_LESSONS_AGENT.md` first. All commands run from `/Users/marklehn/Developer/GitHub/lessons-forge`.
>
> **Scope:**
> - `knowledge/development/gate1-dispositions-2026-07-06.md`
>
> **Evidence-source rule for this step:** the canonical DB is `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db` — reachable from ANY working directory via that absolute path. A worktree having no local DB copy is never a reason to substitute a different DB. All writes in this step target the canonical DB via the module API; do not write raw UPDATE statements.
>
> 1. Map entries to proposal ids mechanically: query the canonical DB for `SELECT id, entry_id FROM lesson_proposals WHERE status='proposed' ORDER BY entry_id`. Expect EXACTLY 15 rows covering entries 123-137. If the count or entry set differs, STOP and report — do not guess a mapping.
> 2. For each of the 15 proposals, call `set_proposal_route(conn, proposal_id, route)` with the route from the CEO disposition table at the top of this plan. Do not modify `status` or any other column.
> 3. Re-query and confirm all 15 have non-NULL routes matching the table before depositing.
>
> **Deposit:** `lessons-forge/knowledge/development/gate1-dispositions-2026-07-06.md` — one opening paragraph (first route-assignment Gate 1; cycle 2026-07-06; API used), then a table with columns entry_id | proposal_id | route as written, then counts (codify/reference/backlog), and an Output Receipt with status. In `### Ledger Updates` include: `#### Project Status` — one paragraph: Gate 1 routes recorded for cycle 2026-07-06 (13 codify / 2 reference) via first live use of `set_proposal_route`; Gate 2 codification pending; `#### Prompt Feedback` — standard.
>
> **Deposits:**
> - `lessons-forge/knowledge/development/gate1-dispositions-2026-07-06.md`
>
> STOP. Do NOT proceed to Step 2. The daemon dispatches Step 2 separately.

---
---

## STEP 2 — QA

---

> **FIRST — before any reads or work: post a short visible message to chat (1-2 sentences) confirming you are starting this step and stating your immediate next action.** Do NOT rename the plan file.
>
> You are Lessons Forge QA. Read your specialist file at `lessons-forge/agents/FORGE_LESSONS_AGENT.md` first. All commands run from `/Users/marklehn/Developer/GitHub/lessons-forge`.
>
> **Rule 20 self-check is gate-enforced on this step.** Your QA report MUST include the byte-exact banner `Rule 20 — QA Self-Check Results` and a `PASSED — SELF-CHECK PASSED` line; end with a self-grep confirming the banner is present in your deposited report.
>
> **Scope:**
> - `knowledge/qa/gate1-route-disposition-qa-2026-07-06.md`
>
> **Evidence-source rule for this step:** every SQL row in your table MUST state which DB it ran against. The canonical DB is reachable from ANY working directory via `sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" "<query>"` — a worktree having no local DB copy is never a reason to substitute. All verification reads use this read-only URI.
>
> Produce a verification table, one row per claim, each against the canonical read-only URI: (1) all rows with `status='proposed'` have non-NULL `route` and count exactly 15; (2) route counts are codify=13, reference=2, backlog=0; (3) per-entry routes match the CEO disposition table at the top of this plan EXACTLY — list every mismatch, zero expected; (4) no collateral writes: count of rows with `status != 'proposed'` AND `route IS NOT NULL` is 0; (5) targeted tests pass in isolation: `test_migration_idempotence_double_init`, `test_migration_adds_route_to_pre_existing_db`, and any test covering `set_proposal_route` — temp-DB evidence, label it as such. If any row fails, report it and halt — do not pass a broken deliverable.
>
> **Deposit:** `lessons-forge/knowledge/qa/gate1-route-disposition-qa-2026-07-06.md` — verification table with per-row DB-source declarations, targeted-test output tails, the Rule 20 self-check block, and an Output Receipt with status. Commit the QA report and the Step 1 deposit if uncommitted. In `### Ledger Updates` include: `#### Project Status` — one paragraph: Gate 1 route dispositions verified against canonical DB (15/15 routed, 13 codify / 2 reference); `#### Prompt Feedback` — standard.
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/gate1-route-disposition-qa-2026-07-06.md`
>
> On full completion, move the plan file to `lessons-forge/knowledge/decisions/Done/` as the absolute last operation.
