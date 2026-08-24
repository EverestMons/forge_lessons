# lessons-forge — CORRECTIVE to 506: restore byte-verbatim `entry_heading` for the two rows a typographic apostrophe broke

**Date:** 2026-08-24 | **Project:** lessons-forge | **Tier:** Small | **Dispatch Mode:** bellows | **cycle_tier:** T1 | **Test Scope:** none (data correction, no code) | **Execution:** Step 1 (DEV) | **Priority:** 1

**auto_close:** false
**pause_for_verdict:** after_step_1

**Depends on:** `Done/diagnostic-506.md` and its deposit `knowledge/research/bare-entry-ruling-2026-08-23.tsv` — **this plan CORRECTS two cells of that deposit and changes no verdict.** Newest same-class, MEASURED: `governance/…/Done/executable-505.md`, ship date 2026-08-23T19:42:41-05:00. Corrective precedent: `Done/executable-500.md` (the corrective to 499).

## Why this exists

`diagnostic-506` deposited a 14-row mapping whose `entry_heading` column the plan required to be the register's heading line **byte for byte** — because the companion executable's ONLY sanctioned locator is whole-line equality against `"## " + entry_heading`.

**Measured: 12 of 14 are byte-exact. Two are not.** Entries `123` and `330` carry **U+2019 `’`** where `LESSONS.md` carries **U+0027 `'`**, and both match **ZERO** lines in the register. They are exactly the only two of the fourteen containing an apostrophe at all.

⚠️ **All ten gates passed on that deposit and the Planner's Rule 22(b) check passed it too** — because every check run was a SET or a COUNT (id set equal to `Q`, 14 non-empty verdicts, 14 pointers resolving with zero dangling and zero orphans). None compared the heading BYTES to the register. A count cannot see a value that is wrong.

⚠️ **And 506's own round-trip proof was scoped to the wrong rows:** it mandated the check for the three quoted-CSV rows (`59`, `82`, `104`), all three of which ARE byte-exact. The drift landed in two rows nobody was told to check, from a different defect class.

## What this plan does NOT do

- **It changes NO verdict, class, target, mechanism or basis.** Only the `entry_heading` cell of entries `123` and `330`, and within those cells only the apostrophe character.
- **It does NOT normalize apostrophes anywhere as a matching rule.** ⚠️ Normalizing inside a lookup key is what orphaned 40 of 370 corpus rows at `exec-499`; the fix is to make the stored value correct, never to make the comparison lenient.
- **It does NOT edit `LESSONS.md`.** The register is correct; the deposit is wrong.

## Numbers discipline

⚠️ **RE-DERIVE every value; if yours differ, yours supersede and you say so.**

| id | pin | value | probe |
|---|---|---|---|
| D1 | rows in the TSV (data rows, excl. header) | **14** | `csv.DictReader(delimiter='\t', quotechar='"')` — ⚠️ the file is quoted-CSV-inside-TSV; a naive split-on-tab does NOT abort, it silently yields still-quoted values |
| D2 | `entry_heading` values byte-exact against `LESSONS.md` — **BEFORE** | **12** | for each row, count lines equal to `"## " + entry_heading` |
| D3 | …the two that are NOT | **`123`, `330`** | the complement of `D2` |
| D4 | U+2019 `’` occurrences in the WHOLE file — **BEFORE** | **4** | `raw.count('’')` on the file read as text |
| D5 | …of those, how many lie in the two target `entry_heading` cells | **4 — ALL of them** | per-cell count across every row and column |
| D6 | U+0027 `'` in those two cells — BEFORE | **0** | per-cell count |
| D7 | TSV sha256 — BEFORE | `53a804617370594a0353fb4f…` | `shasum -a 256` |
| D8 | file size / line count — BEFORE | **4821 bytes / 15 lines** | `wc -c` / `wc -l` |

⚠️ **`D5` is the measurement that shapes this plan: every typographic apostrophe in the file is already inside the two cells being corrected**, so a file-wide replacement and a cell-scoped one produce identical output HERE. **Do the cell-scoped one anyway** — it stays correct if the file ever gains a legitimate `’` elsewhere, and `D4 → 0` is then a post-condition rather than a coincidence.

## Drafting Cycle
**Tier:** T1 computed — **T-2** fires (writes real data: a deposited artifact a downstream executable consumes MECHANICALLY to edit the live register, so a wrong byte here propagates to `LESSONS.md`). T-1 does not fire (two cells, one file). T-5/T-6 do not fire — git-revertible, edits no doctrine, gate, template or contract.
**Walk register:** `governance/knowledge/research/walk-register-executable-bare-entry-heading-bytes.md`
**Walks:** walk 0 pinned; cycle OPEN.
**Walk 0 (context pin) — REAL, measured 2026-08-24:** newest same-class measured by ship date (505, 2026-08-23T19:42:41-05:00, ahead of 502 the same morning). **Anchors:** the two `entry_heading` cells, 4 characters total. **Occurrence counts:** U+2019 = 4 file-wide, all 4 inside those two cells (`D5`). **Last writer of the target lines:** `diagnostic-506`, closed to `Done/` 2026-08-24. **Target sha:** `D7`.
**Direction verdict (after walk 1):** owed.
- Weak spots:          w1 2 folded.
**Cold panel:** computed tier does not require one. Decide at the freeze and record the reasoning.
**Conformance (§5):** owed — `plan_lint` and `propagation_check` at the deposit resolution before the copy-in.
**Close:** not reached — the cycle is open. Restored to canonical form when earned.

