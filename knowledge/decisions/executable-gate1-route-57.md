# Executable: Gate 1 route assignment — proposals 354–410 (23 codify, 23 reject, 6 reference, 3 backlog; 378/389 HELD for the CEO)

**Type:** Executable
**Project:** lessons-forge
**Depends on:** the classified queue from **executable-529/530** (Done 2026-08-25 — ingest + classify; Gate-1 held to a non-author by the 459 law), the Gate-1 decision packet `gate1-packet-2026-08-25.md` at the shop root (**PROVENANCE, not an input any step reads** — the payload is carried inline below), and the clone origin `knowledge/research/draft-gate1-routing-2026-08-11.md` (the proven routing-transaction form: addressing contract, dump-pair recovery instrument, untracked-DB policy).
**Created:** 2026-08-25
**Author:** Planner (Gate-1 non-author session `b52c5d10`, routing delegated by CEO directive "run the gate 1 routing")
**Slug:** `gate1-route-57` (stable across any crash-redo re-deposit — the Rule 20 `plan_slug`)
**dispatch_mode:** bellows
**pause_for_verdict:** always
**Priority:** 10
**cycle_tier:** T1
**qa_steps:** [2]
**Test Scope:** targeted (the 326/342 convention) — this plan changes **no code**. Its writes are DB rows and markdown. The repo's suite is the single module `src/test_lessons_forge.py`, where targeted = full; **Step 2 runs it whole and Step 1 runs none**, because a DEV test run would measure nothing this step touched.

⚠️ **ID NOTE — the deposit filename carries NO plan id and the id is decided AT CLAIM.** `id_sequence` read **536** at authoring (2026-08-25, `bellows/lifecycle.db`) — a prediction, never an identity; every watcher and verdict keys on the SLUG `gate1-route-57` (the 512/513 collision is the measured reason).

---

## Why this exists — the routing IS the deliverable; the decisions are already made

Gate 1 for the 57-proposal queue (the un-run 08-19 gate, ids 354–378, plus the 08-25 cycle, ids 379–410) was decided on 2026-08-25 by the non-author session under the CEO's delegation, with two evidence passes (doctrine coverage against PT v4.89 / DC v2.15 / PST v1.2; shipped-status at source) recorded in the packet. This plan writes those dispositions to the canonical corpus DB in one transaction and proves the write touched exactly the intended rows. **Two proposals — 378 and 389 — are deliberately NOT routed:** they form one linked design fork (the per-project knowledge-home consolidation, touching CEO decision 353) surfaced to the CEO in the packet. **They stay `proposed` and this plan must not touch them.**

**The encoding, from MEASURED corpus vocabulary (2026-08-25, all 414 proposals):** the live combinations are `accepted|codify`, `rejected|NULL` (the majority rejection form, 13 rows), `reference|reference`, `reference|backlog`. **The four payloads follow those forms exactly:**

- **23 items → `status='accepted'`, `route='codify'`** — the Gate-2-consumable state (queue grows 5 → 28).
- **23 items → `status='rejected'`, `route` LEFT NULL** — already covered by live doctrine; the packet cites each covering rule.
- **6 items → `status='reference'`, `route='reference'`** — fix shipped and verified at source (the 146 precedent).
- **3 items → `status='reference'`, `route='backlog'`** — fix verified incomplete; residual tracked, not doctrine.
- **All 55: `status_updated_by='planner'`, `status_updated_at=<transaction time>`** — the router of record is the delegated non-author session, NOT `'ceo'`: the CEO delegated the act, not each disposition, and the verdict-reason discipline forbids stamping an authority the record cannot support. `'planner'` is verified legal against the live CHECK constraint (`status_updated_by IS NULL OR IN ('planner','ceo','auto')`, read from `sqlite_master` 2026-08-25).
- **ZERO `target_artifact` writes** — deliberate; the 08-11 origin's TARGET-1 statement and its ordering trap are ABSENT by construction. Gate 2 assigns homes for NULL targets.

**THE FOUR PAYLOADS (byte-authoritative over any prose):**

