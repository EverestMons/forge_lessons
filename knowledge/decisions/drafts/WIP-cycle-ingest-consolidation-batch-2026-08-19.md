# Lessons Forge — Cycle Run 2026-08-19, PLAN A: ingest the 25-entry consolidation batch (classification held to Plan B)

**Date:** 2026-08-19 | **Tier:** Small | **Dispatch Mode:** bellows | **Test Scope:** targeted | **Execution:** Step 1 (Lessons Agent — ingest the 25) → Step 2 (QA) | **qa_steps:** 2 | **pause_for_verdict:** always
**cycle_tier:** T1 — T-8 (clone of `executable-423`). No T-4: read-mostly, single INSERT-only ingest, dry-run rehearsable against a scratch DB copy.
**Slug:** `cycle-ingest-consolidation-batch-2026-08-19`
**Project:** lessons-forge
**Author:** Planner
**dispatch_mode:** bellows
**Priority:** 1

## CEO Context

**Ingest only.** This plan takes the **25** un-ingested `LESSONS.md` entries into the corpus and stops. **It creates no proposals, writes no report, and classifies nothing.** Classification and the report are **Plan B**; Gate-1 routing is a third plan after that.

⚠️ **Why the split matters more here than it did at 423.** Five of the 25 entries were written by the Planner **today**, and they are the evidence base for changes to `DRAFTING_CYCLE.md` and `PLANNER_TEMPLATE.md` that the Planner authored, evidenced, and benefits from — including the retirement of PT v4.89's project-bin arm. **The corpus path exists so a NON-AUTHOR routes them at Gate 1.** That is the entire reason this plan exists instead of a direct doctrine edit, and a 25-entry batch containing the author's own proposals is the strongest case yet for keeping ingest, classification and routing in three separate plans.

**Clone lineage — measured, not recalled:** … → 411 → **423** (direct origin AND newest same-class cycle plan; `Done/executable-423.md`, closed 2026-08-14). Verified by listing `lessons-forge/knowledge/decisions/Done/` by ship date: 427 and 428 are newer but are a QA-corrective and a Gate-1 routing write, not cycle runs.

### ⚠️⚠️ INHERITED FACTS FROM 423 THAT ARE FALSE HERE — every one re-measured 2026-08-19

