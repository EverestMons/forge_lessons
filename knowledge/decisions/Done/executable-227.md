# Lessons Forge — Gate 1 Route Disposition (cycle 2026-07-17)
**Date:** 2026-07-18 | **Tier:** Small | **Dispatch Mode:** bellows | **Test Scope:** targeted | **Execution:** Step 1 (DEV) → Step 2 (QA) | **qa_steps:** 2 | **pause_for_verdict:** always

## CEO Context

Gate 1 for the six proposals from cycle 2026-07-17 (plans 225/226). **CEO disposition, final, 2026-07-18: ALL SIX → `codify`. Zero backlog, zero reference** — none of the six has a shipped code fix that makes the RULE redundant; all are live gaps in governance text.

**Disposition table (authoritative for both steps):**

| Proposal | Entry | Substance | Route |
|---|---|---|---|
| 149 | 141 | bare expected numbers → verify-and-explain | **codify** |
| 150 | 142 | THE DRAFTING CYCLE (named process) | **codify** |
| 151 | 143 | worktree QA cannot verify live-DB migration | **codify** |
| 152 | 144 | drafting-cycle pass 4 (integration-vs-record) | **codify** |
| 153 | 145 | region-scoped metrics computed unscoped | **codify** |
| 154 | 146 | schema bumps fix version pins same-step | **codify** |

**Linkage binding on Gate 2 (record it, do not act on it here):** 150+152 are ONE governance item — the Drafting Cycle codifies as a named process WITH its fourth lens; the trigger-criteria decision (which plans REQUIRE a cycle) is the CEO's at Gate 2 authoring.

**Gate 1 changes ROUTES ONLY.** All six stay `status='proposed'` — transitions are Gate 2's (plan-206/208 precedent). Writes go through the module API `set_proposal_route()`, never hand-written SQL.

**Blast radius (verified pre-flight 2026-07-18, canonical read-only):** 18 proposals currently carry a route (15 from the 2026-07-06 Gate, 3 from the 2026-07-16 Gate). Expected after: 24, delta exactly +6 — verify and report the ACTUAL numbers; a plan-text number is a hypothesis, never a target (codify-candidate 149 is literally this rule — do not violate it in its own disposition plan).

**Deposit-once discipline:** deposited exactly once.

## How to Run This Plan

**Bootstrap prompt:**
```
Read the plan at lessons-forge/knowledge/decisions/executable-lessons-forge-gate-1-2026-07-18.md. Execute Step 1 ONLY. After completing Step 1, STOP and wait for my confirmation. Do NOT proceed to Step 2.
```

---
---

## STEP 1 — DEV

---

> **FIRST — post a short visible chat message (1-2 sentences) confirming you are starting this plan and your immediate next action.** Do NOT rename the plan file.
>
> You are the Lessons Forge Developer. All commands run from `/Users/marklehn/Developer/GitHub/lessons-forge`. **Write your deposit file relative to your working tree; all canonical-DB access uses the ABSOLUTE path** `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db`.
>
> **This step changes the canonical DB only — no `src/` changes.**
>
> **Scope:**
> - `knowledge/development/gate-1-route-disposition-2026-07-18.md`
>
> **Task A — record the routes.** Via `set_proposal_route(conn, proposal_id, 'codify')` from `src.lessons_forge` for each of 149, 150, 151, 152, 153, 154. Commit the deposit (the DB is untracked).
>
> **Task B — prove routes-only.** Capture the full proposal STATUS distribution before and after and assert IDENTICAL (expected: implemented 99, superseded 28, rejected 15, proposed 6, stale 3, reference 3 — verify and report actual). Read back `SELECT id, entry_id, status, route FROM lesson_proposals WHERE id BETWEEN 149 AND 154` — all six `codify`, all six still `proposed`.
>
> **Task C — blast radius.** `SELECT COUNT(*) FROM lesson_proposals WHERE route IS NOT NULL` before and after — expected 18 → 24, delta exactly +6; verify and report actual; on any other delta, halt and report which rows changed.
>
> **Deposit:** `knowledge/development/gate-1-route-disposition-2026-07-18.md` — the API calls made, before/after status distributions (identical), the six-row read-back, the route-count check, Output Receipt. Canonical Python file-write pattern — no heredoc. In `### Ledger Updates` include `#### Prompt Feedback`.
>
> **Deposits:**
> - `lessons-forge/knowledge/development/gate-1-route-disposition-2026-07-18.md`
>
> **STOP. Do NOT proceed to Step 2. Wait for CEO verdict.**

---
---

## STEP 2 — QA

---

> **Before starting, read the Step 1 deposit and confirm Output Receipt status Complete; otherwise halt and report.** Post a short visible chat message confirming you are starting Step 2 (QA).
>
> You are Lessons Forge QA. All commands from `/Users/marklehn/Developer/GitHub/lessons-forge`. **Verification + reporting only.**
>
> **Rule 20 self-check is gate-enforced.** Your deposit MUST contain, verbatim, `## Rule 20 — QA Self-Check Results` and a line reading exactly `**PASSED — SELF-CHECK PASSED**`; end with a self-grep confirming it.
>
> **Evidence-source rule:** every SQL row states its DB; canonical reads via `sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" "<query>"`. RAW output only.
>
> **Scope:**
> - `knowledge/qa/gate-1-route-disposition-qa-2026-07-18.md`
>
> Verification table, DB-source column on each row: (1) routes per the CEO table — raw six-row read-back, all `codify`; (2) statuses unchanged — all six still `proposed`; full distribution matches Step 1's before-snapshot (quote both); **the route/status columns are DIFFERENT columns — a `status` change here would be a Gate-2 transition smuggled into Gate 1 and is a FAIL**; (3) blast radius — route count went 18 → 24 (verify actual; quote raw counts); no proposal outside 149–154 gained or changed a route; (4) standing regression watch — proposal 145 still `implemented`, stale still 3, `get_unclassified_entries()` still `[]`; (5) targeted tests — `python3 -m pytest src/ -q -k "route or proposal"` (never `timeout`), report actual counts. Any failing row: report and halt.
>
> **Deposit:** `knowledge/qa/gate-1-route-disposition-qa-2026-07-18.md` — table, raw outputs, Rule 20 banner + PASSED line, Output Receipt. Canonical Python file-write pattern — no heredoc. Commit it. In `### Ledger Updates` include: `#### Project Status` — one milestone paragraph (Gate 1 2026-07-18: six proposals → codify, incl. the Drafting Cycle as one linked item; Gate 2 codification pending, target v4.75); `#### Prompt Feedback` — standard.
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/gate-1-route-disposition-qa-2026-07-18.md`
>
> On full completion, move the plan file to `lessons-forge/knowledge/decisions/Done/` as the absolute last operation.
