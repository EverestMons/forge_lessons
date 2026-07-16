# Lessons Forge — Fix: whitespace-only hash flips silently stale implemented proposals (root cause of the duplicate-proposal loop)
**Date:** 2026-07-16 | **Tier:** High | **Dispatch Mode:** bellows | **Test Scope:** both | **Execution:** Step 1 (DEV) → Step 2 (DEV) → Step 3 (QA) | **qa_steps:** 3 | **pause_for_verdict:** always

## CEO Context

**Discovered by plan 203 Step 1 (halted 2026-07-16 on this finding). Root cause is PROVEN, not hypothesised — this plan fixes it.**

**The bug.** The 2026-07-07 wrap commit `e57a22b` appended three lessons to LESSONS.md as **33 insertions, 0 deletions**. The appended block opens with a `---` separator, and `parse_lessons_md` (`src/lessons_forge.py:30`) assigns those separator lines to the **previous** entry's body. Entry 137's `content_hash` flipped `4ff4c905` → `b9875afa` over **7 bytes of trailing whitespace**. Verified by parsing `git show e57a22b^:LESSONS.md` against current: the bodies are byte-identical once the trailing separator is stripped. **Zero substantive change.**

**The damage.** That whitespace-only flip drove the update path in `ingest_lesson_entries` (`src/lessons_forge.py:131-150`), whose stale-marking is `WHERE entry_id = ? AND status != 'stale'` — it demotes **any** status, including terminal ones. Proposal 145 went **`implemented` → `stale`** at 2026-07-16T13:15:46Z (distribution moved implemented 97→96, stale 3→4). A rule already codified in PLANNER_TEMPLATE silently lost its implemented record and re-entered the classification work list.

**It is systematic.** All 4 `stale` proposals in the corpus are this same artifact — each entry was the LAST entry in LESSONS.md when the prior cycle ran, and each got a trailing separator appended by the next wrap:

| Entry | Staled proposal | Reclassified as | Outcome |
|---|---|---|---|
| 93  | 98  | 122 | rejected |
| 116 | 121 | 123 | rejected |
| 123 | 130 | 131 | rejected |
| 137 | 145 (today) | — | blocked by the 203 halt |

Three of three completed instances ended as a **rejected duplicate proposal** — a 100% waste rate. **Proposal 131 — the motivating case for plan 154's entire dedup-advisory build — is a downstream symptom of this bug.** Plan 154 automated catching the duplicates this bug manufactures instead of stopping their manufacture.

**⚠️ THE LOAD-BEARING CONSTRAINT — READ BEFORE WRITING ANY CODE.** Changing the hash function re-hashes **every** entry. Measured on canonical 2026-07-16 (read-only): **all 83 currently-parsed entries change hash under normalization** (they all carry trailing separators), and a **naive** re-hash would drive the update path over all 83 and stale **79 proposals — 64 of them `implemented`**. That is corpus destruction an order of magnitude worse than the bug being fixed. The backfill in Step 2 MUST update `content_hash` **only**, and MUST NOT touch `lesson_proposals` at all. Step 1's stale-guard is the second, independent line of defence. Do not run any cycle/ingest against canonical until Step 2's backfill has landed.

**Scope note:** LESSONS.md parses to 83 entries while `lesson_entries` holds 140 — expected, not a defect. `parse_lessons_md` stops at `^## Archived`, so archived entries keep their DB rows and are no longer re-parsed. The backfill therefore only re-hashes the 83 parsed entries; the other 57 keep their stored hashes and are never compared again.

**Out of scope (deliberate):** (a) plan 154's advisory heuristic — its first production run measured 353 DB-wide overlaps and degenerates to tag equality (10 hits for entry 138, all `tag overlap: bellows`); CEO decision 2026-07-16 is to note and defer its fate to Gate 1 after this fix, since its value may largely evaporate once the duplicate generator is gone. Do NOT modify `detect_recently_implemented_overlaps`. (b) Restoring proposals 98/121/130 — Step 2 AUDITS and reports them; the CEO decides at Gate 1. Only proposal 145 is restored here, because its `implemented` state is directly evidenced (staled today, at a known timestamp, by a proven-whitespace-only change).

**Deposit-once discipline:** deposited exactly once. If a second copy appears, that is a claim-dedup bug — do not double-claim.

## How to Run This Plan

