# Executable: Gate 1 route assignment — proposals 274–314 (32 accepted→codify, 9 reference→backlog, 1 target correction)

**Type:** Executable
**Project:** lessons-forge
**Depends on:** **executable-326** (lessons-forge, Done 2026-08-08 — ⚠️ **the CLONE ORIGIN and newest same-class**; the routing transaction, the addressing contract, the dump-pair recovery instrument and the untracked-DB policy all come from it), the classified batch from **executable-339/340** (Done — 41 proposals, 39 `governance_rule` + 2 `instrumentation`), **executable-341** (Done 2026-08-11 — swept the four void rows out of `knowledge/FORWARD.md` so this batch's wrap emissions land on a clean register), and the CEO routing session of 2026-08-10 (packet `gate1-packet-2026-08-10.md` at the shop root — **PROVENANCE, not an input any step reads**). DRAFTING_CYCLE at **v2.0**.
**Created:** 2026-08-11
**Author:** Planner
**Slug:** `gate1-routing-2026-08-11` (stable across any crash-redo re-deposit — the Rule 20 `plan_slug`)
**dispatch_mode:** bellows
**pause_for_verdict:** always
**Priority:** 10
**cycle_tier:** T1
**qa_steps:** [2]
**Test Scope:** targeted (the 326/311 convention) — this plan changes **no code**. Its writes are DB rows and markdown. The repo's suite is the single module `src/test_lessons_forge.py`, where targeted = full; **Step 2 runs it whole and Step 1 runs none**, because a DEV test run would measure nothing this step touched.

⚠️ **ID NOTE — the deposit filename is decided AT DEPOSIT.** `id_sequence` read **342** at authoring (2026-08-11, `bellows/lifecycle.db`). **Re-read it at deposit and re-token every filename site.** ⚠️ **No deposit filename in this plan carries the plan id** — every one is date-slugged (`…-2026-08-11`), which is deliberate: plan 340's deposit filenames went off-by-one against its step numbers because the id and the filename were coupled.

---

## Why this exists — the routing IS the deliverable; the decisions are already made

Gate 1 for the 339/340 batch: the CEO routed all 41 proposals on 2026-08-10, deciding entry 293 first. This plan writes those dispositions to the canonical corpus DB in one transaction and proves the write touched exactly the intended rows. **The decision payload is carried INLINE below; the packet is provenance, not an input any step reads** — a plan self-contained beats a cross-tree read.

**The encoding, from MEASURED corpus vocabulary (2026-08-11, all 314 proposals):** the live combinations are `accepted|codify` (42), `reference|backlog` (9), `reference|reference` (5). ⚠️⚠️ **`accepted|backlog` has ZERO occurrences and is NOT used here** — an earlier draft of the Gate-1 packet proposed `accepted` for all 41, which would have invented that pairing. **326 set the standing form and it is followed exactly:**

- **32 items → `status='accepted'`, `route='codify'`** — the Gate-2-consumable state.
- **9 items → `status='reference'`, `route='backlog'`** — recorded-not-codified, route naming where it went. This is the form the previous cluster A received and still carries (FORWARD 43).
- **All 41: `status_updated_by='ceo'`, `status_updated_at=<transaction time>`** — the dispositions are the CEO's; this plan is the pen, not the decider.
- **One additional field write:** proposal **301**'s `target_artifact`, `DRAFTING_CYCLE.md` → `funnel-mechanization-v0-2026-08-08.md`.

**THE THREE PAYLOADS (byte-authoritative over any prose):**

- **CODIFY-32:** 274, 276, 277, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 293, 295, 296, 297, 298, 300, 303, 304, 305, 306, 307, 309, 310, 311, 312, 313, 314
- **BACKLOG-9:** 275, 278, 291, 292, 294, 299, 301, 302, 308
- **TARGET-1:** 301 only — `target_artifact` → `funnel-mechanization-v0-2026-08-08.md`

**Arithmetic anchor: 32 + 9 = 41 = the full contiguous id range 274–314.** ⚠️ The two id lists are **disjoint and exhaustive over that range** — verified by partition check at authoring. **301 appears in BACKLOG-9 *and* in TARGET-1; that is correct and is the only intended overlap.**

**Why 301 is in both:** it is entry 293, flag (G)'s meta-rule. The CEO routed it `backlog` and reversed the classifier's `target_artifact`, because the scout had recorded "routing principle, no file target" and the classifier overrode that with `DRAFTING_CYCLE.md`. 293 is a rule for the routing gate, not for a drafting author, so its home is the funnel. **This is the only field change in the batch outside `route`/`status`.**

⚠️⚠️ **WHAT THIS PLAN GROWS, AND IT IS A KNOWN UNFIXED HAZARD — stated because the plan is the thing that grows it.** Verified at source 2026-08-11: `src/lessons_forge.py:31` reads `_TERMINAL_STATUSES = frozenset(('implemented', 'rejected', 'superseded', 'reference'))`. **`accepted` is NOT in that set; `reference` is.** So:

- the **32** rows this plan moves to `accepted|codify` become **stale-able by a future ingest**, joining the **42** already there — **the exposed population goes 42 → 74**;
- the **9** rows moving to `reference|backlog` are **protected**, because `reference` is terminal.

**This is the hazard `knowledge/FORWARD.md` row 12 records** (row 11 was its duplicate, withdrawn by plan 341). **Nothing here fixes it — the guard is procedural and it is the same one 339/340 used: do not run a lessons-forge ingest between this routing and the Gate-2 codification without first checking the `accepted` population.** ⚠️ **A Gate-2 plan that finds fewer than 74 `accepted|codify` rows should HALT rather than proceed on the remainder.**

**What this plan does NOT do:**
- **No FORWARD emission, in either step.** ⚠️ This is carried from 326, which states it: the Rule-46 bellows halves ride the session wrap. The five new rows this batch owes (291/294/299, 274's bellows half, 301's Gate-1 intake check) and the five queue calls on FORWARD 45/46/50/52/54 are **wrap work, not this plan's.** Emitting here would schedule a daemon append to `knowledge/FORWARD.md` inside the plan that follows plan 341's sweep of that same file.
- **No doctrine edit** — Gate-2 plans own those. An agent editing `DRAFTING_CYCLE.md`, `PLANNER_TEMPLATE.md` or the funnel doc has left this plan → **HALT.**
- **No LESSONS.md touch** — routing writes only the proposals table.

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
> ⚠️⚠️ **ADDRESSING CONTRACT — carried verbatim in force from `executable-326`, and re-confirmed live on 2026-08-11 (plan 341 ran at `lessons-forge/.bellows-worktrees/341`).** Your cwd is the **WORKTREE**. All file deposits are **worktree-relative** so they enter `files_changed` and merge. **The DB is UNTRACKED and therefore DOES NOT EXIST in the worktree:** every `sqlite3` command addresses the **CANONICAL absolute path** `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db` — never a relative `lessons-forge.db`, which opens a fresh empty file in the worktree and makes **every count read 0**. A deposit written to the canonical tree instead of the worktree passes `deposit_exists` while dodging `files_changed` — the 317-measured masked state. **Do not mix the two directions up.** The table is `lesson_proposals`.
>
> **Task A0 — PIN THE PRE-STATE; the write is licensed by it and ONLY it.**
> 1. `SELECT COUNT(*) FROM lesson_proposals WHERE status='proposed';` — **must print exactly 41.** Any other number → **HALT, and REPORT THE CAUSE CORRECTLY, because two very different states both land here:**
>    - **Count is 0, and the 41 rows already carry their target dispositions** — ⚠️ **check it, do not eyeball it:** `SELECT status, COALESCE(route,'-'), COUNT(*) FROM lesson_proposals WHERE id BETWEEN 274 AND 314 GROUP BY 1,2;` must return exactly `accepted|codify|32` and `reference|backlog|9`, and `SELECT target_artifact FROM lesson_proposals WHERE id=301;` must return the funnel path → **this is an ALREADY-LANDED REDO**, not a concurrent writer. A prior dispatch committed the transaction and died before its dev log. **Report it as such, do NOT re-run the transaction** (statement 1 would match 0 and roll back anyway), and hand the state to the CEO.
>    - **Anything else** → a concurrent cycle or session touched the batch. **Do not improvise a reconciliation.**
>
>    ⚠️ **The distinction matters because the two demand opposite responses, and a single message blaming a concurrent writer would send the reader hunting for one that does not exist.**
>
> 2. `SELECT COUNT(*), MIN(id), MAX(id) FROM lesson_proposals WHERE status='proposed';` — **must print exactly `41|274|314`.** With ids unique (PK), 41 rows spanning 274–314 inclusive **IS** the contiguity proof, order-independent. Any other triple → **HALT.** Print the `GROUP_CONCAT` id list too, as display for the dev log, **never as the gate.**
> 3. `SELECT id, status, COALESCE(route,'-'), target_artifact FROM lesson_proposals WHERE id=301;` — **must print exactly `301|proposed|-|DRAFTING_CYCLE.md`. Any other row → HALT**, because TARGET-1's guard keys on that value.
>
> **Task A1 — BUILD THE PRE-IMAGE. Execute A1.1–A1.3 in order.** *(A1 no longer commits: the CEO cut the separate pre-image commit on 2026-08-11 — see the note below.)*
>
> ⚠️ **A1 has no forward references: every value it needs is established by an earlier numbered sub-step.**
>
> **A1.1 — Derive `<plan-id>`; Task D's commit message needs it.** Print your full plan path, then extract with **`re.findall(r'executable-(\d+)\.md', basename)` and assert exactly one match.** ⚠️⚠️ **This is plan 341's measured defect, fixed here before it fires:** 341 anchored the same regex with `$`, which matches `in-progress-executable-341.md` but returns **NO MATCH** on `executable-341.md.pristine` — the path Bellows actually serves as the plan document at a resumed or later step. **Anchorless on the right, tolerant of any prefix.** Zero or more than one → **HALT.**
>
> **A1.2 — Know why the SELECT has six columns, before you run it.** ⚠️ **Two are absent from 326's dump, each for a different reason:**
> - **`target_artifact`** — without it the pre/post diff **cannot see TARGET-1 at all**, and TARGET-1 is a third of what this plan does.
> - **`status_updated_at`** — ⚠️ **without it the dump can DIFF but not RESTORE.** Measured 2026-08-11: all 41 rows currently hold **NULL** (the other 273 have it set). The transaction writes a timestamp to all 41, so a rollback driven by a dump blind to those NULLs leaves 41 rows stamped by a transaction that was undone. **The dump is this plan's only recovery instrument for an untracked DB; one that cannot reproduce the pre-state is a diff tool wearing its name.** Inherited incompleteness from the clone origin, closed here.
>
> **A1.3 — Dump the FULL disposition table to the pre-image.** `SELECT id, status, COALESCE(route,'-'), COALESCE(status_updated_by,'-'), COALESCE(status_updated_at,'-'), COALESCE(target_artifact,'-') FROM lesson_proposals ORDER BY id;` redirected to `knowledge/development/gate1-pre-dump-2026-08-11.txt` — **the redirect target is worktree-relative, the deposit direction; the SELECT reads the canonical absolute path.** This file is both the recovery instrument and the untouched-population proof's left side.
>
> ⚠️⚠️ **DO NOT RE-ADD A SEPARATE PRE-IMAGE COMMIT. Built at walk 1, CUT by CEO decision 2026-08-11.** A clone that restores it is re-adding machinery this plan paid to remove. **A1 does not commit; Task D commits all three Scope files once.** The measurement behind the cut, and what it knowingly gives up, are in the Cycle Log's clone-diff record — ⚠️ **read them before restoring it, not after.**
>
> **Task B — ONE transaction, THREE UPDATEs, in-transaction verification before COMMIT.** Canonical Python (`sqlite3` module, `BEGIN IMMEDIATE`), **NO heredoc**. The script opens the CANONICAL absolute DB path.
>
> 1. `UPDATE lesson_proposals SET status='accepted', route='codify', status_updated_by='ceo', status_updated_at=:TS WHERE id IN (274,276,277,279,280,281,282,283,284,285,286,287,288,289,290,293,295,296,297,298,300,303,304,305,306,307,309,310,311,312,313,314) AND status='proposed';` — **rowcount must be exactly 32, or ROLLBACK + HALT.** ⚠️ **The list is inline and literal, not a placeholder to transcribe** — a `<CODIFY-32 verbatim>` token is one more hand-copy between the payload and the script, and the payload is the thing that must not drift.
> 2. `UPDATE lesson_proposals SET status='reference', route='backlog', status_updated_by='ceo', status_updated_at=:TS WHERE id IN (275,278,291,292,294,299,301,302,308) AND status='proposed';` — **rowcount must be exactly 9, or ROLLBACK + HALT.**
>
> ⚠️⚠️ **`:TS` IS ONE VALUE, COMPUTED ONCE BEFORE `BEGIN IMMEDIATE` AND BOUND TO BOTH STATEMENTS.** Do not call `datetime.now()` inside each statement. **QA item 1(d) asserts all 41 rows share a single `status_updated_at`; two separately-computed timestamps differ by microseconds and would fail that item on a perfectly correct run** — batch entry 289's class (*a check that fails a correct run is a check an agent will loosen*), sitting in the very batch this plan routes. **Bind it as a parameter; print it; record it verbatim in the dev log.**
> 3. `UPDATE lesson_proposals SET target_artifact='funnel-mechanization-v0-2026-08-08.md' WHERE id=301 AND target_artifact='DRAFTING_CYCLE.md';` — **rowcount must be exactly 1, or ROLLBACK + HALT.**
>    ⚠️⚠️ **STATEMENT 3 MUST NOT CARRY `AND status='proposed'`, and the reason is an ordering interaction:** statement 2 has already moved 301 to `reference`, so a `status='proposed'` guard here matches **zero rows on a correct run** and rolls the whole transaction back. **Its idempotence guard is the value being changed** — `target_artifact='DRAFTING_CYCLE.md'` — which is the right guard anyway: it re-matches 0 on a redo and HALTs loudly rather than silently rewriting.
>
> - **In-transaction posts, before COMMIT:** `proposed` count now **0**; `accepted`+`codify` within 274–314 = **32**; `reference`+`backlog` within 274–314 = **9**; row 301's `target_artifact` = `funnel-mechanization-v0-2026-08-08.md`. **Any mismatch → ROLLBACK + HALT with the numbers.** ⚠️ **A count is normally not a value guard, and here it is only sufficient because each UPDATE's own `WHERE id IN (…)` already pins the set** — the count confirms the pinned set landed, it does not identify it. **QA item 1 compares SETS, and that is where the identification actually happens.**
> - **Lock behaviour, stated:** journal mode is **WAL** (verified live 2026-08-11). The script sets `PRAGMA busy_timeout=5000` before `BEGIN IMMEDIATE`. A persistent `OperationalError: database is locked` → **HALT with the error verbatim** — an exception before COMMIT rolls back and leaves the DB untouched, so a lock failure is a clean retry-later state, never a half-write.
> - ⚠️ **The `AND status='proposed'` guard on statements 1 and 2 is load-bearing twice over:** it makes the transaction idempotence-safe (a redo after a crash between COMMIT and log re-matches 0 rows and HALTs loudly instead of double-stamping timestamps), **and** it is the A0-to-transaction window guard — if a writer slips between A0's pin and `BEGIN IMMEDIATE`, the rowcounts diverge from 32/9 and the transaction rolls back. **The pin is advisory; the rowcounts are the gate.**
> - ⚠️⚠️ **BUT THE ROWCOUNTS DO NOT COVER THE WHOLE WINDOW, and walk 1's framing overstated them.** The pre-dump is taken and committed *before* `BEGIN IMMEDIATE`, so a concurrent writer in between could alter a field the rowcount guard cannot see — a `target_artifact` on some other row, a `route` on an already-terminal row — leaving the committed pre-image no longer the true pre-state. **What actually covers that window is Task C's foreign-line check**, which compares the two dumps and HALTs on any changed row outside 274–314. **The rowcounts guard the STATUS transition; the diff guards everything else.** Neither alone is the window guard.
> - **RECORD THE TRANSACTION TIMESTAMP VALUE VERBATIM in the dev log** — it is QA item 1(d)'s comparator, and a window test without its recorded reference is unrunnable.
> - ⚠️⚠️ **WHAT THE ROWCOUNT GATE CANNOT SEE, stated because it bounds the whole transaction's assurance.** A rowcount of 32 proves *thirty-two proposed rows moved*; it does **not** prove *which*. A list that is the wrong 32 but still 32 — an id swapped between CODIFY-32 and BACKLOG-9 — produces rowcounts 32 and 9, leaves `proposed` at 0, and **passes every in-transaction gate.** A duplicate or an out-of-range id does NOT survive (the count drops and the transaction rolls back), so the only undetectable error is a **within-range swap**.
> **QA item 1's SET comparison is the sole mechanical guard against it, and it must therefore compare SETS and print the symmetric difference on failure — never compare counts.** ⚠️ **Residual, stated and not engineered away: a swap authored into this plan's payload is invisible to this plan**, because the script and QA both read their reference from it. The countermeasures are the authoring-time partition check (run 2026-08-11: disjoint, exhaustive over 274–314, sizes 32/9, no duplicates) and the human-readable diff of Task C, which shows every row's destination by name.
> - ⚠️⚠️ **THE THREE PAYLOADS ARE IMMUTABLE INPUTS. A rowcount mismatch is NEVER resolved by editing a list** — not by dropping an id to make 32 match, not by adding one. **The only response to any mismatch is ROLLBACK + HALT with the numbers.** The script embeds the lists verbatim from this plan, and the dev log pastes the script so the verdict reader can diff them against the payload above.
>
> **Task C — post-image + the untouched-population proof (a count is not a value guard):**
> 1. Dump the same full table to `knowledge/development/gate1-post-dump-2026-08-11.txt` — **same SELECT, same SIX columns, same ORDER BY.** ⚠️ A post-dump with a different column list makes every diff line spurious.
> 2. `diff` pre vs post. **Expected: exactly the 41 rows for ids 274–314 changing as specified, as PAIRED old/new lines (~82 changed lines plus markers in unified form), and ZERO lines for any other id.** ⚠️ **"41 lines" would misread the paired form as a failure** — count changed *rows*, not changed lines. Paste the **RAW** diff in the dev log. **A single foreign line is the wrong-write proof → HALT and report; do NOT attempt a compensating write.**
> 3. ⚠️ **Confirm 301's line shows BOTH changes** — status/route *and* `target_artifact`. A diff showing only the status change means statement 3 silently matched nothing.
>
> **Scope:**
> - `knowledge/development/gate1-routing-dev-log-2026-08-11.md`
> - `knowledge/development/gate1-pre-dump-2026-08-11.txt`
> - `knowledge/development/gate1-post-dump-2026-08-11.txt`
>
> ⚠️⚠️ **`lessons-forge.db` is deliberately ABSENT from Scope and from the commit.** The DB is UNTRACKED by shop policy (plan 30, commit `dabb301` un-tracked it); `git add`ing it would re-track it against that policy. **The DB mutation's evidence IS the dump pair: the dumps commit, the DB never does.**
>
> **Task D — DEPOSIT AND COMMIT. Execute D1–D4 in order.**
>
> **D1 — Deposit the dev log** at `knowledge/development/gate1-routing-dev-log-2026-08-11.md`, carrying:
> - the resolved **`$ROOT`** and the derived **`<plan-id>`**;
> - both dumps' paths and line counts;
> - the **transaction script text** verbatim, so the verdict reader can diff its id lists against this plan's payload;
> - **all three rowcounts** and the in-transaction post numbers;
> - **the transaction timestamp value verbatim** — QA item 1(d)'s comparator;
> - the **RAW** pre/post diff.
>
> **D2 — Commit ALL THREE Scope files in ONE commit**, pathspec on the COMMIT naming exactly them. Message: `[<plan-id>] Step 1 — gate1 route assignment 274-314 (32 codify, 9 backlog, 1 target)`. **Commit only — NO push.**
>
> **D3 — Assert the commit.** `git show --name-only --format= HEAD` prints **exactly the three Scope files and nothing else.** ⚠️ **One commit, one assertion** — the two-sha union, the `<sha>^..HEAD` caret warning and the three-path caveat all belonged to the split and went with it.
>
> **D4 — Ledger.** `#### Prompt Feedback` in `### Ledger Updates` **if there is any** (carried from 326, which mandates it and which this clone had dropped). ⚠️⚠️ **NO `#### Forward Register` subsection, in either step** — see Scope.
>
> **STOP. Do NOT proceed to Step 2. Wait for CEO verdict.**

**Deposits:**
- `lessons-forge/knowledge/development/gate1-routing-dev-log-2026-08-11.md`
- `lessons-forge/knowledge/development/gate1-pre-dump-2026-08-11.txt`
- `lessons-forge/knowledge/development/gate1-post-dump-2026-08-11.txt`

---
---

## STEP 2 — QA

> **FIRST — resolve the tree:** `ROOT=$(git rev-parse --show-toplevel)`; assert `pwd -P` equals `$ROOT`; print it. QA rows 6 and 7 address `$ROOT` and it must be established before they run.
>
> **Task Q0 — RE-PIN. ⚠️ The DB is untracked, so the pin is CONTENT, not git.**
> 1. `git -C "$ROOT" log -1 --oneline --` the three evidence files — the newest commit touching any of them must be Step 1's; a foreign commit → **HALT.**
> 2. `sqlite3 -readonly /Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db "SELECT COUNT(*) FROM lesson_proposals WHERE status='proposed';"` — **must print 0.** *(A `-readonly` open against a WAL database is precedent-verified: 326's QA used exactly this and closed.)* A nonzero here means a verdict-window write re-opened the batch → **HALT.**
>
> **MANDATORY — Rule 20 self-check (canonical block, the exact template, NOT a paraphrase)** from `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md` (ABSOLUTE path — the governance root is not a worktree). **All FOUR placeholders:** `plan_slug`: `gate1-routing-2026-08-11`; `qa_report_path`: `<your-tree-abs>/knowledge/qa/gate1-routing-qa-2026-08-11.md`; `evidence_dir` derived from `pwd`, NOT hardcoded; `required_evidence_files`: `[suite.txt, routing-verification.txt, diff-audit.txt]`. **Deposit all three BEFORE running the block — it `sys.exit(1)`s on any missing OR ZERO-BYTE file.** Include the block's literal stdout: the banner `Rule 20 — QA Self-Check Results` and the `PASSED — SELF-CHECK PASSED` line, both byte-exact (em-dash U+2014).
>
> ⚠️ **REPORT STRUCTURE — immediately after the verification table write exactly `## Evidence and Narrative`**, keeping the Rule 20 stdout, the Output Receipt and `### Ledger Updates` at `##`-level. The gate scopes its search to a heading containing "verification"; a differently-named section is invisible to it.
>
> **Evidence rule:** RAW command output, never a summary.
>
> **Verification table, one row per claim (HALT on any FAIL):**
>
> **1. THE WRITE LANDED, read from the DB and not from the dev log.**
> - **(a)** `accepted`+`codify` within 274–314: **compare the id SET against CODIFY-32 and print the SYMMETRIC DIFFERENCE.** ⚠️ **Assert the symmetric difference is empty — do NOT assert a count of 32.** A count of 32 is satisfied by the wrong 32; the symmetric difference is what names them.
> - **(b)** `reference`+`backlog` within 274–314: same treatment — **symmetric difference against BACKLOG-9, asserted empty and printed.**
> - **(c)** `proposed` within 274–314 = **0**; `status_updated_by='ceo'` for all 41. ⚠️ **Item (a)'s symmetric difference doubles as the verdict-window guard against a concurrent INGEST:** `accepted` is not terminal, so an ingest between the steps can stale these 32 rows — they would drop out of the `accepted|codify` set and the difference would name them.
> - **(d)** every one of the 41 carries `status_updated_at` equal to the transaction timestamp the dev log recorded verbatim. ⚠️ **A differing timestamp on any row means a second writer touched the batch inside the verdict window.** → `routing-verification.txt`
>
> **2. TARGET-1 LANDED.** Row 301: `target_artifact` = `funnel-mechanization-v0-2026-08-08.md`, `status`=`reference`, `route`=`backlog`. ⚠️ **And assert NO OTHER row's `target_artifact` changed** — compare the full `id,target_artifact` projection against the pre-dump; exactly one row differs. → `routing-verification.txt`
>
> **3. UNTOUCHED POPULATION.** Re-run the `diff` of the committed pre/post dumps in this session. **Every changed row's id is within 274–314; zero foreign ids.** Report the changed-row count (expect 41) and the changed-*line* count separately, so the paired form cannot be misread either way. → `diff-audit.txt`
>
> **4. THE DUMPS ARE THE COMMITTED ONES.** `git show HEAD:<path>` for both dump files and confirm each matches the working-tree copy byte-for-byte. ⚠️ **An uncommitted edit to a dump would make row 3 an audit of something that never shipped.** → `diff-audit.txt`
>
> **5. FULL SUITE.** Run `src/test_lessons_forge.py` whole; record the raw summary line **VERBATIM**. *(⚠️ **Isolation verified at source at authoring, not assumed:** `_setup()` at `src/test_lessons_forge.py:31-35` connects to `":memory:"` and fixtures go to `tempfile.mkstemp` — **the suite never opens the canonical corpus DB, so this run cannot stale the 32 rows Step 1 just wrote.** The inverse would have made QA the thing that broke the plan.)* **Measured at authoring 2026-08-11: `55 passed in 0.12s`** — ⚠️ **a measurement with a timestamp, not a bar.** This plan changes no code, so the expected result is **55 passed**; **a HIGHER count is not a failure** (a sibling plan may have added tests) — report the delta and name it. **Only a FAILURE or a count BELOW 55 is a HALT.** → `suite.txt`
>
> **6. THE DB WAS NOT COMMITTED.** `git -C "$ROOT" log --name-only` over both step commits shows **no `lessons-forge.db`**, and `git ls-files --error-unmatch lessons-forge.db` still errors. ⚠️ **Re-tracking the DB is the one irreversible mistake available here** — plan 30 deliberately un-tracked it. → `routing-verification.txt`
>
> **7. NOTHING ELSE MOVED.** `git status --porcelain` at `$ROOT` is EMPTY, and assert by name that `DRAFTING_CYCLE.md`, `PLANNER_TEMPLATE.md`, `funnel-mechanization-v0-2026-08-08.md`, `LESSONS.md` and `knowledge/FORWARD.md` are absent from both step commits. ⚠️ **`knowledge/FORWARD.md` specifically: this plan emits no rows, so a FORWARD change means the Receipt channel fired against Scope.**
>
> **Then `## Evidence and Narrative`, then the Output Receipt.**
>
> ⚠️ **`### Ledger Updates`** — author via `Write`/`Edit` (the daemon parses assistant text and Write/Edit content, NOT Bash), EXACTLY ONCE, complete, never re-edited; `##`-level after `## Evidence and Narrative`; blank line after the last subsection.
>
> ⚠️⚠️ **OMIT the `#### Forward Register` subsection ENTIRELY. Do not write "None".** Per Scope this plan emits zero rows; the batch's five owed rows and the five queue calls ride the session wrap.
>
> **FINAL ACTION — COMMIT YOUR DEPOSITS**, pathspec on the COMMIT naming exactly the Scope files, then assert `git show --name-only --format= HEAD` prints exactly them. **Commit only — NO push.**
>
> **Scope:**
> - `knowledge/qa/gate1-routing-qa-2026-08-11.md`
> - `knowledge/qa/evidence/gate1-routing-2026-08-11/suite.txt`
> - `knowledge/qa/evidence/gate1-routing-2026-08-11/routing-verification.txt`
> - `knowledge/qa/evidence/gate1-routing-2026-08-11/diff-audit.txt`

**Deposits:**
- `lessons-forge/knowledge/qa/gate1-routing-qa-2026-08-11.md`
- `lessons-forge/knowledge/qa/evidence/gate1-routing-2026-08-11/suite.txt`
- `lessons-forge/knowledge/qa/evidence/gate1-routing-2026-08-11/routing-verification.txt`
- `lessons-forge/knowledge/qa/evidence/gate1-routing-2026-08-11/diff-audit.txt`

---

## Drafting Cycle

**Tier:** T1 — computed, not judged. **T-2 fires** (production-data mutation: 41 rows of the canonical corpus). **T-5 does NOT fire** — ⚠️ **this was measured, not assumed, and the first reading was wrong.** `lessons-forge.db` is gitignored (`.gitignore:6`) and untracked (`git ls-files --error-unmatch` errors), which reads as unrecoverable; but the clone origin's recovery instrument is the **committed pre/post dump pair**, not a `.db` backup, and 326 ran the identical operation at T1 and closed. **T-8 does NOT fire** — eleven closed `Gate 1 Route Disposition` plans, newest `executable-326`, same project, same table, same transaction shape. **T-1 does not fire via the every-row clause:** 41 of 314 rows, not the whole table. **T-6 does not fire** — no doctrine edit; Gate-2 plans own those.

⚠️ **A proven-clone framing is NOT licence to down-tier or skip rigor** (§2.6). The clone-diff against 326 is what produced this plan's three corrections before drafting began: the `accepted|backlog` encoding that has zero corpus instances, the FORWARD emissions that belong at the wrap, and the tier itself.

**Walks:** 7 — five lenses each, strictly sequential, each lens acting on the draft as folded by the previous.
- Weak spots:          w1 5 folded — **5/5 pre-existing**, 1 HIGH. ⚠️ **`status_updated_at` was written as `<ISO-now>` in two separate statements while QA item 1(d) asserts all 41 share ONE value — two `datetime.now()` calls differ by microseconds and would fail that item on a CORRECT run** (batch entry 289's class, in the batch this plan routes). Bound as a single `:TS` parameter. Also: the suite baseline is now a measured `55 passed` with an explicit higher-is-not-a-failure clause, and the CODIFY-32 placeholder was inlined.
- Destruction:         w1 3 folded — **3/3 pre-existing**, 2 HIGH. ⚠️⚠️ **The pre-dump omitted `status_updated_at`, so it could DIFF but not RESTORE** — measured: all 41 rows are NULL today, the transaction sets them, and a rollback from a dump blind to that leaves 41 rows stamped by an undone transaction. **Inherited from the clone origin, closed here.** Also: A0's single HALT message blamed a concurrent writer for a state an already-landed redo produces identically.
- Vulnerabilities:     w1 2 folded — 2/2 pre-existing, 1 HIGH. ⚠️ **The rowcount gate cannot see a WITHIN-RANGE SWAP** — the wrong 32 is still 32, `proposed` still reaches 0, and every in-transaction gate passes. QA item 1 now compares SETS and prints the symmetric difference. **Residual stated, not engineered away: a swap authored into the payload is invisible to this plan**, since script and QA both read it from here.
- Integration-record:  w1 2 folded — 2/2 pre-existing, 1 HIGH. ⚠️⚠️ **Verified at source (`src/lessons_forge.py:31`): `_TERMINAL_STATUSES` omits `accepted`. This plan therefore grows the stale-able population 42 → 74**, while the 9 `reference` rows are protected. It is the hazard `knowledge/FORWARD.md` row 12 records — the pair plan 341 just deduplicated. Stated, with a procedural guard; not fixed here. Also verified rather than assumed: the suite connects to `":memory:"`, so QA's own run cannot stale what Step 1 just wrote.
- ACID:                w1 4 folded — 3 pre-existing, **1 fold-introduced**, 1 HIGH. ⚠️⚠️ **The recovery instrument was uncommitted when the destructive act ran** — a death after `COMMIT` but before the final commit writes the DB and takes the only pre-state record down with the worktree. **The pre-dump now commits ALONE, first**, and the post-commit assertion became a union over Step 1's two commits — because a three-path `git show HEAD` assertion prints two on a correct run, and the only way to satisfy it would be to re-merge the commits and reintroduce the defect.

**Walk 1 total: 16 findings, 16 folded — 15 pre-existing (94%), 1 fold-introduced (6%), 6 HIGH.**

⚠️ **FIVE of the sixteen came from the clone-diff against `executable-326` rather than from reading this draft** — the `accepted|backlog` encoding, the FORWARD-emission routing, the tier, the dump's missing `status_updated_at`, and the pre-dump's commit ordering. **Three of those are defects the ORIGIN carries and this clone would have inherited silently.** That is the measured argument for §2.6's clone-diff mandate, and against reading a "proven clone" as a licence to skip it.

**Walk 2** — the new surface was walk 1's own folds: the `:TS` binding, the two-commit split, the six-column dump, A0's redo branch and the symmetric-difference QA.
- Weak spots:          w2 4 folded — **4/4 fold-introduced**, 1 HIGH. ⚠️ **The commit-split fold left the dump's column rationale ORPHANED AFTER the commit it must precede** — an agent reads the SELECT, commits it, then reads why those columns matter. Moved, and the move verified by count (rationale appears exactly once, order dump→rationale→commit→Task B). Also: a `> >` double-blockquote my own fold introduced, and `[<plan-id>]` left as an unresolved token.
- Destruction:         w2 2 folded — **2/2 fold-introduced.** ⚠️ **Walk 1's framing overstated the rowcounts:** the pre-dump is now committed BEFORE `BEGIN IMMEDIATE`, so a concurrent writer in that window could alter a field the rowcount guard cannot see. **Task C's foreign-line check is what actually covers it** — the rowcounts guard the status transition, the diff guards everything else, and neither alone is the window guard. Also: a lone pre-dump commit is a CLEAN state and is now said to be, so it is not "completed".
- Vulnerabilities:     w2 2 folded — 2/2 fold-introduced, 1 HIGH ⚠️ **RETIRED BY SOURCE READ**: the two-commit split does not break the daemon's gate — `bellows.py:990 _parse_diff_stat` diffs a RANGE (`<baseline> <post>`), so both commits land in `files_changed`. Recorded so nobody collapses the commits "to be safe". Also: the union assertion's `<sha>^..HEAD` form assumed the pre-dump commit has a parent; replaced with two explicit `git show`s.
- Integration-record:  w2 1 folded — 1/1 fold-introduced. ⚠️ **A precedent probe for two-commit steps returned keyword hits too loose to settle anything, and is recorded as NOT ESTABLISHED rather than as an absence.** The mechanism is verified at source; the precedent is unknown; the mechanism is what this rests on.
- ACID:                w2 2 folded — **2/2 fold-introduced**, 1 HIGH. ⚠️ **The redo path hits a FAILING empty commit:** a death between the pre-dump commit and Task B re-enters CLEAN, re-dumps identical bytes, and `git commit` fails with *nothing to commit* — which an agent reads as a failure to repair. Now: already-committed-and-identical is success. Also: "both commit hashes" in the dev log is unsatisfiable when Task B halts and only one exists.

**Walk 2 total: 11 findings, 11 folded — 0 pre-existing, 11 fold-introduced (100%), 3 HIGH.**

⚠️⚠️ **THE ORIGIN SPLIT WENT 94% pre-existing → 100% FOLD-INTRODUCED, and the count fell 16 → 11.** Every finding this walk was damage from walk 1's own repairs, concentrated in the one region walk 1 restructured — the pre-dump commit split, which produced findings in four of the five lenses.

**Walk 3** — the new surface was walk 2's folds, and the prediction made at walk 2's close held exactly.
- Weak spots:          w3 2 folded — **2/2 fold-introduced**, 1 HIGH. ⚠️⚠️ **SIX consecutive paragraphs had accreted across walks 1 and 2, all describing ONE action (commit the pre-image), and the sequence stated a PREREQUISITE — derive `<plan-id>` — AFTER the instruction needing it.** That is batch entry 306's task-accretion class, on the plan that routes entry 306. **COLLAPSED into an ordered Task A1.** Also swept a stale reference to the `<sha>^..HEAD` range form walk 2 had already removed.
- Destruction:         w3 1 folded — **1/1 fold-introduced**, 1 HIGH. ⚠️⚠️ **THE COLLAPSE REPRODUCED THE DEFECT IT FIXED.** It left the re-entry check as a trailing `A1.5`, one paragraph *after* the commit that check gates — **third instance of the ordering class in this region across three walks.** Absorbed into A1.4 so the check is a precondition. **Retention verified mechanically before this fold, not by checklist: 13 distinctive literals, each present exactly once in the body, no duplication, no orphaned pointer.** The absorption then left a dangling `A1.1–A1.5` range in the task heading, swept immediately.
- Vulnerabilities:     w3 dry — the collapsed A1 was probed for degenerate re-entry (tracked-and-identical, tracked-and-differing, untracked) and each has a stated branch.
- Integration-record:  w3 dry on the artifact — ⚠️ but one datum for the record: **this is the SECOND plan in two days where collapsing a region beat patching it** (plan 341's Task A0/A/B → A1–A7 closed four findings; this closed three). Both collapses then produced one further finding each, which is the structural-edit tax and is cheaper than the accretion.
- ACID:                w3 dry — atomicity re-walked across A1.1–A1.4: die anywhere and A0 re-pins, the CLEAN branch re-enters, A1.4's precondition absorbs the already-committed case.

**Walk 3 total: 3 findings, 3 folded — 0 pre-existing, 3 fold-introduced (100%), 2 HIGH. Two lenses ran DRY, and lens 4 found nothing in the artifact.**

⚠️ **THE CURVE: 16 findings (94% pre-existing) → 11 (100% fold-introduced) → 3 (100% fold-introduced, 2 lenses dry).** Falling count, saturated origin split, and the findings now confined to one region that has just been collapsed.

**Walk 4** — CEO direction: meet the bar rather than take a judged stop. Full five lenses over the whole artifact.
- **3 findings, 3 folded — 0 pre-existing, 3 fold-introduced (100%), 0 HIGH, ALL RECORD-CLASS.** The drafting record had leaked into Task A1's instruction body (§3 keeps the record in the Cycle Log); a multiplicity assertion was phrased against `re.search`, which returns at most one match and cannot report it; a blockquote separator was missing between A0 and A1.
- ⚠️ **Both bar conditions were met on this walk** — record-class only, 100% fold-introduced. **But the last event was a fold, not a dry lens pass**, and one finding (`re.search` → `re.findall`) sits close enough to the instruction/record line that claiming it clean without a confirming pass would have been authoring the gate rather than earning it.

**Walk 5 — the CONFIRMING pass, and it was NOT dry.**
- Weak spots:          w5 1 folded — **1/1 fold-introduced, and INSTRUCTION-CHANGING.** ⚠️⚠️ **The Step-1 deposit paragraph had become a WALL: measured 1,489 characters and 5 sentences carrying EIGHT distinct instructions — nearly double the next-largest block in the plan.** It accreted across walks 1–3, one correct appendage at a time. **This is batch entry 306's class — the entry this plan routes — and 306's own finding is that past some length a block stops being an instruction and becomes a passage the agent executes PART of.** Collapsed into an ordered **Task D (D1–D4)**; retention verified mechanically (10 distinctive literals, each present, no orphaned pointer); worst remaining block now 832 chars.
- Destruction:         w5 **dry** — diff review of the D-collapse: nothing dropped, nothing duplicated.
- Vulnerabilities:     w5 **dry** — the re-entry interaction re-walked: when A1.4 takes its already-committed branch this dispatch makes one commit, and D3's explicit two-sha union still resolves because the pre-dump sha is from the prior dispatch.
- Integration-record:  w5 **dry** — §3 record separation now clean; consistent with plan 341's collapse precedent.
- ACID:                w5 **dry** — the commit-set assertion holds on both the clean and re-entry branches.

**Walk 5 total: 1 finding, 1 folded — 100% fold-introduced, FOUR LENSES DRY.**

⚠️⚠️ **THE BAR IS NOT MET, AND THE CONFIRMING PASS IS WHY.** Walk 4 satisfied both conditions; walk 5 then found a defect that **changes what an executing agent does** — an agent given eight instructions in one 1,489-character block executes a subset of them. **§2's record-class condition therefore re-opens the walk.** That is the confirming pass earning its keep exactly as §2 predicts: *you do not know it is dry until you have run it lens-by-lens.* **Walk 6 is owed.**

**Walk 6 — the second confirming pass. Also NOT dry, and also exactly one finding.**
- Weak spots:          w6 1 folded — **1/1 fold-introduced, INSTRUCTION-CHANGING.** ⚠️ **A chicken-and-egg in the deposit ordering:** D1 required the dev log to carry *"the hash of every commit this step made"*, but the dev log is **written at D1 and committed at D2** — a file cannot carry the sha of the commit that creates it. An agent trying to satisfy it would stall or fabricate. **D1 now records A1.4's pre-image sha only (with the inherited-sha case named for the re-entry branch); D3 reports D2's sha after D2 has made it.**
- Destruction:         w6 **dry** — the fold tightened rather than relaxed; the *"do not write both"* nuance dissolved correctly rather than being dropped, and the orphan sweep found the phrase surviving only inside the fold's own quotation of it.
- Vulnerabilities:     w6 **dry** — re-entry re-walked: on A1.4's already-committed branch D1 records the inherited sha and D3's two-sha union still resolves.
- Integration-record:  w6 **dry**.
- ACID:                w6 **dry** — Step 2 needs neither sha (Q0 uses `git log`, QA row 4 uses `git show HEAD:<path>`), so the record is sufficient.

**Walk 6 total: 1 finding, 1 folded — 100% fold-introduced, FOUR LENSES DRY.**

⚠️⚠️ **THE BAR IS NOT MET, AND THE REASON IS NOW A PATTERN RATHER THAN A DEFECT.** Walks 5 and 6 each returned **exactly one finding, each instruction-changing, each in the COMMIT/DEPOSIT machinery** — the wall at walk 5, the sha ordering at walk 6. Add A1's three folds across walks 1–3 and **the commit machinery has produced findings in five of six walks, while the routing transaction itself — the thing this plan exists to do — has been dry since walk 2.**

⚠️ **§2.8 names this: persistent oscillation on one region is a signal to step back and joint-resolve or escalate, not a quota to work through.** The design question underneath it is stated in the Residue below and is a CEO decision, not another fold.

⚠️ **THE CURVE: 16 (94% pre-existing) → 11 → 3 → 3 → 1 → 1, with 0 → 0 → 2 → 0 → 4 → 4 dry lenses.** Every walk since the first has been 100% fold-introduced. **Both walls this cycle collapsed were found by the lens that reads for accretion, and both had accreted across three walks of individually-correct appendages.**

**Clone-diff against the newest same-class (`executable-326`)** — ⚠️ **RESTORED at walk 7: this record was deleted by a walk-4 rewrite of the Cycle Log, and nothing noticed for three walks.** The record decayed while the artifact converged, which is the class §2.7's closing re-read exists for; here integration-vs-record caught it first.
- **CARRIED FAITHFULLY:** the addressing contract; `BEGIN IMMEDIATE` + `busy_timeout` under WAL; the `AND status='proposed'` double-duty guard; rowcount-gate-then-ROLLBACK; immutable payload lists; the pre/post dump pair and its untouched-population diff; the DB-absent-from-Scope policy; no DEV test run; single-commit deposit.
- **ADAPTED:** 51→41 rows, 223–273→274–314, 44/7→32/9.
- **ADDED (no precedent in 326):** the `target_artifact` UPDATE and its ordering interaction with statement 2's guard; `target_artifact` and `status_updated_at` added to both dump SELECTs — without the first the diff cannot see TARGET-1, without the second the dump can diff but not restore.
- ⚠️⚠️ **BUILT THEN CUT — the separate pre-image commit (walk 1 → walk 7, CEO decision 2026-08-11).** Walk 1's argument was sound in the abstract: a recovery instrument still uncommitted when the destructive act runs is not one. **What it never priced is what the dump is needed FOR.** Measured 2026-08-11: all 41 target rows are uniformly `proposed | NULL | NULL | NULL` across every field the transaction writes, so **the 41-row pre-state is fully reconstructible from the payload without the dump.** The dump's unique contribution is the **untouched-population proof for the other 273**, and the split protected only that — against a death in the seconds between Task B's `COMMIT` and Task D's commit, **a state A0's already-landed branch detects and escalates.** **Cost: findings in five of six walks**, while the routing transaction has been dry since walk 2. **Knowingly given up:** on a death in that window the pre-dump is lost with the worktree and the untouched-population proof cannot be reconstructed; A0's redo branch still detects the landed write and hands it to the CEO.

**Walk 7 — the confirming pass on the CUT shape, because a subtractive edit is unreviewed by construction.**
- Weak spots:          w7 1 folded — **record-class.** The cut's own rationale had landed as a 957-character block inside Task A1's instruction body — the same record-in-instruction class walk 4 folded out of A1. **A short do-not-re-add DIRECTIVE stays in the step (§2.6 asks for one); the measurement and the trade-off moved to the clone-diff record above.**
- Destruction:         w7 **dry** — the cut got a DIFF REVIEW, not a retained-material checklist: 12 removed lines, every one belonging to the split; **two dangling range references (`A1.1–A1.4`, `D1–D3`) found and fixed**; the daemon-gate `_parse_diff_stat` note went with the split it justified and is moot under one commit.
- Vulnerabilities:     w7 **dry** — death-state re-walk under one commit: die before Task B → A0's CLEAN branch; die after `COMMIT` → A0's already-landed branch detects and escalates. No new degenerate case.
- Integration-record:  w7 3 folded — **all record-class.** ⚠️ **The clone-diff record had been deleted by a walk-4 Cycle Log rewrite and was missing for three walks; the Conformance line still read "not yet run" after FIVE runs; the Closing line still described walk 3.** All three are the plan's own record decaying while the artifact converged.
- ACID:                w7 **dry**.

**Walk 7 total: 4 findings, 4 folded — 0 pre-existing, 4 fold-introduced (100%), 0 HIGH, ALL RECORD-CLASS. Three lenses dry.**

⚠️⚠️ **THE BAR IS MET — both conditions, on this walk, and stated as numbers rather than asserted.** **Record-class only:** nothing folded at walk 7 changes what an executing agent does — a directive moved between sections, a deleted record restored, two stale lines corrected. **Predominantly fold-introduced: 4 of 4 (100%).** ⚠️ **This is a qualifying close under §2's stated relaxation, NOT the declared deviation taken on plan 341** — that one failed the record-class condition and was taken anyway; this one meets it.

⚠️ **THE CURVE: 16 (94% pre-existing) → 11 → 3 → 3 → 1 → 1 → 4, with 0 → 0 → 2 → 0 → 4 → 4 → 3 dry lenses.** The walk-7 count rose because a SHAPE CUT created new surface — batch entry 294's predicted cost, taken deliberately — and every one of the four was record-class.

**Conformance (§5):** run at shape-stability and re-run after every culmination since, at the DEPOSIT path resolution (`lessons-forge/knowledge/decisions/`), never from `knowledge/research/` — `plan_lint`'s expected-WARN set is location-dependent. **Runs: 5. Latest, after the walk-7 folds: exit 0, ONE warning.**
- `step 1 mentions tests but declares no test scope` — **known-benign**: the header declares `Test Scope: targeted — no code, no tests`, and the token appears only in prose. **Not silenced, not reworded to evade.**
- ⚠️ **The `fold as last event` warning is ABSENT and that is EARNED, not engineered** — the Closing below states a bar-meeting close, not a fold.

**Any OTHER warning at deposit is unexplained → do not deposit.**

### ⚠️ RESIDUE — enumerated individually, per §2

The bar's record-class condition is **met**, so this residue is record-class by the bar's own condition rather than by assertion. Enumerated anyway, because a close is auditable or it is not a close.

| # | residue | class | what read it |
|---|---|---|---|
| R1 | The restored clone-diff record and the cut rationale moved into it | record | written by w7 lens 4 — **no lens has read it** |
| R2 | The short do-not-re-add directive left in Task A1 | record | written by w7 lens 1; lenses 2–5 read the region around it |
| R3 | The corrected Conformance and Closing lines | record | written after w7's lenses; the §2.7 re-read below is their reader |
| R4 | Task D's single-commit shape (D1–D4) | **instruction** | authored at the cut, read by w7 lenses 2–5, all dry |
| R5 | The untouched-population proof's loss in the death window | **deliberate** | CEO decision 2026-08-11, priced and recorded above |

⚠️ **R4 is the one to weigh** — it is instruction-class and was authored during the cut. It was read by four lenses (all dry) but by none of them before it existed. **The mitigating fact is that it is a REVERSION to `executable-326`'s shipped, closed shape, not a new invention.**

**Closing:** ✅ **BAR MET — a qualifying close under §2, not a declared deviation.** Walk 7 returned **4 findings, all record-class, 4 of 4 fold-introduced (100%), with three lenses dry.** Both of §2's conditions hold on the same walk, stated as numbers: record-class only, and predominantly fold-introduced.

**Residue class in a clause apiece:** 3 record-class (a restored clone-diff record, a relocated directive, two corrected status lines), 1 instruction-class (Task D's single-commit shape — a reversion to the clone origin's shipped form, read by four lenses, THREE of them dry: lens 4 was not dry, it found record defects elsewhere in the artifact), 1 deliberate hold (the untouched-population proof in the death window, priced by CEO decision).

⚠️ **What this close costs, stated honestly:** the shape cut at walk 7 created new surface, and R1–R3 were written after the lenses that would have read them. **The §2.7 closing-record re-read is their reader and it is mandatory here** — on T1 there is no cold panel, so that re-read plus this enumeration are the entire remaining reader.

### §2.7 closing-record re-read — RUN, and it raised two

Mandatory at every close, most load-bearing here because R1–R3 were written after the lenses that would have read them. On **T1 there is no cold panel**, so this re-read plus the residue enumeration are the entire remaining reader. Run adversarially against the artifact after the closing record was written.

**2 findings, both record-class, both introduced by the closing record itself:**

1. **A residue line over-claimed its own evidence.** R4 was described as *"read dry by four lenses."* Four lenses did read it, but **lens 4 was not dry** — it found the deleted clone-diff record and two stale status lines. Corrected to *four lenses, three of them dry.* ⚠️ **The over-claim ran in the direction that flatters the close**, which is the direction this re-read exists to catch.
2. **The arithmetic was re-derived rather than trusted:** walk 7's `4 findings` reconciles as lens 1 (1) + lens 4 (3) with lenses 2/3/5 dry — **4 findings, 3 dry lenses**, matching the Closing. The conformance `Runs: 5` was re-counted against the actual invocations on this plan (post-draft, post-walk-3, post-walk-5, post-cut, post-walk-7) and holds.

⚠️ **The re-read found NO defect in the instruction stream** — both findings are in the record about it, which is the expected distribution for a close that meets the record-class condition.

**Fold-and-deposit exactly once.**
