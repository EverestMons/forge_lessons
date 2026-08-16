# Executable: QA-only corrective for plan 425's step 3 — the QA that never ran after an R2 teardown recovery

**Type:** Executable
**Date:** 2026-08-15 | **Tier:** Small | **Dispatch Mode:** bellows | **Test Scope:** targeted | **Execution:** Step 1 (QA — the only step) | **qa_steps:** 1 | **pause_for_verdict:** always
**cycle_tier:** T1
**Slug:** `cycle-classify-residual-bucket-2026-08-15-qa-corrective`
**Project:** lessons-forge
**dispatch_mode:** bellows
**Priority:** 1
**Depends on:** **`lessons-forge/knowledge/decisions/Done/executable-362.md`** — direct clone origin AND newest same-class (QA-only corrective, same project, Done 2026-08-12). The subject: `lessons-forge/knowledge/decisions/halted-executable-425.md` (steps 1–2 complete and landed; step 3 never dispatched) and its register `governance/knowledge/research/walk-register-cycle-classify-residual-bucket-2026-08-15.md`.

## Why
Plan 425's steps 1 and 2 **completed and their substance is landed**; step 3 (QA) **never ran**. The plan halted at the step-2 gate on `worktree_teardown` and the daemon routed it to `halted-` for manual R2 recovery, which the Planner performed: the worktree commit `8bfb954` was landed to main by fast-forward, the byte-identical untracked collision copy was confirmed redundant, and the worktree was removed. **A halted plan cannot resume, so the QA is re-dispatched against committed HEAD — the substance is NOT re-run.**

⚠️ **The teardown failure was caused by a PLAN defect, and this corrective must not reproduce it.** 425's step 2 mandated `output_dir` as an absolute path rooted at the MAIN repo (`…/lessons-forge/reports`) while the agent ran in a worktree, so the report was written outside the sandbox and collided with the merge. **This plan writes nothing outside its own worktree.** Its only deposits are the QA report and its evidence files, both under `knowledge/qa/`, both relative to the worktree root. ⚠️ **The path rule is stated ONCE, in Step 1's `<tree-abs>` binding paragraph, and this section deliberately does not restate it** — every path the agent WRITES is under the worktree; read-only reads (the canonical DB, and row 6's deliberate main-repo shasum) are exempt by design. *(w2-1: this sentence previously carried the blanket "anchor every path at `pwd`" that scout S0-13 corrected in the step body — the corrected site and the uncorrected one coexisted, and the blanket contradicted row 6's mandated absolute read.)*

## Scope
- **Read-only everywhere except this plan's own QA deposits:** the canonical DB via `?mode=ro` at an ABSOLUTE path; no writes to any table, any doctrine file, `LESSONS.md`, any FORWARD register, `reports/`, or `data/backups/`.
- `knowledge/qa/cycle-classify-residual-bucket-qa-2026-08-15.md`
- `knowledge/qa/evidence/cycle-classify-residual-bucket-2026-08-15/`
- Env facts: `grep` is a ugrep shim — `-F` for literals, a zero-count `grep -c` prints `0` and EXITS 1, and a bracket class like `[^*]*` stops at the first `*` and returns a FALSE EMPTY on bold markdown. ⚠️ **`grep -c "^| "` is CORRECT without `-F`** — adding `-F` makes `^` literal and returns 0. Shell state does not persist between invocations. `find`, never a glob. lessons-forge is its own git repo.

