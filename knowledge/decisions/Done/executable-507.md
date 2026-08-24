# lessons-forge — CORRECTIVE to 506: restore byte-verbatim `entry_heading` for the two rows a typographic apostrophe broke

**Date:** 2026-08-24 | **Project:** lessons-forge | **Tier:** Small | **Dispatch Mode:** bellows | **cycle_tier:** T1 | **Test Scope:** none (data correction, no code) | **Execution:** Step 1 (DEV) | **Priority:** 1

**auto_close:** false
**pause_for_verdict:** after_step_1

**Depends on:** `Done/diagnostic-506.md` and its deposit `knowledge/research/bare-entry-ruling-2026-08-23.tsv` — **this plan CORRECTS two cells of that deposit and changes no verdict.** Newest same-class, MEASURED: `/Users/marklehn/Developer/GitHub/governance/knowledge/decisions/Done/executable-505.md`, ship date 2026-08-23T19:42:41-05:00 — ⚠️ **absolute and unelided: an earlier form wrote `governance/…/Done/…`, which resolves to nothing, and it is a GOVERNANCE plan not a lessons-forge one.** This is the identical defect a cold scout caught in `diagnostic-506` (`S0-4`), repeated by the same author one plan later; the two bare `Done/…` references beside it DO resolve, because `506` and `500` both live in this project's `Done/`. Corrective precedent: `Done/executable-500.md` (the corrective to 499).

## Why this exists

`diagnostic-506` deposited a 14-row mapping whose `entry_heading` column the plan required to be the register's heading line **byte for byte** — because the companion executable's ONLY sanctioned locator is whole-line equality against `"## " + entry_heading`.

**Measured: 12 of 14 are byte-exact. Two are not.** Entries `123` and `330` carry **U+2019 `’`** where `LESSONS.md` carries **U+0027 `'`**, and both match **ZERO** lines in the register. They are exactly the only two of the fourteen containing an apostrophe at all.

⚠️ **All ten gates passed on that deposit and the Planner's Rule 22(b) check passed it too** — because every check run was a SET or a COUNT (id set equal to `Q`, 14 non-empty verdicts, 14 pointers resolving with zero dangling and zero orphans). None compared the heading BYTES to the register. A count cannot see a value that is wrong.

⚠️ **And 506's own round-trip proof was scoped to the wrong rows:** it mandated the check for the three quoted-CSV rows (`59`, `82`, `104`), all three of which ARE byte-exact. The drift landed in two rows nobody was told to check, from a different defect class.

## What this plan does NOT do

- **It changes NO verdict, class, target, mechanism or basis.** Only the `entry_heading` cell of entries `123` and `330`, and within those cells only the apostrophe character.
- **It does NOT normalize apostrophes anywhere as a matching rule.** ⚠️ Normalizing inside a lookup key is what orphaned 40 of 370 corpus rows at `exec-499`; the fix is to make the stored value correct, never to make the comparison lenient.
- **It does NOT edit `LESSONS.md`.** The register is correct; the deposit is wrong.

⚠️⚠️ **THIS PLAN EDITS A CLOSED PLAN'S DEPOSIT, AND A CODIFIED LESSON SAYS NOT TO — the deviation is declared here rather than discovered by a later reader.** `LESSONS.md:3993` reads: *When a defect is found in a closed artifact, record it in the consuming verdict/register with a pointer to the source; the closed artifact stays byte-stable.* **Three facts distinguish this case, and if you disagree with them the right move is to stop and say so, not to proceed quietly:** **(1)** that lesson's artifact was a census READ BY HUMANS, where a pointer in the consuming verdict reaches the reader; this TSV is consumed MECHANICALLY by a builder, which reads the cell and never the verdict. **(2)** The lesson's own wording bars editing a closed artifact *silently* — this edit has a plan, a drafting cycle, a register, a verdict and a commit. **(3)** The defect is in the LOCATOR itself, the one field whose entire purpose is machine matching, not in a value a reader interprets. ⚠️ **The cost of the strict reading is the thing that settles it: leave the bytes alone and the companion halts on 2 of 14 entries permanently, with a pointer in a verdict that no builder will ever read.**

