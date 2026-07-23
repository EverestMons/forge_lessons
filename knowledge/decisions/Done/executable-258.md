# Lessons Forge — Gate 1 Route Disposition (cycle 2026-07-22)
**Date:** 2026-07-22 | **Tier:** Small | **Dispatch Mode:** bellows | **Test Scope:** targeted | **Execution:** Step 1 (DEV) → Step 2 (QA) | **qa_steps:** 2 | **pause_for_verdict:** always

## CEO Context

Gate 1 for the 15 proposals from cycle 2026-07-22 (plan 257). **CEO dispositions are final and embedded below: 14 codify, 1 reference, 0 backlog.**

**Disposition table (authoritative for both steps):**

| Proposal | Entry | Topic | Route | Status after |
|---|---|---|---|---|
| 172 | 164 | execute a FALSE-FAIL-able check vs real data | **codify** | `proposed` (unchanged) |
| 173 | 165 | any executable check needs execution vs real data | **codify** | `proposed` (unchanged) |
| 174 | 166 | three-rung successor ladder (halted triage) | **codify** | `proposed` (unchanged) |
| 175 | 167 | a diagnostic's substance is FINDINGS, not code | **codify** | `proposed` (unchanged) |
| 176 | 168 | directory-declared deposit is unfalsifiable | **codify** | `proposed` (unchanged) |
| 177 | 169 | `grep` is ignore-aware → completeness sweeps under-report | **codify** | `proposed` (unchanged) |
| 178 | 170 | re-run the lens that found the defect ON the fix | **codify** | `proposed` (unchanged) |
| 179 | 171 | run the procedure on the hardest real items | **codify** | `proposed` (unchanged) |
| 180 | 172 | restructuring for DRY trades a new seam surface | **codify** | `proposed` (unchanged) |
| 181 | 173 | generalising a guard waters it down — pin the specifics | **codify** | `proposed` (unchanged) |
| 182 | 174 | the deliverable's physical shape is unasked | **codify** | `proposed` (unchanged) |
| **183** | **175** | **read the record before deriving** | **reference** | **`reference`** |
| 184 | 176 | worktree OUTPUT paths relative / reads absolute | **codify** | `proposed` (unchanged) |
| 185 | 177 | mechanical conformance pass (distinct from the 5 lenses) | **codify** | `proposed` (unchanged) |
| 186 | 178 | pre-stated conclusions anchor the executing agent | **codify** | `proposed` (unchanged) |

**⚠️ THIS GATE 1 WRITES STATUS AS WELL AS ROUTE.** Exactly ONE proposal changes status (`183` → `reference`); the other fourteen keep `proposed` because they are Gate-2-bound. This is a **predicted delta**, not identity — do not carry any "distribution byte-identical before/after" invariant into this plan.

**Dedup against the LIVE template was done at Gate-1 authoring (the 2026-06-07 discipline), grep-verified against `PLANNER_TEMPLATE.md` (2024 lines):**
- **183 is ALREADY CODIFIED.** "Read the record before deriving" is the `## The Drafting Cycle` **Integration-vs-Record Mandatory Floor** (`:318` — *"Before depositing any plan, run the integration-vs-record pass: scan the drafted plan against LESSONS.md, `knowledge/decisions/Done/`…"*), also the fourth Drafting-Cycle lens (`:338`). Entry 175's "run it EARLY, before deriving a method" is a timing emphasis on an existing pass, not a new rule → route **reference** (the corpus keeps the record; the template already has the rule).
- **The remaining fourteen are NOT codified** — each grep-checked at authoring. Near-misses ruled out as FALSE ALARMS: line 598 "execute every check" is a QA-*runtime* instruction, not the draft-time verification rule 172/173 add; the fourteen `diagnostic findings` hits are all "cite the diagnostic's findings" prose, not the halted-triage artifact-type classification (174/175 — no halted-triage section exists at all); the two `generalis` hits are Rule 7 ("No generalist *steps*"), unrelated to 181's guard-generalisation; `anchor`×49 is incidental to 186's pre-stated-conclusion rule.
- **Two are PARTIAL overlaps — codify as extensions, NOT competitors** (flagged for Gate 2 below): **178** overlaps Checklist **#26** (sibling sweep, `:1262`) but adds *re-run the lens that found the defect ON the fix* + run executable fixes vs real data; **184** overlaps the absolute-path-for-reads discipline (`:1278`/`:1290`) but adds the *write-relative* half (the plan-225 rule).

