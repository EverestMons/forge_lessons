# Executable: DRAFTING_CYCLE v2.1 — the direction verdict, the context pin, and three fold rules

**Type:** Executable
**Project:** lessons-forge
**Depends on:** `drafting-cycle-findings-2026-08-11.md` (shop root — **the measured evidence; F-numbers below cite it**), `executable-330` (Done — the doctrine-amendment clone origin), `halted-executable-334` (⚠️ **the newest same-class; HALTED, open verdict — see Scope**), LESSONS 2026-08-11 ×5. DRAFTING_CYCLE at **v2.0**.
**Created:** 2026-08-11
**Author:** Planner
**Slug:** `dc-direction-verdict-2026-08-11`
**dispatch_mode:** bellows
**pause_for_verdict:** always
**Priority:** 5
**cycle_tier:** T2
**qa_steps:** [2]
**Test Scope:** targeted — no code. `plan_lint.py` and `gates.py` parse the tier line and the cycle block; **E1 adds a new §2.0 and E2–E4 append bullets — neither changes any structure the gate reads.** ⚠️ **Verify at Task A, do not assume.** Step 2 runs the bellows suite as a floor.

⚠️ **§6 DEVIATION, DECLARED.** §6 mandates the corpus path (LESSONS → Gate 1 → Gate 2). **These findings are LESSONS 2026-08-11 entries 255–259, appended today; no corpus batch exists yet.** This lands as a **CEO-authorized direct amendment**, the v1.5 / v1.6 / v1.7 precedent, and the History row says so. **The corpus catches up at the next forge ingest.**

---

## Why this exists

**Three plans ran end-to-end today. The two that closed did so cleanly. The third — a six-edit doctrine amendment — is still open after seven walks and two cold seats, and its v0 was wrong in three independent ways: wrong clone origin, wrong edit mechanism, wrong site set.**

⚠️⚠️ **The cycle had no way to say so.** It has a convergence bar and a judged stop, and **both assume the artifact is worth converging.** So it folded ninety-odd times on a foundation that was never right.

**The cycle can measure whether a draft is SETTLING. It cannot ask whether the draft is CORRECT IN KIND.** That is the gap this amendment closes.

**Four measured facts drive it** (`drafting-cycle-findings-2026-08-11.md`):
- **F1** — 62% of warm-walk findings were the walk's own fold damage.
- **F2** — every foundation defect was readable before walk 1, by **five commands in ~30 seconds**. Two cold seats spent ~333k tokens re-finding four of them.
- **F3** — five consecutive walks where lens 1's correct fix broke something lens 2 then caught. **A structural cut changed the region and the pattern survived**, so it is a property of how folds are made.
- **F5** — the remedy for three recurring classes already existed in `executable-330`, two generations upstream, unread.

⚠️ **This plan is deliberately small — five edits, given after-text.** A bloated fix for bloat would disprove its own thesis.

## Scope

- **Edits exactly ONE file:** `/Users/marklehn/Developer/GitHub/DRAFTING_CYCLE.md` **(root repo)**. Absolute operands; `git -C` on every root op; the doctrine is **not** a project-prefixed deposit and is absent from `**Deposits:**`.
- **Two commits, two repositories:** the doctrine at the root repo (pathspec-limited, never `git add -A`), the dev log in the `lessons-forge` worktree. ⚠️ **The root commit is invisible to `files_changed`** (`bellows.py:990 _parse_diff_stat` diffs the worktree) — expected; do not "fix" it by copying the doctrine into the worktree.
- ⚠️⚠️ **SEQUENCING — this plan and `gate2-s3-register` both amend the doctrine and cannot both be in flight.** **This one runs FIRST.** ⭐ **`gate2-s3-register` is then re-drafted UNDER the rules this ships** — and on its own record, the direction verdict would have booted it at walk 1.
- ⚠️ **`halted-executable-334` has an open verdict and wrote §2:38 and §3:125. This plan touches NEITHER** — E1 inserts a new subsection, E2–E4 append bullets. **No edit lands on halted text.**
- **One mechanism: E1 INSERTS a new block; E2–E4 APPEND a bullet after a located line; E5 REPLACES the version line.** **No edit replaces a mid-line span.** **No LESSONS touch. No corpus write. No push.**

