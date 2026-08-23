# lessons-forge — diagnostic: which LESSONS.md entries are ENFORCED? Establish the `learned` promotion set under the CEO's completion definition

**Date:** 2026-08-23 | **Project:** lessons-forge | **Tier:** Medium | **Dispatch Mode:** bellows | **cycle_tier:** T1 | **Test Scope:** none (read-only diagnostic) | **Execution:** Step 1 (READ-ONLY DIAGNOSTIC) | **Priority:** 1

**auto_close:** false
**pause_for_verdict:** after_step_1

**Depends on:** `governance/knowledge/decisions/Done/executable-502.md` (which applied the annotation this plan re-grades) and `lessons-forge/knowledge/decisions/Done/diagnostic-501.md` (the mapping and the persisted detector).

## The CEO ruling this plan implements

**`learned` denotes COMPLETION — the lesson is functioning as intended within the system. `codified` is a distinct, lesser state: the rule is written into its target artifact but nothing enforces it.** Three states now: `pending` (nothing done) → `codified` (written down) → `learned` (enforced).

⚠️ **Measured consequence, and the reason this plan exists: NOT ONE of the `X` entries currently marked `learned` meets that bar.** Every one of them routes to prose — the bulk to `PLANNER_TEMPLATE.md` and `DRAFTING_CYCLE.md`, the remainder to three other documents — and **zero** to anything that executes. A rule living in a 411 KB document has no mechanism that makes it fire.

**The evidence is this session's own record.** Three entries marked `learned` were violated repeatedly by the Planner while producing the plan that marked them: the fold-sweep lesson (violated six times in one cycle), the probe-must-match-representation lesson (seven times), and the `grep -c` counts-lines lesson (which nearly caused a correct cold-panel finding to be discarded). Written down did not mean enforced, and the label said it did.

## What this plan is for

A companion executable will re-label all `X` entries `learned` → `codified`. That correction is already evidenced and needs no diagnostic. **This plan runs FIRST so that `learned` is not an empty category when the re-label lands** — it establishes which entries genuinely earn it.

## Numbers discipline

⚠️ **This table owns every quantity this plan cites. If you are about to write one of these numbers anywhere else, reference the symbol instead.** Adopted because the figures below are already restated across the plan's prose — `N` four times, `X` three — and because a plan without this table makes `propagation_check` report COULD-NOT-RUN rather than guarding anything. ⚠️ **These are the Planner's walk-0 measurements, not acceptance criteria: RE-DERIVE every one and report your own. If yours differ, yours supersede.**

| id | pin | value | probe |
|---|---|---|---|
| D0 | **`N`** — dated headings in the register | **327** | `grep -cE '^## 20[0-9][0-9]' <abs LESSONS.md>` |
| D1 | **`X`** — entries currently marked `learned`, i.e. the mislabelled set | **239** | `grep -cE '^## .*\[status: learned\]' <abs LESSONS.md>` |
| D2 | **`P`** — entries marked `pending` | **74** | `grep -cE '^## .*\[status: pending\]' <abs LESSONS.md>` |
| D3 | **`Q`** — entries left BARE, awaiting a CEO ruling | **14** | `N` − `X` − `P` |
| D4 | **`M`** — primary enforcement mechanisms (gates + lettered lint checks + checker scripts) | **36** | 11 `^def _gate_` in `gates.py` + 18 lettered checks in `plan_lint.py` + 7 real checkers in `bellows/scripts/` |
| D5 | **`C`** — lesson-id citations across the whole enforcement surface | **3** | distinct ids from `[Pp]roposal [0-9]+\|entry [0-9]+` over the enforcement files |
| D6 | **`E`** — corpus `lesson_entries` | **370** | `sqlite3 "file:<abs>?immutable=1" "SELECT COUNT(*) FROM lesson_entries"` |

**`X` is the number this arc exists to correct, and `M` versus `N` is the ratio that fixed the method.**

## The method — MECHANISM-FIRST, and the direction is load-bearing

⚠️ **Enumerate the ENFORCEMENT SURFACE and map DOWN to lessons. Do NOT scan 327 lessons looking for mechanisms.** Measured at walk 0: the surface is `M` primary units, plus the hook scripts under `bellows/hooks/` and the `lessons-forge` test file. Every enforced lesson has a mechanism BY DEFINITION, so a mechanism-first sweep cannot miss one; a lesson-first sweep over `N` entries can, and costs an order of magnitude more.

