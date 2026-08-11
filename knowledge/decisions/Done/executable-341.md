# Executable: lessons-forge Forward Register — void-row status sweep (rows 2, 6, 10, 11)

**Type:** Executable
**Project:** lessons-forge
**Depends on:** **executable-293** (governance, Done 2026-08-02 — ⚠️ **the POST-cutover precedent for a dispatched agent writing `knowledge/FORWARD.md`**; its Scope is exactly this path, and it is the clone origin for the write itself), **executable-18** (invoice-pulse, Done — the prior dispatched FORWARD-register *amendment*, ⚠️ **PRE-CUTOVER**, a shape reference only; see the Exception), **executable-294** (bellows, Done, 2026-08-03 — shipped the bullet-aware splitter whose residue is row 8, the row this plan deliberately does NOT act on), **executable-311** (lessons-forge, Done — its dup-append produced rows 9/10), **executable-339 / executable-340** (lessons-forge, Done — the split whose two QA steps each emitted the same item, producing rows 11/12). DRAFTING_CYCLE at **v2.0**.
**Created:** 2026-08-10
**Author:** Planner
**Slug:** `forward-dup-sweep-2026-08-10` (stable across any crash-redo re-deposit — the Task A4 re-entry key and the Rule 20 `plan_slug`)
**dispatch_mode:** bellows
**pause_for_verdict:** always
**Priority:** 10
**cycle_tier:** T1
**qa_steps:** 2
**Test Scope:** targeted — **no code, no tests, no DB.** One markdown register, four Status cells. The lessons-forge suite is NOT run: there is nothing in this change a test can observe, and running it would only manufacture an evidence file that proves something else.

⚠️ **ID NOTE — the deposit filename is decided AT DEPOSIT.** `id_sequence` read **341** at authoring (2026-08-10, `bellows/lifecycle.db`). **Re-read it at deposit and re-token every filename site.** ⚠️ **This plan's own id is also a VALUE it writes** (row 6's `closed-by-plan-N`) — see Task A7, which derives it rather than carrying a literal.

---

## Why this exists

`lessons-forge/knowledge/FORWARD.md` carries **twelve rows, all `open`**, and **four of them are void** — they record no live work:

- **Row 2** — `(Three items listed above under Forward Register section.)` — a parser artifact recording zero items. The three real items are rows 3/4/5, same date. **Row 6 has been asking for exactly this since 2026-08-03:** *"Row 2 of this register is a parser artifact recording zero items and should be superseded."*
- **Rows 9 / 10** — **byte-identical**, 227 characters each (measured at authoring). Plan 311's known dup-append.
- **Rows 11 / 12** — ⚠️ **NOT identical: 237 vs 252 characters.** Row 11 says *"this **plan** carried 42 such rows and guarded them procedurally"*; row 12 says *"this **cycle** carried 42 such rows and guarded them procedurally **at five sites**."* **Row 12 is strictly more informative, so row 11 is the copy that goes** — arrival order would cost content here.

**The status value needs no invention.** `withdrawn` already exists in the sibling register (`bellows/knowledge/FORWARD.md` rows 16, 23, 24, dated 2026-06-12 and 2026-06-14) with exactly the right meaning: *this row is void as a work item; no plan closed it.* Rows 23/24 were canary artifacts; row 16 was moot on arrival. **Verified at authoring: no code reads the Status column** — `grep -F` over `bellows.py`, `gates.py` and `bellows/scripts/*.py` for `closed-by-plan` / `closed-reconciled` / `withdrawn` returns empty at exit 1. ⚠️ **Paired with a same-instrument positive control per §2.7's (D) standard, because a bare negative may not support a finding:** the identical invocation over the identical files for `_append_forward_row` returns two hits at exit 0. **The instrument speaks; the absence is real.** The daemon writes `open` at append and never reads a status back.

**Sequencing, stated as what it is:** Gate 1 for proposals 274–314 emits five new rows into this file. ⚠️ **There is no MECHANICAL block** — the daemon would append them regardless, and nothing breaks. The reason to sweep first is that the CEO's Gate-1 decision made this the ordering, and interleaving five new rows with four void ones makes the register harder to audit at exactly the moment its auditability is the point. **A preference with a reason, not a dependency.**

## ⚠️⚠️ EXCEPTION — a dispatched agent edits `knowledge/FORWARD.md`, and this plan states why

**`PLANNER_TEMPLATE.md:376` rule (1) forbids it:** *"Agents do NOT write to `agent-prompt-feedback.md`, `PROJECT_STATUS.md`, or `knowledge/FORWARD.md` directly."* **This plan is a deliberate, bounded exception, and the reason is that no authorized path exists:**

1. **The Receipt channel cannot do this.** It is append-only and hardcodes `status="open"` (`bellows.py:_append_forward_row`). It can add a row; it cannot change one.
2. **Rule 42's Planner-direct path has no branch for it.** Read at source (`PLANNER_TEMPLATE.md:983-996`): the procedure is *closing plan found → `closed-by-plan-[id]`*, *not found → **no action***. There is no third branch for a row that is **void** rather than **closed**. Three of this plan's four edits are exactly that case.
3. **⚠️⚠️ RETRACTED AND RESTATED — the first version of this clause was FALSE, and it is corrected here rather than quietly dropped.** It claimed *"no post-cutover precedent exists — every dispatched plan that edits a FORWARD register is id ≤ 63."* **That came from a `grep -rl` over `Done/` that was truncated at 20 hits and unsorted; the id range was read off a sample, not a population.** A tight re-probe (FORWARD.md appearing INSIDE a `**Scope:**` or `**Deposits:**` block, all projects) returns six plans — 14, 15, 16, 17, 18 and **`executable-293` (governance, closed 2026-08-02, POST-cutover), whose Scope is exactly `knowledge/FORWARD.md` and which CREATED this register with a dispatched agent.**
   **The true, narrower claim:** a dispatched agent writing this path has post-cutover precedent (293). **What has no precedent, pre- or post-cutover, is UPDATING AN EXISTING ROW'S STATUS** — 14–18 and 293 all CREATE or APPEND. **That is still a novel operation, so T-8 still fires** — but the exception being taken is narrower than the retracted clause claimed, and a reader is entitled to the smaller version.

**The exception is bounded to STATUS CELLS in ONE file.** An agent that edits Item text, adds a row, deletes a row, or touches any other ledger has left this plan → **HALT.**

⚠️⚠️ **WHAT THIS RE-TRIPS, STATED PLAINLY — the agents-don't-write rule is not an arbitrary convention, it is the product of a deliberate multi-plan effort.** The daemon-owned-ledgers architecture (diagnostic 42; plans 45/56/57/61/62/63) moved every ledger write to the daemon **specifically to eliminate the append-only worktree-conflict class**: bellows FORWARD rows **4, 5 and 13** are all *"worktree teardown cherry-pick conflict"* / *"parallel-diagnostic cherry-pick conflicts on shared append-only bookkeeping files at teardown"*, all closed 2026-06-14 with that single reason.

**This plan edits `knowledge/FORWARD.md` inside a worktree that is cherry-picked onto `main` at teardown — the exact operation that class describes.** It is safe here only because of a condition that must be checked, not assumed:

