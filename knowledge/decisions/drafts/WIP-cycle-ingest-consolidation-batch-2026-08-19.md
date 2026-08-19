# Lessons Forge — Cycle Run 2026-08-19, PLAN A: ingest the consolidation batch — `N1` entries, 25 as measured at walk 0 (classification held to Plan B)

**Date:** 2026-08-19 | **Tier:** Small | **Dispatch Mode:** bellows | **Test Scope:** targeted | **Execution:** Step 1 (Lessons Agent — ingest the batch) → Step 2 (QA) | **qa_steps:** 2 | **pause_for_verdict:** always
**cycle_tier:** T1 — T-8 (clone of `executable-423`). No T-4: read-mostly, single INSERT-only ingest, dry-run rehearsable against a scratch DB copy.
**Slug:** `cycle-ingest-consolidation-batch-2026-08-19`
**Project:** lessons-forge
**Author:** Planner
**dispatch_mode:** bellows
**Priority:** 1

## CEO Context

**Ingest only.** This plan takes the **`N1`** un-ingested `LESSONS.md` entries into the corpus and stops. **It creates no proposals, writes no report, and classifies nothing.** Classification and the report are **Plan B**; Gate-1 routing is a third plan after that.

⚠️ **Why the split matters more here than it did at 423.** Five of the `N1` entries were written by the Planner **today**, and they are the evidence base for changes to `DRAFTING_CYCLE.md` and `PLANNER_TEMPLATE.md` that the Planner authored, evidenced, and benefits from — including the retirement of PT v4.89's project-bin arm. **The corpus path exists so a NON-AUTHOR routes them at Gate 1.** That is the entire reason this plan exists instead of a direct doctrine edit, and a multi-entry batch containing the author's own proposals is the strongest case yet for keeping ingest, classification and routing in three separate plans.

**Clone lineage — measured, not recalled:** … → 411 → **423** (direct origin AND newest same-class cycle plan; `Done/executable-423.md`, closed 2026-08-14). Verified by listing `lessons-forge/knowledge/decisions/Done/` by ship date: 427 and 428 are newer but are a QA-corrective and a Gate-1 routing write, not cycle runs.

### ⚠️⚠️ INHERITED FACTS FROM 423 THAT ARE FALSE HERE — every one re-measured 2026-08-19