## Numbers discipline

⚠️⚠️ **TWO DIFFERENT QUANTITIES IN THIS PLAN BOTH EQUAL 14 — `R`, the number of data ROWS, and the number of headings MATCHING after the fix. They are unrelated, and `propagation_check` reports every prose `14` as a restatement of `R` because it cannot tell them apart.** Read every `N/14 matching` as a MATCH count, never as `R`. Said once here rather than qualified at each site. ⚠️ **RE-DERIVE every value; if yours differ, yours supersede and you say so.** ⚠️ **And note the two-arm shape this table gives the step, because `exec-500` is this plan's corrective precedent and its lesson was that a single-arm probe is uninterpretable:** `D2` (12 → 14) is the EFFECT arm, and `D4`/post-conditions 3 and 4 are the CONTROL arm that bounds the blast radius — identical verdict multiset, exactly two rows touched. Neither alone would distinguish a correct fix from a broader one.

| id | pin | value | probe |
|---|---|---|---|
| D1 | **`R`** — rows in the TSV (data rows, excl. header) | **14** | `csv.DictReader(delimiter='\t', quotechar='"')` — ⚠️ the file is quoted-CSV-inside-TSV; a naive split-on-tab does NOT abort, it silently yields still-quoted values |
| D2 | **`M`** — `entry_heading` values byte-exact against `LESSONS.md`, BEFORE | **12** | for each row, count lines equal to `"## " + entry_heading` |
| D3 | …the two that are NOT | **`123`, `330`** | the complement of `D2` |
| D4 | **`A`** — U+2019 `’` occurrences in the WHOLE file, BEFORE | **4** | `raw.count('’')` on the file read as text |
| D5 | **`A_t`** — of those, how many lie in the two target `entry_heading` cells | **4** — all of them | per-cell count across every row and column |
| D6 | U+0027 `'` in those two cells — BEFORE | **0** | per-cell count |
| D7 | `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/research/bare-entry-ruling-2026-08-23.tsv` sha256 — BEFORE | `53a804617370594a0353fb4f56bfce322bdf1653e349a342540a2dd69767c9b5` | `shasum -a 256` — ⚠️ **full digest, not a prefix: an earlier form of this cell was truncated with an ellipsis, which cannot be compared against anything and is the one defect class a pin table exists to prevent** |
| D8 | file size / line count — BEFORE | **4821 bytes / 15 lines** | `wc -c` / `wc -l` |

⚠️ **`D5` is the measurement that shapes this plan: every typographic apostrophe in the file is already inside the two cells being corrected**, so a file-wide replacement and a cell-scoped one produce identical output HERE. **Do the cell-scoped one anyway** — it stays correct if the file ever gains a legitimate `’` elsewhere, and `D4 → 0` is then a post-condition rather than a coincidence.