⚠️ **PRECONDITION — no other plan may be in flight against `lessons-forge` while this runs.** Verified at authoring 2026-08-10: `lessons-forge/knowledge/decisions/` carries only `halted-executable-334.md` (parked), and the bellows verdict queue is empty. **A concurrent plan emitting a Receipt row would have the daemon append to this same file on main while this plan holds a modified copy in a worktree — and teardown would conflict on it.** If a second plan is dispatched against lessons-forge before this closes, **stop this one rather than racing it.**

⚠️ **The doctrinal repair is queued, not performed here:** a Rule 42 third branch — *a row that is void rather than closed (duplicate, parser artifact, canary, moot-on-arrival) takes `withdrawn`, with the superseding row named* — rides the `PLANNER_TEMPLATE.md` Gate-2 batch. **An agent must NOT "fix" this by editing `PLANNER_TEMPLATE.md` or `RULE_20_SELF_CHECK_BLOCK.md` — that is a HALT.**

## Scope

- **Edits exactly ONE file:** `knowledge/FORWARD.md`, **addressed relative to `$ROOT`**.
- ⚠️⚠️ **`$ROOT` IS DERIVED, NEVER HARDCODED — every step of this plan runs in a bellows worktree.** Measured 2026-08-10: plan 340's step ran under a `.bellows-worktrees/<plan-id>` checkout, not at the main tree. **A command addressed to `/Users/marklehn/Developer/GitHub/lessons-forge` therefore reads the MAIN tree — which does not carry this step's commit until post-merge — and Q0 would pin the wrong repository entirely.**
  **Every step's FIRST action:** `ROOT=$(git rev-parse --show-toplevel)`; assert `pwd -P` equals `$ROOT` (`cd "$ROOT"` and re-assert if not); then **identify the repo by CONTENT, not by path**: `$ROOT/knowledge/FORWARD.md` exists and its **first line is exactly `# Lessons Forge — Forward Register`**. **Print `$ROOT` and that line into the receipt.**
  ⚠️⚠️ **An earlier draft of this clause asserted `$(basename $(git rev-parse --git-common-dir))` "resolves under a `lessons-forge` checkout". MEASURED 2026-08-10: that command returns `.git`, so the assertion could NEVER pass** — a check that fails a correct run, and the fourth instance of that class in this cycle. **A path-shaped identity test is the wrong instrument here anyway: a worktree's path is `…/lessons-forge/.bellows-worktrees/<id>`, so any basename test needs a special case the content test does not.** ⚠️ **The ONE deliberate absolute path in this plan is `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md`** — the governance root is not a worktree and must not be `$ROOT`-relative.
- **Four Status cells change. Nothing else in the file changes** — not Item text, not `Added`, not `Type`, not `Plan-id link`, not the preamble, not the header row.
- ⚠️⚠️ **THE HEADER ROW AND THE `|---|` SEPARATOR ROW ARE BYTE-PINNED — recovered by clone-diff against `executable-293`, which pins them and calls them load-bearing.** This plan's assertions all address the twelve DATA rows; **a rewrite that mangled the header or the separator would pass every one of them.** Assert both lines byte-identical pre/post, and the whole non-data remainder of the file (preamble + blockquote + `---`) byte-identical too. **Compare the file's NON-DATA lines as a block, not row by row** — that is the only test that also catches an inserted or deleted blank line.
- ⚠️ **`PLANNER_TEMPLATE.md:993` is binding: *"The table is append-only for auditability; do not delete closed rows."*** **NO row is deleted.** A sweep that removes a duplicate instead of withdrawing it is the reversed-deletion class and is a HALT.
- ⚠️ **DO NOT STRIP THE LEADING `- ` MARKER from any Item.** Measured at authoring: **rows 3, 4, 5, 6, 7, 8, 11 and 12 carry it — eight rows, not the two the handoff named.** Stripping two of eight would make the register *more* inconsistent, and it is an Item-text edit, outside this plan's warrant. ⭐ **The markers are row 8's live specimen** — row 8 records this exact bug, was filed 2026-08-03, is still open, and its class re-fired on 2026-08-10 on rows 11/12. **Row 8 is NOT touched by this plan.**
- ⚠️⚠️ **THIS PLAN EMITS NO `#### Forward Register` ROWS, IN EITHER STEP.** The daemon appends Receipt rows to this same file post-merge; a row emitted here would land as row 13 and **correctly** fail this plan's own row-count assertion. If a step believes a FORWARD item is owed, it reports it in the narrative and does not emit it.
- **No LESSONS.md touch. No DB write. No push** — commit only.

### ⚠️ Environment facts — observed, not predicted

1. `grep` here is a **ugrep shim**: `-F` is mandatory for every literal, and a non-`-F` search **exits 1 silently on a line that is present** — so exit 1 is never a safe "absent".
2. ⚠️⚠️ **THE PARSE CONTRACT — every read and every write in this plan uses it, and nothing else.** No `grep`/`sed`/`awk` one-liner touches this table.
   - **Data row** = a line matching `^\|\s*\d+\s*\|` (line-anchored).
   - **First cell** (the row number): `line.strip().strip('|').split('|', 1)[0].strip()`.
   - **Last cell** (Status): the field after the FINAL interior `|` — take it with `rsplit`, never by indexing a fixed field count.
   - **Item cell**: the 2nd field of the 6 a data row yields. ⚠️ **Measured 2026-08-10: all 12 rows yield exactly 6 fields, so no Item currently contains a `|`** — the fragility is latent, not live. **It will not stay latent: Gate 1 appends five prose rows to this file next.** Treating the middle as opaque and addressing only the first and last cells is what survives that.
   - ⚠️ **Assert EXACTLY ONE line matches each target row number. Zero or two → HALT** — a silent first-match wins is how the wrong row gets edited.
   - ⚠️⚠️ **`encoding="utf-8"` EXPLICITLY on EVERY read and EVERY write — including content recovered from `git show`/`git cat-file`, which arrives as bytes and must be decoded explicitly, not by locale default.** The file carries em-dashes, `§` and backticks; a whole-file rewrite under a locale-default codec mangles every one of them silently, and that is the destruction class this plan exists to avoid. ⭐ **The register's own row 3 records this exact bug class in this project** (`generate_lessons_report` writing with no explicit `encoding=`).
   - **The sha1 pins below are `hashlib.sha1(item_cell.strip().encode("utf-8")).hexdigest()[:12]`** — computed on the Item cell as this contract extracts it, and on nothing else. ⚠️ **A pin computed over the raw line, or without the strip, fails every row on a CORRECT run.**
3. Shell state does NOT persist between commands — assign and use in the same invocation.
4. A zero-match `grep -c` prints `0` and exits **1** — the printed count is the assertion, not the exit code.

---

## The four edits

**Row identity is the FIRST table cell, matched as an exact integer — never by Item text.**