1. **THE BATCH IS `N1`, NOT 1** — see the Numbers table for the measured value. Verified two independent ways at walk 0: a real `ingest_lesson_entries` dry run against a `cp`-made scratch DB, and a content-hash set difference against the live corpus, which agreed exactly.
2. ⚠️ **THE EM-DASH REGIME IS INVERTED.** 423 recorded *0 of 1* headings carrying ` — `, so duplicate detection rested **entirely** on the fallback path. Here **10 of `N1`** carry it — the primary path runs for 10 and the fallback for 15. **423's "rests entirely on the fallback" note is FALSE here and must not be carried.**
3. ⚠️ **A NEW HOSTILE CHARACTER CLASS 423 NEVER FACED: a BACKTICK inside a heading.** Measured: 1 double quote (423's hazard), **4 apostrophes**, and **1 backtick** — and the backtick entry carries both: `` 2026-08-18: `plan_lint`'s dryness check disagrees with §2's bar… ``. Any shell-interpolated probe over that heading must use `grep -F` with single-quoted patterns; a double-quoted shell string would command-substitute the backticks.
4. **BASELINES MOVED:** `E0 = 345` (423: 344), `P0 = 353` (423: 352).
5. ⚠️⚠️ **THE SENTINEL WAS MIS-SPECIFIED AT WALK 0 AND IS CORRECTED HERE.** Walk 0 pinned the **last parsed REGISTER entry** — which is a **batch entry with ZERO corpus rows**, so it could not act as a canary for pre-existing data at all: pre-ingest there is nothing to match it against, and G5 would have verified nothing. **423's sentinel was an already-INGESTED row** (its entry 344), and that is the whole point of the check.
   **The true sentinel is corpus entry 345** — `2026-08-14: A residual "everything else" bucket silently absorbs the class that deserved its own bin [tag: governance-design]`, content-hash `8df4331b1596f12d5498437984ea2dd7ac63959c887a178fc69eda46ed9de962`. *(Pleasingly, it is the very entry 423 ingested — the sentinel chain is continuous.)* ⚠️ **Its heading contains a DOUBLE QUOTE** — 423's own hazard class — so every probe over it uses `grep -F` with a single-quoted pattern, and in `sqlite3` the literal must be single-quoted. *(w5-1.)*
6. **STILL TRUE, verified not assumed — the non-terminal proposal set is UNCHANGED at exactly `{340, 342, 346, 350, 352}`.** 423's G1 value guard carries as written. ⚠️ Recorded explicitly *because* it is the one inherited fact that survived; an unverified carry-forward is what the clone-diff exists to catch.
7. ⚠️⚠️ **423's CRITERION-1 REASONING IS FALSE ON BOTH OPERANDS HERE — the conclusion survives, the reason does not, and the difference is a live hazard.** 423 recorded criterion 1 as *"doubly unfalsifiable"* because (a) `PLANNER_TEMPLATE.md` carries **0** `**Tag:**` lines and (b) the batch entry's `tags` column was **NULL**. Measured 2026-08-19: **(a) is false — PT carries 1 `**Tag:**` occurrence** (line 1967), and **(b) is false for every entry — all `N1` carry tags.** Criterion 1 is nonetheless inert, for a **third reason neither plan stated**: `_TAG_LINE_RE.match(line.strip())` anchors at line start, and PT's occurrence is **mid-line prose** inside step 7's description of the house format — so `ref_tag_sets` builds **empty**. ⚠️ **This is now a ONE-operand guard, not a two-operand one.** A single line-initial `**Tag:**` ever added to `PLANNER_TEMPLATE.md` turns criterion 1 live against every tagged entry at once. **G-DUP therefore ASSERTS `ref_tag_sets` is empty at run time rather than inheriting it.**
8. **DOCTRINE PIN UNCHANGED:** `DRAFTING_CYCLE.md` is still **v2.11**, sha `acce7ebe6fa4f145bd7440485e45a0e66b650a1e`.

## Numbers discipline

⚠️ **This table is the ONLY place a quantity is declared** (honing-notes P-5). Every other section references a symbol.

⚠️⚠️ **`N1`, `N4` and `N7` are ABSOLUTES ON PURPOSE — do not "fix" them into deltas.** The register legitimately grows at every session wrap, and on a *write* plan that would make an absolute a false-halt bug (plan 451 spent two walks removing exactly these). **An ingest is the opposite case.** The fingerprint pin and the entire pre-ingest duplicate audit were computed over one specific set of `N1` headings; a register that has grown means the evidence no longer covers what would be ingested. **A mismatch here is the world moving on correctly and the batch needing re-measurement — a re-scope signal, not a defect and not a bug in the pin.** *(w3-3: stated because a later walk reading `N1` as a stale absolute would delete the guard and call it a fix.)*

| id | pin | before | after | probe |
|---|---|---|---|---|
| N1 | **`N1`** batch size | — | **25** | dry run `inserted`, cross-checked by content-hash set difference |
| N2 | corpus entries `E0` | **345** | `E0` + `N1` = **370** | `select count(*) from lesson_entries` |
| N3 | `would_update` | — | **0** | ⚠️ **the invariant. Non-zero → HALT**: an ingested row's body changed |
| N4 | unchanged | — | **288** | dry run `unchanged` |
| N5 | proposals `P0` | **353** | **353 — UNCHANGED** | this plan classifies nothing; any growth is a scope breach |
| N6 | non-terminal set | `{340,342,346,350,352}` | identical | G1 value guard, keyed by id |
| N7 | parser total | **313** | 313 | `parse_lessons_md` on the register |

## Scope

**One MUTATED artifact — the corpus — plus the backup and the four declared deposits. Six files are written in total; the authorized-writes list in §HALT ROUTING is the single declaration and this section does not restate it.** *(w4-1: this read "write to exactly one artifact", which contradicted both Deposits blocks and the authorized-writes line. An agent following it literally would skip its deposits and fail `deposit_exists`.)*

The corpus is `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db` (1,507,328 bytes at walk 0). ⚠️ **Three look-alike paths, all measured 2026-08-19 — the distinction matters and the plan previously blurred it:** `lessons-forge/forge.db` and `lessons-forge/lessons.db` are **0-byte decoys** that answer every query with a false absence; **`forge/forge.db` is a REAL, DIFFERENT, 61.6 MB database** belonging to another project — opening it is not a false absence but a wrong answer from real data. Never open either kind. *(w4-2.)* Do **not** classify, do **not** create proposals, do **not** write a cycle report, do **not** touch `LESSONS.md`, `PLANNER_TEMPLATE.md` or `DRAFTING_CYCLE.md`.

## HALT ROUTING

Any measured value outside its stated expectation → **HALT**, quoting every measured input. **Never repair forward.** On any HALT: commit existing deposit files by explicit pathspec and record the gate, its measured value, and **whether the ingest committed** — that last fact is what a resume needs and what a lost session destroys.

**Authorized writes, and nothing else:** the `.backup`, the single `ingest_lesson_entries` call **and its `conn.commit()`**, and this step's deposits.

## STEP 1 — Lessons Agent: ingest the batch (NO classification anywhere in this plan)

> **FIRST — post a short visible chat message (1–2 sentences).** Do NOT rename the plan file.
>
> You are the Forge Lessons Agent. Read `agents/FORGE_LESSONS_AGENT.md` first. ⚠️ **Its DB paths are relative and you run in a worktree** — every canonical-DB access uses the ABSOLUTE path `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db`. **`forge/forge.db` is a REAL but DIFFERENT database — never open it**; sibling `lessons.db` is a 0-byte decoy that returns false absences.
>
> ⚠️ **NO CLASSIFICATION.** `get_unclassified_entries()` returning an `N1`-id work list is this plan's **CORRECT closing state**, not an omission. Proposals must remain at `P0` — see N5.
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
> **Baseline capture (read-only, raw output):** (1) the zero-emitting distribution over ALL EIGHT statuses — **RECORD it raw; do NOT gate on the individual counts.** ⚠️ **These are absolutes that a legitimate Gate-1 routing would move, and unlike `N1` a moved proposal status does NOT invalidate this batch** — the ingest is over `lesson_entries`, not proposals, so a re-routed proposal is orthogonal and gating on it would be a pure false halt. **Gate only on the SUM equalling `N5`**, which is what actually protects the scope boundary. Walk-0 reading, for comparison not for matching: `implemented 282 · superseded 28 · reference 20 · rejected 15 · accepted 5 · stale 3 · proposed 0 · ambiguous 0`. *(w4-3.)* (2) proposals by category; (3) `E0`; (4) sentinel hash; (5) `STALE_COUNT`; (5b) `SURFACEABLE_BASE` ⚠️ **labelled distinctly from NT**; (5c) **`UNCLASSIFIED_BASE`** = `len(get_unclassified_entries(conn))`, captured pre-ingest — **0** at walk 6; Step 2 item 4's expectation is computed from it, never hard-coded *(w6-3)*; (6) `P0`; (7) **NT captured BY ID, not by count** — `SELECT 'NT='||GROUP_CONCAT(id) FROM (SELECT id FROM lesson_proposals WHERE status IN ('proposed','accepted','ambiguous') ORDER BY id);` → **a printed token is required; silence = broken invocation → HALT**; (8) FORWARD baseline `grep -c "^| "`, raw. **Capture only — the gates own the verdicts.**
>
> ### Step 1a-ter — commit the before-anchor BEFORE the ingest
> Write and `git commit` the dev-log stub: `Status: Partial — in flight (pre-ingest stub)`; the absolute backup path; `E0`/`P0`; **the NT id-list line**; STALE; SURFACEABLE; the FORWARD baseline; the full distribution; the sentinel hash; the doctrine pins raw — **HALT unless all print.** The final Receipt rewrites this file but carries any first-dispatch ingest dict forward **verbatim**.
>
> ### Step 1a-bis — pre-ingest guard (READ-ONLY, against a scratch copy)
> 1. `parse_lessons_md("/Users/marklehn/Developer/GitHub/LESSONS.md")` → assert **N7**. Dry-run `ingest_lesson_entries` against a **FRESH `cp`-made scratch DB**, never the live file.
> **Make a fresh `cp` for every dry run, assert the copy's count equals `E0` before using it, and never hand the live DB to a call described as dry.**
> ⚠️ **CORRECTION to w1-6, which stated a FALSE reason for this guard.** Walk 1 claimed `ingest_lesson_entries` "contains a `conn.commit()`" so rollback could not be trusted. **That was wrong.** Traced at walk 3: **all three `conn.commit()` occurrences in `lessons_forge.py` (:127, :212, :436) are DOCSTRING SENTENCES saying the function does NOT commit.** My walk-1 probe was `'conn.commit()' in source` — it matched prose. The function genuinely leaves the transaction to the caller, and the rollback that worked did so correctly, not by luck. **The guard stays** — a fresh copy is cheap and removes a whole class of resume ambiguity — **but it is defence-in-depth, not a fix for a commit that does not exist.** *(w3-1. Same probe-vs-representation trap this plan criticises 423 for in inherited-fact 7, committed by its own author one walk later.)* **FRESH → assert `inserted == N1` AND `updated == N3`.** **RESUME → `updated == N3` and `inserted ∈ {0, N1}`.**
> ✅ **Unlike 423, a multi-entry batch HAS intermediate values** — any `inserted` strictly between 0 and `N1` is positive evidence of a foreign writer and is a HALT, not an ambiguity. 423 could not make this check because its batch was 1.
> 1b. **BATCH FINGERPRINT** — sha256 of `"\n".join(<would-insert headings in parse order>)` == **`4484828a0a400696a9148b89a422cffcbd2443be1a8df81df3e06691621fd34c`**. Mismatch → HALT. **RESUME with `inserted == 0` → SKIP, record `FINGERPRINT SKIPPED (post-ingest resume)`.**
> 2. **Sentinel:** the parsed entry matching the corpus sentinel heading — **measure the match count and PRINT it**; exactly 1 match with equal hash → PASS, else HALT.
> 3. **G-DUP — the duplicate pre-check, mirrored by hand.**
> ⚠️⚠️ **DO NOT CALL `detect_duplicates` FOR BATCH ENTRIES — IT CANNOT ANSWER, AND IT ANSWERS ANYWAY.** It reads each id from `lesson_entries` and hits `if row is None: continue` (`lessons_forge.py:363–369`) for an entry not yet ingested, returning `[]` — a confident false zero on the one pre-mutation check this plan calls a HALT condition.
> Do this instead, and **assert both operands rather than inheriting them**:
> - **Criterion 1 — ASSERT `ref_tag_sets` IS EMPTY.** Build it exactly as `lessons_forge.py:339–354` does (`_TAG_LINE_RE.match(line.strip())` over `PLANNER_TEMPLATE.md`) and assert the resulting set is empty. **Non-empty → HALT**: every batch entry carries tags, so a single line-initial `**Tag:**` in PT would mark the whole batch duplicate. Measured empty at walk 0 — and note PT *does* contain one mid-line `**Tag:**` at :1967 that the anchor correctly ignores. **Inheriting 423's "0 tag lines" reason would have hidden this.**
> - **Criterion 2 — mirror it by hand.** Read `PLANNER_TEMPLATE.md` once, lowercase it, and for each batch heading compute the title the code computes: split on `_EM_DASH_SEP` (`' — '`) and take the **right** side if present, else the **whole stripped heading**; assert the lowercased title is **not** a substring. Measured: **the separator path and the fallback are BOTH exercised (counts at walk 0 in the register), so each acts as an in-batch control for the other.** 423 had no such control. Expected matches: **0**.
> - Pre-existing ids: mirror the ingest's candidate construction, PRINT the list length first (**HALT if 0 or wildly off**), then `detect_duplicates(conn, <ids>)` read-only → non-empty = HALT. *(Legitimate here: those ids ARE in the corpus.)*
>
> ### Step 1b — THE ONE MUTATION
> A single `ingest_lesson_entries` call against the live corpus by absolute path. Nothing else writes.
>
> ⚠️⚠️ **THEN `conn.commit()`. THE INGEST DOES NOT PERSIST WITHOUT IT.** `ingest_lesson_entries` leaves the transaction to the caller (`lessons_forge.py:127` — *"Does NOT call conn.commit()"*). **Measured 2026-08-19 on a scratch copy: after the call the connection reports 370 entries; after closing WITHOUT a commit, a fresh connection reports 345.** Without this line the step runs, reports a full `inserted` count, and **changes nothing.**
>
> ⚠️ **Verify the post-conditions on a FRESH CONNECTION, not the writing one.** A read on the writing connection sees the uncommitted transaction and returns the expected values whether or not the commit happened — so same-connection verification can pass on a corpus that was never changed. Close, reopen read-only by absolute path, then assert.
> *(w7-1. Lineage worth recording: w1-6 wrongly claimed the function commits; w3-1 correctly disproved that — and **removed a false belief without installing the true requirement.** The commit obligation this creates went unstated for four walks. A correction can open a gap.)*
>
> **Post-conditions, all measured on the reopened connection:** `inserted` == **N1**, `updated` == **N3**, `unchanged` == **N4** (from the returned dict), and `E` == **N2**.
>
> ### Gates G1–G7 (post-mutation, read-only)
> ⚠️ **G1 and G2 are NOT independent of the mutation, and are safe here only because `N3` is 0.** Traced at walk 3: `ingest_lesson_entries` marks proposals `stale` and flags terminal-status proposals **only inside its UPDATE branch** (`lessons_forge.py:160–194`), and the stale UPDATE explicitly excludes terminal statuses — so it targets exactly the non-terminal set G1 pins. **With `updated == 0` no proposal status can change; if an update ever occurs, G1 failing is the CORRECT behaviour, not corruption.** Read a G1 failure alongside `N3` before treating it as damage. *(w3-2.)*
>
> **G1 — NT UNCHANGED, by id:** re-run the NT query; the id list must equal **N6** exactly. A count match with a different id set is a FAIL.
> **G2 — proposals unchanged:** `P` == **N5**. Any growth means classification ran → HALT, this plan's hardest scope boundary.
> **G3 — corpus count:** `E` == **N2**.
> **G4 — `updated` was 0:** re-assert `updated == N3` from the returned dict. ⚠️ **This clause previously added "and confirm no pre-existing `content_hash` changed", which had NO probe** — the baseline captures no hash manifest, so it was unverifiable as written. It is also **redundant once traced**: the only write path to an existing row's `content_hash` is the UPDATE branch at `lessons_forge.py:160–168`, and that branch increments `updated`. **`updated == 0` IS the guarantee**, not a proxy for it. *(w5-2.)*
> **G5 — sentinel intact:** corpus entry **345**'s `content_hash` still equals `8df4331b…` post-ingest. This is the canary that the ingest touched no pre-existing row; it is meaningful **only** because the sentinel is an already-ingested entry (see inherited-fact 5).
> **G6 — `stale_proposals_marked` and `terminal_proposals_flagged` recorded raw** (measured 0 and `[]` at authoring; a non-empty flag list is information, not necessarily a fault — record and report, do not silently pass).
> **G7 — FORWARD unchanged** against the baseline.
>
> ### Deposit
> Write both deposits, `git add` **by explicit pathspec**, commit. **Do not `git add -A`.** ⚠️ **Commit the deposits in this step** — a declared deposit that is never committed fails `deposit_uncommitted`, exactly as plan 451 did.

## STEP 2 — QA

> **QA SELF-CHECK — Rule 20.** Post the block from `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md` verbatim under the banner `Rule 20 — QA Self-Check Results`, and close with the literal line `PASSED — SELF-CHECK PASSED`. ⚠️ **Both strings are matched literally by `plan_lint` (c)** — paraphrasing either FAILs the gate. *(w2-2.)*
>
> Verification only. **Evidence must be RAW command output pasted verbatim — never a summary, never a claim that a check passed.**
>
> **Deposits:**
> - `knowledge/development/qa-cycle-ingest-consolidation-2026-08-19.md`
> - `knowledge/development/qa-evidence-cycle-ingest-2026-08-19.txt`
>
> ⚠️ The `.txt` is required for `qa_test_result`. ⚠️ **The bullet-list form is load-bearing** — `plan_lint` parses paths from bullets; an inline `**Deposits:** \`a\` and \`b\`` yields **zero** paths and FAILs `(b)`. *(w2-1: I re-introduced plan 451's S1-3(b) defect in a different shape one step after citing it.)*
>
> 1. Re-run every pin in `## Numbers discipline` in table order, printing raw output. **Do not restate values here** — that table is the single declaration.
> 2. Re-run G1 (NT by id) and G2 (`P` == N5) independently of Step 1's report.
> 3. Confirm the backup exists, passes `PRAGMA integrity_check`, and its `MAX(id)` equals the **pre-ingest** baselines — the restore point is only real if it is verified.
> 4. Confirm **no classification ran**: `lesson_proposals` unchanged (`P` == `N5`), and `get_unclassified_entries()` returns **`UNCLASSIFIED_BASE` + `N1`** ids.
> ⚠️ **`get_unclassified_entries()` is NOT scoped to this batch** — it returns every corpus entry lacking a non-stale proposal. A bare `N1` expectation is right only while the pre-existing unclassified count is zero, which this plan must **measure, not assume**. Measured at walk 6: **`UNCLASSIFIED_BASE` = 0**, so the expectation is 25 today — but capture it at baseline (Step 1a) and compute the expectation from it. *(w6-3: the same shape as inherited-fact 7 — a correct conclusion resting on an unstated, unverified operand.)*
> 5. `git show --stat <this step's commit>` — assert only the declared deposits changed.

## Drafting Cycle

- Weak spots — steps authored from 423's machinery; `detect_duplicates` proven unable to answer pre-mutation (w1-2, w1-4).
- Destruction — one INSERT-only mutation behind a verified restore point; scope boundary (no classification) guarded by G2, not asserted in prose.
- Vulnerabilities — backtick/apostrophe headings, ugrep exit-1, the `?immutable=1` backup trap, `.db`-scoped resume glob (w1-3).
- Integration — 423's criterion-1 reasoning false on both operands (w1-1); plan 451's `.txt` deposit lesson folded (w1-5).
- ACID — the dry-run/commit claim of w1-6 was **DISPROVED at w3-1** (all three `conn.commit()` hits are docstrings saying it does NOT commit); the fresh-copy guard is retained as defence-in-depth. G1/G2 are safe only because `N3` is 0 (w3-2). `N1`/`N4`/`N7` are absolutes on purpose (w3-3); the proposal distribution is not (w4-3).

**Walk 0 (context pin):** register `lessons-forge/knowledge/research/walk-register-cycle-ingest-consolidation-batch-2026-08-19.md`. Clone-diff against 423 run BEFORE lens 1; seven inherited facts re-measured, **five false, one still true, one unchanged doctrine pin**. Batch **25** verified two ways · dry run `25/0/288` · `E0` 345 · `P0` 353 · non-terminal set unchanged · em-dash regime inverted · new backtick hazard. **Direction verdict at walk 1: PROCEED.** Walks 1–6 folded 22 findings; see the register.