## Drafting Cycle
**Tier:** T1 computed — **T-2** fires (writes real data: a deposited artifact a downstream executable consumes MECHANICALLY to edit the live register, so a wrong byte here propagates to `LESSONS.md`). T-1 does not fire (two cells, one file). T-5/T-6 do not fire — git-revertible, edits no doctrine, gate, template or contract.
**Walk register:** `governance/knowledge/research/walk-register-executable-bare-entry-heading-bytes.md`
**Walks:** walk 0 pinned; walks 1–5 complete (five lenses each, sequential, per-lens commits).
**Walk 0 (context pin) — REAL, measured 2026-08-24:** newest same-class measured by ship date (505, 2026-08-23T19:42:41-05:00, ahead of 502 the same morning). **Anchors:** the two `entry_heading` cells, 4 characters total. **Occurrence counts:** U+2019 = 4 file-wide, all 4 inside those two cells (`D5`). **Last writer of the target lines:** `diagnostic-506`, closed to `Done/` 2026-08-24. **Target sha:** `D7`.
**Direction verdict (after walk 1): PROCEED.** Tested against the three forcing findings, not judged: (a) `exec-500`'s corrective lesson was folded IN, not invalidated; (b) W1-3 declared the closed-deposit deviation with its cost, and the mechanism is sound and now idempotent-safe; (c) every premise held under re-derivation. None fires.
- Weak spots:          w1 2 folded — instruction 2 / record 0; w2 1 folded — instruction 1 / record 0; w3 1 folded — instruction 1 / record 0; w4 1 folded — instruction 1 / record 0; w5 dry.
- Destruction:         w1 1 folded — instruction 1 / record 0; w2 dry; w3 dry; w4 dry; w5 dry.
- Vulnerabilities:     w1 1 folded — instruction 1 / record 0; w2 1 folded — instruction 1 / record 0; w3 dry; w4 dry; w5 dry.
- Integration-record:  w1 2 folded — instruction 2 / record 0; w2 1 folded — instruction 1 / record 0; w3 1 folded — instruction 1 / record 0; w4 1 folded — instruction 0 / record 1; w5 1 folded — instruction 0 / record 1.
- ACID:                w1 1 folded — instruction 1 / record 0; w2 1 folded — instruction 1 / record 0; w3 dry; w4 dry; w5 dry.
**Cold panel:** ⚠️ **DECIDED AT THE FREEZE — DECLINED, with the reasoning recorded rather than the decision deferred a second time.** The computed tier (T1) does not require one, and the case for spending one here is weak on measured grounds: this plan changes **four characters**, its full mandated procedure was EXECUTED end-to-end in a scratch repo producing exactly the predicted post-conditions (`2\t2`, 0 CRs, 0 U+2019, 14 rows), its blast radius was proven bounded by constructed adversarial variants, and all eight pins re-derive against the live files. It carries **no judgement calls** — unlike `diagnostic-506`, whose panel earned 44 findings because that plan graded fourteen entries. ⚠️ **A judgement, not a waiver: the CEO may call one, and the residual risk is stated plainly — the one thing a cold reader would most likely catch is a wrong premise about the COMPANION's needs, since this plan's whole justification is that the companion's locator requires byte-exact headings.**
**Conformance (§5):** run per lens from walk 1, recorded here with its phase as §5 requires. Last run at **walk 5 (the close)**: `plan_lint` exit **0**, 0 FAIL, PIN-CHECK `kind=sha256 result=ok`; `propagation_check` exit **1** (restated-value divergences, the expected class); `fold_check` PASS; walk register CONFORMANT (read from STDERR). ⚠️ The phase label is the LAST run, not the first — §5 requires the exit code recorded with the phase it was taken at, and an earlier form of this line still said *walk 2 lens 4* two walks later. ⚠️⚠️ **Until walk 2 lens 4, `propagation_check` was returning exit 2 — *could not run* — because the pin table declared no SYMBOLS in the form its detector (1) requires (`| Dn | **`SYM`** … | **VALUE** |`). Exit 2 is not a clean result and was being read as though the check had passed.** Symbols `R`/`M`/`A`/`A_t` declared on the four pins the plan acts on, after which the detector parses them and runs. Re-run at the deposit path before the copy-in.
**Closing:** **walk 5 met the bar — instruction 0 / record 1**: one deictic reference in the conformance line that lost its referent when walk 4 re-stamped that line's phase label. Fold-introduced, record-class, and it landed IN the closing record, so the closing-record re-read covers it and the residue list is empty. Five walks, five lenses each, **per-lens commits throughout** — sequential execution is provable from the record rather than attested. No restructuring fold. Instruction-class series **7 → 4 → 2 → 1 → 0**. Closing-record re-read run: it raised three staleness items, all swept here, including the cold-panel decision this line had deferred twice. ⚠️ **The cycle is CLOSED; the DEPOSIT is a separate act.**