| row | Status from | Status to | reason |
|---|---|---|---|
| **2** | `open` | `withdrawn` | parser artifact recording zero items; superseded by rows 3–5 |
| **6** | `open` | `closed-by-plan-<N>` | its ask is discharged by this plan. ⚠️ **Row 6 literally asks that row 2 be *"superseded"*, and this plan writes `withdrawn` instead.** Measured 2026-08-10 across all six registers: `superseded` appears **0** times as a status, `withdrawn` **3** times (same-instrument positive control). **Writing `superseded` would invent a value — the precise error this sweep exists to avoid — so row 6's ask is honoured in substance with the vocabulary that exists.** **`<N>` is DERIVED, see Task A7** |
| **10** | `open` | `withdrawn` | byte-identical duplicate of row 9 (plan 311 dup-append), `sha1:7ace3a3fc14f` both. ⚠️ **Which copy goes is ARBITRARY — they are the same bytes.** Fixed here as *withdraw the higher row number*; **row 9 survives** |
| **11** | `open` | `withdrawn` | near-duplicate of row 12, whose text is strictly more complete; **row 12 survives** |

**Rows 1, 3, 4, 5, 7, 8, 9 and 12 remain `open` and untouched.**

⚠️⚠️ **THE STATUS LITERALS ARE BYTE-EXACT, LOWERCASE, AND CARRY NOTHING ELSE.** The cell holds `withdrawn` or `closed-by-plan-<N>` — **not `Withdrawn`, not `withdrawn ` with a trailing space, not `withdrawn (dup of row 9)`.** An annotated or case-variant cell reads as neither open nor closed to every human and every future reconciliation pass, and a `.lower()`-ing or substring-matching check would wave it through. **Every assertion on these cells compares the STRIPPED cell for EQUALITY against the exact literal, case-sensitively.**

**Expected final distribution, MEASURED at authoring 2026-08-10 and stated as a measurement with a timestamp, never a constant: 12 rows, all `open` → 8 `open`, 3 `withdrawn`, 1 `closed-by-plan-<N>`.**

⚠️⚠️ **Every downstream assertion is RELATIVE to Step 1's Task-A capture, not to these literals.** A wrap reconciliation or a Receipt append between authoring and dispatch legitimately moves the totals, and an "exactly 12" post-condition would then **fail a correct run** — which is batch entry 289's measured class (*a check that fails a correct run is a check an agent will loosen*), committed against the plan that ingests it. **The invariants that actually bind are: `rows_after == rows_before`, `open_after == open_before − 4`, `withdrawn_after == withdrawn_before + 3`, and the four named cells by row number.**

---

## STEP 1 — DEV

> ⚠️⚠️ **TASKS A0/A/B WERE COLLAPSED INTO ONE ORDERED TASK A AT WALK 3.** Across three walks that region took **eleven** findings — every patch individually correct, and each one re-created a forward reference (A0 invoking a discriminator that lived in Task A; a landed branch skipping the baseline it needed; two clauses each claiming to run "first"). **Repeated folds on one region are a signal to restructure it, not to patch it again.** The rule below is what makes that hold: **Task A has no forward references. Every value it needs is established by an earlier numbered sub-step in the same task.**