⚠️ **The provenance trail is nearly absent and you must not assume it.** Measured at walk 0: only `C` distinct proposal/entry ids are cited across the whole enforcement surface, and `plan_lint.py`, `propagation_check.py` and `cycle_check.py` cite **none**. ⚠️ **`C` is a single-digit value, and `propagation_check` deliberately skips those** (`propagation_check.py:95` — one-digit values are too common to be signal), so nothing mechanical guards its restatement. Reference the symbol by hand and do not write the numeral. The mapping is a reading task, not a grep.

## ⚠️ The bar for `learned` — DEMONSTRATE THE FIRE

**A lesson is `learned` only if you can produce a violating input and SHOW the mechanism rejecting it.** "A check exists" is not the bar. "The check's name resembles the lesson" is not the bar. **Construct the violation, run the mechanism, paste the failure.** This is the same discipline as writing a regression guard before the fix and watching it go red: a guard only ever observed passing is not evidence it would catch anything.

Report each candidate as **DEMONSTRATED** (violation constructed, mechanism observed rejecting it) or **ASSERTED** (mechanism read, fire not exercised). ⚠️ **Only DEMONSTRATED entries may be recommended for promotion.** An ASSERTED list is still valuable — it is the next plan's work — but it must be reported separately and never merged into the promotion set.

## Drafting Cycle
**Tier:** T1 — triggers fired: **T-7** (a companion executable consumes the promotion set without re-deriving it) and **T-8** (novel: no prior plan grades lessons by whether a mechanism rejects a violation). T-5/T-6 do NOT fire — read-only, edits no doctrine, gate, template or contract.
**Walk register:** `governance/knowledge/research/walk-register-diagnostic-learned-promotion.md`
**Walks:** in progress — walks 0-3 run.
**Walk 0 (context pin) — REAL, measured 2026-08-23:** newest same-class is `Done/diagnostic-501.md` (2026-08-22), same project and class, and the plan that produced the mapping this one re-grades. This plan replaces text in no existing file, so §2.0's anchor measurements are structurally empty rather than skipped. Two measurements decided the plan's shape: **~36 primary mechanisms against 327 entries** fixed the method as mechanism-first, and **only `C` lesson-id citations across the whole enforcement surface** established that the mapping is a reading task and became Q6. 4 folded at walk 0.
- Weak spots:          w0 1 folded (1.2); w1 3 folded — instruction 3 / record 0; w2 1 folded — instruction 1 / record 0; w3 dry.
- Destruction:         w1 1 folded — instruction 1 / record 0; w2 dry; w3 dry.
- Vulnerabilities:     w0 1 folded (3.1); w1 1 folded — instruction 1 / record 0; w2 1 folded — instruction 1 / record 0; w3 dry.
- Integration-record:  w0 2 folded (4.1, 4.4); w1 dry; w2 1 folded — instruction 1 / record 0; w3 1 folded — instruction 1 / record 0.
- ACID:                w1 1 folded — instruction 1 / record 0; w2 dry; w3 1 folded — instruction 1 / record 0.
- Conformance:         w2 2 folded — instruction 2 / record 0 (symbol table; the 7 restatements it then caught); w3 1 folded — instruction 0 / record 1.
**Conformance (§5):** `plan_lint` exit **0**; `propagation_check` exit **0** — it can run only because walk 2 added the symbol table, having reported COULD-NOT-RUN before that.
**Cold panel:** not required at T1; scout at the Planner's call.

## MUST-PRESERVE