1. **THE BATCH IS 25, NOT 1.** Verified two independent ways: a real `ingest_lesson_entries` dry run against a `cp`-made scratch DB returned **`inserted 25 / updated 0 / unchanged 288`**, and a content-hash set difference against the live corpus returned the same 25. Parser total **313**.
2. ⚠️ **THE EM-DASH REGIME IS INVERTED.** 423 recorded *0 of 1* headings carrying ` — `, so duplicate detection rested **entirely** on the fallback path. Here **10 of 25** carry it — the primary path runs for 10 and the fallback for 15. **423's "rests entirely on the fallback" note is FALSE here and must not be carried.**
3. ⚠️ **A NEW HOSTILE CHARACTER CLASS 423 NEVER FACED: a BACKTICK inside a heading.** Measured: 1 double quote (423's hazard), **4 apostrophes**, and **1 backtick** — and the backtick entry carries both: `` 2026-08-18: `plan_lint`'s dryness check disagrees with §2's bar… ``. Any shell-interpolated probe over that heading must use `grep -F` with single-quoted patterns; a double-quoted shell string would command-substitute the backticks.
4. **BASELINES MOVED:** `E0 = 345` (423: 344), `P0 = 353` (423: 352).
5. **THE SENTINEL MOVES** to `2026-08-19: A knowledge destination that is not ingested cannot improve the system…`, content-hash `76b1b344208b36f99b80ecda8a878aab8825c0a5901650b38c572b574bce0125`.
6. **STILL TRUE, verified not assumed — the non-terminal proposal set is UNCHANGED at exactly `{340, 342, 346, 350, 352}`.** 423's G1 value guard carries as written. ⚠️ Recorded explicitly *because* it is the one inherited fact that survived; an unverified carry-forward is what the clone-diff exists to catch.
7. ⚠️⚠️ **423's CRITERION-1 REASONING IS FALSE ON BOTH OPERANDS HERE — the conclusion survives, the reason does not, and the difference is a live hazard.** 423 recorded criterion 1 as *"doubly unfalsifiable"* because (a) `PLANNER_TEMPLATE.md` carries **0** `**Tag:**` lines and (b) the batch entry's `tags` column was **NULL**. Measured 2026-08-19: **(a) is false — PT carries 1 `**Tag:**` occurrence** (line 1967), and **(b) is false for every entry — all 25 carry tags.** Criterion 1 is nonetheless inert, for a **third reason neither plan stated**: `_TAG_LINE_RE.match(line.strip())` anchors at line start, and PT's occurrence is **mid-line prose** inside step 7's description of the house format — so `ref_tag_sets` builds **empty**. ⚠️ **This is now a ONE-operand guard, not a two-operand one.** A single line-initial `**Tag:**` ever added to `PLANNER_TEMPLATE.md` turns criterion 1 live against all 25 tagged entries at once. **G-DUP therefore ASSERTS `ref_tag_sets` is empty at run time rather than inheriting it.**
8. **DOCTRINE PIN UNCHANGED:** `DRAFTING_CYCLE.md` is still **v2.11**, sha `acce7ebe6fa4f145bd7440485e45a0e66b650a1e`.

## Numbers discipline

⚠️ **This table is the ONLY place a quantity is declared** (honing-notes P-5). Every other section references a symbol.

| id | pin | before | after | probe |
|---|---|---|---|---|
| N1 | batch size | — | **25** | dry run `inserted`, cross-checked by content-hash set difference |
| N2 | corpus entries `E0` | **345** | `E0` + 25 = **370** | `select count(*) from lesson_entries` |
| N3 | `would_update` | — | **0** | ⚠️ **the invariant. Non-zero → HALT**: an ingested row's body changed |
| N4 | unchanged | — | **288** | dry run `unchanged` |
| N5 | proposals `P0` | **353** | **353 — UNCHANGED** | this plan classifies nothing; any growth is a scope breach |
| N6 | non-terminal set | `{340,342,346,350,352}` | identical | G1 value guard, keyed by id |
| N7 | parser total | **313** | 313 | `parse_lessons_md` on the register |

## Scope

Write to exactly one artifact: `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db`. ⚠️ **The corpus is `lessons-forge/lessons-forge.db`** — sibling `forge.db` and `lessons.db` are 0-byte decoys that return false absences. Do **not** classify, do **not** create proposals, do **not** write a cycle report, do **not** touch `LESSONS.md`, `PLANNER_TEMPLATE.md` or `DRAFTING_CYCLE.md`.

## HALT ROUTING

Any measured value outside its stated expectation → **HALT**, quoting every measured input. **Never repair forward.** On any HALT: commit existing deposit files by explicit pathspec and record the gate, its measured value, and **whether the ingest committed** — that last fact is what a resume needs and what a lost session destroys.

**Authorized writes, and nothing else:** the `.backup`, the single `ingest_lesson_entries` call, and this step's deposits.

## STEP 1 — Lessons Agent: ingest the batch (NO classification anywhere in this plan)

> **FIRST — post a short visible chat message (1–2 sentences).** Do NOT rename the plan file.
>
> You are the Forge Lessons Agent. Read `agents/FORGE_LESSONS_AGENT.md` first. ⚠️ **Its DB paths are relative and you run in a worktree** — every canonical-DB access uses the ABSOLUTE path `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db`. **`forge/forge.db` is a REAL but DIFFERENT database — never open it**; sibling `lessons.db` is a 0-byte decoy that returns false absences.
>
> ⚠️ **NO CLASSIFICATION.** `get_unclassified_entries()` returning a 25-id work list is this plan's **CORRECT closing state**, not an omission. Proposals must remain at `P0` — see N5.
>
> **Env facts:** `grep` is a ugrep shim — `-F` mandatory for literals; **a zero-match `grep -c` prints `0` and EXITS 1** (read stdout, never `$?`). ⚠️⚠️ **One batch heading contains a BACKTICK** (`` `plan_lint`'s dryness check… ``) **and four contain apostrophes.** Every shell probe over a heading uses `grep -F` with a **single-quoted** pattern; a double-quoted shell string would command-substitute the backticks. 423 never faced this class.
>
> **Deposits:**
> - `knowledge/development/dev-log-cycle-ingest-consolidation-2026-08-19.md`
> - `knowledge/development/evidence-cycle-ingest-2026-08-19.txt` — ⚠️ **a named `.txt` is REQUIRED or `qa_test_result` cannot pass**; plan 451 hit exactly this and burned a verdict on it.
>
> ### Step 0 — dispatch state
> Three-place probe on the dev-log path (committed HEAD; working tree; `git log --all` + `branch --list 'bellows-preserved/*'`), each with its exit code captured. ⚠️ Probe 3's exit carries **no** signal — pair it with a positive control against `knowledge/FORWARD.md` before reading silence as a no-hit. Any hit → **RESUME**. All absent → **FRESH**. State the determination first.
>
> **Single-writer check:** `get_unclassified_entries` stable across two reads; `ls /Users/marklehn/Developer/GitHub/lessons-forge/knowledge/decisions/in-progress-*.md` — **THIS PROJECT ONLY**; this plan's own file present is normal, **ZERO matches means the probe is broken**, any OTHER match → HALT.
>
> ### Step 1a — restore point, then baseline
> ```
> mkdir -p /Users/marklehn/Developer/GitHub/lessons-forge/data/backups
> BK="/Users/marklehn/Developer/GitHub/lessons-forge/data/backups/lessons-forge-pre-cycle-<id>-$(date -u +%Y%m%dT%H%M%SZ).db"
> sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" ".backup '$BK'"
> ```
> `<id>` = this plan's ACTUAL minted id. VERIFY **in exactly this form**: `sqlite3 -readonly "file:$BK?immutable=1" 'PRAGMA integrity_check;'` → `ok`. ⚠️ **The `file:` prefix and `?immutable=1` are BOTH load-bearing** — `.backup` writes a WAL-header DB with no `-shm`, and a plain `sqlite3 -readonly "$BK"` fails with `unable to open database file (14)`.
> ⚠️ **Date the backup with `date -u`, not the session date** — proposal 352 and the midnight-boundary lesson both bite here.
> Resume glob: `find … -name 'lessons-forge-pre-cycle-<id>-*.db'` — **`.db`-scoped; a bare prefix matches sidecars and returns ~3 per backup, firing a spurious HALT.** EARLIEST match; prove pristine by `MAX(id)` = `E0`/`P0`.
>
> **Baseline capture (read-only, raw output):** (1) the zero-emitting distribution over ALL EIGHT statuses — expected `implemented 282 · superseded 28 · reference 20 · rejected 15 · accepted 5 · stale 3 · proposed 0 · ambiguous 0`; (2) proposals by category; (3) `E0`; (4) sentinel hash; (5) `STALE_COUNT`; (5b) `SURFACEABLE_BASE` ⚠️ **labelled distinctly from NT**; (6) `P0`; (7) **NT captured BY ID, not by count** — `SELECT 'NT='||GROUP_CONCAT(id) FROM (SELECT id FROM lesson_proposals WHERE status IN ('proposed','accepted','ambiguous') ORDER BY id);` → **a printed token is required; silence = broken invocation → HALT**; (8) FORWARD baseline `grep -c "^| "`, raw. **Capture only — the gates own the verdicts.**
>
> ### Step 1a-ter — commit the before-anchor BEFORE the ingest
> Write and `git commit` the dev-log stub: `Status: Partial — in flight (pre-ingest stub)`; the absolute backup path; `E0`/`P0`; **the NT id-list line**; STALE; SURFACEABLE; the FORWARD baseline; the full distribution; the sentinel hash; the doctrine pins raw — **HALT unless all print.** The final Receipt rewrites this file but carries any first-dispatch ingest dict forward **verbatim**.
>
> ### Step 1a-bis — pre-ingest guard (READ-ONLY, against a scratch copy)
> 1. `parse_lessons_md("/Users/marklehn/Developer/GitHub/LESSONS.md")` → assert **N7**. Dry-run `ingest_lesson_entries` against a **FRESH `cp`-made scratch DB**, never the live file.
> ⚠️ **A "dry run" here is not dry — treat it as a mutation.** `ingest_lesson_entries` contains a `conn.commit()` (`lessons_forge.py`), so the caller's `rollback()` cannot be relied on to undo it. *(Measured 2026-08-19: in one specific invocation the rollback DID hold and the scratch copy returned to `E0` — but whether that `commit()` fires depends on a branch not fully traced, and **a safety property that rests on an untraced branch is not a safety property**.)* **Make a fresh `cp` for every dry run, assert the copy's count equals `E0` before using it, and never hand the live DB to a call described as dry.** *(w1-6.)* **FRESH → assert `inserted == N1` AND `updated == N3`.** **RESUME → `updated == N3` and `inserted ∈ {0, N1}`.**
> ✅ **Unlike 423, a batch of 25 HAS intermediate values** — any `inserted` strictly between 0 and 25 is positive evidence of a foreign writer and is a HALT, not an ambiguity. 423 could not make this check because its batch was 1.
> 1b. **BATCH FINGERPRINT** — sha256 of `"\n".join(<would-insert headings in parse order>)` == **`4484828a0a400696a9148b89a422cffcbd2443be1a8df81df3e06691621fd34c`**. Mismatch → HALT. **RESUME with `inserted == 0` → SKIP, record `FINGERPRINT SKIPPED (post-ingest resume)`.**
> 2. **Sentinel:** the parsed entry matching the corpus sentinel heading — **measure the match count and PRINT it**; exactly 1 match with equal hash → PASS, else HALT.
> 3. **G-DUP — the duplicate pre-check, mirrored by hand.**
> ⚠️⚠️ **DO NOT CALL `detect_duplicates` FOR BATCH ENTRIES — IT CANNOT ANSWER, AND IT ANSWERS ANYWAY.** It reads each id from `lesson_entries` and hits `if row is None: continue` (`lessons_forge.py:363–369`) for an entry not yet ingested, returning `[]` — a confident false zero on the one pre-mutation check this plan calls a HALT condition.
> Do this instead, and **assert both operands rather than inheriting them**:
> - **Criterion 1 — ASSERT `ref_tag_sets` IS EMPTY.** Build it exactly as `lessons_forge.py:339–354` does (`_TAG_LINE_RE.match(line.strip())` over `PLANNER_TEMPLATE.md`) and assert the resulting set is empty. **Non-empty → HALT**: all 25 entries carry tags, so a single line-initial `**Tag:**` in PT would mark the whole batch duplicate. Measured empty 2026-08-19 — and note PT *does* contain one mid-line `**Tag:**` at :1967 that the anchor correctly ignores. **Inheriting 423's "0 tag lines" reason would have hidden this.**
> - **Criterion 2 — mirror it by hand.** Read `PLANNER_TEMPLATE.md` once, lowercase it, and for each batch heading compute the title the code computes: split on `_EM_DASH_SEP` (`' — '`) and take the **right** side if present, else the **whole stripped heading**; assert the lowercased title is **not** a substring. Measured: **10 take the separator path, 15 the fallback — both paths are exercised, so each acts as an in-batch control for the other.** 423 had no such control. Expected matches: **0**.
> - Pre-existing ids: mirror the ingest's candidate construction, PRINT the list length first (**HALT if 0 or wildly off**), then `detect_duplicates(conn, <ids>)` read-only → non-empty = HALT. *(Legitimate here: those ids ARE in the corpus.)*
>
> ### Step 1b — THE ONE MUTATION
> A single `ingest_lesson_entries` call against the live corpus by absolute path. Nothing else writes.
> **Post-conditions:** `inserted` == **N1**, `updated` == **N3**, `unchanged` == **N4**, and `E` == **N2**.
>
> ### Gates G1–G7 (post-mutation, read-only)
> **G1 — NT UNCHANGED, by id:** re-run the NT query; the id list must equal **N6** exactly. A count match with a different id set is a FAIL.
> **G2 — proposals unchanged:** `P` == **N5**. Any growth means classification ran → HALT, this plan's hardest scope boundary.
> **G3 — corpus count:** `E` == **N2**.
> **G4 — `updated` was 0:** re-assert from the returned dict, and confirm no pre-existing `content_hash` changed.
> **G5 — sentinel intact.**
> **G6 — `stale_proposals_marked` and `terminal_proposals_flagged` recorded raw** (measured 0 and `[]` at authoring; a non-empty flag list is information, not necessarily a fault — record and report, do not silently pass).
> **G7 — FORWARD unchanged** against the baseline.
>
> ### Deposit
> Write both deposits, `git add` **by explicit pathspec**, commit. **Do not `git add -A`.** ⚠️ **Commit the deposits in this step** — a declared deposit that is never committed fails `deposit_uncommitted`, exactly as plan 451 did.

## STEP 2 — QA

> **QA SELF-CHECK — Rule 20.** Post the block from `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md` verbatim under the banner **`Rule 20 — QA Self-Check Results`**, closing with the **`PASSED`** line.
>
> Verification only. **Evidence must be RAW command output pasted verbatim — never a summary, never a claim that a check passed.**
>
> **Deposits:** `knowledge/development/qa-cycle-ingest-consolidation-2026-08-19.md` **and** `knowledge/development/qa-evidence-cycle-ingest-2026-08-19.txt` — the `.txt` is required for `qa_test_result`.
>
> 1. Re-run every pin in `## Numbers discipline` in table order, printing raw output. **Do not restate values here** — that table is the single declaration.
> 2. Re-run G1 (NT by id) and G2 (`P` == N5) independently of Step 1's report.
> 3. Confirm the backup exists, passes `PRAGMA integrity_check`, and its `MAX(id)` equals the **pre-ingest** baselines — the restore point is only real if it is verified.
> 4. Confirm **no classification ran**: `get_unclassified_entries()` returns a 25-id list and `lesson_proposals` is unchanged.
> 5. `git show --stat <this step's commit>` — assert only the declared deposits changed.

## Drafting Cycle

**Walk 0 (context pin):** register `lessons-forge/knowledge/research/walk-register-cycle-ingest-consolidation-batch-2026-08-19.md`. Clone-diff against 423 run BEFORE lens 1; seven inherited facts re-measured, **five false, one still true, one unchanged doctrine pin**. Batch **25** verified two ways · dry run `25/0/288` · `E0` 345 · `P0` 353 · non-terminal set unchanged · em-dash regime inverted · new backtick hazard. **Direction verdict pending walk 1.**