> **Task A — ESTABLISH STATE. Nothing else runs until this completes.** Execute A1–A7 in order.
>
> **A1 — Resolve the tree.** `ROOT=$(git rev-parse --show-toplevel)`; assert `pwd -P` equals `$ROOT` (`cd "$ROOT"` and re-assert if not). **Identify the repo by CONTENT:** `$ROOT/knowledge/FORWARD.md` exists and its first line is exactly `# Lessons Forge — Forward Register`. **Print `$ROOT` and that line.** Once A1 holds, `knowledge/FORWARD.md` and `$ROOT/knowledge/FORWARD.md` are the same file and either form may be used.
>
> **A2 — Sweep the stray.** If a **`FORWARD.md.new` sibling beside the register** exists it is debris from a died dispatch — **delete it and say so.** It is never a source of truth, and QA row 8 asserts its absence.
>
> **A3 — Read the live state, and record every field before classifying anything.** From the live file: the **Status cell of rows 2, 6, 10, 11**; `git -C "$ROOT" status --porcelain -- knowledge/FORWARD.md`; `git -C "$ROOT" log -1 --oneline -- knowledge/FORWARD.md`. **Print all of it.**
>
> **A4 — Classify, using ONLY A3's output. Default-deny.**
> - **All four cells `open`** → **CLEAN**, ⚠️ **and A3's porcelain output MUST be empty — a non-empty porcelain on this branch means an uncommitted foreign edit to `FORWARD.md`, so `PRE_EDIT_BLOB` would pin a state nobody committed and every later comparison would rest on it. Non-empty here → HALT.** *(This guard existed before the walk-3 collapse and the collapse dropped it; recovered by diff review.)*
> - **All four carry their target values** *(for row 6 the test is `^closed-by-plan-\d+$`, **NOT** equality with this dispatch's `<N>` — the slug is the stable crash-redo re-entry key, so a re-deposit mints a new id while the register still carries the old one; matching on `<N>` would false-HALT the exact recovery this branch exists for. ⚠️ **Report the id found beside the id derived, LEAVE THE RECORDED VALUE IN PLACE, and do not "repair" it** — it names a real plan that really did the work. Also dropped by the collapse and recovered by diff review)* → **LANDED**, and A3's porcelain output splits it: **non-empty → LANDED-UNCOMMITTED**; **empty AND `HEAD` is this plan's own commit → LANDED-COMMITTED** *(⚠️ **the test, because a named condition with no test is not a check:** `git -C "$ROOT" log -1 --format=%s` contains the literal slug `forward-dup-sweep-2026-08-10` **AND** `git -C "$ROOT" show --name-only --format= HEAD` prints exactly the two Scope paths. **Both, or it is not this plan's commit.**)*; **empty and HEAD is NOT this plan's commit → HALT** (the before-state is unrecoverable and every Step-2 assertion depends on it).
> - **Anything else, including any mixed state** → **HALT and report the exact cells as unclassified.** ⚠️ **Default-deny is carried from `executable-293`:** this gates a write to a file the daemon also writes, so an unrecognised state is reported, never reconciled. **Never guess, never `git restore`** (rollback is a CEO decision).
>
> **A5 — Establish THE BEFORE-STATE. This is the single source for every baseline in this plan.**
> - **CLEAN** → the before-state is the live file.
> - **LANDED-UNCOMMITTED** → `git -C "$ROOT" show HEAD:knowledge/FORWARD.md`.
> - **LANDED-COMMITTED** → `git -C "$ROOT" show HEAD~1:knowledge/FORWARD.md`.
>
> ⚠️⚠️ **DERIVE ALL FOUR BASELINES FROM THE BEFORE-STATE, NEVER FROM THE LIVE FILE.** On both LANDED branches the live file is the AFTER-state, so a baseline taken from it is an after-value wearing a before-label — and QA row 2's *"open down exactly 4"* would then compare 8 against 8 and **fail a correct run.**
> 1. **`PRE_EDIT_BLOB`** — the blob hash of the before-state, recorded under that exact name. ⚠️ **Never `hash-object` of the live file on a LANDED branch:** QA row 4 materializes this blob and diffs it against the live file, so a post-edit `PRE_EDIT_BLOB` makes that row compare the file **against itself and pass trivially** — the plan's central proof, silently voided.
> 2. the **data-row count** (QA row 1 compares to it);
> 3. the **status distribution** (QA row 2 compares deltas to it);
> 4. the **row-number SET of Items beginning with the literal `- `** (QA row 6 compares to it).
>
> **Record the branch name beside all four.** ⚠️ At authoring the blob was `0958b1660084343de0350ddb280f99ad207d84b8` with 12 data rows, all `open` — **a measurement with a timestamp, not a constant.** A different blob is not automatically a defect; a wrap reconciliation or a Receipt append moves it legitimately.
>
> **A6 — Verify the identity pins against the BEFORE-STATE**, each computed exactly as the parse contract (environment fact 2) defines it and in no other way. Measured at authoring 2026-08-10:
>
> | row | len | sha1[:12] |
> |---|---|---|
> | 2 | 58 | `3b3a00974a0e` |
> | 6 | 92 | `6c85ab9e27ee` |
> | 9 | 227 | `7ace3a3fc14f` |
> | 10 | 227 | `7ace3a3fc14f` |
> | 11 | 237 | `53ac66a097c2` |
> | 12 | 252 | `265c9f0a9ab4` |
>
> **Any target row whose Item sha1 does not match → HALT**: the numbering has moved and the edits would land on the wrong items. ⚠️⚠️ **Rows 9 and 10 share a sha1 — they are byte-identical, so no pin can tell them apart.** That is expected and is the whole reason one is a duplicate. **Row identity is the FIRST CELL and nothing else**; the pins verify Item CONTENT, never which physical row is which.
>
> **A7 — Derive `<N>`, this plan's own id. Do not carry a literal.** **Print the FULL plan path**, then extract with `re.search(r'executable-(\d+)\.md$', basename)`. ⚠️ **The filename may carry an execution prefix** — this project's `CLAUDE.md` RUN EXE protocol renames a claimed plan to `in-progress-executable-<N>.md`, and a halted one carries `halted-`; anchoring on `executable-(\d+)\.md$` tolerates any prefix. Assert exactly one match parsing as an integer; **zero matches → HALT** rather than guessing an id into the register. ⚠️ **A hardcoded id is wrong by construction** — `id_sequence` is minted at claim, and an in-window dispatch can consume the value read at authoring.
>
> **⚠️ ROUTING OUT OF TASK A.** **CLEAN** → Task C. **LANDED-UNCOMMITTED** → **skip Task C** (re-applying is the double-apply A4 exists to prevent), run D, E, F, commit. **LANDED-COMMITTED** → **the work is DONE**: run D and E as a re-verification, write the dev log only if it is missing, and **DO NOT COMMIT**. A `git commit` with nothing staged fails, and an agent reading that failure as an error is how a completed step gets "repaired". **Report the state and stop — but STILL EMIT THE FULL OUTPUT RECEIPT and the Deposits list.** ⚠️ *"Stop"* means **make no commit**, not *skip the receipt*: the daemon reads the receipt to close the step, and a step that ends without one reads as a death rather than as a completed re-entry.
>
> **Task C — APPLY VIA TEMP-AND-REPLACE. The real file is never written until the result has been verified.** ⚠️⚠️ **An in-place whole-file rewrite is the operation that has destroyed a live artifact three times in this shop, and Task A4 forbids `git restore` — so an in-place corruption would have NO authorized recovery path.** Therefore:
> 1. Read the file. In line-anchored Python, for each of rows 2, 6, 10, 11 locate the single line whose **first table cell equals that integer** and replace **only the final cell**. **Do not use `sed`, `awk`, or a `grep`-driven edit** (environment fact 2).
> 2. ⚠️ **Immediately before writing, re-hash the live file and assert it still equals `PRE_EDIT_BLOB`.** Task A's pin and this write need not be one invocation, and anything that touched the file in between would make the temp a rewrite of a stale read. **A mismatch → HALT**, naming both hashes. Then write the result to a **temp path inside the repo working dir** (e.g. the **`FORWARD.md.new` sibling**).
> 3. **Run the Task-D COMPARATOR (the code, not the task) against the TEMP file.** ⚠️ **Ordering, stated because two folds meet here:** the comparator is written once and called twice — **here against a **`FORWARD.md.new` sibling beside the register** as a pre-replace GATE, and again in Task D against the replaced real file as the RECEIPT.** Task D is not run early and is not skipped later; the second run is what proves the replace itself landed intact. Only on a full pass, `os.replace()` the temp over `$ROOT/knowledge/FORWARD.md`.
> 4. **On any comparator failure: delete the temp file, leave `knowledge/FORWARD.md` UNTOUCHED, and HALT** naming the failing row. ⚠️ **Delete the temp file on every exit path** — a stray `FORWARD.md.new` would land in `git status` and fail QA row 8.
>
> **Task D — PROVE THE POST-CONDITION, both directions.** ⚠️ **Match rows by FIRST CELL, never positionally** — the before-state and the live file need not carry the same row set, and a positional zip mis-aligns everything after an insertion. **Report any row number present in one and absent from the other, and HALT on an asymmetry.** ⚠️ **Compare the NON-DATA block as a block too** (Scope's byte-pin) — it is part of this post-condition, not only of the dev log. Re-read the file and produce a receipt showing, per row: `Added`, `Item`, `Type`, `Plan-id link` **byte-identical to the pre-edit capture for all twelve rows**, and the Status cell changed for **exactly** rows 2, 6, 10, 11 and no others. ⚠️ **Assert `after != before` for those four and `after == before` for the other eight** — a check that only greps for the target value can certify an edit that never landed.
>
> **Task E — CONTROL THE COMPARATOR, BOTH DIRECTIONS.** The Task-D comparator asserts an ABSENCE (no Item text changed), and an absence result is worthless without proof the instrument can report presence — **or worse, if it reports everything, in which case its clean run means nothing either.**
> - **Positive half:** in a fresh `mktemp -d` **outside every git tree**, copy the post-edit file, mutate **exactly one character of ROW 4's Item cell** (named, so the control is reproducible — row 4 is short and carries the `- ` marker), run the same comparator, and show it reports **row 4 and only row 4 as an ITEM change** — ⚠️ **the comparator also reports the four legitimate STATUS changes, and it must still report exactly those four here.** "Row 4 and only row 4" is a claim about the ITEM channel; a control that conflates the two channels passes whether or not the instrument works.
> - **Negative half:** run the comparator on the unmutated post-edit file and show it reports **the four Status changes as expected and ZERO Item changes.** A comparator that flags the legitimate Status edits as violations would HALT a correct run.
> - Discard the scratch copy. **Record both outputs verbatim.**
>
> **Task F — DEV LOG.** Deposit `$ROOT/knowledge/development/forward-dup-sweep-dev-log-2026-08-10.md` carrying, at minimum:
> - the resolved **`$ROOT`** and the full plan path A7 parsed (Step 2 re-derives both and compares);
> - ⚠️ the **A4 classification** (CLEAN / LANDED-UNCOMMITTED / LANDED-COMMITTED), whether A2 swept a stray temp, and **which source A5 used for the before-state** — Step 2 cannot interpret a single baseline without knowing which branch produced it;
> - the **pre-edit and post-edit blob hashes** — ⚠️ the pre-edit hash is the ONLY way Step 2 can materialize the before-state for QA row 4; without it that row is unrunnable;
> - the derived **`<N>`**;
> - the **row count, status distribution and `- `-marker row-number set BEFORE the edit** — every Step-2 assertion is relative to these, so an omission makes them unevaluable;
> - the **twelve-row before/after receipt** with each row's Item sha1;
> - ⚠️ the **sha1 of the NON-DATA block** (preamble + blockquote + `---` + header row + separator row) **before and after** — QA re-compares it and has no baseline otherwise;
> - the **Task-E control output, both halves.**
>
> **RAW output, never a summary.**
>
> **FINAL ACTION — COMMIT, ON THE CLEAN AND LANDED-UNCOMMITTED BRANCHES ONLY.** Pathspec on the commit naming exactly the two Scope files, then assert `git show --name-only --format= HEAD` prints exactly them. **Commit only — NO push.**
> ⚠️ **On LANDED-COMMITTED this step does NOT run** — Task A's routing already ended the step, the deposits are already committed, and a `git commit` with nothing staged fails in a way an agent reads as an error to repair. **Two instructions cannot both be final: Task A's routing wins.**
>
> **Scope:**
> - `knowledge/FORWARD.md`
> - `knowledge/development/forward-dup-sweep-dev-log-2026-08-10.md`
>
> **Deposits:**
> - `lessons-forge/knowledge/FORWARD.md`
> - `lessons-forge/knowledge/development/forward-dup-sweep-dev-log-2026-08-10.md`
>
> **STOP. Do NOT proceed to Step 2. Wait for CEO verdict.**

## STEP 2 — QA

---

⚠️⚠️ **THE RISK HERE IS A SILENT ITEM-TEXT EDIT, NOT A WRONG STATUS.** A wrong status is visible in one glance; a character lost from an Item cell during a whole-file rewrite is not, and this shop has destroyed a live draft three times on exactly that operation. **Rows 3–8's `- ` markers and row 12's fuller wording are the fragile payload — row 4's Item is a single sentence that reads as noise and is the easiest thing in the file to "tidy".**

> **FIRST — resolve `$ROOT` and assert `pwd -P` matches it** (Scope's every-step rule), then **Deliverable Verification (Rule 8 / Rule 17).** Open the Step-1 dev log, confirm its Output Receipt is Complete, verify every file it claims exists and carries the described change. Table: `| Deliverable | Expected | Status (✅/❌) | Evidence |`. Any ❌ → report and HALT; make no edits yourself.
>
> **Task Q0 — RE-PIN BEFORE MEASURING, AND PIN BY BLOB.** ⚠️ **The guard is `git hash-object knowledge/FORWARD.md` equalling the POST-edit hash Step 1 recorded — not commit identity.** A daemon merge or worktree teardown legitimately produces a newer commit touching this path while carrying Step 1's exact tree, so a "newest commit must be Step 1's" test **fails a correct run**; the blob does not.
> - `git -C "$ROOT" log --oneline -- knowledge/FORWARD.md knowledge/development/forward-dup-sweep-dev-log-2026-08-10.md | head -5` — record it, with `$ROOT` printed beside it. **A newer commit is investigated, not auto-halted: if the blob matches Step 1's, name the commit and continue; if it does not, HALT.**
> - `git -C "$ROOT" status --porcelain --` the same two paths must be **EMPTY**. An uncommitted verdict-window edit is a baseline nobody wrote, and `log` cannot see it.
>
> **MANDATORY — Rule 20 self-check (canonical block, the exact template, NOT a paraphrase)** from `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md` (ABSOLUTE path). **All FOUR placeholders:** `plan_slug`: `forward-dup-sweep-2026-08-10`; `qa_report_path`: `<your-tree-abs>/knowledge/qa/forward-dup-sweep-qa-2026-08-10.md`; `evidence_dir` derived from `pwd`, NOT hardcoded; `required_evidence_files`: `[forward-before.txt, forward-after.txt, column-invariance.txt]`. **Deposit all three BEFORE running the block — it `sys.exit(1)`s on any missing OR ZERO-BYTE file.** ⚠️ **All three are receipts, never bare diff streams:** an expected-empty diff written verbatim is a zero-byte file, which fails the block on a CORRECT run and inverts this gate. Include the block's literal stdout — the banner `Rule 20 — QA Self-Check Results` and the `PASSED — SELF-CHECK PASSED` line, both byte-exact (em-dash U+2014).
>
> ⚠️ **REPORT STRUCTURE — immediately after the verification table write exactly `## Evidence and Narrative`**, keeping the Rule 20 stdout, the Output Receipt and `### Ledger Updates` at `##`-level. ⚠️ The gate scopes its search to a heading containing "verification"; a differently-named section is invisible to it.
>
> **Evidence rule:** RAW command output, never a summary.
>
> **Verification table, one row per claim (HALT on any FAIL):**
>
> **1. ROW COUNT UNCHANGED.** Re-derive the data-row count from the live file in line-anchored Python and assert it equals **the count Step 1's Task A recorded** — not a literal. ⚠️ **`+1` means a Receipt row was emitted against this plan's Scope prohibition; `−1` means a row was deleted.** Either is a HALT, and the count is the only instrument that sees them. ⚠️ **Because the daemon appends post-merge, a Receipt row emitted by Step 1 lands AFTER Step 1's commit and BEFORE this step reads — so the relative comparison still catches exactly the thing it exists for.** → `forward-after.txt`
> **2. STATUS DISTRIBUTION, AS A DELTA.** Against Step 1's Task-A capture: `open` **down exactly 4**, `withdrawn` **up exactly 3**, `closed-by-plan-<N>` **up exactly 1**, every other status value unchanged. ⚠️ `<N>` is re-derived from this plan's own deposited filename **independently of the dev log**, printed with the FULL plan path beside it, and asserted equal to the value written in the file. **A distribution that matches while `<N>` differs is a wrong-id write that every other row in this table would pass.** → `forward-after.txt`
> **3. THE FOUR CELLS, BY ROW NUMBER — and the rest AS A DERIVED SET.** Rows 2 → `withdrawn`, 6 → `closed-by-plan-<N>`, 10 → `withdrawn`, 11 → `withdrawn`, each compared for **byte-exact case-sensitive equality on the stripped cell**. ⚠️ **Then: every row NOT in {2, 6, 10, 11} carries the status it carried in the BEFORE-STATE** — derived, not the hardcoded list `1, 3, 4, 5, 7, 8, 9, 12` this row used to name. **The relative-not-constant fold reached QA rows 1-2 at walk 1 and rows 6-7 at walk 2 and missed this row both times**; a literal set is also wrong the moment the register gains a row. The second half is what catches an over-broad edit. → `forward-after.txt`
> **4. ⚠️⚠️ COLUMN INVARIANCE — the plan's central proof.** Materialize the pre-edit file with **`git cat-file -p <PRE_EDIT_BLOB> > $S/FORWARD.md`** where `S=$(mktemp -d)` is created and used in the SAME invocation. ⚠️ **NOT `git show <blob>:path`, which is FATAL — a blob is not a tree and cannot be path-addressed.** Compare **in three parts, and all three must hold:**
> - **(a) the twelve data rows cell-by-cell** — `Added`, `Item`, `Type`, `Plan-id link` byte-identical; Status differing for exactly rows 2/6/10/11.
> - **(b) ⚠️⚠️ THE NON-DATA BLOCK** (preamble + blockquote + `---` + header row + `|---|` separator) **byte-identical, compared AS A BLOCK** — the only test that also catches an inserted or deleted blank line. ⚠️ **This guard was mandated in Scope at walk 2 and recorded in the dev log, and until walk 3 NOTHING CHECKED IT** — the dev-log line even claimed *"QA re-compares it."* That is batch entry 302's mandate-without-an-observer class, firing on the plan that ingests it, for the third time in this cycle.
> - **(c) row-number JOIN, not positional zip** — ⚠️ **the before-state and the live file may not have the same rows.** Match rows by their FIRST CELL and report any row number present in one and absent from the other; a positional comparison silently mis-aligns every row after an insertion and reports twelve differences or none. **A row-number asymmetry → HALT.**
>
> **PASS = (a), (b) and (c).** Any Item-text or non-data difference of any size → **HALT**. → `column-invariance.txt`
> **5. CONTROL THE COMPARATOR, RE-RUN IN THIS SESSION, BOTH HALVES.** Do not inherit Step 1's Task-E result. **Positive:** in a scratch copy outside every git tree, mutate exactly one character of **ROW 4's** Item cell and confirm the comparator reports **row 4 and only row 4**. **Negative:** run it on the unmutated file and confirm it reports the four Status changes and **ZERO Item changes**. ⚠️ **Both halves — a comparator that reports everything passes the positive test and would HALT a correct run.** An invariance check that cannot report a difference is not evidence of invariance; one that cannot report agreement is not usable as a gate. → `column-invariance.txt`
> **6. THE MARKERS SURVIVED — as a delta, not a constant.** Count rows whose Item begins with the literal `- ` and assert the count and the **row-number set** are **identical to Step 1's Task-A capture** (measured at authoring: 8 rows — 3, 4, 5, 6, 7, 8, 11, 12 — stated as a measurement, not a bar). ⚠️ **Rows 11 and 12 dropping out means someone "fixed" them**, which this plan forbids and which would destroy row 8's live specimen. **Report the row-number set, never just the count** — two offsetting changes leave a count intact. → `column-invariance.txt`
> **7. ROWS 9 AND 12 ARE INTACT AND OPEN.** Their Item sha1 equal to the pre-edit capture and their Status still `open`. **These are the two surviving halves of the duplicate pairs; withdrawing the wrong copy of either is the one error this sweep can make that loses information.** ⚠️ **Assert row 12's Item is LONGER than row 11's, comparing the two live cells** — the surviving copy of that pair must be the fuller one, and comparing them to each other is what proves it. Do not compare against the literal 252. ⚠️ For 9/10 no such test exists or is needed: they are byte-identical, so the survivor is correct by construction. → `forward-after.txt`
> **8. NOTHING ELSE MOVED — named paths, not "unexpected".** `git -C "$ROOT" status --porcelain` must be **EMPTY**. ⚠️ *"No unexpected modification"* is unfalsifiable — the reader supplies the expectation. **Assert emptiness, then additionally assert by name that `lessons-forge.db`, the **`FORWARD.md.new` sibling**, `PROJECT_STATUS.md` and `agent-prompt-feedback.md` are absent from the output**, and that no commit in this plan touched `PLANNER_TEMPLATE.md` or `RULE_20_SELF_CHECK_BLOCK.md` (`git log --name-only` over both step commits).
>
> **Then `## Evidence and Narrative`, then the Output Receipt.**
>
> ⚠️ **`### Ledger Updates`** — author via `Write`/`Edit` (the daemon parses assistant text and Write/Edit content, NOT Bash), EXACTLY ONCE, complete, never re-edited; `##`-level after `## Evidence and Narrative`; blank line after the last subsection.
>
> ⚠️⚠️ **OMIT the `#### Forward Register` subsection ENTIRELY. Do not write "None".** Per Scope, this plan emits zero rows; row 6 is closed by this plan's own edit, and rows 2/10/11 are withdrawn by it. **A row emitted here lands as row 13 and fails verification row 1.**
>
> **FINAL ACTION — COMMIT YOUR DEPOSITS**, pathspec on the COMMIT naming exactly the Scope files, then assert `git show --name-only --format= HEAD` prints exactly them. **Commit only — NO push.**
>
> **Scope:**
> - `knowledge/qa/forward-dup-sweep-qa-2026-08-10.md`
> - `knowledge/qa/evidence/forward-dup-sweep-2026-08-10/forward-before.txt`
> - `knowledge/qa/evidence/forward-dup-sweep-2026-08-10/forward-after.txt`
> - `knowledge/qa/evidence/forward-dup-sweep-2026-08-10/column-invariance.txt`
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/forward-dup-sweep-qa-2026-08-10.md`
> - `lessons-forge/knowledge/qa/evidence/forward-dup-sweep-2026-08-10/forward-before.txt`
> - `lessons-forge/knowledge/qa/evidence/forward-dup-sweep-2026-08-10/forward-after.txt`
> - `lessons-forge/knowledge/qa/evidence/forward-dup-sweep-2026-08-10/column-invariance.txt`

---

## Drafting Cycle

**Tier:** T1 — computed, not judged. **T-2 fires** (writes the project's canonical register of record; §1's *"if unsure whether a trigger fires, it fires"*). **T-8 fires** (novel pattern — ⚠️ **on the RESTATED basis, not the retracted one:** a dispatched agent writing this path has post-cutover precedent in `executable-293`; what is novel is **updating an existing row's Status**, which 14–18 and 293 never do. See Exception clause 3). **T-5 does NOT fire** — no deletion, no history rewrite, cleanly revertible by `git`. **T-6 does NOT fire** — the Rule 42 amendment is explicitly out of scope and rides the Gate-2 template batch.

**Walks:** 3 — five lenses each, strictly sequential, each lens acting on the draft as folded by the previous.
- Weak spots:          w1 6 folded — **6/6 pre-existing**, 3 HIGH (the A0 resume branch routed through the APPLY task; an unsatisfiable HALT precondition; QA constants that fail a correct run).
- Destruction:         w1 4 folded — 3 pre-existing, **1 fold-introduced**, 1 HIGH (the in-place whole-file rewrite had no authorized recovery path, since A0 forbids `git restore`).
- Vulnerabilities:     w1 6 folded — 5 pre-existing, **1 fold-introduced**, 3 HIGH. ⚠️ **The live one: the plan hardcoded the main-tree path and every step runs in a worktree** — measured, plan 340's step ran at `lessons-forge/.bellows-worktrees/340`.
- Integration-record:  w1 3 folded — **3/3 pre-existing**, 2 HIGH, **one a RETRACTION of this plan's own premise** (see below).
- ACID:                w1 5 folded — 2 pre-existing, **3 fold-introduced**, 2 HIGH (an unpinned status literal; a fold interaction between the temp-and-replace gate and Task D).

⚠️⚠️ **A PREMISE OF THIS PLAN WAS RETRACTED AT WALK 1 LENS 4, and the cause is worth more than the correction.** The Exception's clause 3 claimed *"no post-cutover precedent exists — every dispatched plan editing a FORWARD register is id ≤ 63."* **False.** It came from a `grep -rl` over `Done/` **truncated at 20 hits and unsorted**, off which an id RANGE was read as though it were a population. A tight re-probe — FORWARD.md inside a `**Scope:**`/`**Deposits:**` block — returns `executable-293` (governance, closed 2026-08-02, post-cutover), whose Scope is exactly this path. **The exception being taken is narrower than the plan claimed, and the narrower version is now what it claims.**

⚠️ **Fold-introduction is concentrated in ACID and all three of its instances trace to walk-1 folds** (temp-and-replace ×2, `$ROOT` ×1). Tasks A0/C/D/F carry this walk's unreviewed surface; walk 2 should expect to find more there.

**Walk 2** — the new surface walk 1 created was Tasks A0/C/D/F; a walk covers, so all five lenses read the whole artifact.
- Weak spots:          w2 6 folded — **6/6 fold-introduced.** ⚠️ **The HIGH: walk 1's own fold retargeted A0's landed branch to "skip to Task D" — and Task D reads Task A's baseline and Task B's `<N>`, both of which that skip bypassed.** Also: the retracted premise was still live in the Tier line, folded in the Exception only.
- Destruction:         w2 3 folded — **3/3 fold-introduced**, 1 HIGH. ⚠️ **Walk 1's `$ROOT` fold asserted `basename $(git rev-parse --git-common-dir)` "resolves under a lessons-forge checkout" — MEASURED, it returns `.git`, so the assertion could never pass.** Replaced with a content identity test (FORWARD.md's first line).
- Vulnerabilities:     w2 3 folded — 2 fold-introduced, 1 pre-existing, 1 HIGH. ⚠️ **In the already-landed branch `PRE_EDIT_BLOB` would have been the hash of the ALREADY-EDITED file, making QA row 4 diff the file against itself and pass trivially** — the central proof, silently voided. Pre-existing: the id regex could not survive the `in-progress-` prefix this project's own `CLAUDE.md` mandates.
- Integration-record:  w2 3 folded — **3/3 pre-existing**, 1 HIGH. ⚠️ **Clone-diff against `executable-293` (named as origin only at walk 1) recovered a guard this plan had dropped: 293 byte-pins the header and separator rows and calls them load-bearing. Every assertion here addressed the twelve DATA rows — a rewrite mangling the header would have passed all of them.** Also: row 6 asks for *"superseded"*; measured across all six registers `superseded` appears **0** times and `withdrawn` **3**, so the substitution is right and is now stated.
- ACID:                w2 3 folded — 2 fold-introduced, 1 pre-existing. The committed-landed re-entry would have re-committed finished work; the pin→write window was unguarded.

**Walk 2 total: 18 findings, 18 folded — 5 pre-existing (28%), 13 fold-introduced (72%), 4 HIGH.**

⚠️ **THE ORIGIN SPLIT TURNED: 21% fold-introduced at walk 1, 72% at walk 2.** That is §2's convergence direction, and lens 4 is the reason it is not higher — **it is the only lens that reads OUTSIDE the artifact, and it returned 3-for-3 pre-existing in both walks.** Every other lens is now largely reading its own predecessors' folds.

**Walk 3** — the new surface was the collapsed Task A; a walk covers, so all five lenses read the whole artifact.
- Weak spots:          w3 6 folded — **6/6 fold-introduced**, 3 HIGH. ⚠️⚠️ **A0/A/B had taken ELEVEN findings across three walks — every patch correct, each re-creating a forward reference (A0 invoking a discriminator that lived in Task A; a landed branch skipping the baseline it needed; two clauses each claiming to run "first"; baselines derived from the live file on a branch where the live file is the AFTER-state). COLLAPSED into one ordered Task A (A1-A7) with no forward references.** The collapse then orphaned six references elsewhere, swept in the same fold.
- Destruction:         w3 3 folded — **3/3 fold-introduced**, 1 HIGH. ⚠️ **A diff review of the collapse — not a retained-material checklist — recovered TWO guards it had silently dropped:** the `porcelain must be EMPTY` requirement on the clean branch, and the *leave the recorded id in place, do not "repair" it* instruction. Also: `FINAL ACTION — COMMIT` contradicted the new LANDED-COMMITTED routing.
- Vulnerabilities:     w3 3 folded — 2 fold-introduced, 1 pre-existing, 2 HIGH. ⚠️⚠️ **The non-data byte-pin added at walk 2 was mandated in Scope and recorded in the dev log — whose own line claimed "QA re-compares it" — and NOTHING CHECKED IT.** That is batch entry 302's mandate-without-an-observer class, on the plan that ingests it, **third instance this cycle.** Also: `HEAD is this plan's own commit` was a named condition with no test; and the before/after comparison zipped positionally where the row sets may differ.
- Integration-record:  w3 2 folded — 1 pre-existing, 1 record. ⚠️ **§5 conformance RUN for the first time, at the deposit path resolution** (`lessons-forge/knowledge/decisions/`, not `knowledge/research/`, per the location-dependence of `plan_lint`'s expected set). **First run: exit 0, 5 WARNs.** Two were prose citations the `(o1)` check parsed as declared paths (a `.bellows-worktrees` path and the temp sibling); reworded across all five sites. **Re-run: exit 0, 3 WARNs** — two known-benign steps-mention-tests (Test Scope IS declared in the header) and the closing WARN, which is **TRUE and EARNED**.
- ACID:                w3 2 folded — **2/2 fold-introduced.** QA row 3 still named a hardcoded untouched-row set — **the relative-not-constant fold reached QA rows 1-2 at walk 1 and 6-7 at walk 2 and missed row 3 twice.** And the LANDED-COMMITTED stop would have ended the step with no Output Receipt, which the daemon reads as a death.

**Walk 3 total: 16 findings, 16 folded — 3 pre-existing (19%), 13 fold-introduced (81%), 5 HIGH.**

⚠️⚠️ **THE ORIGIN SPLIT: 21% → 72% → 81% fold-introduced.** Three walks, monotonically rising, which is §2's convergence direction. **But the bar's OTHER condition has failed three times running:** five HIGH findings this walk were instruction-changing, and three of them — the two guards the collapse dropped, and the mandate with no observer — **would have shipped a plan whose central proof was unchecked.**

⚠️⚠️ **THE COST LINE, STATED PLAINLY: this artifact is now ~270 lines and 57 findings to change FOUR TABLE CELLS.** That is `executable-332`'s shape exactly — *"248 lines to change two regexes whose measured corpus impact is ZERO"* — which the CEO CUT rather than walked further. **The findings are no longer about the edit; they are about the machinery around the edit, and the machinery is generating them.** ⚠️ Per §2.8 that is the oscillation signal, and per §2 a pass whose findings are mostly its predecessor's fold damage **is the noise floor, not progress.** **A judged stop, or a cut, is the indicated move — not walk 4.**

**Walk 1 total: 24 findings, 24 folded — 19 pre-existing (79%), 5 fold-introduced (21%), 11 HIGH.** Per-finding detail for both walks: `scratchpad/walk-register-forward-dup-sweep-2026-08-10.md`.

**Conformance (§5):** run at shape-stability and **re-run after every culmination since**, at the DEPOSIT path resolution (`lessons-forge/knowledge/decisions/`) — not from `knowledge/research/`, because `plan_lint`'s expected-WARN set is location-dependent (`project_root` is the segment before `/knowledge/`). **Latest run, after the walk-3 lens-5 folds: exit 0, THREE warnings, unchanged from the previous run.**
- ×2 `step N mentions tests but declares no test scope` — **known-benign**: the header declares `Test Scope: targeted — no code, no tests`, and the token appears only in Task E's control prose. **Not silenced, not reworded to evade.**
- ×1 `Drafting Cycle closing indicates fold as last event, not a dry lens pass` — ⚠️ **TRUE and EARNED. The closing genuinely is a fold.** It is expected at deposit and must not be cleared by authoring a dry line.

**Any OTHER warning at deposit is unexplained → do not deposit.**

### ⚠️ RESIDUE — enumerated individually, per §2, because a judged stop is auditable or it is not a stop

**The bar's record-class condition FAILED at walk 3, so this residue is NOT record-class by construction and must be listed rather than assumed.** Four of the eight items are instruction-class and each is a thing walk 4 would have read first.

| # | residue | class | what would have read it |
|---|---|---|---|
| R1 | QA row 3's **derived** untouched-row set (replacing the hardcoded `1,3,4,5,7,8,9,12`) | **instruction** | added by w3 lens 5 — **no lens has read it** |
| R2 | The LANDED-COMMITTED clause requiring the Output Receipt without a commit | **instruction** | added by w3 lens 5 — **no lens has read it** |
| R3 | QA row 4's three-part (a) data-rows / (b) non-data block / (c) row-number join | **instruction** | added by w3 lens 3; read by lenses 4 and 5 only |
| R4 | The collapsed **Task A (A1–A7)** in its final form | **instruction** | ⚠️ **created BY w3 lens 1, so lens 1 has never read the arrangement it produced.** Lenses 2–5 did, and lens 2's diff review recovered two dropped guards from it |
| R5 | The six orphan-pointer sweeps the collapse forced (slug, ID note, edit table, Task C, dev log ×2) | record | read by lenses 2–5; mechanical pointer updates |
| R6 | The five temp-path rewordings that cleared two `(o1)` WARNs | record | read by lens 5, and **mechanically re-verified** — conformance re-run exit 0 |
| R7 | The `- ` marker inconsistency across eight rows | **deliberate** | out of scope by design; row 8 is its live specimen |
| R8 | The Rule 42 third branch for `withdrawn` | **deliberate** | queued to the `PLANNER_TEMPLATE.md` Gate-2 batch |

⚠️ **R4 is the one to weigh.** The collapse is this cycle's highest-value fold and it is the least-reviewed structure in the plan by its own lens. Lens 2's diff review found it had dropped two guards — **which is evidence that a structural edit sheds guards silently, not evidence that it has now stopped doing so.**

**Closing:** ⚠️⚠️ **JUDGED STOP ON A CEO DECISION (2026-08-10), AND IT IS A DECLARED §2 DEVIATION — NOT A BAR-MEETING CLOSE.** §2 requires a judged stop to meet the bar; **walk 3 met the origin-split condition (13 of 16 fold-introduced, 81%) and FAILED the record-class condition** — five instruction-changing HIGH findings, which by §2's own words re-open the walk. The stop is taken anyway, on the `executable-332` precedent (CEO, 2026-08-09), and the reasoning is recorded rather than engineered away.

**The reasoning:** three walks produced **58 findings against a four-cell edit** in a plan **measured at 285 lines when the cost argument was made at walk 3** (the closing record itself then added ~30 — ⚠️ **the figure is a measurement with a timestamp, and it went stale inside the very paragraph that cites it; re-derive at deposit rather than quoting either number**) — `executable-332`'s shape exactly (*"248 lines to change two regexes whose measured corpus impact is ZERO"*), which was cut rather than walked. **The origin split rose monotonically 21% → 72% → 81%**, so by §2 each pass is now predominantly reading its predecessor's fold damage: the noise floor, not progress. **Walk 3's single most productive move was REMOVING structure, not adding it** — the collapse closed four findings that three walks of patching had kept re-creating. A fourth walk would harden machinery around an edit whose substance — *which four cells, to which values, and why* — has not changed since walk 0.

**Residue class in a clause apiece:** 4 instruction-class (an unread derived-set rewrite; an unread receipt clause; a three-part QA row read by two lenses; a collapsed task its own lens never re-read), 2 record-class (pointer sweeps; lint-driven rewordings, mechanically re-verified), 2 deliberate holds (the marker inconsistency; the Rule 42 branch).

**What this costs, stated honestly:** R1–R4 are instruction-class and unread or under-read. The specific risk is the one lens 2 measured on this very artifact — **a structural edit drops guards silently** — and R4 is a structural edit. The mitigation actually in place is not another lens: it is that **every CLASSIFICATION and VERIFICATION branch in Task A is HALT-shaped** — A4 on an unrecognised state, A5 on an unrecoverable before-state, A6 on a pin mismatch, A7 on a missing id — and that §5 conformance is clean at exit 0 with three earned warnings. ⚠️ **An earlier phrasing of this sentence claimed Task A's failure modes are ALL HALT-shaped. They are not: A2 DELETES a stray temp and A5 DERIVES four baselines, neither behind a HALT.** The over-claim is corrected rather than dropped, because it was the sentence carrying the stop's whole mitigation argument.

### §2.7 closing-record re-read — RUN, and it raised three

Mandatory at every close, most load-bearing on a judged stop, and on **T1 there is no cold panel**, so this re-read plus the residue enumeration are the entire reader. Run adversarially against the artifact after the closing record was written. **3 findings, all record-class, all fold-introduced by the closing record itself:**

1. **A stale cost figure that went stale INSIDE the paragraph citing it** — "285-line plan" was measured at walk 3, and writing this record added ~30 lines. Now stated as a timestamped measurement with a re-derive-at-deposit instruction.
2. **An over-claim carrying the whole mitigation argument** — "Task A's failure modes are ALL HALT-shaped." They are not: A2 deletes a stray temp and A5 derives four baselines, neither behind a HALT. Corrected in place rather than dropped, because it was the sentence the stop rests on.
3. ⚠️⚠️ **The audit trail the stop invokes did not contain the walk being stopped.** The Closing cited the walk register for per-finding detail and **walk 3's sixteen findings had never been appended to it.** Appended. **On a judged stop the register IS the auditability, so this was the re-read's sharpest catch and it was a defect in the stop itself, not in the plan.**

⚠️ **The re-read also corrected this record's own arithmetic:** the Cycle Log said walk 3 folded 15 and lens 1 folded 5; the register says 16 and 6. **The record decayed while the artifact converged** — and only the artifact gets verified, which is why this pass exists.

⚠️⚠️ **A FOURTH FINDING, AND THE MECHANICAL CHECK CAUGHT IT AFTER THE JUDGMENT PASS DID NOT.** The two headings this closing record introduced were authored at `##`, which **ends the `## Drafting Cycle` block** — so `**Closing:**` fell OUTSIDE it and `plan_lint` reported `Drafting Cycle block has no **Closing:** line`. **The re-read had just read that same prose adversarially and did not see it**, because the defect is in markdown structure, not in what the words claim. Demoted to `###`; conformance back to exit 0 / 3 earned WARNs / 8 PASS.

⚠️ **This is FORWARD row 45's class — record sections colliding with block boundaries — landing on the plan that ingests entry 305 about it.** It is also the strongest datum this cycle produced for the funnel: **a mechanical check caught what a judgment pass, aimed at exactly that paragraph, had just missed.** ⭐ **And it lands on the last edit before deposit, which is by construction the least-reviewed text in any plan.**

**Fold-and-deposit exactly once.**