- **READ-ONLY.** No edit to `LESSONS.md`. No write to any `.db`. No re-label — that is the companion executable's job, and this plan must not pre-empt it.
- ⚠️ **Invoke every checker by ABSOLUTE path** — they live in `/Users/marklehn/Developer/GitHub/bellows/scripts/`, and shell state does not persist between invocations. A relative invocation after a `cd` reports `can't open file`, which exits non-zero and is easily misread as the mechanism FIRING. The Planner made this exact error repeatedly while authoring this plan.
- ⚠️ **Demonstrations are SCRATCH-ONLY.** To show a mechanism firing you will construct violating inputs. **Never place a plan-shaped file (`executable-*.md`, `diagnostic-*.md`) under a real `knowledge/decisions/` directory** — the bellows daemon claims AND DISPATCHES it within one second; this has happened live. Build violating specimens under your own scratch directory and run the checkers against those paths.
- ⚠️ **Corpus reads via `file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?immutable=1`** — `immutable=1`, NOT `mode=ro`: the corpus is in WAL mode, and `mode=ro` both fails against a copy with no `-shm` sidecar and touches the live `-shm` mtime. 21 stale `pre-*.db` snapshots sit beside it answering fluently and wrong; assert `lesson_entries` equals `E` before trusting any read.
- ⚠️ **`LESSONS.md` is in the governance ROOT repo** — `/Users/marklehn/Developer/GitHub/LESSONS.md` — and is now ANNOTATED. Entries carry `[status: learned|pending]`; `Q` are deliberately bare pending a CEO ruling.
- **`grep` here is ugrep: `-F` for every literal search.** ⚠️ A zero-match `grep -c` prints `0` and EXITS 1 — read the printed count, never the exit status. An unescaped bracketed pattern run without `-F` is a character class.
- **Do not "fix" any mechanism you find broken.** A check that does not fire when it should is a FINDING and a candidate lesson of its own — report it, never repair it here.

## STEP 1 — READ-ONLY DIAGNOSTIC

**Role:** DEV (read-only audit). Contract: `/Users/marklehn/Developer/GitHub/READONLY_AUDIT_CONTRACT.md`.

**Contract parameters.** `cwd`: your bellows worktree under `lessons-forge/.bellows-worktrees/<id>/`. `deposit_paths`: the two files in Deposits. `extra_forbidden`: any write to `LESSONS.md`, to any `.db`, or to any real `knowledge/decisions/` directory. `extra_preflight`: assert the corpus identity (path, byte size, `lesson_entries` equal to `E`). ⚠️ **`C7` REPO SET, pinned explicitly because the contract HALTs on an unnamed set:** `/Users/marklehn/Developer/GitHub` (root), `/Users/marklehn/Developer/GitHub/lessons-forge`, `/Users/marklehn/Developer/GitHub/bellows`, `/Users/marklehn/Developer/GitHub/forge`.

**Q1 — Inventory the enforcement surface.** Enumerate every mechanism that can FAIL on a violation: the gates in `bellows/gates.py`, the lettered checks in `bellows/scripts/plan_lint.py`, the checker scripts in `bellows/scripts/`, the hooks under `bellows/hooks/`, and the tests in `lessons-forge/src/test_lessons_forge.py`. ⚠️ **Bellows' own test suite is ~811 tests. The rule that makes it tractable is principled, not a quota: A TEST THAT GUARDS A MECHANISM IS NOT ITSELF A MECHANISM — the mechanism is.** `test_gate_scope_check_*` does not enforce a lesson; `scope_check` does, and the test enforces that `scope_check` keeps working. Count the gate once and do not count its tests. **Include a test as a mechanism in its own right ONLY when the test IS the enforcement** — when nothing else would catch the violation, as with `test_key_heading_annotated_matches_unannotated`, where the property holds only because that test asserts it. State which side of that line each included test falls on. Report the inventory with a one-line statement per mechanism of **what rule it enforces**.

**Q2 — Map mechanisms to `LESSONS.md` entries.** For each mechanism, find the entry or entries stating the rule it enforces, if any. ⚠️ **The mapping is MANY-TO-MANY and the deliverable must not flatten it:** one gate can enforce several lessons, and one lesson can be enforced by several mechanisms. Report both directions, and say explicitly when a lesson is only PARTLY enforced — a mechanism that catches some violations of a rule but not others is not completion, and collapsing it to a single row would hide that. ⚠️ **Report the mechanisms that map to NO entry — that set is as interesting as the mapping**: it is enforcement the corpus never captured, and it may mean the lesson was learned without ever being written.

**Q3 — DEMONSTRATE THE FIRE for every candidate.** Per the bar above: construct a violating input in scratch, run the mechanism, paste the raw rejection. ⚠️⚠️ **CONFIRM THE REJECTION IS FOR THE RIGHT REASON.** A non-zero exit is not a demonstration — a malformed specimen can fail a DIFFERENT check and look like a fire. The output must name the specific gate, check letter, or assertion that corresponds to the lesson. ⚠️ Pair it with a positive control: the same specimen WITHOUT the violation must pass that same check. A fire you have only ever seen in the failing direction does not prove the check discriminates. Classify each candidate **DEMONSTRATED** or **ASSERTED**. ⚠️ **Some mechanisms cannot be fired from a read-only context at all** — a gate that only runs inside a live dispatch is the clear case. That is an expected outcome, not a failure: mark it ASSERTED and **state precisely what would have been required to demonstrate it**. ⚠️ The reason for not running is itself a claim, so "could not be demonstrated" must name the obstacle; an unexplained ASSERTED is not a result. ⚠️ **A mechanism that does NOT reject its violation is the most valuable result in this plan** — it means a lesson believed enforced is not. Report those first and separately.