- **CODIFY-23:** 354, 355, 361, 364, 365, 366, 368, 370, 372, 373, 379, 383, 384, 385, 386, 387, 390, 393, 395, 401, 406, 407, 409
- **REJECT-23:** 356, 357, 358, 359, 362, 363, 367, 374, 375, 376, 377, 380, 381, 382, 392, 394, 396, 397, 398, 399, 400, 404, 410
- **REFREF-6:** 388, 391, 402, 403, 405, 408
- **REFBACK-3:** 360, 369, 371
- **HELD-2 (never written):** 378, 389

**Arithmetic anchor: 23 + 23 + 6 + 3 = 55, and 55 + 2 held = 57 = the full contiguous id range 354–410.** ⚠️ The five id lists are **disjoint, and their union is exactly that range** — verified by an executed partition check at authoring (2026-08-25, printed `PARTITION OK`). ⚠️⚠️ **The four WRITTEN payloads are NOT exhaustive over the range — that is the point.** A guard phrased "every proposed row in 354–410 moved" would be WRONG here: exactly two must remain.

⚠️⚠️ **WHAT THIS PLAN GROWS, AND IT IS A KNOWN UNFIXED HAZARD — stated because the plan is the thing that grows it.** Verified at source 2026-08-25: `src/lessons_forge.py:31` reads `_TERMINAL_STATUSES = frozenset(('implemented', 'rejected', 'superseded', 'reference'))`. **`accepted` is NOT in that set; `rejected` and `reference` are.** So:

- the **23** rows moving to `accepted|codify` become **stale-able by a future ingest**, joining the 5 already there — **the exposed population goes 5 → 28**;
- the 23 rejected and 9 reference rows are **protected** (terminal).

The 204 normalization fix killed the append-staling generator, so the residual exposure is genuine edits to routed entries only — but the procedural guard stands, and it is URGENT here because **the cycle-nudge has already fired (an ingest is due): do NOT run a lessons-forge ingest between this routing and the Gate-2 codification without first checking the `accepted` population. A Gate-2 plan that finds fewer than 28 `accepted|codify` rows should HALT rather than proceed on the remainder.**

**What this plan does NOT do:**
- **No FORWARD emission, in either step** — carried from the origin: wrap work, not this plan's.
- **No doctrine edit** — Gate-2 plans own those. An agent editing `DRAFTING_CYCLE.md`, `PLANNER_TEMPLATE.md`, `PANEL_SEAT_TEMPLATE.md` or any shop-root doc has left this plan → **HALT.**
- **No LESSONS.md touch** — routing writes only the proposals table.
- **No write to rows 378 or 389** — the held fork is the CEO's; QA row 3 proves their bytes did not move.

---

## How to Run This Plan

**Bootstrap prompt:**
```
Read the plan at knowledge/decisions/in-progress-executable-<id>.md (the daemon renames the deposited placeholder on claim). Execute Step 1 ONLY. After completing Step 1, STOP and wait for my confirmation.
```

---
---

## STEP 1 — DEV (the routing transaction)

