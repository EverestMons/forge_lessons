# Lessons Forge — Gate 1 Route Disposition (cycle 2026-07-16)
**Date:** 2026-07-16 | **Tier:** Small | **Dispatch Mode:** bellows | **Test Scope:** targeted | **Execution:** Step 1 (DEV) → Step 2 (QA) | **qa_steps:** 2 | **pause_for_verdict:** always

## CEO Context

Gate 1 for the 3 proposals from cycle 2026-07-16 (plan 205). **CEO dispositions are final and embedded below: 2 codify, 1 reference, 0 backlog.**

**Disposition table (authoritative for both steps):**

| Proposal | Entry | Category | Route |
|---|---|---|---|
| 146 | 138 | structural | **reference** |
| 147 | 139 | governance_rule | **codify** |
| 148 | 140 | governance_rule | **codify** |

**Why 146 → reference (not codify, not backlog).** Entry 138's suggested fix — detect the session-limit message shape and pause-and-hold/park instead of surfacing a gate failure — **already shipped**. Planner-verified on disk 2026-07-16: `_check_session_limit` (`bellows/runner.py:74`), `_parse_session_reset` (`bellows/runner.py:36`), park machinery (`record_park`, `parked_steps`) in `bellows.py`, plan 185 commit `38c1670` (2026-07-14). This matches the plan-133 precedent, which routed entries 132/133 to `reference` precisely because their fixes had already shipped. The known residual — Bash-using DEV/QA steps still `gate_fail` on a cap rather than parking — is **a deliberate design trade-off, not an oversight**: exec-197 made `has_mutating_tool_use` block a park specifically to avoid stranding uncommitted work. It is already tracked in the shop baton, so routing 146 to `backlog` would duplicate a live thread.