**Q4 — Emit the promotion set.** Deposit `knowledge/research/learned-promotion-2026-08-23.tsv` with columns `entry_id`, `entry_heading`, `mechanism`, `mechanism_file`, `violation_used`, `observed_rejection`. ⚠️ **ONE ROW PER (ENTRY, MECHANISM) PAIR — not per entry.** Q2 established the mapping is many-to-many, and a one-row-per-entry schema would silently pick one mechanism and discard the rest, destroying exactly the evidence that makes a promotion trustworthy. An entry enforced by three mechanisms gets three rows. ⚠️ **Report the distinct-entry count separately from the row count** — they differ, and the companion executable promotes ENTRIES, not rows. ⚠️ **Carry `entry_id` where the entry has a corpus row** — a heading is an unstable identifier (it is editable, and `Q` entries have no corpus row at all), and the companion executable must be able to find the row it is promoting even if the heading moves. Leave it blank rather than inventing one where none exists, and report how many rows are blank. This is the companion executable's input, so it must be data, not prose. ⚠️ **STATE THE SET'S AUTHORITY.** A row in this file promotes an entry to the state that means DONE, in an artifact the shop greps to decide what to build. **A wrong promotion re-commits the exact error this arc exists to correct**, and it is worse than the original because it will now carry a demonstration alongside it. The executable may apply DEMONSTRATED rows mechanically and may apply NOTHING else — say so in the findings, and give the counts for each class so the executable cannot infer one from the other.

**Q5 — Size the three states.** Given the promotion set, state the resulting counts for `learned`, `codified` and `pending`, and reconcile them to `N`. ⚠️ Assert the arithmetic; do not transcribe a figure from this plan.

**Q6 — Propose the convention that makes this mechanical next time.** Walk 0 measured only `C` lesson-id citations across the entire enforcement surface, so "is this lesson enforced?" is today a reading task. Propose the durable fix — how a mechanism should record which entry it enforces — and state what it would cost to backfill. ⚠️ **Prior art exists and you should start from it rather than inventing:** the few citations that DO exist use two incompatible forms, a bare `(500)` plan-id in `test_lessons_forge.py` and a `proposal NNN` / `entry NNN` form elsewhere. Say which is right, or whether neither is, and note that a plan id, a proposal id and an entry id are three different keys. ⚠️ **Argue whether the citation belongs in the CODE or in the corpus**, rather than assuming. ⚠️ **And note what already mints the label:** `lessons-forge/scripts/detect_learned.py:245` emits `"proposed_status": "learned"` unconditionally for every detector PASS. Under the CEO's ruling that emitter is now wrong — it produces the very label this arc is correcting — so your Q6 answer should say what it should emit instead, since the companion executable has to change it.

**Findings document:** Q1–Q6, each answered with command output or `file:line`. Close with `## What could not be measured`, `## Open forks`, and `## Recommended executables`.

**Scope:**
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/research/learned-promotion-2026-08-23.md`
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/research/learned-promotion-2026-08-23.tsv`

**Deposits:**
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/research/learned-promotion-2026-08-23.md`
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/research/learned-promotion-2026-08-23.tsv`

**Commit:** ⚠️ **WORKTREE DISCIPLINE.** You are dispatched into `lessons-forge/.bellows-worktrees/<id>/`. Write both deposits at the SAME relative paths under YOUR cwd and commit them there in one commit: `git -C <your-worktree> add knowledge/research/<both> && git -C <your-worktree> commit -m "..."`. ⚠️ Do NOT write to the main checkout — `gates._resolve_deposit_path` falls back to "path as-is" and `_check_deposit_uncommitted` swallows the out-of-worktree git error, so writing to the wrong checkout passes both gates SILENTLY and the teardown-merge never picks your files up. Absolute for everything you READ, relative-to-cwd for everything you WRITE.