**⚠️ Notes for Gate 2 (NOT this plan's job — routing only here):**
- **The execute-before-deposit CLUSTER — 172, 173, 178, 179 — shares one spine** ("run the executable check / fix / procedure against real corpus data before deposit; the lenses cannot validate an executable check, only running it can"). Codify them as a coherent rule/set in `## The Drafting Cycle`, not four scattered edits.
- **174 and 175 are a halted-triage PAIR** → a new halted-plan-triage section (successor ladder + artifact-type-before-disposition).
- **178 amends Checklist #26** (extend/cross-reference, don't add a competing rule); **184 clarifies the Bellows-dispatch path rules** (split reads-absolute / writes-relative); **185 adds a mechanical conformance pass** distinct from the five lenses (broader than the `:1252` plan_lint mandate). **⚠️ Live datapoint for Gate 2 on 184:** cycle 257 ran IN-PLACE (no worktree) despite the plan's worktree assumption — Gate 2 should phrase 184 as read/write path *roles*, not a worktree presupposition.

**Scope discipline: routes and the ONE named status ONLY.** Do NOT edit `PLANNER_TEMPLATE.md` — codification is Gate 2. Do NOT touch `src/` — no code changes. Do not pre-draft template wording in any deposit.

**Deposit-once discipline:** deposited exactly once. **Authoring self-check:** `bellows/scripts/plan_lint.py` run at authoring — exit 0, all checks PASS, zero warnings (no test file belongs in any step's scope; Step 1 is a DB write, Step 2 verification-only).

## How to Run This Plan

**Bootstrap prompt:**
```
Read the plan at lessons-forge/knowledge/decisions/in-progress-executable-<id>.md (daemon renames the deposited placeholder on claim). Execute Step 1 ONLY. After completing Step 1, STOP and wait for my confirmation. Do NOT proceed to Step 2.
```

---
---

## STEP 1 — DEV

---

> **FIRST — before any reads or work: post a short visible chat message (1-2 sentences) confirming you are starting this plan and your immediate next action.** Do NOT rename the plan file.
>
> You are the Lessons Forge Developer (`/Users/marklehn/Developer/GitHub/forge/agents/FORGE_DEVELOPER.md` — skip with a note if absent). Run commands from **your own working tree**. **All canonical-DB access uses the ABSOLUTE path** `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db` — never substitute or skip a verification because a relative path resolves to nothing. `forge/forge.db` is a REAL but DIFFERENT database — never open it. **This step changes the canonical DB only; it MUST NOT touch `src/`.**
>
> **Open canonical read-WRITE** (`sqlite3.connect(<abs path>)`; do NOT reuse a `?mode=ro` handle for the writes). **⚠️ Task A and Task A2 are ONE transaction: a SINGLE `conn.commit()` after BOTH have run, never one commit per task** — a route written without its paired status change is the exact broken state QA row 3 calls a FAIL. The helper does not commit internally; the DB is gitignored so this is a SQLite commit, not a git commit.
>
> **Scope:**
> - `knowledge/development/gate-1-route-disposition-2026-07-22.md`
>
> **Task A00 — TAKE A RESTORE POINT BEFORE ANY WRITE.** Task A2 issues a hand-written SQL `UPDATE`; a missing `WHERE` clause would rewrite `status` on all 186 proposals with no undo path. **Use `.backup`, NOT `cp`** (live WAL). **Write to the MAIN tree by ABSOLUTE path** (a worktree-local backup dies at teardown): `mkdir -p /Users/marklehn/Developer/GitHub/lessons-forge/data/backups && sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" ".backup '/Users/marklehn/Developer/GitHub/lessons-forge/data/backups/lessons-forge-pre-gate1-<UTC-timestamp-colon-free>.db'"`. `.gitignore` matches `*.db` — confirm absent in `git -C /Users/marklehn/Developer/GitHub/lessons-forge status --porcelain`. **State the absolute path in your dev log. If the backup fails for ANY reason (non-zero exit, missing/zero-byte file) — HALT and write nothing.**
>
> **Task A0 — ISOLATION pre-flight, from the tree where the state lives.** This is an `R(before) → W → R(after)` schedule; assert no other writer. **Read the lifecycle state by ABSOLUTE MAIN-TREE path — a worktree-relative `ls` passes VACUOUSLY** (proposal 184, which this plan routes, is that exact class). Run `ls /Users/marklehn/Developer/GitHub/lessons-forge/knowledge/decisions/` and assert the POSITIVE signal: **your own plan file MUST appear** (as `in-progress-*` or `verdict-pending-*`) AND no OTHER `in-progress-*`/`verdict-pending-*` lessons plan. If your file is absent, you are reading the wrong tree — HALT. Do NOT use `get_unclassified_entries()` as the quiescence signal (it filters on `status`, never `route` — the exact conflict here is invisible to it); instead read the route-NOT-NULL count and status distribution twice a moment apart and confirm both unchanged. Concurrent writer possible → HALT.
>
> **Task A0 — PRECONDITION: verify targets match the disposition table BEFORE writing.** `SELECT id, entry_id, status, route FROM lesson_proposals WHERE id BETWEEN 172 AND 186 ORDER BY id` and assert all fifteen: the id→entry_id mapping is exactly `172→164, 173→165, …, 186→178` (contiguous, the cycle-257 batch); each `status` is `proposed` **or** already the target `reference` for 183 (idempotent re-run — tolerated); each `route` is **NULL or already this plan's target** (`codify` for the fourteen, `reference` for 183). **HALT only on genuine drift** (missing id, wrong entry_id, a status outside {`proposed`, its target}, or a route this plan never assigns for that id).
>
> **Task A0 also CAPTURES the "before" snapshots — pre-write.** Record and KEEP: (1) the full status distribution, (2) the route-NOT-NULL count. **Authoring-time expectation, to be confirmed not assumed:** status distribution `implemented 119, superseded 28, rejected 15, proposed 15, reference 6, stale 3` (total 186); route-NOT-NULL **41**. Report the ACTUAL; a mismatch is a finding, not a number to adjust to. Do NOT re-read "before" after Task A's write.
>
> **Task A — record the fifteen routes** with `set_proposal_route(conn, proposal_id, route)` from `src.lessons_forge` (NOT hand-written SQL):
> - `codify`: **172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 184, 185, 186** (fourteen)
> - `reference`: **183** (one)
>
> **Task A2 — record the ONE status change (hand-written SQL, deliberately).** No status-setter exists in `src/lessons_forge.py` (verified), so SQL is correct here, not a violation. For **183 ONLY**, set `status='reference'`, `status_updated_by='ceo'`, `status_updated_at` = current UTC (matching the existing reference rows 140/141/146/161/164/169, all `status_updated_by='ceo'`). Use a parameterised `UPDATE lesson_proposals SET status=?, status_updated_by=?, status_updated_at=? WHERE id=183` — **never a bare `UPDATE … SET status=…` without WHERE.** State the exact SQL in your dev log. **Why terminal:** `reference` is in `_TERMINAL_STATUSES`, so a future ingest whose entry-hash changes cannot silently stale this CEO disposition.
>
> **Then a SINGLE `conn.commit()`** (covers Task A + Task A2).
>
> **Task B — verify the ABSOLUTE post-state, then the delta as a fresh-run cross-check.**
> **B1 (primary, resume-invariant):** read the distribution now and assert exactly `proposed 14`, `reference 7`, `implemented 119`, `superseded 28`, `rejected 15`, `stale 3` — **total 186.** Any other value → HALT. (If the A0 pre-write snapshot did NOT match the authoring expectation, say so and halt rather than assuming these targets hold.)
> **B2 (fresh-run cross-check):** if A0 showed `proposed 15 / reference 6`, confirm the movement was `proposed −1`, `reference +1`, with implemented/superseded/rejected/stale untouched and no rows created/destroyed. If A0 already showed `proposed 14 / reference 7`, record `B2: N/A (resume)` and let B1 carry it. Then `SELECT id, entry_id, status, route FROM lesson_proposals WHERE id BETWEEN 172 AND 186 ORDER BY id` and confirm every row matches the disposition table on BOTH columns (trap: fourteen rows must show `route='codify'` with `status='proposed'` STILL; exactly one — 183 — shows `route='reference'` + `status='reference'`).
>
> **Task C — confirm the blast radius.** Measure and report actuals (do NOT hardcode): (1) the Task-B read-back of all fifteen; (2) route-NOT-NULL count rose by **≤15** over the A0 before-count (exactly 15 on a clean run → 56; fewer only on a resume); (3) `status='reference'` count rose by **≤1** (→ 7).
>
> **Deposit:** `knowledge/development/gate-1-route-disposition-2026-07-22.md` — the `set_proposal_route` calls made, the exact Task A2 SQL, the A0 pre-write snapshots + the after-values proving the delta, and the read-back of all fifteen rows as **RAW command output, not a summary** (qa-evidence-raw-output), plus an Output Receipt. Canonical Python file-write — no heredoc. Commit the deposit. In `### Ledger Updates` include `#### Prompt Feedback`.
>
> **Deposits:**
> - `lessons-forge/knowledge/development/gate-1-route-disposition-2026-07-22.md`
>
> **STOP. Do NOT proceed to Step 2. Wait for CEO verdict.**

---
---

## STEP 2 — QA

---

> **Before starting, read the Step 1 deposit and confirm Output Receipt status Complete; otherwise halt and report.** Post a short visible chat message confirming you are starting Step 2 (QA). You are Lessons Forge QA. Run commands from your own working tree; canonical DB by ABSOLUTE path is the only exception. **Verification + reporting only — no product-code changes and no DB writes.** If a check fails, report it — do NOT fix it. Do NOT use Monitor. Do NOT edit PROJECT_STATUS directly.
>
> **MANDATORY — Rule 20 self-check banner.** Your deposit MUST contain, verbatim, `## Rule 20 — QA Self-Check Results` and a line `**PASSED — SELF-CHECK PASSED**`. End with a self-grep confirming the banner.
>
> **Evidence-source rule.** Every SQL row states which DB it ran against (canonical = `sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" "<query>"`). Deposit **RAW command output, never a summary of it.**
>
> **Scope:**
> - `knowledge/qa/gate-1-route-disposition-qa-2026-07-22.md`
>
> Verification table, one row per claim, DB-source column (HALT on any FAIL):
> 1. **All fifteen dispositions applied.** `SELECT id, entry_id, status, route FROM lesson_proposals WHERE id BETWEEN 172 AND 186 ORDER BY id` — raw output. Assert against the disposition table: `codify` on the fourteen, `reference` on 183. Any mismatch → FAIL.
> 2. **The fourteen codify proposals are STILL `status='proposed'`** (Gate-2-bound). Any at a non-`proposed` status → FAIL.
> 3. **The one terminal status landed.** 183 shows `status='reference'` AND `status_updated_by='ceo'` AND non-NULL `status_updated_at`. A route without the status change (or vice versa) → FAIL.
> 4. **Status distribution is exactly the target** (resume-invariant primary): `proposed 14`, `reference 7`, `implemented 119`, `superseded 28`, `rejected 15`, `stale 3`, total **186**. Any other value → FAIL. Reconcile with the A0 before-snapshot in Step 1's deposit: fresh run showed `proposed 15 / reference 6` (movement −1/+1); a resume showed `14 / 7` (B2 legitimately N/A — not a failure). Before-snapshot missing entirely → halt (unverifiable).
> 5. **Blast radius.** Total proposals still 186; route-NOT-NULL rose by ≤15 from the Step-1 before-count (→56); `status='reference'` rose by ≤1 (→7). Report actuals.
> 6. **No proposal outside 172-186 changed.** `SELECT COUNT(*) FROM lesson_proposals WHERE route IS NOT NULL AND id < 172` equals the Step-1 A0 before-total (**41**); `SELECT COUNT(*) FROM lesson_proposals WHERE status='reference' AND id < 172` equals **6** (the pre-existing 140/141/146/161/164/169). Either differing → FAIL (unscoped write).
> 7. **`PLANNER_TEMPLATE.md` UNCHANGED by this gate.** ⚠️ `lessons-forge` is a submodule; the template is tracked by the ROOT repo and does NOT exist in your worktree — a plain `git diff` passes VACUOUSLY (**this is proposal 184, which this plan routes**). Run `git -C /Users/marklehn/Developer/GitHub diff --exit-code -- PLANNER_TEMPLATE.md` and show the exit code (0 = pass; any diff = FAIL). Codification is Gate 2.
> 8. **`src/` untouched and suite green.** `git -C /Users/marklehn/Developer/GitHub/lessons-forge status --porcelain -- src/` empty, and `python3 -m pytest src/ -q` passes. Compute the baseline from `--collect-only` and reconcile against the most recent prior QA in `knowledge/qa/` (2026-07-22 cycle QA recorded 55 — reconciliation only). Raw tail shown.
> 9. **`get_unclassified_entries(conn)` still returns `[]`.** `reference` is non-stale, so 183 keeps its entry classified. Any non-empty result → FAIL.
>
> If any row fails, report and halt.
>
> **Deposit:** `knowledge/qa/gate-1-route-disposition-qa-2026-07-22.md` — verification table with DB-source column, raw query output, the Rule 20 banner + PASSED line, Output Receipt. Canonical Python file-write — no heredoc. Commit it. In `### Ledger Updates` include `#### Project Status` (one milestone paragraph: Gate 1 complete for cycle 2026-07-22 — 14 codify / 1 reference / 0 backlog; the fourteen codify are Gate-2-bound and remain `proposed`; 183 terminal at `reference`; Gate 2 owes the execute-before-deposit cluster [172/173/178/179], the halted-triage pair [174/175], the #26 extension [178], the path-role split [184], and the conformance pass [185]) and `#### Prompt Feedback`.
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/gate-1-route-disposition-qa-2026-07-22.md`
>
> **Do NOT move this plan to `Done/`.** The close path is owned by Bellows on continue-verdict consumption — never by the agent (a Mode-A `unauthorized_done_move` violation force-recovers the file and FAILs this step's gates).
