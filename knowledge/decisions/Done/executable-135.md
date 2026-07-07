# Lessons Forge — Reference terminal status: migration + apply to proposals 140/141
**Date:** 2026-07-07 | **Tier:** Small | **Dispatch Mode:** bellows | **Test Scope:** targeted | **Execution:** Step 1 (DEV) → Step 2 (QA) | **qa_steps:** 2 | **pause_for_verdict:** always

## CEO Context

CEO decision B (2026-07-07): reference-routed proposals get an honest terminal status — `reference` added to the `lesson_proposals.status` CHECK constraint — rather than remaining `proposed` with route as an implicit terminal marker. First reference-routed proposals ever: 140 and 141 (entries 132/133, cycle 2026-07-06; fixes already shipped in plans 62/63). Gate 2 (plan 134) closed with these two deliberately untouched. After this plan, `status='proposed'` again means exactly "awaiting disposition" (expected count 0).

SQLite cannot ALTER a CHECK constraint on an existing table — this is a guarded table-rebuild migration. The route-column migration (guarded, idempotent, runs at connect/init against pre-existing DBs) is the in-repo precedent for migration shape and test coverage; follow its pattern, adapted for rebuild.

**Locked:**
1. New allowed status value: `reference` (terminal). No other status semantics change.
2. Apply `status='reference', status_updated_at='2026-07-07', status_updated_by='ceo'` to proposals 140 and 141 (they carry Gate 1 CEO dispositions).
3. Canonical DB is `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db` — the migration must run against it (guarded), not only fresh test DBs.

---
---

## STEP 1 — DEV

---

> **FIRST — before any reads or work: post a short visible message to chat (1-2 sentences) confirming you are starting this plan and stating your immediate next action.** Do NOT rename the plan file.
>
> You are Forge DEV. Read your specialist file at `lessons-forge/agents/FORGE_LESSONS_AGENT.md` first. All commands run from `/Users/marklehn/Developer/GitHub/lessons-forge`.
>
> **Scope:**
> - `src/` (only files needed for the migration; follow the route-column migration's home)
> - `tests/` (only if needed)
> - `knowledge/development/reference-status-migration-2026-07-07.md`
>
> 1. Locate the existing route-column migration and the `lesson_proposals` schema definition by grep, not recall. Implement a guarded, idempotent table-rebuild migration that adds `reference` to the status CHECK constraint, preserving all rows, indexes, and triggers. The guard must detect whether the rebuild already happened (safe on every connect/init, matching the route migration's guard style).
> 2. Add targeted tests following the route-migration test patterns: idempotence (double-run), pre-existing-DB migration, CHECK accepts `reference`, CHECK still rejects an invalid value, row-count and data preservation across rebuild.
> 3. Run the migration against the canonical DB at `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db` (absolute path — worktree DB absence is never a substitution reason), then apply: `UPDATE lesson_proposals SET status='reference', status_updated_at='2026-07-07', status_updated_by='ceo' WHERE id IN (140,141) AND route='reference';` Confirm exactly 2 rows changed and `SELECT COUNT(*) FROM lesson_proposals WHERE status='proposed'` returns 0.
> 4. Run the full pytest suite to a pass/fail result and read the tail output — never infer green from a collect count.
>
> **Deposit:** `lessons-forge/knowledge/development/reference-status-migration-2026-07-07.md` — migration design (rebuild steps, guard condition), test additions, canonical-DB application evidence (rows changed, proposed count), suite tail, Output Receipt with status. In `### Ledger Updates` include: `#### Project Status` — one paragraph: reference terminal status live, proposals 140/141 applied, proposed backlog at 0; `#### Prompt Feedback` — standard.
>
> **Deposits:**
> - `lessons-forge/knowledge/development/reference-status-migration-2026-07-07.md`
>
> STOP. Do NOT proceed to Step 2.

---
---

## STEP 2 — QA

---

> **FIRST — before any reads or work: post a short visible message to chat (1-2 sentences) confirming you are starting this step and stating your immediate next action.** Do NOT rename the plan file.
>
> You are Forge QA. Read your specialist file at `lessons-forge/agents/FORGE_LESSONS_AGENT.md` first. All commands run from `/Users/marklehn/Developer/GitHub/lessons-forge`.
>
> **Rule 20 self-check is gate-enforced on this step.** Your QA report MUST include the byte-exact banner `Rule 20 — QA Self-Check Results` and a `PASSED — SELF-CHECK PASSED` line; author and run the canonical block per `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md`, reproduce its stdout byte-identically, then self-grep your report for the banner.
>
> **Scope:**
> - `knowledge/qa/reference-status-migration-qa-2026-07-07.md`
>
> **Evidence-source contract (Plan Authoring Checklist #28):** every SQL verification row MUST declare its DB source. Canonical reads: `sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" "<query>"` — resolves from any worktree; worktree DB absence is never a substitution reason. Temp-DB test evidence must be labeled as such.
>
> Verification table, one PASS/FAIL row per claim: (1) canonical DB: proposals 140 and 141 have `status='reference'`, `status_updated_by='ceo'`; (2) canonical DB: `status='proposed'` count is 0; (3) canonical DB: status distribution matches expected (implemented 97, superseded 28, rejected 15, stale 3, reference 2); (4) canonical DB: PRAGMA/schema shows the rebuilt CHECK includes `reference` (Rule 8: live-DB schema verification, not fresh-DB only); (5) temp DB: migration idempotence and data-preservation tests pass in isolation; (6) temp DB: CHECK rejects an invalid status value; (7) full suite green — run to pass/fail, quote the tail. If any row fails, report and halt.
>
> **Deposit:** `lessons-forge/knowledge/qa/reference-status-migration-qa-2026-07-07.md` — verification table with per-row DB-source declarations, suite tail, Rule 20 block stdout, Output Receipt. Commit the QA report and Step 1 deposits if uncommitted. In `### Ledger Updates` include: `#### Project Status` — one paragraph: reference status verified live on canonical DB, cycle 2026-07-06 fully terminal; `#### Prompt Feedback` — standard.
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/reference-status-migration-qa-2026-07-07.md`
>
> On full completion, move the plan file to `lessons-forge/knowledge/decisions/Done/` as the absolute last operation.