**Bootstrap prompt:**
```
Read the plan at lessons-forge/knowledge/decisions/executable-lessons-forge-hash-normalization-fix-2026-07-16.md. Execute Step 1 ONLY. After completing Step 1, STOP and wait for my confirmation. Do NOT proceed to Step 2.
```

---
---

## STEP 1 — DEV

---

> **FIRST — before any reads or work: post a short visible chat message (1-2 sentences) confirming you are starting this plan and your immediate next action.** Do NOT rename the plan file.
>
> You are the Lessons Forge Developer. Read `/Users/marklehn/Developer/GitHub/forge/agents/FORGE_DEVELOPER.md` first (cross-repo; skip with a note if absent). All commands run from `/Users/marklehn/Developer/GitHub/lessons-forge`.
>
> **This step changes CODE ONLY. It MUST NOT touch the canonical DB** (`/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db`) — no backfill, no restore, no ingest. That is Step 2. Tests use synthetic in-memory/temp DBs only.
>
> **Scope:**
> - `src/lessons_forge.py`
> - `src/test_lessons_forge.py`
> - `knowledge/development/hash-normalization-fix-step-1-2026-07-16.md`
>
> **Task A — normalize the hash input (the root-cause fix).** In `parse_lessons_md`, replace the `content_hash` computation (currently `hashlib.sha256(raw_content.encode("utf-8"))` at ~line 66) so the hash is taken over a **normalized** form of the body: trailing whitespace and any trailing markdown horizontal-rule separator lines (`^[ \t]*-{3,}[ \t]*$`) stripped, repeatedly, until the body ends in real content. Factor it into a module-level helper (e.g. `_normalize_for_hash(raw_content) -> str`) with a docstring citing this bug.
>
> **CRITICAL — normalization affects the HASH ONLY.** `raw_content` must continue to be **stored verbatim**, unnormalized, in `lesson_entries.raw_content`. The classifier reads `raw_content`; do not let normalization reach it. Assert this in a test.
>
> **Task B — guard the stale path (independent second defence).** In `ingest_lesson_entries`, the update path must **never demote a terminal status**. Add a module-level `_TERMINAL_STATUSES = frozenset(('implemented', 'rejected', 'superseded', 'reference'))` and restrict the stale UPDATE so it only affects non-terminal, non-stale rows (i.e. `proposed` / `ambiguous`). A CEO disposition is not something an ingest may silently undo.
>
> **Do not silently swallow the case either.** When an entry's body genuinely changed AND it carries a terminal-status proposal, collect it rather than ignoring it: add a `terminal_proposals_flagged` key to `ingest_lesson_entries`'s returned dict — a list of `{"entry_id": int, "proposal_id": int, "status": str}` — and surface that same key upward through `run_full_lessons_cycle`'s returned dict so a future cycle can put it in front of Gate 1. Keep the existing return keys unchanged (`inserted`, `updated`, `unchanged`, `stale_proposals_marked`).
>
> **Tests (`src/test_lessons_forge.py`) — synthetic DBs only, never the live DB.** Add:
> 1. **The exact regression:** a body hashed identically with and without a trailing `\n\n---\n\n` separator (this is the 137 case — assert the two hashes are EQUAL).
> 2. A **substantive** body edit still changes the hash (the fix must not blind real edits).
> 3. `raw_content` is stored **verbatim including** its trailing separator (normalization did not leak into storage).
> 4. **Terminal-status guard:** an entry whose body genuinely changes, carrying an `implemented` proposal → proposal stays `implemented`, and it appears in `terminal_proposals_flagged`. Parametrise across all four terminal statuses.
> 5. **Non-terminal still stales:** a genuine body change with a `proposed` proposal → still marked `stale` (existing behaviour preserved).
> 6. **The catastrophic case, asserted directly:** re-ingesting entries whose ONLY delta is a trailing separator marks **zero** proposals stale and reports `updated == 0`.
>
> **Self-verify.** Run the TARGETED tests you added plus the existing `ingest`/`parse` tests (`python3 -m pytest src/test_lessons_forge.py -v -k "hash or ingest or parse or stale or normal"`). Use `python3 -m pytest` — NOT the `timeout` binary, unavailable on macOS. The full suite is Step 3's job, not yours. **Commit** with a descriptive message.
>
> **Deposit:** `knowledge/development/hash-normalization-fix-step-1-2026-07-16.md` — the normalization rule chosen (and why it is safe against real edits), the terminal-status guard, targeted-test output tail, commit hash, and an Output Receipt with status. Canonical Python file-write pattern — no heredoc. In `### Ledger Updates` include `#### Prompt Feedback`.
>
> **Deposits:**
> - `lessons-forge/src/lessons_forge.py`
> - `lessons-forge/src/test_lessons_forge.py`
> - `lessons-forge/knowledge/development/hash-normalization-fix-step-1-2026-07-16.md`
>
> **STOP. Do NOT proceed to Step 2. Wait for CEO verdict.**