## What is already true — measured at authoring 2026-08-15, read-only, and to be RE-MEASURED by QA
| fact | value |
|---|---|
| lessons-forge HEAD | `b8b98e4` (step-2 commit `8bfb954` landed by fast-forward, then the halted- rename recorded) |
| proposal created | **353** — `entry_id=345`, `category=governance_rule`, `confidence=high`, `status='proposed'`, `route IS NULL` |
| P0 / COUNT proposals | **353 / 353** (moved 352 → 353; the write COMMITTED) |
| entries | **345**, unchanged |
| work list | `get_unclassified_entries()` == **`[]`** — the classify-plan inversion |
| NT id-set | **`{340,342,346,350,352,353}`** — the five pre-existing plus this one |
| STALE | **3** (98/121/130) |
| sentinel | entry **344**, `e7b607bd…` |
| the 08-15 report | tracked in main, **2593 bytes**, sha `b2128116…` |
| ⚠️ the AT-RISK artifact | `reports/lessons-report-2026-08-14.md`, sha **`f1807cf2…`** — byte-unchanged throughout the incident |
| FORWARD | **18** rows |
| suite | **55 passed** (`python3 -m pytest src/ -v` from the lessons-forge root) |
| `decisions/` non-Done | 1 — `halted-executable-425.md` (the subject; its disposition is NOT this plan's business) |

## Freeze checklist (deposit path — items 1–3 BEFORE the copy, item 4 immediately AFTER)
1. `plan_lint` at a FAITHFUL deposit-shaped scratch mirror — never the real `decisions/`; the measured `(o1)` set is the declared expected state.
2. A0-fresh: lessons-forge porcelain clean, `decisions/` contains only `halted-executable-425.md`, corpus values still as tabled above.
3. **Read `id_sequence` AT deposit** (read-only) and re-token every filename id site — it read **426** at authoring and this arc has watched it move three times.
4. **Residual-token probe:** `grep -cF -- '<id' <deposit>` and `grep -cF 'PIN-AT-FREEZE' <deposit>` — both 0 (an unresolved template token is malformed); and the deposited file is byte-identical to the linted mirror copy (`diff` empty). *(scout S0-9: both probes are 362's, dropped in the clone.)*
5. Post-deposit `ls`, then commit the daemon's claim rename so the tree is clean while the plan is in flight.

## Conflict Ledger
- **C1 — QA verifies, never repairs.** A failing check is reported as ❌ with its measured value. **No writes to the corpus, the reports, or the halted plan file.** *(observer: Scope; row 0 porcelain)*
- **C2 — every path the agent WRITES is under `<tree-abs>`; read-only reads exempt** (the rule's single site is Step 1's binding paragraph). *(observer: the QA report states `pwd` as its first evidence line, and the Rule 20 block's absolute paths resolve under it)*
- **C3 — the 08-14 report is byte-unchanged at `f1807cf2…`.** This is the artifact 425's whole guard existed to protect, and it survived the incident; QA re-asserts it. *(observer: row 6)*

## How to Run This Plan
**Bootstrap prompt:**
```
Read the plan at knowledge/decisions/in-progress-executable-<id>.md (the daemon renames the deposited placeholder on claim). Execute Step 1 ONLY. After completing Step 1, STOP and wait for my confirmation.
```

---

## STEP 1 — QA (the only step)

> **FIRST — post a short visible chat message; do NOT rename this plan file** *(scout S0-10: the do-not-rename mandate is 362's opening line and was dropped)*. You are Lessons Forge QA (`agents/FORGE_LESSONS_AGENT.md`). Own working tree; canonical DB **read-only** (`?mode=ro`, ABSOLUTE path). **Verification and reporting only — a failing check is reported, never fixed. No Monitor. No classification. No routing.**
>
> ⚠️ **First evidence line is `pwd`.** You run in a worktree. **`<tree-abs>` in this plan is DEFINED as that `pwd` output** — bind it once, echo the binding, and **HALT if it equals `/Users/marklehn/Developer/GitHub/lessons-forge`** (that would mean you are NOT in a worktree, and every write would land in main). *(scout S0-2: `<tree-abs>` was unbound, and the main repo is the guessable binding — the exact sandbox-escape class this plan corrects.)* **Every path you WRITE is under `<tree-abs>`. Reads of the canonical DB use its mandated absolute path — read-only reads are exempt from the anchor rule by design** *(scout S0-13: the blanket "anchor every path at pwd" contradicted the absolute DB read one paragraph above it)*.
>
> **⚠️ A0 — the subject-state precondition, narrowly keyed, first match wins.** Before any row, verify against the canonical DB read-only and the repo: (1) **proposal 353 exists** with `entry_id=345, status='proposed', route IS NULL` AND `COUNT(*) FROM lesson_proposals` == 353 AND `get_unclassified_entries()` == `[]` AND main HEAD contains `8bfb954` → **PROCEED**. (2) proposal 353 **absent** → HALT: the classification did not land and this corrective has nothing to verify. (3) proposal 353 present but `route IS NOT NULL` → HALT: something ROUTED it, which Gate 1 has not yet done. (4) `COUNT(*)` > 353, or any extra row with `entry_id > 344` → HALT naming every id: a foreign writer. (5) main HEAD does NOT contain `8bfb954` → HALT: the R2 recovery did not land and the deposits under verification are not in HEAD. **(6) ANY OTHER STATE — including a 353 whose `status` is anything but `'proposed'` (`'ambiguous'` is legal per the DDL), a non-empty work list, or a COUNT below 353 → HALT, quoting the full measured row.** *(scout S0-1: the recovering fold rebuilt A0 with five specific arms and lost the universal catch-all; `status='ambiguous'` matched NO arm — an A0 without a floor is a table again, not a gate.)* ⚠️ **State the determination and its measured values FIRST, before writing anything.** *(w0-1: parent 362 opens with exactly such an A0 and this clone carried only a passive state table — a table records, a gate stops.)*
>
> **⚠️ ORDER IS LOAD-BEARING** *(w0-2: 362 spells this out because its own subject plan skipped it; spelled here for the same reason, even though this plan's subject skipped QA entirely rather than skipping the block)*: **(i)** run every row check and write **EVERY file named in `required_evidence_files`** — the list is the single count site *(w2-2: this clause said "ALL FIVE" against a six-file contract after the S0-8 fold — the third occurrence of the stale-count-in-prose class in two days; de-numerated rather than re-counted)*; **(ii)** write the report with its complete verification table; **(iii)** ONLY THEN run the Rule 20 block and APPEND its stdout; **(iv)** end with the self-grep. The block exits nonzero on missing files, so any other order fails mechanically.
>
> **Rule 20 self-check** (canonical block from `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md`): `plan_slug` `cycle-classify-residual-bucket-2026-08-15-qa-corrective`; `qa_report_path` `<tree-abs>/knowledge/qa/cycle-classify-residual-bucket-qa-2026-08-15.md`; `evidence_dir` `<tree-abs>/knowledge/qa/evidence/cycle-classify-residual-bucket-2026-08-15/`; `required_evidence_files` `["pytest_targeted.txt", "proposal.txt", "queue-untouched.txt", "report.txt", "schema.txt", "recovery.txt"]` *(scout S0-8: rows 0, 10 and 12 previously wrote to no evidence file the Rule 20 block checks — row 0 and 12 output now lands in `recovery.txt` alongside row 10's)*. EVERY file in `required_evidence_files` AND the report with its table written BEFORE the block; APPEND the stdout; banner `Rule 20 — QA Self-Check Results` + `PASSED — SELF-CHECK PASSED` verbatim; end with the self-grep. Rule 19 verbatim; one glyph per status cell; no `|` in cells; `## Evidence and Narrative` immediately after the table.
>
> **Scope:**
> - `knowledge/qa/cycle-classify-residual-bucket-qa-2026-08-15.md`
> - `knowledge/qa/evidence/cycle-classify-residual-bucket-2026-08-15/`
>
> Table under `## Verification Table`, columns `| # | Claim | Status (✅/❌) | Measured value | DB source | Evidence |` — **run ALL rows before halting.** These are 425's step-3 rows, re-pointed at committed HEAD:
> 0. **Deliverables (Rule 17)** — for 425's landed deposits (`knowledge/development/dev-log-classify-residual-bucket-step-1-2026-08-15.md`, `…-step-2-…md`, `reports/lessons-report-2026-08-15.md`): `git log --oneline -1 -- <path>` non-empty AND `git status --porcelain -- <path>` empty.
> 1. **Targeted suite** — `python3 -m pytest src/ -v`, raw tail → `pytest_targeted.txt`; value cell `<N> passed` ONLY. Run **from `<tree-abs>`** (the worktree root — *scout S0-15: "the lessons-forge root" was ambiguous between main and the worktree*). Baseline **55 passed**, measured by this row's own command. A delta is reported with both numbers, never asserted away — ⚠️ and a delta is a FINDING to report, not a failure of this row by itself.
> 2. **Exactly ONE proposal, correctly shaped** — `SELECT id, entry_id, category, confidence, status, route FROM lesson_proposals WHERE id = 353` → one row, `entry_id=345`, `route IS NULL`, `status='proposed'`; `COUNT(*)` == **353**. → `proposal.txt`
> 3. ⚠️⚠️ **The Gate-2 queue is UNTOUCHED** — the pre-existing five `340,342,346,350,352` all still `accepted|codify` **by id set, not by count**; STALE still 3; sentinel entry-344: **compare the `content_hash` COLUMN value to `e7b607bd…` — never recompute it naively; the column is sha256 over `_normalize_for_hash(raw_content)`, and a bare `sha256(raw_content)` returns `2c942a8e…`, a FALSE mismatch on a true state** *(scout S0-6, reproduced at authoring)*; entries still 345. → `queue-untouched.txt`
> 4. **`reasoning` carries all three markers** — `grep -Fc` each of `[DEDUP]`, `[REMEDY-GATED]`, `[AUTHOR-CONFLICT]` in the field read from the DB → each **1**. ⚠️ **Presence only; adequacy is Gate 1's judgement, not QA's.** → `proposal.txt`
> 5. ⚠️⚠️ **`get_unclassified_entries(conn)` == `[]`** — the classify-plan inversion. A non-empty list means classification did not complete. → `proposal.txt`
> 6. ⚠️⚠️ **The at-risk artifact survived — measured IN MAIN, read-only** — `shasum -a 256 /Users/marklehn/Developer/GitHub/lessons-forge/reports/lessons-report-2026-08-14.md` == **`f1807cf266b369541ce5ae56f17e83966e354dd36d0ac8daa7ec73d4ec454c85`**. ⚠️ **The absolute MAIN-repo path is deliberate and READ-ONLY** *(scout S0-3: a relative shasum measures the worktree checkout, which equals the blob by construction — it can only agree with HEAD and proves nothing about the file the incident put at risk)*. And `reports/lessons-report-2026-08-15.md` (relative — the tracked copy) exists and surfaces **1** proposal. → `report.txt`
> 7. **Report content** — zero `- **Route:**` lines (`grep -Fc -- '- **Route:**' <report>; echo "EXIT=$?"`, both `-F` and `--`, never piped to `head`); zero `Recently-implemented` lines (`grep -Fc -- 'Recently-implemented' <report>; echo "EXIT=$?"` — same echoed-exit form as the Route check; a bare zero-count grep exits 1 and a `&&` chain would misread it); and the entry's DOUBLE-QUOTED phrase `"everything else"` appears intact in the report, joined against the DB heading **bound as a query parameter**. → `report.txt`
> 8. **The 8-status distribution — against THIS pinned baseline** *(scout S0-7: "the pre-cycle baseline" named no numbers and was undecidable)*: implemented **281** · superseded **28** · reference **20** · rejected **15** · accepted **5** · **proposed 1** · stale **3** · ambiguous **0** — total **353**. Every bucket equal; a total count cannot see a row moving between terminal buckets. → `queue-untouched.txt`
> 9. **No schema drift** — PRAGMA table_info + constraints vs `src/db.py` DDL; raw `.schema` both tables → `schema.txt`
> 10. ⚠️ **R2 recovery is clean — and a BROKEN recovery must FAIL this row** *(scout S0-3)*: (a) `git -C /Users/marklehn/Developer/GitHub/lessons-forge worktree list` shows NO worktree for **425** — ⚠️ **your OWN worktree (this plan's id) WILL appear; its presence is correct, not a failure** *(scout S0-14)*; (b) main HEAD contains `8bfb954`; (c) **`git -C /Users/marklehn/Developer/GitHub/lessons-forge status --porcelain`, read-only against MAIN, is EMPTY — or contains EXACTLY this plan's own claim-rename pair** (` D knowledge/decisions/executable-<id>.md` + `?? knowledge/decisions/in-progress-executable-<id>.md`) **and nothing else**. ⚠️ The pair is EXPECTED, not a failure: the daemon renames on disk within a second of claim and the Planner's rename commit can land after this row runs — the window was observed live at plans 423 and 425 *(w1-1: the S0-3 fold's unqualified EMPTY would have failed a correct run — a post-condition that fails on correct execution is as broken as one that passes on incorrect)*. **Any OTHER porcelain line is the finding this check exists for** — leftover collision debris from the recovery, invisible to every other row; (d) the TOP-LEVEL PLAN FILES of `decisions/` are exactly `halted-executable-425.md` plus this plan's own `in-progress-*` file *(scout S0-5: the subject's own row said "this plan's own file only" and the clone dropped the self-reference; and the raw `find` also returns `.gitkeep`, `Done/`, `archived-halted-plans/` — enumerate `-maxdepth 1 -name '*.md'` only)*. **Report the halted file's presence; do not move, rename or dispose of it.** → `recovery.txt`
> 11. **The DISPOSITION line** — `grep -Fc -- 'DISPOSITION | entry=345' <tree-abs>/knowledge/development/dev-log-classify-residual-bucket-step-1-2026-08-15.md` → **1**, and the line carries `proposal=353` and all three marker names. *(scout S0-4: this row was 425's step-3 row 8, the designed reader of that line — and this corrective is the LAST QA that will ever read it; without this row "these are 425's step-3 rows" was false.)* → `proposal.txt`
> 12. **Register posture** — `knowledge/FORWARD.md` is **18** rows by `grep -c "^| "` (⚠️ NOT `-F`).
>
> `## Evidence and Narrative` · Receipt · `### Ledger Updates` · `#### Prompt Feedback` · `#### Forward Register`: `NONE`. **FINAL ACTION** — commit deposits: cd-absolute in the same compound as the commit, explicit pathspec; post-commit assert by **`git log --oneline -1 -- <each deposit path>`** (never a bare `HEAD` show — *scout S0-11: 362 forbids keying the assert on HEAD, which a concurrent commit can move*) + bare `git rev-parse --show-toplevel`.
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/cycle-classify-residual-bucket-qa-2026-08-15.md`
> - `lessons-forge/knowledge/qa/evidence/cycle-classify-residual-bucket-2026-08-15/pytest_targeted.txt`
> - `lessons-forge/knowledge/qa/evidence/cycle-classify-residual-bucket-2026-08-15/proposal.txt`
> - `lessons-forge/knowledge/qa/evidence/cycle-classify-residual-bucket-2026-08-15/queue-untouched.txt`
> - `lessons-forge/knowledge/qa/evidence/cycle-classify-residual-bucket-2026-08-15/report.txt`
> - `lessons-forge/knowledge/qa/evidence/cycle-classify-residual-bucket-2026-08-15/schema.txt`
> - `lessons-forge/knowledge/qa/evidence/cycle-classify-residual-bucket-2026-08-15/recovery.txt`

---

## Drafting Cycle
**Tier:** T1 — read-only verification, structure-clone of shipped 362. ⚠️ T-5 does not fire: this plan deletes nothing and writes only its own QA deposits.
**Walk register:** `governance/knowledge/research/walk-register-qa-corrective-residual-bucket-2026-08-15.md` *(slug-keyed — scout S0-12: the draft's register name keyed on the bare id 425, colliding with the subject's own register namespace)*, **schema v0.3** — carrying a literal `**schema_version:** \`0.3\`` line ABOVE any table row, which is what `walk_register_lint` keys on. *(Earned the hard way this session: a register whose title said "(schema v0.3)" and whose prose claimed conformance still reported `PRE-SCHEMA`.)*
**Status:** cycle CLOSED 2026-08-15 on a fully DRY walk. Walk count, fold count and per-finding detail live ONLY in the register.

**Per-lens lines** *(required by §3 and `plan_lint`; outcome-only — ids and dispositions live in the register)*:
- **Weak spots:** findings at walks 0–2 (the A0 floor, unbound `<tree-abs>`, undecidable baselines, the surviving anchor blanket); final walk dry.
- **Destruction:** the cycle's headline — a broken R2 recovery would have PASSED every row; the shasum measured the wrong copy and no row read main's porcelain. Corrected; final walk dry.
- **Vulnerabilities:** the sentinel-recompute trap (reproduced, not assumed), the rename-race window (observed live twice), the echoed-exit forms; final walk dry.
- **Integration-record:** dominated by origin-carried-by-OMISSION against parent 362, plus the stale-count and unswept-fold classes; final walk dry.
- **ACID:** dry at every walk — single step, fresh deposit paths, one create.

**Closing:** the final walk read **DRY on all five lenses — instruction 0 / record 0**, with no restructuring fold, so §2's bar is met on a dry pass and there is no residue to enumerate. Evidenced: **18 of 18** load-bearing values re-verified against live state at close (the proposal's full shape; P0 and COUNT; entries; the empty work list; the NT id-set; STALE; the sentinel column; its normalized recompute equal to that column; the pinned 8-status distribution; the at-risk 08-14 sha live and in-plan; the tracked 08-15 report at 2593 bytes; HEAD ancestry of `8bfb954`; no 425 worktree; FORWARD; the `decisions/` top-level set; the DISPOSITION line; the suite; main porcelain); **all 20 finding attributions in the body resolve to register rows**; faithful-mirror `plan_lint` at close carries only the one mirror-fidelity `(o1)` (the step-1 dev log, verified real in the project). Fold-and-deposit exactly once.
**Walks:** recorded in the walk register, the single site for walk count, fold count and per-finding detail.
