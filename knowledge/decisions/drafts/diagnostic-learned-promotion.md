# lessons-forge — diagnostic: which LESSONS.md entries are ENFORCED? Establish the `learned` promotion set under the CEO's completion definition

**Date:** 2026-08-23 | **Project:** lessons-forge | **Tier:** Medium | **Dispatch Mode:** bellows | **cycle_tier:** T1 | **Test Scope:** none (read-only diagnostic) | **Execution:** Step 1 (READ-ONLY DIAGNOSTIC) | **Priority:** 1

**auto_close:** false
**pause_for_verdict:** after_step_1

**Depends on:** `governance/knowledge/decisions/Done/executable-502.md` (which applied the annotation this plan re-grades) and `lessons-forge/knowledge/decisions/Done/diagnostic-501.md` (the mapping and the persisted detector).

## The CEO ruling this plan implements

**`learned` denotes COMPLETION — the lesson is functioning as intended within the system. `codified` is a distinct, lesser state: the rule is written into its target artifact but nothing enforces it.** Three states now: `pending` (nothing done) → `codified` (written down) → `learned` (enforced).

⚠️ **Measured consequence, and the reason this plan exists: NOT ONE of the 239 entries currently marked `learned` meets that bar.** All 239 route to prose — 148 to `PLANNER_TEMPLATE.md`, 87 to `DRAFTING_CYCLE.md`, 4 to three other documents — and **zero** to anything that executes. A rule living in a 411 KB document has no mechanism that makes it fire.

**The evidence is this session's own record.** Three entries marked `learned` were violated repeatedly by the Planner while producing the plan that marked them: the fold-sweep lesson (violated six times in one cycle), the probe-must-match-representation lesson (seven times), and the `grep -c` counts-lines lesson (which nearly caused a correct cold-panel finding to be discarded). Written down did not mean enforced, and the label said it did.

## What this plan is for

A companion executable will re-label all 239 `learned` → `codified`. That correction is already evidenced and needs no diagnostic. **This plan runs FIRST so that `learned` is not an empty category when the re-label lands** — it establishes which entries genuinely earn it.

## The method — MECHANISM-FIRST, and the direction is load-bearing

⚠️ **Enumerate the ENFORCEMENT SURFACE and map DOWN to lessons. Do NOT scan 327 lessons looking for mechanisms.** Measured at walk 0: the surface is ~36 primary units (11 gates in `gates.py`, 18 lettered `plan_lint` checks, 7 checker scripts) plus two hook scripts and the `lessons-forge` test file's 58 tests. Every enforced lesson has a mechanism BY DEFINITION, so a mechanism-first sweep cannot miss one; a lesson-first sweep over 327 entries can, and costs an order of magnitude more.

⚠️ **The provenance trail is nearly absent and you must not assume it.** Measured at walk 0: only **3** distinct proposal/entry ids are cited across the whole enforcement surface, and `plan_lint.py`, `propagation_check.py` and `cycle_check.py` cite **none**. The mapping is a reading task, not a grep.

## ⚠️ The bar for `learned` — DEMONSTRATE THE FIRE

**A lesson is `learned` only if you can produce a violating input and SHOW the mechanism rejecting it.** "A check exists" is not the bar. "The check's name resembles the lesson" is not the bar. **Construct the violation, run the mechanism, paste the failure.** This is the same discipline as writing a regression guard before the fix and watching it go red: a guard only ever observed passing is not evidence it would catch anything.

Report each candidate as **DEMONSTRATED** (violation constructed, mechanism observed rejecting it) or **ASSERTED** (mechanism read, fire not exercised). ⚠️ **Only DEMONSTRATED entries may be recommended for promotion.** An ASSERTED list is still valuable — it is the next plan's work — but it must be reported separately and never merged into the promotion set.

## Drafting Cycle

*(to be completed — this draft is walk 0)*

## MUST-PRESERVE

- **READ-ONLY.** No edit to `LESSONS.md`. No write to any `.db`. No re-label — that is the companion executable's job, and this plan must not pre-empt it.
- ⚠️ **Demonstrations are SCRATCH-ONLY.** To show a mechanism firing you will construct violating inputs. **Never place a plan-shaped file (`executable-*.md`, `diagnostic-*.md`) under a real `knowledge/decisions/` directory** — the bellows daemon claims AND DISPATCHES it within one second; this has happened live. Build violating specimens under your own scratch directory and run the checkers against those paths.
- ⚠️ **Corpus reads via `file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?immutable=1`** — `immutable=1`, NOT `mode=ro`: the corpus is in WAL mode, and `mode=ro` both fails against a copy with no `-shm` sidecar and touches the live `-shm` mtime. 21 stale `pre-*.db` snapshots sit beside it answering fluently and wrong; assert `lesson_entries` = 370 before trusting any read.
- ⚠️ **`LESSONS.md` is in the governance ROOT repo** — `/Users/marklehn/Developer/GitHub/LESSONS.md` — and is now ANNOTATED. Entries carry `[status: learned|pending]`; 14 are deliberately bare pending a CEO ruling.
- **`grep` here is ugrep: `-F` for every literal search.** ⚠️ A zero-match `grep -c` prints `0` and EXITS 1 — read the printed count, never the exit status. An unescaped bracketed pattern run without `-F` is a character class.
- **Do not "fix" any mechanism you find broken.** A check that does not fire when it should is a FINDING and a candidate lesson of its own — report it, never repair it here.

