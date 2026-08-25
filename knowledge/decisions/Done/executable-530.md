# Lessons Forge — Cycle Run 2026-08-25, PLAN B: classify the 32-entry ingest batch and deposit the report (Gate-1 routing held to a NON-AUTHOR — and a 25-proposal Gate-1 BACKLOG from 2026-08-19 is surfaced, not touched)

**Date:** 2026-08-25 | **Tier:** Small | **Dispatch Mode:** bellows | **Test Scope:** targeted | **Execution:** Step 1 (Lessons Agent — classify) → Step 2 (DEV — report) → Step 3 (QA) | **qa_steps:** 3 | **pause_for_verdict:** always
**cycle_tier:** T1 — clone of `Done/executable-459.md` (the direct origin; its own lineage 423→425→427→428 and its halt-autopsy inherited below).
**Project:** lessons-forge
**Priority:** 1

## CEO Context

**Classify only.** This plan classifies the **`W`** unclassified entries that plan **529** ingested, and deposits the cycle report. **It routes nothing.** Every proposal it creates leaves `route` **NULL** and `status` **`proposed`**; Gate-1 routing belongs to a NON-AUTHOR (the 459 law, verbatim: *the classifier may propose; only Gate 1 may accept, and Gate 1 is not the Planner*).

⚠️⚠️ **THE AUTHOR-CONFLICT IS STRUCTURAL FOR THIS BATCH.** Every register entry is written by Planner sessions at wraps; four entries are dated **2026-08-25** — the classifying Planner's own same-day lessons, including two arguing for practices this very session shipped and benefits from (the instruction→tool convergence; resurrect-with-hardening). The deterministic marker window is `entry_date = '2026-08-25'` (M7=4, the 459 date-keyed rule); the broader structural conflict is stated here once for Gate 1's reading, not re-litigated per entry.

⚠️⚠️ **MEASURED AT AUTHORING AND NEW SINCE 459: GATE 1 NEVER RAN ON THE PREVIOUS CYCLE.** The 08-19 batch's 25 proposals (ids **354–378**) all still sit `proposed` with `route` NULL. This plan does NOT touch them (M6 guards that) — but the report (Step 2's generator output) will show them, and the CEO should know Plan C's queue is now **25 + K**, all awaiting a non-author.