## Cycle Manifest
tier: T1
target: knowledge/research/bare-entry-ruling-2026-08-23.tsv
class: governed-tooling
reads: /Users/marklehn/Developer/GitHub/LESSONS.md, /Users/marklehn/Developer/GitHub/lessons-forge/knowledge/research/bare-entry-ruling-2026-08-23.tsv, /Users/marklehn/Developer/GitHub/lessons-forge/knowledge/research/bare-entry-ruling-2026-08-23.md
writes: knowledge/research/bare-entry-ruling-2026-08-23.tsv
open_forks: (1) the companion executable is BLOCKED on this correction; (2) 506's findings document may carry the same drift in its `### <id>` section headings — out of scope here, checked and reported by this plan
walks: 5
yields: 7, 4, 2, 1, 0
validation: cycle_check=BAR_MET, plan_lint=0_FAIL, fold_check=PASS
coherence: N/A — the emitter's sentinel; NOT hand-filled, because §3 makes it a COMPUTED field
N/A

## MUST-PRESERVE

- ⚠️⚠️ **EVERY DATE IN THIS PLAN IS A FIXED LITERAL.** The deposit filename carries `2026-08-23` and is NOT to be re-stamped; this plan was authored 2026-08-24 and may dispatch later.
- ⚠️⚠️ **NO VERDICT MAY CHANGE.** Assert it: the multiset of `(entry_id, class, target_artifact, mechanism, rule1_partly, rule2_circular, verdict, basis)` is IDENTICAL before and after. The only permitted delta is inside two `entry_heading` cells.
- ⚠️ **The file is QUOTED CSV inside a TSV.** Read and write it with `csv` (`delimiter='\t'`, `quotechar='"'`), and write with **`lineterminator='\n'`** and `QUOTE_MINIMAL` — the default terminator is `\r\n` and would put a stray carriage return on all 14 rows, a whole-file diff for a 4-character fix. ⚠️ **MEASURED, so you need not re-litigate it: under exactly those settings a pure parse-and-rewrite with NO edit is BYTE-IDENTICAL to the original (4,767 characters in, 4,767 out).** The round trip is safe; the settings are what make it safe.
- ⚠️ **`LESSONS.md` is in the governance ROOT repo** — `/Users/marklehn/Developer/GitHub/LESSONS.md` — read-only for this plan and not in your worktree.
- **`grep` here is ugrep: `-F` for every literal.** A zero-match `grep -c` prints `0` and EXITS 1 — read the printed count, never the exit status.
- ⚠️ **Prove each post-condition can FAIL before you edit** — run every assertion against the PRE-edit file and confirm it returns the failing value. `D2 = 12` and `D4 = 4` are exactly that proof; record them. ⚠️ **On the NOT-YET-APPLIED branch only** — the already-applied branch has no distinct pre-edit state to fail against, which is why the post-condition set is split by branch at Step 1. An earlier form of this bullet stated the requirement unconditionally, and the fix for it landed only in that Step-1 preamble.

## STEP 1 — DEV

**Role:** DEV.

**Task.** In `knowledge/research/bare-entry-ruling-2026-08-23.tsv`, in the `entry_heading` cell of entries **`123`** and **`330`** ONLY, replace every **U+2019 `’`** with **U+0027 `'`**. Change nothing else.

⚠️ **Do it cell-scoped, not file-wide** — `D5` says the two are equivalent on today's bytes, and the cell-scoped form is the one that stays correct if that stops being true.

⚠️⚠️ **CLASSIFY THE STARTING STATE THREE WAYS BEFORE WRITING ANYTHING — this step can be RE-DISPATCHED after a transient death, and a two-way check calls the applied state a broken premise.** Measured: after a successful apply the file has **0** U+2019 and **14/14** headings matching, so a re-run that only asks *is `D5` 4-of-4?* answers no and reports *the premise moved*, which is false.
- **4 U+2019, all in the two target cells, and 12/14 matching → NOT YET APPLIED.** Proceed.
- **0 U+2019 and 14/14 matching → ALREADY APPLIED.** Report it as an idempotent no-op, write nothing, and let the post-conditions pass on the existing bytes. This is a SUCCESS, not a halt.
- **Anything else → the premise genuinely moved. STOP and report what you measured.**