**Why 147 and 148 → codify (the advisory's subsumption flags are FALSE POSITIVES — verified, do not re-litigate).** The plan-154 advisory flagged **the same two proposals (127/128) against both** entries 139 and 140, purely on shared `planner-discipline` tag equality. Planner read both: **127** is "any gate-enforced QA action must have a MANDATORY callout at the TOP of the QA step"; **128** is "DEV self-verify and Planner review must each run the full pytest suite". Neither has anything to do with disk-verifying filesystem claims (139) or `qa_steps` header semantics (140). **Neither proposal is subsumed.** Codify both.

**CEO decisions recorded here for the record — NO ACTION in this plan:**
- **Proposals 98/121/130 stay `stale`.** Plan 204's audit recommendation, CEO-accepted 2026-07-16: their underlying rules are already codified via the 06-03/06-07 ratifications, and their reclassified twins (122/123/131) were all correctly rejected — restoring them would manufacture proposals for rules that already exist. **Do not touch them in this plan.**
- **Plan 154's advisory: RETIRE.** CEO decision 2026-07-16, on evidence that it is not merely noisy but **anti-correlated with relevance** (see below). **Out of scope here** — a separate plan follows. Do NOT modify `detect_recently_implemented_overlaps` or `generate_lessons_report` in this plan.

**Evidence behind the retire decision (context only, no action here):** first and only production run — 353 overlaps DB-wide; 14 advisory lines across 3 proposals (~4.7 each); **4 of 4 hits examined were false positives, 0 true positives**; and it MISSES proposal 139 (entry 131, `planner-discipline`, `implemented` 2026-07-07, well inside the 45-day window) — the nearest genuinely adjacent implemented proposal to entry 140's `qa_steps` lesson. Its motivating case (proposal 131) is now known to be a downstream symptom of the bug plan 204 fixed.

**Gate 1 changes ROUTES ONLY.** Proposal `status` values are NOT changed here — status transitions happen at Gate 2 (plan-133 precedent). All three proposals stay `proposed`.

**Deposit-once discipline:** deposited exactly once. If a second copy appears, that is a claim-dedup bug — do not double-claim.

## How to Run This Plan

**Bootstrap prompt:**
```
Read the plan at lessons-forge/knowledge/decisions/executable-lessons-forge-gate-1-2026-07-16.md. Execute Step 1 ONLY. After completing Step 1, STOP and wait for my confirmation. Do NOT proceed to Step 2.
```

---
---

## STEP 1 — DEV

---

> **FIRST — before any reads or work: post a short visible chat message (1-2 sentences) confirming you are starting this plan and your immediate next action.** Do NOT rename the plan file.
>
> You are the Lessons Forge Developer. Read `/Users/marklehn/Developer/GitHub/forge/agents/FORGE_DEVELOPER.md` first (cross-repo; skip with a note if absent). All commands run from `/Users/marklehn/Developer/GitHub/lessons-forge`. **All canonical-DB access uses the ABSOLUTE path** `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db` — the worktree has no DB copy and that is never a reason to substitute or skip a verification.
>
> **This step changes the canonical DB only. It MUST NOT touch `src/`** — no code changes, no advisory removal (that is a separate plan).
>
> **Scope:**
> - `knowledge/development/gate-1-route-disposition-2026-07-16.md`
>
> **Task A — record the routes.** Use the shipped module API `set_proposal_route(conn, proposal_id, route)` from `src.lessons_forge` — **not hand-written SQL**. Apply exactly the CEO disposition table:
> - `146` → `reference`
> - `147` → `codify`
> - `148` → `codify`
>
> Commit the DB work is not applicable (the DB is untracked); commit the dev-log deposit.
>
> **Task B — verify, and prove you changed nothing else.** Capture the proposal status distribution BEFORE and AFTER and assert they are **identical** — Gate 1 assigns routes only; if any `status` changed, you have a bug: halt and report. Then read back `SELECT id, entry_id, status, route FROM lesson_proposals WHERE id IN (146,147,148)` and confirm: routes are `reference`/`codify`/`codify` respectively, and all three are still `status='proposed'`.
>
> **Task C — confirm the blast radius is exactly 3 rows.** Assert that no proposal OUTSIDE {146,147,148} had its route changed: capture `SELECT COUNT(*) FROM lesson_proposals WHERE route IS NOT NULL` before and after (expect before=0, after=3 — no cycle has ever assigned a route on these; the 2026-07-06 Gate 1 routes were on earlier proposals, so verify rather than assume, and report the actual numbers). **Do NOT touch proposals 98/121/130** — CEO decision is they stay `stale` untouched; confirm their statuses are unchanged.
>
> **Deposit:** `knowledge/development/gate-1-route-disposition-2026-07-16.md` — the `set_proposal_route` calls made, before/after status distributions **proving they are identical**, the read-back of all three rows, the route-count blast-radius check, confirmation that 98/121/130 are untouched, and an Output Receipt with status. Canonical Python file-write pattern — no heredoc. In `### Ledger Updates` include `#### Prompt Feedback`.
>
> **Deposits:**
> - `lessons-forge/knowledge/development/gate-1-route-disposition-2026-07-16.md`
>
> **STOP. Do NOT proceed to Step 2. Wait for CEO verdict.**

---
---

## STEP 2 — QA

---

> **Before starting, read the Step 1 deposit and confirm Output Receipt status Complete; otherwise halt and report.** Post a short visible chat message confirming you are starting Step 2 (QA).
>
> You are Lessons Forge QA. Read `agents/FORGE_LESSONS_AGENT.md` for domain context (skip with a note if absent). All commands run from `/Users/marklehn/Developer/GitHub/lessons-forge`. **Verification + reporting only — no product-code changes.** If you find a blocker, STOP and report it.
>
> **MANDATORY — Rule 20 self-check banner.** Your deposit MUST contain, verbatim, a section headed exactly `## Rule 20 — QA Self-Check Results` followed (anywhere below it) by a line reading exactly `**PASSED — SELF-CHECK PASSED**`. End with a self-grep confirming the banner is present in your deposited report.
>
> **Evidence-source rule (entries 136/137 are this lesson; entry 139 demands disk-verification).** Every SQL row states which DB it ran against. Canonical reads use `sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" "<query>"`. Worktree DB absence is never a substitution reason. Deposit **RAW command output**, never a summary.
>
> **Scope:**
> - `knowledge/qa/gate-1-route-disposition-qa-2026-07-16.md`
>
> Verification table, one row per claim, each with a DB-source column:
> 1. **Routes recorded exactly per the CEO table** — 146=`reference`, 147=`codify`, 148=`codify`. Raw `SELECT id, entry_id, status, route FROM lesson_proposals WHERE id IN (146,147,148)` output.
> 2. **Gate 1 changed no status** — all three still `proposed`; full status distribution is `implemented 97, proposed 3, reference 2, rejected 15, stale 3, superseded 28` (unchanged from cycle close). **Note the trap:** proposal 146's ROUTE is `reference` while its STATUS stays `proposed` — these are different columns. Do not conflate them; a `status='reference'` on 146 would be a FAIL (that transition is Gate 2's call, not Gate 1's).
> 3. **Blast radius exactly 3** — `SELECT COUNT(*) FROM lesson_proposals WHERE route IS NOT NULL` returns 3; no proposal outside {146,147,148} carries a route.
> 4. **98/121/130 untouched** — all three still `stale`, per the CEO decision. Raw output.
> 5. **The 204 fix still holds (standing regression watch)** — proposal 145 still `implemented`; `stale` still 3; `get_unclassified_entries()` still `[]`.
> 6. **Targeted tests green** — `python3 -m pytest src/ -v -k "route or proposal"` (use `python3 -m pytest`, NOT the `timeout` binary — unavailable on macOS). Full suite is not required for a DB-disposition plan; baseline for reference is 61 passed.
>
> If any row fails, report and halt — do not pass a broken deliverable.
>
> **Deposit:** `knowledge/qa/gate-1-route-disposition-qa-2026-07-16.md` — verification table with DB-source column, raw output, the mandatory Rule 20 banner + PASSED line, and an Output Receipt with status. Canonical Python file-write pattern — no heredoc. Commit it. In `### Ledger Updates` include: `#### Project Status` — one milestone paragraph (Gate 1 2026-07-16 complete: 3 proposals dispositioned — 2 codify, 1 reference; 98/121/130 left stale per CEO; plan-154 advisory retirement queued separately; Gate 2 codification pending); `#### Prompt Feedback` — standard.
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/gate-1-route-disposition-qa-2026-07-16.md`
>
> On full completion, move the plan file to `lessons-forge/knowledge/decisions/Done/` as the absolute last operation.
