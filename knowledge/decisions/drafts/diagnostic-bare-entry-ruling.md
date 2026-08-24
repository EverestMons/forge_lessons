# lessons-forge — rule on the 14 bare `LESSONS.md` entries: grade them under the CEO's `history` ruling and emit the executable's input

**Date:** 2026-08-23 | **Project:** lessons-forge | **Tier:** Medium | **Dispatch Mode:** bellows | **cycle_tier:** T1 | **Test Scope:** none (read-only diagnostic) | **Execution:** Step 1 (READ-ONLY DIAGNOSTIC) | **Priority:** 1

**auto_close:** false
**pause_for_verdict:** after_step_1

**Depends on:** `Done/diagnostic-501.md` and its mapping `knowledge/research/annotation-mapping-2026-08-22.tsv` (the quarantine list); `Done/diagnostic-504.md` and `knowledge/research/promotion-corrected-2026-08-23.md` (the two grading rules); `/Users/marklehn/Developer/GitHub/governance/knowledge/decisions/Done/executable-502.md` (which quarantined these 14 by construction) and `/Users/marklehn/Developer/GitHub/governance/knowledge/decisions/Done/executable-505.md` (which set the current state) — ⚠️ **both are GOVERNANCE plans, not lessons-forge ones**, and a bare `Done/…` reference to either resolves to a file that does not exist. Newest same-class and clone origin: **`Done/diagnostic-504.md`**, shipped 2026-08-23.

## Why this exists

`executable-502.md` annotated 313 mapping rows and left **14 untouched by design** — its D2 row reads "rows QUARANTINED, untouched … `proposed_status` is `unknown`". Those 14 headings are the register's only bare ones. They were never a judgement the pipeline made and lost; they are a judgement it declined to make.

**CEO ruling, 2026-08-23:** `[status: history]` is a **fourth legal value** — for a register entry that RECORDS what happened rather than states an enforceable rule. It exists because the three-value taxonomy has no cell for such an entry: `pending` claims buildable work that does not exist, `codified` claims a target that does not exist, `learned` claims an enforcement that does not exist. Under the SESSION 59 ruling `learned` means COMPLETION, so all three would be false of the same entry.

This plan grades the 14 under that ruling and emits the mapping a companion executable applies.

## What walk 0 measured, and why it changes the plan's shape

The 14 quarantine under three stated causes. **All three dissolve on measurement, each for a different reason** — so this is not "grade 14 hard cases", it is "three quarantine classes, none of which is what its label says".

1. **`target_layer = 'none'` occurs EXACTLY 5 times in the whole 378-proposal corpus, and those 5 entries are `59, 82, 88, 104, 112`.** An earlier classification pass had already recorded the record-not-rule judgement as data; the annotation pipeline had no status value that could express it, so it surfaced as `no_target` and then as bare. ⚠️ **This is a corroboration, not an authority** — it was produced by the same class of pass this plan is auditing, and Q2 tests the 5 from their BODIES. It is stated here because a reader must be able to tell a converging second measurement from a circular one.
2. **`conflicting-proposals-quarantined` is a misnomer.** Entries `93, 116, 123` carry exactly 2 proposals each, and measured, **both members of every pair are non-live** — one `stale`, one `rejected`. There is no live proposal to choose between and nothing to reconcile. The detector quarantined a pair with no live member.
3. **The 2 `threshold` entries are the ONLY bare entries carrying a `target_artifact`, and it is CODE** — `walk_register_lint.py` for both `330` and `331`. The detector scores a prose-term ratio against the target's text; run against a Python file that ratio measures nothing. **The threshold class is a detector defect, not an undecidable entry** — and these two are the set's strongest `learned` candidates, because a guard actually shipped.

## What this plan does NOT do

- **It does NOT edit `LESSONS.md`, write to any `.db`, or re-label anything.** Read-only. Its output is the executable's input.
- **It does NOT re-open the 317 annotated entries.** They are not candidates. ⚠️ Say so explicitly in the findings rather than leaving it implied — a reader must be able to tell "not a candidate" from "considered and rejected".
- **It does NOT re-run the annotation detector over the corpus**, and it does not need to: the three sub-class causes above are measured facts about the mapping and the corpus, and Q2's question — is this entry a record or a rule — is answered by reading the entry, not by re-scoring it. ⚠️ **The two exceptions are `330`, `331` and `122`, where the verdict DOES depend on whether a mechanism exists and fires** (Q4). Run those; do not assume them.
- ⚠️ **It does NOT accept the corpus's `target_layer` as the answer to Q2.** See the warning in pin 1.