---
---

## STEP 2 — DEV (canonical DB backfill + restore + audit)

---

> **Before starting, read the Step 1 deposit and confirm Output Receipt status Complete; otherwise halt and report.** Post a short visible chat message confirming you are starting Step 2.
>
> You are the Lessons Forge Developer. All commands run from `/Users/marklehn/Developer/GitHub/lessons-forge`. **All canonical-DB access uses the ABSOLUTE path** `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db` — the worktree has no DB copy and that is never a reason to substitute or skip a check.
>
> **This step MUTATES the canonical DB. Read the load-bearing constraint in CEO Context before your first write.**
>
> **Scope:**
> - `scripts/backfill_normalized_hashes_2026-07-16.py`
> - `knowledge/development/hash-normalization-backfill-2026-07-16.md`
>
> **Task A — back up first.** Copy the canonical DB to `/tmp/lessons-forge-backup-2026-07-16.db` and record the byte size + `SELECT COUNT(*)` from both tables. If any later task misfires, this is the restore point. Report the backup path in the receipt.
>
> **Task B — the backfill (hash column ONLY).** Write `scripts/backfill_normalized_hashes_2026-07-16.py` (create `scripts/` if absent) that, against canonical: for each row in `lesson_entries` matched to a currently-parsed LESSONS.md entry by `source_heading`, recomputes the hash using the NEW normalized function from Step 1 and issues `UPDATE lesson_entries SET content_hash = ? WHERE id = ?` — **nothing else**.
>
> **Hard constraints, all of which you must assert in the script itself:**
> - It issues **NO** statement against `lesson_proposals`. Not one. Verify by capturing the full proposal status distribution before and after and asserting equality.
> - It does **NOT** call `ingest_lesson_entries` or `run_full_lessons_cycle` — those carry the stale path. Direct SQL only.
> - It does **NOT** modify `raw_content`.
> - It is **idempotent**: a second run must report 0 changes.
> - Expected scale: ~83 rows updated (all currently-parsed entries). The 57 archived entries are not parsed and must be left untouched.
>
> **Task C — restore proposal 145.** Set proposal 145 `status='implemented'`, `status_updated_by='ceo-plan-203-recovery'`, `status_updated_at=<now>`. Its pre-corruption `status_updated_at` is unrecoverable (overwritten at 2026-07-16T13:15:46Z) — note that in the dev-log rather than inventing one. Verify entry 137's proposal set afterwards is exactly `{145: implemented}`.
>
> **Task D — prove the loop is closed.** With the backfill applied, run `get_unclassified_entries(conn)` against canonical and confirm entry **137 is NO LONGER in the work list** (its proposal is implemented again, not stale). Then re-run `run_full_lessons_cycle(conn)` against canonical and confirm it now reports `updated == 0`, `stale_proposals_marked == 0`, and a work list of exactly **[138, 139, 140]** — the three genuine new entries, with entry 137 gone. **Commit the DB-mutating work is not applicable (the DB is untracked); commit the script + dev-log.**
>
> **Task E — audit 98/121/130 (REPORT ONLY — restore NOTHING).** For each, record: entry id, current status, `status_updated_at`, the reclassified twin (122/123/131 respectively) and that twin's disposition. State plainly that their pre-stale status is **unrecoverable from the DB** (overwritten), and note any external evidence (e.g. whether the rule is present in PLANNER_TEMPLATE). Recommend — do not perform — a disposition for CEO Gate 1. **Do NOT change their status.**
>
> **Deposit:** `knowledge/development/hash-normalization-backfill-2026-07-16.md` — backup path + sizes, rows re-hashed, the before/after proposal-status distributions **proving they are identical** (this is the critical evidence), the idempotency re-run result, proposal 145 restoration, Task D work-list proof, the Task E audit table, and an Output Receipt. Canonical Python file-write pattern — no heredoc. In `### Ledger Updates` include `#### Prompt Feedback`.
>
> **Deposits:**
> - `lessons-forge/scripts/backfill_normalized_hashes_2026-07-16.py`
> - `lessons-forge/knowledge/development/hash-normalization-backfill-2026-07-16.md`
>
> **STOP. Do NOT proceed to Step 3. Wait for CEO verdict.**