### ⚠️⚠️ WHY THE CLONE ORIGIN'S ORIGIN HALTED — inherited from 459, re-stated
1. ⛔ **THE WORKTREE ABSOLUTE-PATH TRAP (killed 425):** `output_dir` anchored at the MAIN repo writes outside the sandbox and strands teardown. **The fix is `"$(pwd)/reports"` — absolute WITHIN the sandbox.** Step 2 carries the full apparatus.
2. **`insert_proposal` DOES NOT COMMIT** — one commit after all inserts; post-conditions on a FRESH read-only connection (a read on the writing connection cannot distinguish committed from uncommitted).
3. **The reports directory is destructible** — sha-pinned before/after; recovery is `git checkout --`, all pinned reports are tracked.
4. **The classify-inversion is the definitive proof:** after classification `get_unclassified_entries()` == `[]`.
5. **Cluster apparatus:** deliberately omitted again (459's recorded omission stands); this batch's relatedness (ten 08-24 E-family entries; four 08-25) is Gate-1 reading material via the DISPOSITION lines, not classifier machinery.

## Numbers discipline

⚠️ **This table is the ONLY place a quantity is declared.** Every other section references a symbol. All values measured 2026-08-25 by the Planner read-only against the live DB post-529; the agent re-measures each in pre-flight; mismatch → HALT with measured vs expected.

| id | pin | before | after | probe |
|---|---|---|---|---|
| M1 | **`W`** work list | **32** (ids 371–402, contiguous) | **0** | `len(get_unclassified_entries(conn))` — the inversion, on a FRESH connection |
| M2 | **`P0`** proposals | **378** | `P0` + `K`; **`K` ≥ `W` derivable, K UNPINNED** (record-only — pinning K forces fabrication) | `SELECT COUNT(*) FROM lesson_proposals` |
| M3 | route on every NEW proposal | — | **NULL, every one** | `SELECT COUNT(*) FROM lesson_proposals WHERE id > 378 AND route IS NOT NULL` → **0** (bind the P0 bound from pre-flight, never hard-code beyond this authoring pin) |
| M4 | status on every NEW proposal | — | every one is `proposed` | `SELECT COUNT(*) FROM lesson_proposals WHERE id > 378 AND status <> 'proposed'` → **0** |
| M5 | **`E0`** corpus entries | **402** | **402 — UNCHANGED** | this plan classifies; it must not ingest |
| M6 | pre-existing non-terminal set | **30 ids: {340,342,346,350,352} ∪ {354..378}** (the un-routed 08-19 backlog) | **still present, byte-untouched** — their status/route must not move | the full `(id, status, route)` triple-set for ids <= 378 with non-terminal status, captured pre-flight and re-selected post — SET-IDENTICAL, not merely count-equal (a count cannot see a status or route moving between values) |
| M7 | `[AUTHOR-CONFLICT]` markers | — | **one per proposal derived from an entry with `entry_date='2026-08-25'`** → **4** distinct entry_ids | parameter-bound COUNT over the new-proposal band's reasoning LIKE '%[AUTHOR-CONFLICT]%'; the date is the defining property, never an id range |
| M8 | the five destructible reports | `08-12` 7,299 B `b76e3ddd588e7be0…` · `08-13` 12,212 B `7cfd7904c8491976…` · `08-14` 7,256 B `f1807cf266b36954…` · `08-15` 2,593 B `b21281169ac1a138…` · `08-19` 21,895 B `7f9b283bf42a31eb…` | **all five byte-identical** | `shasum -a 256` with the same worktree-anchored prefix the generator uses; recovery on a fired post-check: `git -C "$(pwd)" checkout -- reports/<file>` — all five tracked, no backup copies made |
| M9 | today's report | **ABSENT** | **exists, and is none of M8** | `ls "$(pwd)/reports/lessons-report-2026-08-25.md"` — worktree-anchored |
| M10 | **sentinel** — corpus entry **370** (the last pre-batch entry) | `76b1b344208b36f9…` | **unchanged** | classification writes only `lesson_proposals` |
| M11 | `STALE_COUNT` | **3** (ids 98/121/130) | **3, unchanged** | `SELECT COUNT(*) FROM lesson_proposals WHERE status='stale'` |
| M12 | `SURFACEABLE_BASE` | **25** (the backlog — NOT 0 as at 459) | **25 + `K` — RECORD-ONLY, expected to move** | `SELECT COUNT(*) FROM lesson_proposals WHERE status IN ('proposed','ambiguous')` |
| M13 | duplicates on this batch | **0** (Planner-measured: `detect_duplicates(conn, W-ids)` returned 0 matches) | **0 new `category='duplicate'` proposals** | the classifier does not run detect_duplicates; the pin records the cycle's deterministic half is a no-op for this batch |

## STEP 1 — Lessons Agent: classify the `W` entries (no report, no routing)

> **FIRST — post a short visible chat message (1–2 sentences).** Do NOT rename the plan file.
>
> You are the Forge Lessons Agent. Read `agents/FORGE_LESSONS_AGENT.md` first. ⚠️ **Its DB paths are relative and YOU RUN IN A WORKTREE** — every canonical-DB access uses the ABSOLUTE path `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db`. **`forge/forge.db` is a REAL, DIFFERENT database — never open it**; `lessons-forge/forge.db` and `lessons-forge/lessons.db` are **0-byte decoys** returning false absences.
>
> **⚠️ NO ROUTING.** `route` stays **NULL** at insert and `status` stays at its default `proposed`. Gate 1 belongs to a non-author. **No ingest, no UPDATE, no delete — the M6 backlog (ids 354–378) especially is READ-NEVER-WRITE.**
>
> **Env facts:** ⚠️ **the interactive grep shim is BROKEN on this machine — EVERY `grep` invocation errors `unknown option '-G'`, all forms. Use `/usr/bin/grep` for every grep; a zero-match `/usr/bin/grep -c` prints 0 and EXITS 1 (read stdout, never `$?`).** ⚠️ **Batch headings contain backticks, apostrophes and quotes — bind every entry id and heading as a PARAMETER; never interpolate a heading into a `sqlite3` CLI string.**
>
> **Deposits:**
> - `knowledge/development/dev-log-classify-2026-08-25.md`
> - `knowledge/development/evidence-classify-2026-08-25.txt`
>
> ### Step 0 — dispatch state
> Three-place probe on this step's dev-log path (committed HEAD; working tree; `git log --all` + `branch --list 'bellows-preserved/*'`), each exit code captured; probe 3 paired with a positive control against `knowledge/FORWARD.md`. Any hit → **RESUME**; all absent → **FRESH**. State the determination first.
> **RESUME semantics (single-commit design):** work list == `W` → prior dispatch died pre-commit, proceed as FRESH and say so; work list == 0 → classification landed — do NOT re-insert; record `RESUME (classification already committed)`, re-run post-conditions read-only, deposit, stop; **work list strictly between 0 and `W` → HALT** (a single-commit design cannot produce a partial list; a subset is positive evidence of a foreign writer).
> **Single-writer check:** `get_unclassified_entries` stable across TWO reads; `ls /Users/marklehn/Developer/GitHub/lessons-forge/knowledge/decisions/in-progress-*.md` — THIS PROJECT ONLY; this plan's own file is normal, ZERO matches means the probe is broken, any OTHER match → HALT.
>
> ### Pre-flight (read-only, raw output for each)
> `get_unclassified_entries(conn)` == exactly ids 371–402 (`W`=32, contiguous) · `SELECT COUNT(*) FROM lesson_proposals WHERE entry_id IN (<the W ids, parameter-bound>)` == **0** · **M5** · **M2 before** · **M6** (capture the non-terminal `(id,status,route)` triple-set — the post-condition compares SET-IDENTITY) · **M10** · **M11** · **M12 before (25 — recorded, not gated as 0: the 459 value moved because the backlog exists)** · reports dir contains exactly the FIVE M8 artifacts and no `lessons-report-2026-08-25.md`. Any mismatch → HALT with measured vs expected.
>
> ### Classify
> For each of the `W` entries: parameter-bound `SELECT raw_content, source_heading, tags FROM lesson_entries WHERE id = ?`, then `insert_proposal` (`src/lessons_forge.py:210`) with `route=None`. ⚠️ **Its six required positionals are `conn, entry_id, category, suggested_action, reasoning, confidence` — a SEVENTH positional binds to `status`. Pass everything after `confidence` BY KEYWORD.**
> ⚠️⚠️ **DISCLOSURE MARKERS — mechanically asserted, not left to judgement.** `[AUTHOR-CONFLICT]` is DETERMINISTIC: exactly the entries dated **2026-08-25** (M7=4), no others — the broader all-entries-are-Planner-authored fact is CEO-Context's disclosure, not a per-proposal marker. `[DEDUP]` and `[REMEDY-GATED]` are CONDITIONAL — apply only where true; **their counts are recorded raw and never pinned** (pinning forces fabrication).
> **THE DISPOSITION LINE — one per entry, byte-exact prefix:**
> ```
> DISPOSITION | entry=<id> | proposal=<id> | remedy: <one clause> | markers: <those that apply, or NONE>
> ```
> `markers: NONE` is legitimate and expected. **Post-condition: `/usr/bin/grep -cF 'DISPOSITION | entry=' <dev log>` == 32.**
>
> ### THE COMMIT
> ⚠️⚠️ **`insert_proposal` DOES NOT COMMIT.** Issue exactly ONE `conn.commit()` after all `W` inserts — proven in this lineage (456): an uncommitted run reads correct inside its own transaction and vanishes on close.
>
> ### Post-conditions — ON A FRESH READ-ONLY CONNECTION
> Assert **M1** (the inversion — `[]`), **M3**, **M4**, **M5**, **M6** (triple-set identical to pre-flight), **M7**, **M10**, **M11**, **M13** (zero new duplicate-category proposals); record **M2** (`K`, asserting only `K` ≥ 32) and **M12** raw.
>
> ### Deposit
> Write both deposits, `git add` **by explicit pathspec**, commit. **Do not `git add -A`.**

## STEP 2 — DEV: generate the report

> **Step 1's Receipt status must be `Status: Complete`.** Anything else → HALT.
> **Dispatch-state probe first** (three-place, positive control). Any hit → RESUME: the report may already exist; re-verify, never regenerate over your own prior output.
> Post a short visible chat message. You are the Forge Developer.
>
> ⚠️⚠️ **THIS IS THE STEP THAT HALTED 425.** Call **`generate_lessons_report(conn, cycle_date, output_dir)`** (`src/lessons_forge.py:523`) with BOTH arguments explicit:
> - **`cycle_date="2026-08-25"`** — the PLAN's cycle date, fixed when the batch was assembled; do NOT recompute from `date`, do NOT copy from the lineage (the parents carry `2026-08-19` and older).
> - ⛔ **`output_dir`: run `pwd` FIRST and print it; pass `"$(pwd)/reports"` — absolute, anchored at the WORKTREE ROOT.** The 425 halt: an absolute path rooted at the MAIN repo writes outside the sandbox and strands teardown; the fix for CWD-relative is "absolute WITHIN the sandbox".
>
> **Destruction guard — M8 and M9 before AND after:** shasum all FIVE pinned reports pre-generation and re-assert post — same worktree-anchored prefix as the generator. Recovery if the post-check fires: `git -C "$(pwd)" checkout -- reports/<file>` — all five tracked; no backup copies.
>
> **Deposits:**
> - `knowledge/development/dev-log-report-2026-08-25.md`
> - `reports/lessons-report-2026-08-25.md`
>
> `git add` by explicit pathspec; commit in this step. ⚠️ The bullet-list Deposits form is load-bearing — `plan_lint` parses paths from bullets (the thrice-repeated personal defect recorded at 459 w1-2).

## STEP 3 — QA

> **Step 2's Receipt status must be `Status: Complete`.** Dispatch-state probe first. Post a short visible chat message. You are the Forge QA agent.
>
> Re-run, on a FRESH read-only connection with raw output into the QA evidence file: **M1** (`[]`), **M3**, **M4**, **M5** (402), **M6** (triple-set identical), **M7** (4), **M10**, **M11** (3), **M13** (0), M2/M12 recorded raw; the DISPOSITION-line count == 32 in Step 1's dev log; **M8** all five shas byte-identical; **M9** today's report exists worktree-anchored and its `## Proposals` (or equivalent) section shows the new batch AND the 25-proposal backlog — quote the backlog's rendering in the evidence (this is what routes Plan C).
> ⚠️ **Targeted tests:** `python3 -m pytest src/test_lessons_forge.py -q` from the worktree root — the forge's own suite; report the count, zero failures.
>
> **Deposits:**
> - `knowledge/qa/qa-classify-2026-08-25.md`
> - `knowledge/qa/evidence-qa-classify-2026-08-25.txt`
>
> > **QA SELF-CHECK — Rule 20.** Post the block from `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md` verbatim, under the banner **`Rule 20 — QA Self-Check Results`**, and close with **`PASSED — SELF-CHECK PASSED`** only if every check genuinely passed. ⚠️ Both literals are matched by `plan_lint` check (c) and neither may be paraphrased.
>
> `git add` by explicit pathspec; commit.

## Drafting Cycle
**Tier:** T1 computed — T-8 clone of `Done/executable-459.md` with every pin re-measured at authoring (the clone-diff is the walk-0 record).
**Walk register:** `governance/knowledge/research/walk-register-executable-forge-classify.md`
**Walks:** walk 0 = the measured clone-diff (8 numbered deltas incl. the Gate-1 backlog discovery); **walks 1–2 complete** — five lenses each; walk 1 folded 1 (M6's count→triple-set identity, the count-is-not-a-value-guard lesson), walk 2 dry across all five lenses.
**Direction verdict (after walk 1): PROCEED.** Tested, not judged.
- Weak spots:          w1 dry; w2 dry
- Destruction:         w1 dry; w2 dry
- Vulnerabilities:     w1 1 folded — instruction 1 / record 0; w2 dry
- Integration-record:  w1 dry; w2 dry — close obligations discharged at this freeze
- ACID:                w1 dry; w2 dry
**Cold panel: NOT convened, decided with reasoning** — T-8 clone of a plan that itself closed through the full lane twice-corrected (425→459); every inherited hazard carries its autopsy inline; the batch differs in size and pins, not in shape.
**Conformance (§5):** recorded at the freeze from actual runs: walk_register_lint CONFORMANT (verdict channel, branched-on); cycle_check BAR_MET post-finalization (verdict channel, branched-on); plan_lint 0 FAIL at the scratch-mirror path.
**Closing:** **walk 2 met the bar — all five lenses dry.** Instruction series **1 → 0**. Receipt BEFORE staging (structural since 527) → shop-infra hold → release under the CEO's classification directive → claim.

## Cycle Manifest
tier: T1
target: lessons-forge.db
class: shop-infra
reads: /Users/marklehn/Developer/GitHub/lessons-forge/src/lessons_forge.py, /Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db, /Users/marklehn/Developer/GitHub/lessons-forge/agents/FORGE_LESSONS_AGENT.md, /Users/marklehn/Developer/GitHub/lessons-forge/knowledge/decisions/Done/executable-459.md, /Users/marklehn/Developer/GitHub/lessons-forge/knowledge/research/forge-heading-key-migration-2026-08-25.md
writes: lessons-forge.db, knowledge/development/dev-log-classify-2026-08-25.md, knowledge/development/evidence-classify-2026-08-25.txt, knowledge/development/dev-log-report-2026-08-25.md, reports/lessons-report-2026-08-25.md, knowledge/qa/qa-classify-2026-08-25.md, knowledge/qa/evidence-qa-classify-2026-08-25.txt
open_forks: none — Gate-1 routing (the 25-backlog + K) is Plan C's, held to a non-author by standing law, surfaced not decided
walks: 2
yields: 1, 0
validation: cycle_check=BAR_MET, plan_lint=0_FAIL, fold_check=N/A
coherence: N/A

## Rule 20 — QA Self-Check Block

Step 3 is the QA step; the block is posted there per its mandate. Steps 1–2 are agent/DEV-only.