> **FIRST — resolve the tree, then post a short visible chat message (1–2 sentences) confirming you are starting this plan and your immediate next action.** Do NOT rename this plan file. Read your specialist file.
> ⚠️ **`ROOT=$(git rev-parse --show-toplevel)`; assert `pwd -P` equals `$ROOT` (`cd "$ROOT"` and re-assert if not); print `$ROOT`.** Every worktree-relative path below is safe only under that assertion, and every step of this plan runs in a worktree.
>
> ⚠️⚠️ **ADDRESSING CONTRACT — carried verbatim in force from the clone origin, re-confirmed live 2026-08-25 (plans 528–530 ran in `.bellows-worktrees/`).** Your cwd is the **WORKTREE**. All file deposits are **worktree-relative** so they enter `files_changed` and merge. **The DB is UNTRACKED and therefore DOES NOT EXIST in the worktree:** every `sqlite3` command addresses the **CANONICAL absolute path** `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db` — never a relative `lessons-forge.db`, which opens a fresh empty file in the worktree and makes **every count read 0**. A deposit written to the canonical tree instead of the worktree passes `deposit_exists` while dodging `files_changed`. **Do not mix the two directions up.** The table is `lesson_proposals`.
>
> **Task A0 — PIN THE PRE-STATE; the write is licensed by it and ONLY it.**
> 1. `SELECT COUNT(*), MIN(id), MAX(id) FROM lesson_proposals WHERE status='proposed';` — **must print exactly `57|354|410`.** Any other triple → **HALT, and REPORT THE CAUSE CORRECTLY, because two very different states both land here:**
>    - **Count is 2 and the ids are exactly 378 and 389** — ⚠️ **check it, do not eyeball it:** `SELECT status, COALESCE(route,'-'), COUNT(*) FROM lesson_proposals WHERE id BETWEEN 354 AND 410 GROUP BY 1,2;` must return exactly `accepted|codify|23`, `rejected|-|23`, `reference|reference|6`, `reference|backlog|3`, `proposed|-|2` → **this is an ALREADY-LANDED REDO**, not a concurrent writer. A prior dispatch committed the transaction and died before its dev log. **Report it as such, do NOT re-run the transaction** (every statement would match 0 and roll back anyway), and hand the state to the CEO.
>    - **Anything else** → a concurrent cycle or session touched the batch. **Do not improvise a reconciliation.**
> 2. `SELECT id, status, COALESCE(route,'-'), COALESCE(target_artifact,'-') FROM lesson_proposals WHERE id IN (378,389) ORDER BY id;` — **must print exactly `378|proposed|-|PLANNER_TEMPLATE.md` and `389|proposed|-|-`. Any other rows → HALT** — the held fork's pre-state is part of the license.
>
> **Task A1 — DERIVE THE PLAN ID AND BUILD THE PRE-IMAGE. Execute A1.1–A1.3 in order.** *(A1 does not commit — the origin's CEO-cut single-commit shape, Task D, is carried.)*
>
> **A1.1 — Derive `<plan-id>`; Task D's commit message needs it.** Print your full plan path, then extract from the BASENAME with **`re.findall(r'^(?:in-progress-)?executable-(\d+)\.md(?:\.pristine)?$', basename)` and assert exactly one match.** ⚠️ **The anchors are load-bearing in BOTH directions here:** the right-tolerance covers the `.pristine` serve path (plan 341's measured defect), and the FULL anchoring is what stops the deposit slug itself from matching — this plan's deposited name `executable-gate1-route-57.md` contains the digits `57`, and an unanchored `executable-(\d+)\.md` would extract them as a phantom plan id. **Zero matches or more than one → HALT** and report the basename verbatim.
>
> **A1.2 — Know why the SELECT has six columns, before you run it** (inherited, closed defects of the origin's origin — carried): **`target_artifact`** so the diff can see any target write (this plan makes none — the diff proving ZERO target changes is evidence, not decoration); **`status_updated_at`** so the dump can RESTORE, not merely diff — verified 2026-08-25: **all 57 queued rows hold NULL** there, the transaction stamps 55 of them, and a rollback driven by a dump blind to those NULLs leaves rows stamped by a transaction that was undone.
>
> **A1.3 — Dump the FULL disposition table to the pre-image.** `SELECT id, status, COALESCE(route,'-'), COALESCE(status_updated_by,'-'), COALESCE(status_updated_at,'-'), COALESCE(target_artifact,'-') FROM lesson_proposals ORDER BY id;` redirected to `knowledge/development/gate1-pre-dump-2026-08-25.txt` — **the redirect target is worktree-relative (the deposit direction); the SELECT reads the canonical absolute path.** This file is both the recovery instrument and the untouched-population proof's left side.
>
> **Task B — ONE transaction, FOUR UPDATEs, in-transaction verification before COMMIT.** Canonical Python (`sqlite3` module, `BEGIN IMMEDIATE`, `PRAGMA busy_timeout=5000` first), **NO heredoc**. The script opens the CANONICAL absolute DB path. ⚠️⚠️ **`:TS` IS ONE VALUE, COMPUTED ONCE BEFORE `BEGIN IMMEDIATE` AND BOUND TO ALL FOUR STATEMENTS** — QA row 1(d) asserts all 55 rows share a single `status_updated_at`; separately-computed timestamps fail a correct run. **Bind it as a parameter; print it; record it verbatim in the dev log.**
>
> 1. `UPDATE lesson_proposals SET status='accepted', route='codify', status_updated_by='planner', status_updated_at=:TS WHERE id IN (354,355,361,364,365,366,368,370,372,373,379,383,384,385,386,387,390,393,395,401,406,407,409) AND status='proposed';` — **rowcount must be exactly 23, or ROLLBACK + HALT.** ⚠️ **The list is inline and literal, not a placeholder to transcribe.**
> 2. `UPDATE lesson_proposals SET status='rejected', status_updated_by='planner', status_updated_at=:TS WHERE id IN (356,357,358,359,362,363,367,374,375,376,377,380,381,382,392,394,396,397,398,399,400,404,410) AND status='proposed';` — **rowcount must be exactly 23, or ROLLBACK + HALT.** ⚠️ **This statement deliberately does NOT set `route`** — `rejected|NULL` is the majority corpus form for rejections; writing a route here would invent a pairing.
> 3. `UPDATE lesson_proposals SET status='reference', route='reference', status_updated_by='planner', status_updated_at=:TS WHERE id IN (388,391,402,403,405,408) AND status='proposed';` — **rowcount must be exactly 6, or ROLLBACK + HALT.**
> 4. `UPDATE lesson_proposals SET status='reference', route='backlog', status_updated_by='planner', status_updated_at=:TS WHERE id IN (360,369,371) AND status='proposed';` — **rowcount must be exactly 3, or ROLLBACK + HALT.**
>
> ⚠️ **There is NO ordering interaction among the four statements** — the id sets are disjoint by the executed partition check, and every statement carries `AND status='proposed'`. That guard is load-bearing twice over: it makes the transaction idempotence-safe (a redo after a crash between COMMIT and log re-matches 0 rows and HALTs loudly), **and** it is the A0-to-transaction window guard — a writer slipping between A0's pin and `BEGIN IMMEDIATE` diverges the rowcounts and the transaction rolls back. **The pin is advisory; the rowcounts are the gate.**
>
> - **In-transaction posts, before COMMIT:** `proposed` count within 354–410 = **2** and `GROUP_CONCAT(id)` over them = `378,389` (⚠️ the SET, not the count — a count of 2 is satisfied by the wrong two); the four (status,route) counts within 354–410 read `accepted|codify|23`, `rejected|NULL|23`, `reference|reference|6`, `reference|backlog|3`. **Any mismatch → ROLLBACK + HALT with the numbers.**
> - ⚠️⚠️ **WHAT THE ROWCOUNT GATE CANNOT SEE (carried from the origin):** a **within-payload swap** — the wrong 23 is still 23. A duplicate or out-of-range id does not survive (the count drops); the only undetectable error is a swap between two payload lists, and **QA row 1's SET comparisons with printed symmetric differences are the sole mechanical guard.** Residual, stated and not engineered away: a swap authored into this plan's payload is invisible to this plan; the countermeasures are the executed authoring-time partition check and the packet's per-id basis table, which shows every row's destination by name.
> - ⚠️⚠️ **THE FOUR PAYLOADS ARE IMMUTABLE INPUTS. A rowcount mismatch is NEVER resolved by editing a list.** The only response to any mismatch is ROLLBACK + HALT with the numbers. The dev log pastes the script so the verdict reader can diff its id lists against the payload above.
> - **Lock behaviour:** journal mode is **WAL** (verified live 2026-08-25). A persistent `OperationalError: database is locked` → **HALT with the error verbatim** — an exception before COMMIT rolls back and leaves the DB untouched.
>
> **Task C — post-image + the untouched-population proof (a count is not a value guard):**
> 1. Dump the same full table to `knowledge/development/gate1-post-dump-2026-08-25.txt` — **same SELECT, same SIX columns, same ORDER BY.**
> 2. `diff` pre vs post. **Expected: exactly the 55 rows for the four payload id sets changing as specified, as PAIRED old/new lines, and ZERO lines for any other id — including 378 and 389.** Count changed *rows*, not changed lines (the paired form doubles them). Paste the **RAW** diff in the dev log. **A single foreign line — a 378 or 389 line especially — is the wrong-write proof → HALT and report; do NOT attempt a compensating write.**
> 3. ⚠️ **Confirm ZERO `target_artifact` changes** — any row whose sixth column differs between the dumps is a wrong write.
>
> **Scope:**
> - `knowledge/development/gate1-routing-dev-log-2026-08-25.md`
> - `knowledge/development/gate1-pre-dump-2026-08-25.txt`
> - `knowledge/development/gate1-post-dump-2026-08-25.txt`
>
> ⚠️⚠️ **`lessons-forge.db` is deliberately ABSENT from Scope and from the commit.** The DB is UNTRACKED by shop policy (verified `git ls-files --error-unmatch` errors, 2026-08-25); `git add`ing it would re-track it against that policy. **The DB mutation's evidence IS the dump pair: the dumps commit, the DB never does.**
>
> **Task D — DEPOSIT AND COMMIT. Execute D1–D4 in order.**
>
> **D1 — Deposit the dev log** at `knowledge/development/gate1-routing-dev-log-2026-08-25.md`, carrying: the resolved **`$ROOT`** and the derived **`<plan-id>`**; both dumps' paths and line counts; the **transaction script text** verbatim; **all four rowcounts** and the in-transaction post numbers including the printed `378,389` set; **the transaction timestamp value verbatim** (QA row 1(d)'s comparator); the **RAW** pre/post diff. D1 records A0's pre-image state only; D3 reports D2's sha after D2 has made it.
>
> **D2 — Commit ALL THREE Scope files in ONE commit**, pathspec on the COMMIT naming exactly them. Message: `[<plan-id>] Step 1 — gate1 route assignment 354-410 (23 codify, 23 reject, 6 ref, 3 backlog; 378/389 held)`. **Commit only — NO push.**
>
> **D3 — Assert the commit.** `git show --name-only --format= HEAD` prints **exactly the three Scope files and nothing else.** ⚠️ There is no already-committed branch here: in this single-commit shape only D2 commits Scope files, and a death after the transaction's COMMIT re-enters through A0's redo branch, which HALTs before reaching D3.
>
> **D4 — Ledger.** `#### Prompt Feedback` in `### Ledger Updates` **if there is any**. ⚠️⚠️ **NO `#### Forward Register` subsection, in either step.**
>
> **STOP. Do NOT proceed to Step 2. Wait for the verdict.**