## Cycle Manifest
tier: T1
target: knowledge/research/bare-entry-ruling-2026-08-23.tsv
class: governed-tooling
reads: /Users/marklehn/Developer/GitHub/LESSONS.md, /Users/marklehn/Developer/GitHub/lessons-forge/knowledge/research/bare-entry-ruling-2026-08-23.tsv, /Users/marklehn/Developer/GitHub/lessons-forge/knowledge/research/bare-entry-ruling-2026-08-23.md
writes: knowledge/research/bare-entry-ruling-2026-08-23.tsv
open_forks: (1) the companion executable is BLOCKED on this correction; (2) 506's findings document may carry the same drift in its `### <id>` section headings — out of scope here, checked and reported by this plan
walks: open
yields: open
validation: owed
coherence: owed — cycle open
N/A

## MUST-PRESERVE

- ⚠️⚠️ **EVERY DATE IN THIS PLAN IS A FIXED LITERAL.** The deposit filename carries `2026-08-23` and is NOT to be re-stamped; this plan was authored 2026-08-24 and may dispatch later.
- ⚠️⚠️ **NO VERDICT MAY CHANGE.** Assert it: the multiset of `(entry_id, class, target_artifact, mechanism, rule1_partly, rule2_circular, verdict, basis)` is IDENTICAL before and after. The only permitted delta is inside two `entry_heading` cells.
- ⚠️ **The file is QUOTED CSV inside a TSV.** Read and write it with `csv` (`delimiter='\t'`, `quotechar='"'`), and write with **`lineterminator='\n'`** and `QUOTE_MINIMAL` — the default terminator is `\r\n` and would put a stray carriage return on all 14 rows, a whole-file diff for a 4-character fix. ⚠️ **MEASURED, so you need not re-litigate it: under exactly those settings a pure parse-and-rewrite with NO edit is BYTE-IDENTICAL to the original (4,767 characters in, 4,767 out).** The round trip is safe; the settings are what make it safe.
- ⚠️ **`LESSONS.md` is in the governance ROOT repo** — `/Users/marklehn/Developer/GitHub/LESSONS.md` — read-only for this plan and not in your worktree.
- **`grep` here is ugrep: `-F` for every literal.** A zero-match `grep -c` prints `0` and EXITS 1 — read the printed count, never the exit status.
- ⚠️ **Prove each post-condition can FAIL before you edit** — run every assertion against the PRE-edit file and confirm it returns the failing value. `D2 = 12` and `D4 = 4` are exactly that proof; record them.

## STEP 1 — DEV

**Role:** DEV.

**Task.** In `knowledge/research/bare-entry-ruling-2026-08-23.tsv`, in the `entry_heading` cell of entries **`123`** and **`330`** ONLY, replace every **U+2019 `’`** with **U+0027 `'`**. Change nothing else.

⚠️ **Do it cell-scoped, not file-wide** — `D5` says the two are equivalent on today's bytes, and the cell-scoped form is the one that stays correct if that stops being true. Re-derive `D5` first; **if it is not 4-of-4, STOP and report** — a `’` living somewhere else means this plan's premise moved.

**Post-conditions, all asserted after the write and all proven failable against the pre-edit file:**
1. `entry_heading` values matching exactly one `"## " + heading` line in `LESSONS.md`: **12 → 14.** State both numbers.
2. U+2019 file-wide: **4 → 0.**
3. The verdict multiset (MUST-PRESERVE) is **identical** — print it before and after and diff.
4. `git diff --numstat` on the file shows exactly **`2\t2\t<path>`** — ⚠️ **determinate, not a range: entry `123` is data row 9 (file line 10) and entry `330` is data row 12 (file line 13), two distinct rows, so the edit is two insertions and two deletions.** An earlier form of this post-condition offered `1/1` and accepted `2/2` as also correct; a condition that accepts either value asserts nothing. `git diff` must contain **no `\r`** and touch no line but those two.
5. The file still parses to **14 rows** with the same 14 `entry_id`s.

**Also check and REPORT (do not fix):** whether `bare-entry-ruling-2026-08-23.md` carries the same U+2019 drift in its `### <id> — <heading>` section headings. Those headings are explicitly NOT locators (506 keys the pointer assert on the id alone), so drift there is harmless — but the companion's author should know whether it exists.

**Deposits:**
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/research/bare-entry-ruling-2026-08-23.tsv`

**Scope:**
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/research/bare-entry-ruling-2026-08-23.tsv`

**Commit:** ⚠️ **WORKTREE DISCIPLINE.** You are dispatched into `lessons-forge/.bellows-worktrees/<id>/`. Edit and commit the file at its relative path under YOUR cwd: `git -C <your-worktree> add knowledge/research/bare-entry-ruling-2026-08-23.tsv && git -C <your-worktree> commit -m "..."`. ⚠️ Do NOT write to the main checkout — `gates._resolve_deposit_path` falls back to "path as-is" and `_check_deposit_uncommitted` swallows the out-of-worktree git error, so writing to the wrong checkout passes both gates SILENTLY and the teardown-merge never picks your file up.