**Post-conditions — asserted after the write, and proven failable against the pre-edit file** ⚠️ *(the failability proof is available on the NOT-YET-APPLIED branch only; on the already-applied branch there is no distinct pre-edit state to fail against, and saying so is why the branch split below exists)*:
1. `entry_heading` values matching exactly one `"## " + heading` line in `LESSONS.md`: **12 → 14.** State both numbers.
2. U+2019 file-wide: **4 → 0.**
3. The verdict multiset (MUST-PRESERVE) is **identical** — print it before and after and diff.
4. ⚠️ **On the NOT-YET-APPLIED branch only** — `git diff --numstat` on the file shows exactly **`2\t2\t<path>`** — ⚠️ **determinate, not a range: entry `123` is data row 9 (file line 10) and entry `330` is data row 12 (file line 13), two distinct rows, so the edit is two insertions and two deletions.** An earlier form of this post-condition offered `1/1` and accepted `2/2` as also correct; a condition that accepts either value asserts nothing. `git diff` must contain **no `\r`** and touch no line but those two.
5. The file still parses to **14 rows** with the same 14 `entry_id`s.

⚠️⚠️ **THE TWO BRANCHES TAKE DIFFERENT POST-CONDITION SETS, and saying so is not a relaxation — an earlier form of this step required post-condition 4 unconditionally, which the already-applied branch CANNOT satisfy because it writes nothing.** On **NOT-YET-APPLIED**: all five as written, with (4) reading `2\t2`. On **ALREADY-APPLIED** the shape changes, and *hold as they would after a write* was too loose to act on — ⚠️ **(1) and (2) are TRANSITIONS (`12 → 14`, `4 → 0`) and there is no transition on a branch that writes nothing.** State them as END STATES instead: **(1) 14 headings matching, (2) 0 U+2019 file-wide**; (3) and (5) are already end-state assertions and are unchanged; and **(4) reads `0\t0` — an empty diff is the CORRECT and REQUIRED result there**, because the no-op branch's whole claim is that the file already carries the fix. ⚠️ **State which branch you took before reporting any post-condition**, so a reader can tell an idempotent no-op from a step that silently skipped its work.

⚠️⚠️ **IF ANY POST-CONDITION FAILS AFTER THE WRITE: do NOT commit, do NOT revert, and do NOT retry.** The three-way classification above guards the START; nothing guarded the finish. Leave the edited file uncommitted in your worktree, report every post-condition's measured value, and raise it under `### Flags for CEO` — `_gate_ceo_flags` turns a non-null flag into a blocking gate failure, which is the intended outcome. **The uncommitted state IS the evidence**: a revert destroys what a reader needs to diagnose, and a retry re-enters the three-way classification from a state that is now neither of the two clean ones. ⚠️ **On the ALREADY-APPLIED branch there is no edited file to leave, because nothing was written — that disposition assumes a write. There, simply report every measured value and flag it; the working tree stays clean and that cleanliness is itself part of the evidence** (a no-op branch that leaves a dirty tree has done something it did not declare). ⚠️ The most likely genuine cause is that one of the fourteen headings changed in `LESSONS.md` between your pre-check and your post-check — say which entry and what you measured, and do not adjust `Q`.

**Also check and REPORT (do not fix):** whether `bare-entry-ruling-2026-08-23.md` carries the same U+2019 drift in its `### <id> — <heading>` section headings. Those headings are explicitly NOT locators (506 keys the pointer assert on the id alone), so drift there is harmless — but the companion's author should know whether it exists.

**Deposits:**
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/research/bare-entry-ruling-2026-08-23.tsv`

**Scope:**
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/research/bare-entry-ruling-2026-08-23.tsv`

**Commit:** ⚠️ **WORKTREE DISCIPLINE.** You are dispatched into `lessons-forge/.bellows-worktrees/<id>/`. Edit and commit the file at its relative path under YOUR cwd: `git -C <your-worktree> add knowledge/research/bare-entry-ruling-2026-08-23.tsv && git -C <your-worktree> commit -m "..."`. ⚠️ Do NOT write to the main checkout — `gates._resolve_deposit_path` falls back to "path as-is" and `_check_deposit_uncommitted` swallows the out-of-worktree git error, so writing to the wrong checkout passes both gates SILENTLY and the teardown-merge never picks your file up.