**Deposits:**
- `lessons-forge/knowledge/development/gate1-routing-dev-log-2026-08-25.md`
- `lessons-forge/knowledge/development/gate1-pre-dump-2026-08-25.txt`
- `lessons-forge/knowledge/development/gate1-post-dump-2026-08-25.txt`

---
---

## STEP 2 — QA

> **FIRST — resolve the tree:** `ROOT=$(git rev-parse --show-toplevel)`; assert `pwd -P` equals `$ROOT`; print it.
>
> **Task Q0 — RE-PIN. ⚠️ The DB is untracked, so the pin is CONTENT, not git.**
> 1. `git -C "$ROOT" log -1 --oneline --` the three evidence files — the newest commit touching any of them must be Step 1's; a foreign commit → **HALT.**
> 2. `sqlite3 -readonly /Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db "SELECT COUNT(*) FROM lesson_proposals WHERE status='proposed' AND id BETWEEN 354 AND 410;"` — **must print 2.** *(A `-readonly` open against a WAL database is precedent-verified.)* ⚠️ **The range scope is deliberate:** an unscoped count conflates a verdict-window write to THIS batch (a true halt) with a concurrent cycle's brand-new proposals at ids > 410 (not this plan's concern — row 1's set checks still guard the batch). Any number other than 2 → **HALT.**
>
> **MANDATORY — Rule 20 self-check (canonical block, the exact template, NOT a paraphrase)** from `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md` (ABSOLUTE path — the governance root is not a worktree). **All FOUR placeholders:** `plan_slug`: `gate1-route-57`; `qa_report_path`: `<your-tree-abs>/knowledge/qa/gate1-route-57-qa-2026-08-25.md`; `evidence_dir` derived from `pwd`, NOT hardcoded; `required_evidence_files`: `[pytest_full.txt, routing-verification.txt, diff-audit.txt]`. **Deposit all three BEFORE running the block — it `sys.exit(1)`s on any missing OR ZERO-BYTE file.** Include the block's literal stdout: the banner `Rule 20 — QA Self-Check Results` and the `PASSED — SELF-CHECK PASSED` line, both byte-exact (em-dash U+2014).
>
> ⚠️ **REPORT STRUCTURE — immediately after the verification table write exactly `## Evidence and Narrative`**, keeping the Rule 20 stdout, the Output Receipt and `### Ledger Updates` at `##`-level. The gate scopes its search to a heading containing "verification".
>
> **Evidence rule:** RAW command output, never a summary. ⚠️ When writing about a failed check, backtick any ❌ marker inside quoted literals (the rule_22(c) report discipline).
>
> **Verification table, one row per claim (HALT on any FAIL):**
>
> **1. THE WRITE LANDED, read from the DB and not from the dev log.**
> - **(a)** the `accepted|codify` id SET within 354–410: **compare against CODIFY-23 and print the SYMMETRIC DIFFERENCE, asserted empty** — never a count; a count of 23 is satisfied by the wrong 23.
> - **(b)** the `rejected` id SET within 354–410 (⚠️ match `route IS NULL` too): symmetric difference against REJECT-23, asserted empty and printed.
> - **(c)** the `reference|reference` and `reference|backlog` id SETs: symmetric differences against REFREF-6 and REFBACK-3, asserted empty and printed. ⚠️ **Item (a)'s symmetric difference doubles as the verdict-window guard against a concurrent INGEST** — `accepted` is not terminal; staled rows drop out of the set and the difference names them.
> - **(d)** every one of the 55 carries `status_updated_by='planner'` and `status_updated_at` equal to the transaction timestamp the dev log recorded verbatim. **A differing timestamp on any row means a second writer touched the batch inside the verdict window.** → `routing-verification.txt`
>
> **2. THE HELD ROWS DID NOT MOVE.** Rows 378 and 389: all six dump columns byte-identical between pre-dump and live DB — `proposed`, route NULL, `status_updated_by` NULL, `status_updated_at` NULL, targets `PLANNER_TEMPLATE.md` / NULL respectively. ⚠️ **This is the fork's integrity proof; a stamp on either row means the plan decided what it promised to surface.** → `routing-verification.txt`
>
> **3. UNTOUCHED POPULATION.** Re-run the `diff` of the committed pre/post dumps in this session. **Every changed row's id is within the four payload sets; zero foreign ids; zero `target_artifact` changes.** Report the changed-row count (expect 55) and the changed-*line* count separately. → `diff-audit.txt`
>
> **4. THE DUMPS ARE THE COMMITTED ONES.** `git show HEAD:<path>` for both dump files matches the working-tree copy byte-for-byte. → `diff-audit.txt`
>
> **5. FULL SUITE.** Run `src/test_lessons_forge.py` whole; record the raw summary line **VERBATIM**. *(Isolation verified at source at authoring: the suite connects to `":memory:"` and tempfiles — it never opens the canonical corpus DB, so this run cannot stale what Step 1 wrote.)* **Measured at authoring 2026-08-25: `63 passed in 0.11s`** — a measurement with a timestamp, not a bar. This plan changes no code; **a HIGHER count is not a failure** — report the delta and name it. **Only a FAILURE or a count BELOW 63 is a HALT.** → `pytest_full.txt`
>
> **6. THE DB WAS NOT COMMITTED.** `git -C "$ROOT" log --name-only` over both step commits shows **no `lessons-forge.db`**, and `git ls-files --error-unmatch lessons-forge.db` still errors. → `routing-verification.txt`
>
> **7. NOTHING ELSE MOVED.** `git status --porcelain` at `$ROOT` is EMPTY, and assert by name that `DRAFTING_CYCLE.md`, `PLANNER_TEMPLATE.md`, `PANEL_SEAT_TEMPLATE.md`, `LESSONS.md` and `knowledge/FORWARD.md` are absent from both step commits.
>
> **Then `## Evidence and Narrative`, then the Output Receipt.**
>
> ⚠️ **`### Ledger Updates`** — author via `Write`/`Edit` (the daemon parses assistant text and Write/Edit content, NOT Bash), EXACTLY ONCE, complete, never re-edited; `##`-level after `## Evidence and Narrative`; blank line after the last subsection. ⚠️⚠️ **OMIT the `#### Forward Register` subsection ENTIRELY. Do not write "None".**
>
> **FINAL ACTION — COMMIT YOUR DEPOSITS**, pathspec on the COMMIT naming exactly the Scope files, then assert `git show --name-only --format= HEAD` prints exactly them. **Commit only — NO push.**
>
> **Scope:**
> - `knowledge/qa/gate1-route-57-qa-2026-08-25.md`
> - `knowledge/qa/evidence/gate1-route-57/pytest_full.txt`
> - `knowledge/qa/evidence/gate1-route-57/routing-verification.txt`
> - `knowledge/qa/evidence/gate1-route-57/diff-audit.txt`