## The verdict derivation (the constraint Q2–Q5 share)

⚠️ **Sites: Q2, Q3, Q4, Q5.** Stated here rather than inside one question because it spans four, and a constraint carried by whichever question the author happened to be drafting is the half-carried-guard class.

Each entry's status is DERIVED, never chosen:

| class (Q2) | is the rule already written into a named artifact? (Q3) | does a mechanism REJECT a violation? (Q4) | status |
|---|---|---|---|
| RECORD | n/a | n/a | `history` |
| RULE | yes | yes, and the pair passes BOTH 504 rules | `learned` |
| RULE | yes | no mechanism, or one failing either 504 rule | `codified` |
| RULE | no — no artifact contains it yet | not reached | `pending` |
| UNDECIDED | — | — | `unknown` — surfaced, never auto-routed (Fork 3, SESSION 58b) |

⚠️ **Rows three and four are the pair this plan exists to separate, and Q3 is where they separate.** `codified` and `pending` differ ONLY by whether the target artifact ALREADY CONTAINS the rule — so naming a target does not settle it, and Q3 must answer both halves. ⚠️ **The second half is an ABSENCE CLAIM against a 420KB file and it carries the §2.7 discipline in full:** derive the probe from the entry's OWN text rather than composing one from memory, and pair every zero with a positive control. A bare-word probe is worthless here and the Planner measured it — `canary` returns 17 hits in `PLANNER_TEMPLATE.md` and settles nothing about the live-canary entry.

⚠️ **Every one of the `Q` entries receives a value.** `unknown` is the escape for a genuinely undecidable entry; **bare is not**, and bare must be 0 after the companion executable runs.

## Numbers discipline

⚠️ **This table owns every quantity the plan ACTS ON.** Values measured at walk 0, 2026-08-23. **RE-DERIVE every one; if yours differ, yours supersede and you say so.**

| id | pin | value | probe |
|---|---|---|---|
| D0 | **`Q`** — bare headings, this plan's whole subject | **14** | ⚠️ **enumerate, do not merely count** — `grep -n '^## ' <abs LESSONS.md>` filtered to lines NOT containing `[status:`; the COUNT is `D1` − `D5`, and a probe returning only the count cannot supply the set every later question acts on |
| D1 | **`N`** — dated headings in the register | **331** | `grep -cE '^## 20[0-9][0-9]' <abs LESSONS.md>` — equals the all-H2 count, so every H2 is a dated entry |
| D2 | `learned` | **14** | `grep -cE '^## .*\[status: learned\]' <abs LESSONS.md>` |
| D3 | `codified` | **225** | same form, `codified` |
| D4 | `pending` | **78** | same form, `pending` |
| D5 | headings carrying ANY `[status:]` | **317** | `grep -cE '^## .*\[status: ' <abs LESSONS.md>` — and `D2`+`D3`+`D4` must equal it |
| D6 | headings carrying `[target:]` | **239** | `grep -cE '^## .*\[target: ' <abs LESSONS.md>` — equals `D2`+`D3`; ⚠️ **no bare entry carries a target**, so a check expecting a mix fails on a correct run |
| D7 | mapping rows with `proposed_status = unknown` | **14** | `awk -F'\t' 'NR>1 && $4=="unknown"' <mapping tsv> \| wc -l` — must equal `Q`, and the id sets must be EQUAL, not merely equinumerous |
| D8 | sub-class `no_target` / `conflicting` / `threshold` | **9 / 3 / 2** | partition `D7` on the `basis` column |
| D9 | corpus-wide proposals with `target_layer = 'none'` | **5** | `SELECT COUNT(*) FROM lesson_proposals WHERE target_layer='none'` |
| D10 | corpus `lesson_entries` — negative pin | **370** | `sqlite3 "file:<abs>?immutable=1" "SELECT COUNT(*) FROM lesson_entries"` |
| D11 | `/Users/marklehn/Developer/GitHub/LESSONS.md` sha256 | `8ba177d0400c87da4673247fb4de9af116a140845b8e30868ef70f8e7e22d363` | `shasum -a 256` — 641,081 bytes |