## STEP 1 — READ-ONLY DIAGNOSTIC

**Role:** DEV (read-only audit). Contract: `/Users/marklehn/Developer/GitHub/READONLY_AUDIT_CONTRACT.md`.

**Contract parameters.** `cwd`: your bellows worktree under `lessons-forge/.bellows-worktrees/<id>/`. `deposit_paths`: the two files in Deposits. `extra_forbidden`: any write to `LESSONS.md`, to any `.db`, or to any real `knowledge/decisions/` directory. `extra_preflight`: assert the corpus identity (path, byte size, `lesson_entries` = 370). ⚠️ **`C7` REPO SET, pinned explicitly because the contract HALTs on an unnamed set:** `/Users/marklehn/Developer/GitHub` (root), `/Users/marklehn/Developer/GitHub/lessons-forge`, `/Users/marklehn/Developer/GitHub/bellows`, `/Users/marklehn/Developer/GitHub/forge`.

**Q1 — Inventory the enforcement surface.** Enumerate every mechanism that can FAIL on a violation: the gates in `bellows/gates.py`, the lettered checks in `bellows/scripts/plan_lint.py`, the checker scripts in `bellows/scripts/`, the hooks under `bellows/hooks/`, and the tests in `lessons-forge/src/test_lessons_forge.py`. ⚠️ **Bellows' own test suite is ~811 tests and is OUT OF SCOPE as a whole** — include a bellows test only where it demonstrably guards a LESSON rather than general code behaviour, and say how you decided. Report the inventory with a one-line statement per mechanism of **what rule it enforces**.

**Q2 — Map mechanisms to `LESSONS.md` entries.** For each mechanism, find the entry stating the rule it enforces, if any. ⚠️ **Report the mechanisms that map to NO entry — that set is as interesting as the mapping**: it is enforcement the corpus never captured, and it may mean the lesson was learned without ever being written.

**Q3 — DEMONSTRATE THE FIRE for every candidate.** Per the bar above: construct a violating input in scratch, run the mechanism, paste the raw rejection. Classify each candidate **DEMONSTRATED** or **ASSERTED**. ⚠️ **A mechanism that does NOT reject its violation is the most valuable result in this plan** — it means a lesson believed enforced is not. Report those first and separately.

**Q4 — Emit the promotion set.** Deposit `knowledge/research/learned-promotion-2026-08-23.tsv`: one row per DEMONSTRATED entry, columns `entry_heading`, `mechanism`, `mechanism_file`, `violation_used`, `observed_rejection`. This is the companion executable's input, so it must be data, not prose.

**Q5 — Size the three states.** Given the promotion set, state the resulting counts for `learned`, `codified` and `pending`, and reconcile them to 327. ⚠️ Assert the arithmetic; do not transcribe a figure from this plan.

**Q6 — Propose the convention that makes this mechanical next time.** Walk 0 measured only 3 lesson-id citations across the entire enforcement surface, so "is this lesson enforced?" is today a reading task. Propose the durable fix — how a mechanism should record which entry it enforces — and state what it would cost to backfill. ⚠️ **Argue whether the citation belongs in the CODE or in the corpus**, rather than assuming.

**Findings document:** Q1–Q6, each answered with command output or `file:line`. Close with `## What could not be measured`, `## Open forks`, and `## Recommended executables`.

**Scope:**
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/research/learned-promotion-2026-08-23.md`
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/research/learned-promotion-2026-08-23.tsv`

**Deposits:**
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/research/learned-promotion-2026-08-23.md`
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/research/learned-promotion-2026-08-23.tsv`

**Commit:** ⚠️ **WORKTREE DISCIPLINE.** You are dispatched into `lessons-forge/.bellows-worktrees/<id>/`. Write both deposits at the SAME relative paths under YOUR cwd and commit them there in one commit: `git -C <your-worktree> add knowledge/research/<both> && git -C <your-worktree> commit -m "..."`. ⚠️ Do NOT write to the main checkout — `gates._resolve_deposit_path` falls back to "path as-is" and `_check_deposit_uncommitted` swallows the out-of-worktree git error, so writing to the wrong checkout passes both gates SILENTLY and the teardown-merge never picks your files up. Absolute for everything you READ, relative-to-cwd for everything you WRITE.