**Deposits:**
- `lessons-forge/knowledge/qa/gate1-route-57-qa-2026-08-25.md`
- `lessons-forge/knowledge/qa/evidence/gate1-route-57/pytest_full.txt`
- `lessons-forge/knowledge/qa/evidence/gate1-route-57/routing-verification.txt`
- `lessons-forge/knowledge/qa/evidence/gate1-route-57/diff-audit.txt`

---

## Drafting Cycle

**Tier:** T1 — computed, not judged. **T-2 fires** (production-data mutation: 55 rows of the canonical corpus). **T-5 does NOT fire** — the recovery instrument is the committed pre/post dump pair, not a `.db` backup; the origin and its origin (326) both ran this operation at T1 and closed. **T-8 does NOT fire** — twelve closed Gate-1 route-disposition plans, newest the 08-11 form (dispatched and closed as the 274–314 routing), same project, same table, same transaction shape. **T-6 does not fire** — no doctrine edit.

**Clone-diff against the origin (`draft-gate1-routing-2026-08-11.md`), three passes (facts / artefacts / structure):**
- **Facts (5 checked, 5 re-verified live 2026-08-25):** WAL mode ✓; `_TERMINAL_STATUSES` at `src/lessons_forge.py:31`, `accepted` absent ✓ (the hazard population is 5 → 28 here, not 42 → 74); DB untracked ✓; all queued `status_updated_at` NULL ✓ (57 rows, not 41); suite baseline **63 passed** (origin said 55 — re-measured, not inherited).
- **Artefacts (origin's named mechanisms, each accounted for):** addressing contract CARRIED; single `:TS` binding CARRIED (four statements now); `AND status='proposed'` double-duty guard CARRIED on ALL statements (the origin's statement-3 exemption existed only for its target write, which this plan does not have); rowcount-gate-then-ROLLBACK CARRIED; immutable-payload law CARRIED; six-column dump pair CARRIED; single-commit Task D (the origin's CEO-cut shape) CARRIED with its redo branch; symmetric-difference QA CARRIED and EXTENDED to four sets; fullmatch-anchored plan-id regex ADAPTED — ⚠️ the origin's anchorless form is UNSAFE for this plan because the slug `gate1-route-57` itself matches `executable-(\d+)\.md` unanchored; the anchored form fails closed on the slug-named serve path.
- **Structure (what composes differently):** 3 statements → 4, all disjoint → NO ordering interaction (the origin's statement-3 ordering trap is absent by construction); the written payloads are deliberately NON-exhaustive over the range — every "all rows moved" guard from the origin is re-phrased as "exactly the 55, and the held two unmoved" (A0's redo branch, the in-transaction posts, QA rows 1–3); TARGET-1 machinery DELETED whole (statement, dump rationale half, QA row 2 replaced by the held-rows proof).

**Walks:** 2 — five lenses each, strictly sequential, each lens acting on the draft as folded by the previous.
- Weak spots:          w1 2 folded — 2/2 pre-existing, 1 HIGH. ⚠️ **The plan-id regex inherited anchorless from the origin would extract `57` from this plan's OWN deposit filename** `executable-gate1-route-57.md` — a phantom plan id on the pristine serve path; replaced with the fullmatch-anchored form and a HALT-on-zero. Also: QA row 1(b) gained the explicit `route IS NULL` match — a rejected row with a stray route would otherwise pass the set check.
- Destruction:         w1 1 folded — 1/1 pre-existing. A0's redo branch initially checked only the count `2`; a wrong-two state (e.g. 378 routed, 354 left) satisfied it — the branch now requires the full five-way GROUP BY signature AND the held-row check is separate (A0.2), so both must agree before the redo reading is reported.
- Vulnerabilities:     w1 1 folded — 1/1 pre-existing. The in-transaction post printed the held count; a count of 2 is satisfied by the wrong two — now prints and asserts the `GROUP_CONCAT` id set `378,389`.
- Integration-record:  w1 1 folded — 1/1 pre-existing. `status_updated_by='planner'` was asserted legal from memory; now verified against the live CHECK constraint read from `sqlite_master` and recorded in the header block. Also recorded: the rule_22(c) backtick-the-marker report discipline in QA's evidence rule.
- ACID:                w1 dry — die before Task B → A0 re-pins clean; die after COMMIT before D2 → A0's redo branch detects the landed five-way signature and escalates; die between D2 and Step 2 → Q0.1 re-pins Step 1's commit. The four-statement disjointness removes the origin's only intra-transaction ordering concern.
- **Walk 1 total: 5 findings, 5 folded — 5/5 pre-existing (from the clone adaptation surface), 1 HIGH.**
- Weak spots:          w2 dry.
- Destruction:         w2 dry — the A0 redo re-read: both branches (clean 57-pin, landed signature) re-derived against the folded text; no third state reachable without HALT.
- Vulnerabilities:     w2 1 folded — **fold-introduced, instruction-class:** D3 carried the origin's already-committed-is-success clause, which is UNREACHABLE in this single-commit shape (only D2 commits Scope files; a post-COMMIT death re-enters through A0's redo branch and HALTs) — an agent reading it could mis-classify a genuinely foreign commit as a benign redo. Replaced with the no-such-branch statement.
- Integration-record:  w2 1 folded — record-class: the clone-diff's artefact pass had not named the origin's statement-3 guard exemption as accounted-for; one sentence added above so a later reader does not re-import the exemption.
- ACID:                w2 dry.
- **Walk 2 total: 2 findings, 2 folded — 1 instruction-class (the unreachable D3 branch), 1 record-class, both fold/clone-introduced, 0 HIGH. Three lenses dry. ⚠️ The instruction-class finding re-opens the walk — the bar is NOT met at walk 2.**
- Walk 3 — mechanical arm EXECUTED (not read): the four payload declarations AND the four SQL IN-lists extracted from this file and diffed against the authoring-time verified partition — byte-identical, held ids absent from every IN-list, exactly 2 H2 STEP headers (`WALK3-MECH OK`, 2026-08-25). Read arm: 1 folded — **instruction-class:** Q0.2's unscoped proposed-count conflated a verdict-window write to THIS batch with a concurrent cycle's new proposals at ids > 410, failing a correct state; range-scoped to `BETWEEN 354 AND 410`. Other four lenses dry on the read.
- **Walk 3 total: 1 finding, 1 folded — instruction-class → the bar is NOT met at walk 3; walk 4 owed.**
- Walk 4 — the confirming pass over walks 2–3's folds: the D3 replacement re-derived against A0's redo branch (consistent — HALT precedes D3 on every post-COMMIT death); Q0.2's scope re-derived against QA row 1's set checks (the batch guard survives the scoping); a leftover sweep for un-adapted origin fragments (`already-committed`, `must print 0`, `A1.4`, orphan `41`/`274` literals) found only legitimate citations; A0.1's `2|378|389` triple re-derived (for exactly two rows MIN/MAX identifies the set, and the GROUP BY signature is the non-eyeball check). **All five lenses dry on the instruction stream; 0 findings.**

**Closing:** ✅ **BAR MET at walk 4 — a dry confirming pass, all five lenses, after two consecutive instruction-class walks.** The §2.7 closing re-read ran after this record was written: it re-derived the walk arithmetic (w1 5/5 pre-existing; w2 2 folded, 1 instruction; w3 1 instruction + executed mechanical arm; w4 0) and found no instruction-stream defect; the one candidate it raised — whether QA row 5's higher-is-not-a-failure clause could mask a concurrent forge code change — is answered by row 7 (nothing else moved) and Scope (no code files), and is recorded here rather than folded.

**Conformance (§5):** `plan_lint` run at the DEPOSIT path resolution (`lessons-forge/knowledge/decisions/`) under a `lintmirror-` name (the admission-predicate-verified non-claimable form), exit code recorded pre-deposit. Any warning beyond the known-benign test-mention class is unexplained → do not deposit.

**Fold-and-deposit exactly once.**