⚠️ **`D1` is 331, not the 327 the mapping was generated against.** SESSION 59's wrap appended after `diagnostic-501` ran. The appends landed at the END of the file, so the mapping's `line_no` column still resolves today — **but that is luck, not a contract. Locate every heading by WHOLE-LINE equality against `"## " + original_heading` and assert the occurrence count is exactly 1; never by the mapping's line number.**

## Drafting Cycle
**Tier:** T1 — triggers fired: **T-7** (a companion executable applies this plan's verdicts without re-deriving them) and **T-8** (novel: no prior plan grades the quarantine set, and none has ever applied the `history` value). T-5/T-6 do NOT fire — read-only, edits no doctrine, gate, template or contract.
**Walk register:** `governance/knowledge/research/walk-register-diagnostic-bare-entry-ruling.md`
**Walks:** walk 0 pinned; walk 1 in progress.
**Walk 0 (context pin) — REAL, measured 2026-08-23:** see the walk register. Newest same-class and clone origin are the same plan, `Done/diagnostic-504.md`. This plan replaces text in no existing file, so §2.0's anchor measurements are structurally empty rather than skipped. The three measurements that fixed its shape are the three numbered pins above.
**Direction verdict (after walk 1):** owed.
- Weak spots:          w1 4 folded — instruction 4 / record 0.
**Cold panel:** computed tier does not require one. ⚠️ **Live question at the freeze, not a waiver:** the immediately preceding plan in this exact class — `diagnostic-503` — shipped a promotion set that was wrong in both directions and reached an executable, and its own identity check could not see it. Unlike `504`, this plan's premise came from the Planner's own reading rather than from a cold seat, so no cold reading has been spent on it. Decide at the freeze and record the reasoning either way.
**Conformance (§5):** owed — `plan_lint` and `propagation_check` run at the deposit PATH before the copy-in.
**Closing:** owed.

## Cycle Manifest
tier: T1
target: knowledge/research/bare-entry-ruling-2026-08-23.md
class: read-only
reads: /Users/marklehn/Developer/GitHub/LESSONS.md, /Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db, /Users/marklehn/Developer/GitHub/lessons-forge/knowledge/research/annotation-mapping-2026-08-22.tsv, /Users/marklehn/Developer/GitHub/lessons-forge/knowledge/research/promotion-corrected-2026-08-23.md, /Users/marklehn/Developer/GitHub/lessons-forge/scripts/detect_learned.py, /Users/marklehn/Developer/GitHub/bellows/scripts/walk_register_lint.py, /Users/marklehn/Developer/GitHub/bellows/bellows_root.py
writes: knowledge/research/bare-entry-ruling-2026-08-23.md, knowledge/research/bare-entry-ruling-2026-08-23.tsv
open_forks: (1) the companion executable is BLOCKED on this plan's output; (2) detect_learned.py:245 emits `learned` unconditionally and cannot emit `history`; (3) no validator defines the legal `[status:]` value set; (4) nothing tells a wrap appender to add `[status: pending]`
walks: open
yields: open
validation: owed
coherence: owed — cycle open
N/A

## MUST-PRESERVE

- **READ-ONLY.** No edit to `LESSONS.md`, no write to any `.db`, no re-label, no new annotation.
- ⚠️ **Corpus reads via `file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?immutable=1`** — `immutable=1`, NOT `mode=ro`: the corpus is WAL, and `mode=ro` fails against a copy with no `-shm` sidecar and touches the live `-shm` mtime. **21 stale `pre-*.db` snapshots sit beside it answering fluently and wrong, and the siblings `forge.db` / `lessons.db` are 0-byte decoys that return FALSE ABSENCES.** Assert `lesson_entries` equals `D10` before trusting any read.
- ⚠️ **`LESSONS.md` is in the governance ROOT repo** — `/Users/marklehn/Developer/GitHub/LESSONS.md` — not in lessons-forge, and not in your worktree.
- ⚠️ **The mapping TSV is QUOTED CSV inside a TSV, not raw TSV.** Headings containing `"` are wrapped in quotes with the inner quotes doubled (measured at exec-502; a naive split-on-tab parse aborts the run). Three of the 14 bare rows are in that form. Parse accordingly and prove your parse recovers all `D7` rows.
- ⚠️ **A bare heading has NO marker to strip** — that is what makes it bare. Do not reach for the `_key_heading` normalizer to locate one; whole-line equality against `"## " + original_heading` is the locator, with an asserted occurrence count of exactly 1.
- **`grep` here is ugrep: `-F` for every literal search.** ⚠️ A zero-match `grep -c` prints `0` and EXITS 1 — read the printed count, never the exit status. ⚠️ A `-E` pattern with a nested quantifier over this corpus can exceed the shim's complexity limit and ERROR rather than return empty; if that happens, narrow the pattern — do not read the error as an absence.
- ⚠️ **Every negative probe in this plan needs a positive control.** Absence looks identical whether the thing, the pattern, the path or the unit is wrong, and this plan asks repeatedly whether a mechanism exists. State the control alongside each absence claim.
- ⚠️ **Invoke any checker by ABSOLUTE path** from `/Users/marklehn/Developer/GitHub/bellows/scripts/`; shell state does not persist between invocations, and a relative call after a `cd` reports `can't open file` and exits non-zero, which is easily misread as a check failing.

## STEP 1 — READ-ONLY DIAGNOSTIC

**Role:** DEV (read-only audit). Contract: `/Users/marklehn/Developer/GitHub/READONLY_AUDIT_CONTRACT.md`.

**Contract parameters.** `cwd`: your bellows worktree under `lessons-forge/.bellows-worktrees/<id>/`. `deposit_paths`: the two files in Deposits. `extra_forbidden`: any write to `LESSONS.md`, to any `.db`, or to any real `knowledge/decisions/` directory. `extra_preflight`: assert the corpus identity (path, byte size, `lesson_entries` equal to `D10`) and the `LESSONS.md` sha equal to `D11`. ⚠️ **`C7` REPO SET, pinned explicitly because the contract HALTs on an unnamed set:** `/Users/marklehn/Developer/GitHub` (root), `/Users/marklehn/Developer/GitHub/lessons-forge`, `/Users/marklehn/Developer/GitHub/bellows`, `/Users/marklehn/Developer/GitHub/forge`.

**Q1 — Reproduce the quarantine.** Re-derive `Q` and the three sub-classes from the mapping, and list the ids in each. ⚠️ **Prove the two 14s are the SAME 14** — the bare headings in the file and the `unknown` rows in the mapping — by comparing id/heading SETS, not counts; two disjoint sets of 14 would satisfy every count check in this plan. Assert `D2`+`D3`+`D4` = `D5` and `D6` = `D2`+`D3`, and state that no bare entry carries a `[target:]` marker.

**Q2 — RULE THREE: is this entry a RECORD or a RULE?** The CEO's discriminator: a RECORD accounts for what happened; a RULE states something a future actor must do or not do, such that a violation is identifiable. ⚠️ **Grade all 14, not only the 5 the corpus flags** — the question is whether the corpus's `none` set is COMPLETE or merely the part someone got to, and that is answerable only by grading the other 9 against the same discriminator. ⚠️ **Read the BODY, not the heading** — a heading is a one-line summary and several of these bodies end in an explicit "**The discipline rule:**" paragraph that the heading does not carry. ⚠️ **Flag the near cases in both directions**: an entry whose body states a rule that has since become unbuildable because the workflow it governs no longer exists is a genuinely close call, and so is a record that happens to contain one imperative sentence. State the reasoning per entry; do not emit a bare verdict. ⚠️ **UNDECIDED is a legal third answer and you are expected to use it rather than force a binary** — 504's own instruction on the equivalent question reads *mark it undecided rather than assuming*. An UNDECIDED entry takes `unknown` per the derivation table, which is a surfaced state, not a silent one.

**Q3 — Assign a target for every RULE entry.** Nine of the 14 have a NULL `target_artifact`, which is why the detector never graded them. For each entry graded RULE, name the artifact its rule belongs in, using the Fork-2 discriminator already decided: **DEFINITION → `glossary.md`, RUNBOOK → `CLAUDE.md`, TRAP → CODE.** ⚠️ **Then answer the SECOND half, which is what actually separates `codified` from `pending`: does that artifact ALREADY CONTAIN the rule?** Naming a target does not settle the status — see the derivation table — and this half is an absence claim carrying the full §2.7 discipline (probe derived from the entry's own text, positive control beside every zero). ⚠️ **"No artifact exists yet" is a legal answer and you must be willing to give it** — it means the entry is `pending` with a named build item, not that a target must be invented to fill the column. Name the build item when you give it.

**Q4 — Grade each RULE entry against 504's two rules.** Rule One: a mechanism that leaves a material part of the lesson's scope uncovered is `codified`, not completion. Rule Two: a mechanism cannot enforce a lesson about that mechanism's own insufficiency — ask whether the mechanism REJECTS A VIOLATION of the lesson or is merely the lesson's SUBJECT. ⚠️ **Read `promotion-corrected-2026-08-23.md` §Q2–Q3 for both rules as stated, and cite the discriminator you applied; do not reconstruct them from this plan's summary.** ⚠️ **Three entries need a mechanism DEMONSTRATED, not assumed, and the verdict turns on it:**
- **`330` and `331`** name guards in `walk_register_lint.py` (`duplicate_row`, `headerless_rows`). Confirm each exists, then RUN it — a violating input must be rejected AND a clean control must pass. A guard that fires on everything proves nothing. Then apply Rule One: each lesson's "How to apply" carries a second clause the guard does not cover.
- **`122`** names a discipline (resolve roots by marker walk-up). `bellows/bellows_root.py` implements it and no `__file__`-relative root constant survives in `bellows/*.py`. ⚠️ **That is the FIX, and the fix is not the enforcement** — the discriminating question is whether anything REJECTS a newly-authored `__file__`-relative root. Look for it, state the control for your search, and if nothing rejects it, the verdict is `codified` with the guard as a named build item.

**Q5 — Emit the mapping.** Deposit `knowledge/research/bare-entry-ruling-2026-08-23.tsv` with columns `entry_id`, `heading_line_no`, `entry_heading`, `class`, `target_artifact`, `mechanism`, `mechanism_file`, `rule1_partly`, `rule2_circular`, `verdict`, `basis`. One row per (entry, mechanism) pair; an entry with no mechanism gets one row with the mechanism columns empty. `class` is `RECORD`, `RULE` or `UNDECIDED`; `verdict` is `HISTORY`, `LEARNED`, `CODIFIED`, `PENDING` or `UNKNOWN`, and it is DERIVED from the table above rather than chosen — state which row of that table each entry took. ⚠️ **Rule Two is a property of the PAIR** — an entry is graded on its best-passing mechanism, so state the per-entry verdict and the distinct-entry count separately from the row count. ⚠️ **STATE THE SET'S AUTHORITY:** the executable may apply these verdicts mechanically and may apply NOTHING else — no inference from a neighbouring row, no reconciliation against the 501 mapping, no arithmetic that recovers a different set. ⚠️ **Then reconcile the post-application state**: `learned` + `codified` + `pending` + `history` + `unknown` must equal `D1`, and bare must be 0. **Assert the arithmetic from your own re-derived figures; do not transcribe a numeral from this plan.**

**Q6 — What must change so `bare` cannot recur?** Four known gaps. Size each, say where it belongs (`detect_learned.py`, a checker, the diagnostic template, or doctrine), and state what it would cost:
(a) `scripts/detect_learned.py:245` emits `learned` unconditionally — wrong under the SESSION 59 ruling, and with no way to emit `history` at all;
(b) nothing anywhere defines the legal `[status:]` value set, so neither a bare heading nor a misspelled value is catchable;
(c) nothing tells a wrap appender to add `[status: pending]`, so every append is invisible to the build queue — SESSION 59's three appends carried it by hand;
(d) the detector scores a prose-term ratio against a target that may be CODE, where the score means nothing — the mechanism that quarantined `330` and `331`.
⚠️ **Say which single one of the four would have prevented the largest share of this plan's work**, and argue it.

**Findings document:** Q1–Q6, each answered with command output or `file:line`. Close with `## What could not be measured`, `## Open forks`, and `## Recommended executables`.

**Scope:**
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/research/bare-entry-ruling-2026-08-23.md`
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/research/bare-entry-ruling-2026-08-23.tsv`

**Deposits:**
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/research/bare-entry-ruling-2026-08-23.md`
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/research/bare-entry-ruling-2026-08-23.tsv`

**Commit:** ⚠️ **WORKTREE DISCIPLINE.** You are dispatched into `lessons-forge/.bellows-worktrees/<id>/`. Write both deposits at the SAME relative paths under YOUR cwd and commit them there in ONE commit: `git -C <your-worktree> add knowledge/research/<both> && git -C <your-worktree> commit -m "..."`. ⚠️ Do NOT write to the main checkout — `gates._resolve_deposit_path` falls back to "path as-is" and `_check_deposit_uncommitted` swallows the out-of-worktree git error, so writing to the wrong checkout passes both gates SILENTLY and the teardown-merge never picks your files up. Absolute for everything you READ, relative-to-cwd for everything you WRITE.