---
---

## STEP 3 — QA

---

> **Before starting, read the Step 1 and Step 2 deposits and confirm both Output Receipt statuses are Complete; otherwise halt and report.** Post a short visible chat message confirming you are starting Step 3 (QA).
>
> You are Lessons Forge QA. Read `agents/FORGE_LESSONS_AGENT.md` for domain context (skip with a note if absent). All commands run from `/Users/marklehn/Developer/GitHub/lessons-forge`. **Verification + reporting only — no product-code changes.** If you find a blocker, STOP and report it.
>
> **MANDATORY — Rule 20 self-check banner.** Your QA deposit MUST contain, verbatim, a section headed exactly `## Rule 20 — QA Self-Check Results` followed (anywhere below it) by a line reading exactly `**PASSED — SELF-CHECK PASSED**`. End with a self-grep confirming the banner is present in your deposited report.
>
> **Evidence-source rule (entries 136/137 are literally this lesson — do not reproduce the miss).** Every SQL/PRAGMA row states which DB it ran against. Canonical reads use `sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" "<query>"`. Worktree DB absence is never a substitution reason. Deposit **RAW command output**, never a summary of it.
>
> **Scope:**
> - `knowledge/qa/hash-normalization-fix-qa-2026-07-16.md`
>
> Verification table, one row per claim, each with a DB-source column:
> 1. **Full suite** — `python3 -m pytest src/ -v` (`python3 -m pytest`, NOT `timeout`) to an explicit pass/fail with the tail shown. Baseline was **52 passed** pre-plan; confirm 0 regressions and report the new count.
> 2. **The regression is actually fixed** — a trailing-separator-only delta produces an identical hash (Step 1 test 1 exists and passes).
> 3. **Corpus integrity held (THE critical row)** — proposal status distribution on canonical is **implemented 97, superseded 28, rejected 15, stale 3, reference 2**. This is the pre-corruption baseline restored: implemented back to 97 (145 restored) and stale back down to 3. Any other distribution is a FAIL — in particular, if `implemented` is anywhere near 33 (i.e. 64 demoted), the backfill breached its constraint and you must halt loudly.
> 4. **Backfill touched only hashes** — read `scripts/backfill_normalized_hashes_2026-07-16.py` and confirm by inspection it issues no `lesson_proposals` statement; corroborate with the Step 2 before/after distributions.
> 5. **`raw_content` unnormalized in storage** — entry 137's stored `raw_content` still ends with its trailing `---` separator (normalization did not leak into storage).
> 6. **The loop is closed** — `get_unclassified_entries(conn)` on canonical returns exactly **[138, 139, 140]**; entry 137 is absent.
> 7. **Terminal-status guard** — confirm tests cover all four terminal statuses and that `terminal_proposals_flagged` surfaces through `run_full_lessons_cycle`.
> 8. **No schema drift** — `.schema lesson_entries` / `.schema lesson_proposals` on canonical vs `src/db.py` DDL. This plan changes NO schema; the `route` column and the `reference` CHECK value are expected (plans 128/135). Any delta is a FAIL.
>
> If any row fails, report and halt — do not pass a broken deliverable.
>
> **Deposit:** `knowledge/qa/hash-normalization-fix-qa-2026-07-16.md` — the verification table with its DB-source column, the raw full-suite tail, the mandatory Rule 20 banner + PASSED line, and an Output Receipt with status. Canonical Python file-write pattern — no heredoc. Commit it. In `### Ledger Updates` include: `#### Project Status` — one milestone paragraph (root cause of the duplicate-proposal loop fixed: whitespace-only hash flips no longer stale proposals, terminal statuses guarded, ~83 hashes backfilled, proposal 145 restored, corpus integrity verified; cycle 203 to be re-dispatched; 98/121/130 audit pending CEO Gate 1); `#### Prompt Feedback` — standard.
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/hash-normalization-fix-qa-2026-07-16.md`
>
> On full completion, move the plan file to `lessons-forge/knowledge/decisions/Done/` as the absolute last operation.