### ⚠️ Environment facts — observed
1. `grep` is a ugrep shim: `-F` mandatory; a non-`-F` search **exits 1 silently on a present line**.
2. Shell state does not persist — `git -C <abs>` on every root operation.
3. The doctrine carries em-dashes, `§`, backticks and apostrophes — **`encoding="utf-8"` explicitly; DOUBLE-quote every probe; match apostrophe-bearing anchors in Python, never a shell string.**
4. ⚠️⚠️ **E3's anchor BEGINS WITH `-`, so it MUST be passed as `grep -c -F -e "<anchor>"`** — measured live: without `-e`, ugrep parses it as an option and errors. This is §2.7's own dash-leading-pattern rule firing on the plan that ships the fix.

---

## The amendment — AFTER text is GIVEN; the agent PLACES it and composes nothing except the History row

⚠️ **Each anchor is asserted `grep -c -F` = 1 before its edit. `>1` → lengthen the anchor. `0` → HALT.**

### E1 — INSERT a new block immediately BEFORE the line beginning `### 2.1 Lens 1 — Weak spots`

> ### 2.0 Walk 0 — the context pin and the direction verdict
>
> **Before lens 1 runs, MEASURE the ground the draft stands on. Never recall it.** Record in the Cycle Log: (1) `git log --oneline -- <target file>` — the **newest same-class plan**, which is the §2.6 clone-diff target; (2) for every anchor the plan will edit, its **line number, the line's total length, and the fragment's start column** — is this a whole line or a span inside one, and what else is on that line; (3) a file-wide occurrence count for every token being replaced; (4) for every target line, **which plan last wrote it and that plan's `lifecycle_state`**; (5) the target file's sha. **Five measurements. They cost seconds and they are the foundation every later pass assumes.**
>
> **Then, after walk 1, the author issues a DIRECTION VERDICT — one of three, recorded with its reasoning:**
> - **PROCEED** — the angle is right; walk on.
> - **CUT-AND-PROCEED** — the angle is right but a region must be removed first (§2.8's third resolution).
> - ⛔ **RE-DRAFT — the angle is WRONG. The cycle ENDS here without a deposit. The draft returns to conversation and a new v0 is authored; it is not repaired in place.**
>
> ⚠️⚠️ **RE-DRAFT is a NORMAL, SUCCESSFUL outcome of a drafting cycle, not a failure.** A cycle that identifies a wrong angle at walk 1 and stops has done its job at the lowest cost available. **The failure mode it exists to prevent is folding an artifact whose foundation is wrong** — measured at 62% of warm-walk findings being the walk's own fold damage, on a plan whose v0 was wrong in three ways and which had, at seven walks, still not converged.
>
> ⚠️ **THREE FINDINGS FORCE A RE-DRAFT VERDICT — they are not weighed, they decide:** a finding that invalidates **(a) the plan's clone origin or the precedent it inherits from**, **(b) the mechanism by which its edits act**, or **(c) a premise that licenses its scope**. **Any one of these is a DIRECTION finding, not a fold.** Folding it repairs a sentence and leaves the artifact built on the thing that was wrong.

### E2 — APPEND to §2, after the line ending `Fold-and-deposit **exactly once**.`

> ⚠️ **A RE-DRAFT verdict (§2.0) ends the cycle without a deposit and without meeting this bar.** The bar measures whether an artifact is settling; it says nothing about whether the artifact is correct in kind, and a cycle must be able to answer the second question without first satisfying the first.

### E3 — APPEND to §2.7, after the line beginning `- **Re-run the finding lens on its own fix.**`

> - ⚠️ **A fold that RECLASSIFIES, REORDERS, MERGES or DELETES a branch is a control-flow change, not a wording change — diff it as one.** For every input value, name the branch it took **before** and **after**, and confirm each still terminates the same way. **A stop that disappears is the failure mode and it is invisible in a diff of the sentence**, because the name of a state and the branch for that state live in the same sentence. Measured: five consecutive walks where a correct reclassification silently widened what proceeds.
> - ⚠️ **A COUNT IN PROSE THAT NO ASSERTION READS WILL GO STALE. Declare a set ONCE — a table, a list — and have every other site point at it rather than restate its size.** Measured: eight instances in one cycle, each individually corrected, the eighth contradicting a standing CEO hold.
> - ⚠️ **A CONSTRAINT THAT SPANS STEPS is named as a constraint WITH ITS SITES, never as prose inside one step** — otherwise it is carried by whichever step the author happens to be drafting and the other half is silently dropped. Measured: three half-carried guards in one cycle, one leaving the plan's highest-value check with no independent observer.
> - ⚠️⚠️ **PROVE EVERY POST-CONDITION CAN FAIL, BEFORE THE EDIT.** Run each new assertion's literal against the **pre-edit** state and confirm it returns the failing value. **A post-condition that already passes before the edit is not a post-condition.** Measured: three successive post-conditions in one cycle, each of which would have HALTED a correct run.

### E4 — APPEND to §3, after the line beginning `The compact form is **load-bearing**`

> ⚠️ **The Cycle Log records the walk-0 context pin (§2.0) and the direction verdict with its reasoning.** A cycle that ended in RE-DRAFT records the pin, the verdict and which of the three forcing findings produced it — **that record is the input to the next v0, and it is the whole return on the cycle.**

### E5 — REPLACE the version line (whole line, anchor asserted = 1)

> **BEFORE:** `**Version:** 2.0 (2026-08-09). Amended only through the Iteration Protocol (§6).`
> **AFTER:** `**Version:** 2.1 (2026-08-11). Amended only through the Iteration Protocol (§6).`

⚠️ **`2.0 (2026-08-09)` occurs TWICE** (version line + the v2.0 History row). **Anchor on the whole line; never a token replace.** The date is **declared**, not computed.

---

## STEP 1 — DEV

> **FIRST — post a short chat message. Do NOT rename this plan file. Read your specialist file.**
>
> **Task A — ESTABLISH STATE.**
> 1. `git -C /Users/marklehn/Developer/GitHub rev-parse --show-toplevel` = `/Users/marklehn/Developer/GitHub`, else **HALT**.
> 2. **FILE PIN:** `shasum -a 256` on the doctrine — **compare the HASH FIELD ONLY** — must equal `0964e1a70d6752f8656051b865ebcbdf76cb3e35e1b12415e547b54c45e4a7c7`. **Mismatch → HALT. Do not adjust it, do not re-derive it.**
> 3. `git -C … hash-object DRAFTING_CYCLE.md` → `PRE_EDIT_BLOB`; `git -C … status --porcelain -- DRAFTING_CYCLE.md` **EMPTY**.
> 4. **FRESH-RUN GATE — one rule, no branches.** Print all: slug `dc-direction-verdict-2026-08-11` count = **0**; version reads **2.0**; each of the five anchors counts **exactly 1**. **All hold → proceed. ANY otherwise → STOP, report all values, hand to the CEO.**
> 5. **EARNABILITY:** every AFTER literal returns **0** against the pre-edit file. **Record the zeros.**
> 6. **GATE-SURFACE CHECK (§6 coordinate-doctrine-and-gate):** `grep -c -F` for `### 2.0`, `DIRECTION VERDICT`, `RE-DRAFT` over `bellows/scripts/plan_lint.py` and `bellows/gates.py` — **expect 0**, with a same-instrument positive control (`Drafting Cycle` in `plan_lint.py`, expected 11). **Nonzero → HALT: a gate edit is owed and this plan is not chartered for it.**
>
> **Task B — PLACE E1–E5.** Each anchor asserted = 1 first. **E1–E4 INSERT; E5 REPLACES one whole line. Compose nothing but the History row.**
>
> **Task C — HISTORY ROW** (composed): prepend as the FIRST bullet under `## History` — the slug; **CEO-authorized direct amendment, a declared §6 deviation** (v1.5/1.6/1.7 precedent); ⚠️ **and a declared DRAFTING-CYCLE deviation: this plan did not run one, by CEO direction, because its subject is the cycle itself**; the LESSONS entries and `drafting-cycle-findings-2026-08-11.md` as evidence; units amended (**new §2.0; §2; §2.7; §3**); **§6's gate clause discharged by Task A(6)'s measurement**; inheritors: **`gate2-s3-register` re-drafts under these rules**, the two queued Gate-2 batches, and the §2 rewrite.
>
> **Task D — PROVE, BOTH DIRECTIONS.** Every AFTER literal present exactly once; **every anchor line byte-identical apart from the insertions**; version line and History row agree on `2.1`; `PRE_EDIT_BLOB != POST_EDIT_BLOB`. **Report the `git diff` hunk list as evidence, gating on nothing** — adjacent hunks coalesce.
>
> **Task E — DEV LOG** at `lessons-forge/knowledge/development/dc-direction-verdict-dev-log-2026-08-11.md`: `$ROOT`, both blobs, the root-repo commit sha, the earnability zeros, the Task-A(6) counts with their control, a per-edit BEFORE/AFTER pair, the composed History row verbatim, the RAW diff. **RAW output only.** End with `### Ledger Updates` and `#### Prompt Feedback`; **no `#### Forward Register`.**
>
> **FINAL ACTION — TWO COMMITS.** (1) root repo: `git -C … add DRAFTING_CYCLE.md`, pathspec commit, assert `git show --name-only --format= HEAD` prints exactly it, **record the sha**; (2) worktree: commit the dev log, same assertion. **No push.**
>
> **Scope (worktree):**
> - `knowledge/development/dc-direction-verdict-dev-log-2026-08-11.md`
>
> **Scope (root repo — outside the daemon's view, asserted by the step itself):**
> - `/Users/marklehn/Developer/GitHub/DRAFTING_CYCLE.md`
>
> **STOP. Do NOT proceed to Step 2. Wait for CEO verdict.**

**Deposits:**
- `lessons-forge/knowledge/development/dc-direction-verdict-dev-log-2026-08-11.md`

---

## STEP 2 — QA

> **FIRST — resolve `$ROOT`, assert `pwd -P` matches it.** Then **Deliverable Verification (Rule 8 / Rule 17)**: open the Step-1 dev log, confirm its Output Receipt is Complete, verify every file it claims. Any ❌ → report and HALT; make no edits yourself.
>
> **Task Q0 — RE-PIN.** `git -C "$ROOT" log --oneline` over the evidence paths; `git -C … hash-object DRAFTING_CYCLE.md` equals Step 1's `POST_EDIT_BLOB`; `git -C … status --porcelain` on both Scope paths EMPTY.
>
> **MANDATORY — Rule 20 self-check (canonical block, NOT a paraphrase)** from `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md`. **All FOUR placeholders:** `plan_slug`: `dc-direction-verdict-2026-08-11`; `qa_report_path`: `<your-tree-abs>/knowledge/qa/dc-direction-verdict-qa-2026-08-11.md`; `evidence_dir` derived from `pwd`; `required_evidence_files`: `[suite.txt, amendment-audit.txt, gate-surface.txt]`. **Deposit all three BEFORE running the block.** **Include the block's literal stdout — the banner `Rule 20 — QA Self-Check Results` and the `PASSED — SELF-CHECK PASSED` line, both byte-exact (em-dash U+2014).**
>
> ⚠️ **REPORT STRUCTURE — immediately after the verification table write exactly `## Evidence and Narrative`.** **Evidence rule: RAW command output, never a summary.**
>
> **Verification table (HALT on any FAIL):**
>
> **1. THE FIVE EDITS LANDED.** Each AFTER literal present exactly once; **quote §2.0's three verdict values and its three RE-DRAFT-forcing findings verbatim** — a §2.0 carrying two of three verdicts is a partial codification and **FAILS**. → `amendment-audit.txt`
> **2. NOTHING ELSE MOVED IN THE DOCTRINE.** Materialize `PRE_EDIT_BLOB` (`git cat-file -p <blob>`), diff against live: **only the five edit sites and the History block differ.** ⚠️ **§2 line 38 and §3 line 125 — halted plan 334's text — MUST be byte-identical.** → `amendment-audit.txt`
> **3. VERSION AND CHANGELOG AGREE**, both `2.1`, and the row names **both** declared deviations (§6, and the no-drafting-cycle one). → `amendment-audit.txt`
> **4. NO GATE EDIT WAS OWED OR MADE.** Re-run Task A(6) independently with its positive control; `git log --name-only` over both commits shows **no bellows file**. → `gate-surface.txt`
> **5. REGRESSION FLOOR.** `python3 -m pytest src/test_lessons_forge.py -q` from `$ROOT`; raw summary line. **Baseline 55 passed**; higher is not a failure, lower or failing is a **HALT**. → `suite.txt`
> **6. NOTHING ELSE MOVED.** `git -C "$ROOT" status --porcelain --` the two Scope paths is EMPTY; assert by name that `PLANNER_TEMPLATE.md`, `RULE_20_SELF_CHECK_BLOCK.md` and `LESSONS.md` are absent from both commits. ⚠️ **Do NOT assert a clean shop-root tree — the submodule pointer moves as a matter of course.**
>
> **Then `## Evidence and Narrative`, then the Output Receipt.**
>
> ⚠️ **`### Ledger Updates`** — authored via `Write`/`Edit`, EXACTLY ONCE, `##`-level after `## Evidence and Narrative`. ⚠️⚠️ **OMIT `#### Forward Register` entirely — do not write "None".**
>
> **FINAL ACTION — COMMIT YOUR DEPOSITS**, pathspec on the COMMIT, then assert `git show --name-only --format= HEAD` prints exactly them. **Commit only — NO push.**
>
> **Scope:**
> - `knowledge/qa/dc-direction-verdict-qa-2026-08-11.md`
> - `knowledge/qa/evidence/dc-direction-verdict-2026-08-11/suite.txt`
> - `knowledge/qa/evidence/dc-direction-verdict-2026-08-11/amendment-audit.txt`
> - `knowledge/qa/evidence/dc-direction-verdict-2026-08-11/gate-surface.txt`

**Deposits:**
- `lessons-forge/knowledge/qa/dc-direction-verdict-qa-2026-08-11.md`
- `lessons-forge/knowledge/qa/evidence/dc-direction-verdict-2026-08-11/suite.txt`
- `lessons-forge/knowledge/qa/evidence/dc-direction-verdict-2026-08-11/amendment-audit.txt`
- `lessons-forge/knowledge/qa/evidence/dc-direction-verdict-2026-08-11/gate-surface.txt`

---

## Drafting Cycle

⛔ **NOT RUN, BY CEO DIRECTION 2026-08-11 — A DECLARED DEVIATION.** ⚠️⚠️ **THIS PLAN DOES NOT GO THROUGH THE DRAFTING CYCLE. No walks, no cold panel.** CEO direction, taken on the evidence and recorded here rather than in a verdict.

**The reasoning, stated so a later reader can judge it:** this plan's subject **is** the drafting cycle, and the evidence it ships is that the cycle **folds ninety-odd times on artifacts whose foundation is wrong and has no way to stop.** Running the remedy through the process it repairs would spend the cycle's measured failure mode on the fix for that failure mode. **The findings are measurements, not arguments** — `drafting-cycle-findings-2026-08-11.md`, drawn from three plans run end-to-end today, every number reproducible from the repo. **Precedent: v1.5, v1.6 and v1.7 all landed as CEO-authorized direct amendments to this same file.**

⚠️ **WHAT THIS GIVES UP, stated plainly:** no lens read this artifact. Its guards are inherited from `executable-330` and `halted-executable-334` by direct diff rather than discovered by walking, and **the E1 block's wording is the Planner's and has been reviewed by nobody.** **The mitigations actually in place are mechanical, not judgemental:** the walk-0 context pin below (run, recorded); `plan_lint` at the deposit resolution; Task A's fresh-run gate, earnability run and gate-surface check; and Step 2's independent QA, unchanged and full-strength.

⚠️⚠️ **THE DEVIATION HAS A MEASURED COST, PAID DURING AUTHORING.** While recording this very section I destroyed the draft with a whole-file rewrite whose anchor matched an earlier mention of the same string, and rebuilt it from context — **the fourth instance of that class in this shop's record and the first with no snapshot to recover from.** **A drafting cycle would have caught it at the next lens.** It is recorded here because a deviation's cost belongs in the artifact, not in a chat log.

**Tier:** T2 — **T-6 fires** (doctrine). Recorded for the register even though no cycle runs, because the tier is what a future clone inherits. **T-8 does not fire for the mechanism** — E1–E4 are insertions and E5 is a whole-line replacement, both with direct precedent; ⚠️ **no edit here replaces a mid-line span**, the mechanism that had no precedent and cost the sibling plan four walks.

**Walk-0 context pin — the rule this plan ships, applied to itself and RUN 2026-08-11:**
1. **Newest same-class:** `git log --oneline -- DRAFTING_CYCLE.md` → `759b171 [334]` (HALTED, open verdict), then `0fb567a [330]` (closed). **Both read.**
2. **Anchor geometry:** all five anchors are whole-line inserts or a whole-line replace — **no mid-line spans, deliberately.**
3. **Token counts:** `2.0 (2026-08-09)` = **2** (version line + v2.0 History row) → E5 anchors on the whole line.
4. **Provenance:** §2's `Fold-and-deposit exactly once` line, §2.7's `Re-run the finding lens` line, §3's `The compact form is load-bearing` line — **none written by 334**; E1's insertion point precedes §2.1. **No edit lands on halted text.**
5. **File sha:** `0964e1a70d6752f8656051b865ebcbdf76cb3e35e1b12415e547b54c45e4a7c7` (2026-08-11) — **re-verify at deposit.**

⚠️ **The pin earned its keep before any lens could have:** it produced the newest-same-class correction, the no-mid-line-span decision, the twice-occurring version token, and the halted-text avoidance — **four of the defects that cost the sibling plan seven walks and two cold seats.** Conformance then caught three more (a dash-leading anchor ugrep parses as an option, a missing Rule-20 banner pair, a brace-expansion Scope block that parsed to zero entries). **Seven defects, zero lenses.**

**Conformance (§5):** run at the deposit path resolution after every edit to this draft.

**Closing:** ✅ **DEPOSITABLE ON CEO DIRECTION.** No cycle was run and none is owed; the deviation, its reasoning and its cost are recorded above rather than discovered later.
