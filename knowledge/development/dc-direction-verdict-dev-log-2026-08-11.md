# Dev Log — dc-direction-verdict-2026-08-11 (Step 1)

**Plan:** executable-343
**Slug:** dc-direction-verdict-2026-08-11
**Date:** 2026-08-11
**Step:** 1 (DEV)

---

## Environment

- **$ROOT:** `/Users/marklehn/Developer/GitHub`
- **PRE_EDIT_BLOB:** `9348ce51ebe099f6fbcd5897bf4260cd28940dfe`
- **POST_EDIT_BLOB:** `d58cfe004e933e17103100866a38ad4bc01e65ee`
- **Root-repo commit:** `ecee4b374482a0a6bca2b262e6228375fb4915f6`
- **File SHA-256:** `0964e1a70d6752f8656051b865ebcbdf76cb3e35e1b12415e547b54c45e4a7c7` (verified = expected)

---

## Task A — Earnability Zeros

Every AFTER literal returns 0 against the pre-edit file:

```
grep -c -F "### 2.0 Walk 0"                                    → 0
grep -c -F "A RE-DRAFT verdict (§2.0) ends the cycle"           → 0
grep -c -F "A fold that RECLASSIFIES, REORDERS, MERGES or DELETES" → 0
grep -c -F "A COUNT IN PROSE THAT NO ASSERTION READS"           → 0
grep -c -F "A CONSTRAINT THAT SPANS STEPS"                      → 0
grep -c -F "PROVE EVERY POST-CONDITION CAN FAIL"                → 0
grep -c -F "The Cycle Log records the walk-0 context pin"       → 0
grep -c -F "**Version:** 2.1 (2026-08-11)"                     → 0
```

---

## Task A(6) — Gate-Surface Check

```
grep -c -F "### 2.0"            bellows/scripts/plan_lint.py → 0
grep -c -F "DIRECTION VERDICT"  bellows/scripts/plan_lint.py → 0
grep -c -F "RE-DRAFT"           bellows/scripts/plan_lint.py → 0
grep -c -F "### 2.0"            bellows/gates.py             → 0
grep -c -F "DIRECTION VERDICT"  bellows/gates.py             → 0
grep -c -F "RE-DRAFT"           bellows/gates.py             → 0

Positive control:
grep -c -F "Drafting Cycle"     bellows/scripts/plan_lint.py → 11
```

---

## Per-Edit BEFORE/AFTER

### E1 — INSERT new §2.0 block before `### 2.1 Lens 1 — Weak spots`

**BEFORE (context):**
```
Each lens states its **core question**, its **standing sub-questions** (numbered — these are the addressable units §6 amends), its **required evidence**, and its **skip-conditions**.

### 2.1 Lens 1 — Weak spots
```

**AFTER (context):**
```
Each lens states its **core question**, its **standing sub-questions** (numbered — these are the addressable units §6 amends), its **required evidence**, and its **skip-conditions**.

### 2.0 Walk 0 — the context pin and the direction verdict

**Before lens 1 runs, MEASURE the ground the draft stands on. Never recall it.** Record in the Cycle Log: (1) `git log --oneline -- <target file>` — the **newest same-class plan**, which is the §2.6 clone-diff target; (2) for every anchor the plan will edit, its **line number, the line's total length, and the fragment's start column** — is this a whole line or a span inside one, and what else is on that line; (3) a file-wide occurrence count for every token being replaced; (4) for every target line, **which plan last wrote it and that plan's `lifecycle_state`**; (5) the target file's sha. **Five measurements. They cost seconds and they are the foundation every later pass assumes.**

**Then, after walk 1, the author issues a DIRECTION VERDICT — one of three, recorded with its reasoning:**
- **PROCEED** — the angle is right; walk on.
- **CUT-AND-PROCEED** — the angle is right but a region must be removed first (§2.8's third resolution).
- ⛔ **RE-DRAFT — the angle is WRONG. The cycle ENDS here without a deposit. The draft returns to conversation and a new v0 is authored; it is not repaired in place.**

⚠️⚠️ **RE-DRAFT is a NORMAL, SUCCESSFUL outcome of a drafting cycle, not a failure.** A cycle that identifies a wrong angle at walk 1 and stops has done its job at the lowest cost available. **The failure mode it exists to prevent is folding an artifact whose foundation is wrong** — measured at 62% of warm-walk findings being the walk's own fold damage, on a plan whose v0 was wrong in three ways and which had, at seven walks, still not converged.

⚠️ **THREE FINDINGS FORCE A RE-DRAFT VERDICT — they are not weighed, they decide:** a finding that invalidates **(a) the plan's clone origin or the precedent it inherits from**, **(b) the mechanism by which its edits act**, or **(c) a premise that licenses its scope**. **Any one of these is a DIRECTION finding, not a fold.** Folding it repairs a sentence and leaves the artifact built on the thing that was wrong.

### 2.1 Lens 1 — Weak spots
```

### E2 — APPEND to §2, after `Fold-and-deposit **exactly once**.`

**BEFORE (context):**
```
Fold-and-deposit **exactly once**.

Each lens states its **core question**
```

**AFTER (context):**
```
Fold-and-deposit **exactly once**.

⚠️ **A RE-DRAFT verdict (§2.0) ends the cycle without a deposit and without meeting this bar.** The bar measures whether an artifact is settling; it says nothing about whether the artifact is correct in kind, and a cycle must be able to answer the second question without first satisfying the first.

Each lens states its **core question**
```

### E3 — APPEND to §2.7, after `- **Re-run the finding lens on its own fix.**`

**BEFORE (context):**
```
- **Re-run the finding lens on its own fix.** Treat a fold as a new draft; an accommodation for one edge case often breaks on that exact edge.
- **Novel lens = provisional fold.**
```

**AFTER (context):**
```
- **Re-run the finding lens on its own fix.** Treat a fold as a new draft; an accommodation for one edge case often breaks on that exact edge.
- ⚠️ **A fold that RECLASSIFIES, REORDERS, MERGES or DELETES a branch is a control-flow change, not a wording change — diff it as one.** For every input value, name the branch it took **before** and **after**, and confirm each still terminates the same way. **A stop that disappears is the failure mode and it is invisible in a diff of the sentence**, because the name of a state and the branch for that state live in the same sentence. Measured: five consecutive walks where a correct reclassification silently widened what proceeds.
- ⚠️ **A COUNT IN PROSE THAT NO ASSERTION READS WILL GO STALE. Declare a set ONCE — a table, a list — and have every other site point at it rather than restate its size.** Measured: eight instances in one cycle, each individually corrected, the eighth contradicting a standing CEO hold.
- ⚠️ **A CONSTRAINT THAT SPANS STEPS is named as a constraint WITH ITS SITES, never as prose inside one step** — otherwise it is carried by whichever step the author happens to be drafting and the other half is silently dropped. Measured: three half-carried guards in one cycle, one leaving the plan's highest-value check with no independent observer.
- ⚠️⚠️ **PROVE EVERY POST-CONDITION CAN FAIL, BEFORE THE EDIT.** Run each new assertion's literal against the **pre-edit** state and confirm it returns the failing value. **A post-condition that already passes before the edit is not a post-condition.** Measured: three successive post-conditions in one cycle, each of which would have HALTED a correct run.
- **Novel lens = provisional fold.**
```

### E4 — APPEND to §3, after `The compact form is **load-bearing**`

**BEFORE (context):**
```
...a gate-matching string quoted in the log is evaluated as if the QA step had said it.

**The Cycle Log is part of the artifact
```

**AFTER (context):**
```
...a gate-matching string quoted in the log is evaluated as if the QA step had said it.

⚠️ **The Cycle Log records the walk-0 context pin (§2.0) and the direction verdict with its reasoning.** A cycle that ended in RE-DRAFT records the pin, the verdict and which of the three forcing findings produced it — **that record is the input to the next v0, and it is the whole return on the cycle.**

**The Cycle Log is part of the artifact
```

### E5 — REPLACE version line

**BEFORE:**
```
**Version:** 2.0 (2026-08-09). Amended only through the Iteration Protocol (§6).
```

**AFTER:**
```
**Version:** 2.1 (2026-08-11). Amended only through the Iteration Protocol (§6).
```

---

## History Row (composed, verbatim)

- **2.1 (2026-08-11):** slug dc-direction-verdict-2026-08-11; CEO-authorized direct amendment, a declared §6 deviation (v1.5/v1.6/v1.7 precedent); ⚠️ a declared DRAFTING-CYCLE deviation: this plan did not run a drafting cycle, by CEO direction, because its subject is the cycle itself (the reasoning and its cost are recorded in the plan's `## Drafting Cycle` block). Evidence: LESSONS 2026-08-11 entries 255–259 and `drafting-cycle-findings-2026-08-11.md`. Units amended: new §2.0 (Walk 0 — the context pin and the direction verdict); §2 (RE-DRAFT bar exemption); §2.7 (four fold rules — control-flow change, count-in-prose, cross-step constraint, pre-edit post-condition); §3 (walk-0 pin and direction verdict in the Cycle Log). §6's coordinate-doctrine-and-gate clause discharged by measurement: `### 2.0`, `DIRECTION VERDICT`, `RE-DRAFT` all return 0 in `plan_lint.py` and `gates.py` (positive control: `Drafting Cycle` in `plan_lint.py` = 11). Inheritors: `gate2-s3-register` re-drafts under these rules, the two queued Gate-2 batches, and the §2 rewrite.

---

## RAW Diff

```diff
diff --git a/DRAFTING_CYCLE.md b/DRAFTING_CYCLE.md
index 9348ce5..d58cfe0 100644
--- a/DRAFTING_CYCLE.md
+++ b/DRAFTING_CYCLE.md
@@ -2,7 +2,7 @@
 
 **Single source of truth.** This file publishes the Drafting Cycle: the adversarial pre-deposit analysis every orchestration plan passes through. `PLANNER_TEMPLATE.md`'s `## The Drafting Cycle` section references this file and does not restate it. Modelled on `RULE_20_SELF_CHECK_BLOCK.md` and `READONLY_AUDIT_CONTRACT.md` — one canonical location, referenced not inlined.
 
-**Version:** 2.0 (2026-08-09). Amended only through the Iteration Protocol (§6).
+**Version:** 2.1 (2026-08-11). Amended only through the Iteration Protocol (§6).
 
 **The two-layer contract this belongs to.** The Drafting Cycle hardens the **plan** *before* deposit. Planner verification at the verdict gate hardens the **deliverable** *after* each step. Both are required; neither substitutes for the other. Leaning on the second to catch what the first should is a known failure mode — the 216→217 boundary established the distinction. This file codifies the first layer as a mechanical system: **compute the tier (§1) → run the lenses that tier requires (§2) → record the Cycle Log (§3) → the self-check enforces it (§4).**
 
@@ -37,8 +37,23 @@ A plan may always self-escalate above the computed tier; it may never drop below
 
 Walk the lenses **in order, one pass per lens per walk.** Fold all accepted findings after each pass. Re-run a lens only on a **subsequent** walk — a fold's defect is usually caught by a *different* lens on different evidence. The cycle is **done** when a full walk returns findings that are **record-class only** — nothing that would change what an executing agent DOES — **and predominantly fold-introduced**, meaning defects this cycle's own folds created rather than defects that pre-existed it. **Both conditions are required, and the origin split is stated as a number in the Cycle Log** (`N of M fold-introduced`). ⚠️ **A falling finding-count is NOT the convergence signal** — severity falls because the same regions are being re-read, not because the artifact is sound. Budget for a cold panel's yield staying **flat**: a five-lens sequential panel returned 11 / 12 / 12 / 12 / 12 with no decay, roughly a third of each round being defects the immediately preceding round's folds introduced. **The signal is the noise floor, not an unexamined region:** after walk 1 there is none — a walk is every lens over the whole artifact — so no pass may be justified by naming one. A pass instead names the **new surface the last culmination created**, and reports the origin split of what it found; a pass whose findings are mostly its predecessor's fold damage is the noise floor, not progress (measured: 14 of 19 at exec-330, walk 4 at 0-for-3 pre-existing; 3 of 4 at exec-332; ten of ten ACID passes catching a culmination-introduced defect). The **last event before deposit is either a dry lens pass or a declared judged stop meeting the bar above** — **a judged stop is a normal outcome, not a deviation**, recorded with its reasoning. ⚠️ **A finding that is not record-class RE-OPENS THE WALK:** the bar is unmet and the cycle continues. Folds made on a closing walk that DOES meet the bar are record-class by the bar's own condition; those landing in the closing record are read by the closing-record re-read (§2.7), and **any that land elsewhere are enumerated individually in the residue list** — the re-read covers the record, not the whole artifact, and must not be cited as though it did. ⚠️ **This is a stated relaxation, not an oversight:** the prior criterion required a further confirming pass whenever the final pass folded anything, so a qualifying close may now deposit with record-class edits no lens has read. On T2 the cold panel supplies that reader (§2.6 — the panel is not waived by a judged stop). **On T1 there is no such reader, so a T1 judged stop rests on the residue enumeration and the closing-record re-read alone.** ⚠️ **A judged stop is auditable or it is not a stop.** Both of the bar's conditions are the author's own judgement, and the author is the party who wants to finish, so a bare assertion of record-class-ness is not a close — the older criterion was checkable by anyone (zero findings is observable) and its replacement stays checkable only by showing the work. **The Closing line therefore carries the origin split as a number and NAMES each residue finding's class in a clause apiece** (`3 record-class: two count-word lags, one stale label`); the per-finding detail — what each was, where, and which fold produced it — lives in the scratchpad walk register, which the closing-record re-read reads. ⚠️ **This is the ONE bounded exception to §3's compact-form rule, and §3 states it** — the bar cannot be audited from a log that may not name what it stopped on. Fold-and-deposit **exactly once**.
 
+⚠️ **A RE-DRAFT verdict (§2.0) ends the cycle without a deposit and without meeting this bar.** The bar measures whether an artifact is settling; it says nothing about whether the artifact is correct in kind, and a cycle must be able to answer the second question without first satisfying the first.
+
 Each lens states its **core question**, its **standing sub-questions** (numbered — these are the addressable units §6 amends), its **required evidence**, and its **skip-conditions**.
 
+### 2.0 Walk 0 — the context pin and the direction verdict
+
+**Before lens 1 runs, MEASURE the ground the draft stands on. Never recall it.** Record in the Cycle Log: (1) `git log --oneline -- <target file>` — the **newest same-class plan**, which is the §2.6 clone-diff target; (2) for every anchor the plan will edit, its **line number, the line's total length, and the fragment's start column** — is this a whole line or a span inside one, and what else is on that line; (3) a file-wide occurrence count for every token being replaced; (4) for every target line, **which plan last wrote it and that plan's `lifecycle_state`**; (5) the target file's sha. **Five measurements. They cost seconds and they are the foundation every later pass assumes.**
+
+**Then, after walk 1, the author issues a DIRECTION VERDICT — one of three, recorded with its reasoning:**
+- **PROCEED** — the angle is right; walk on.
+- **CUT-AND-PROCEED** — the angle is right but a region must be removed first (§2.8's third resolution).
+- ⛔ **RE-DRAFT — the angle is WRONG. The cycle ENDS here without a deposit. The draft returns to conversation and a new v0 is authored; it is not repaired in place.**
+
+⚠️⚠️ **RE-DRAFT is a NORMAL, SUCCESSFUL outcome of a drafting cycle, not a failure.** A cycle that identifies a wrong angle at walk 1 and stops has done its job at the lowest cost available. **The failure mode it exists to prevent is folding an artifact whose foundation is wrong** — measured at 62% of warm-walk findings being the walk's own fold damage, on a plan whose v0 was wrong in three ways and which had, at seven walks, still not converged.
+
+⚠️ **THREE FINDINGS FORCE A RE-DRAFT VERDICT — they are not weighed, they decide:** a finding that invalidates **(a) the plan's clone origin or the precedent it inherits from**, **(b) the mechanism by which its edits act**, or **(c) a premise that licenses its scope**. **Any one of these is a DIRECTION finding, not a fold.** Folding it repairs a sentence and leaves the artifact built on the thing that was wrong.
+
 ### 2.1 Lens 1 — Weak spots
  - **Core:** is the plan itself correct and safe?
  - **Sub-questions:** (1.1) does each step do what its prose claims? (1.2) are the pre/post-conditions real and checkable? (1.3) does any step rest on an unstated assumption? (1.4) **for a diagnostic**, aim weak-spots at the QUESTIONS themselves — is each answerable, answerable *from here*, and phrased so "unknown" is an acceptable answer rather than a failure the agent papers over? (diag-229 Q6/Q7, struck for answering data questions from data that did not exist.)
@@ -92,6 +107,10 @@ This registry defines brief TEXT only. It sets no seat count, seat structure, or
  - **Re-read the closing record after the close.** A walk certifies everything except the paragraph that records it — the closing prose is written after the last pass has run, so it is pass-unexamined **by construction**, a structural blind spot rather than an oversight. After the final pass and its folds, re-read the closing record alone — the Closing line, the per-lens summary lines, the status header — adversarially and against the artifact. This is a short read of a paragraph, never a walk, and it is **mandatory at EVERY close — dry or judged stop alike.** It is most load-bearing on a judged stop, because the bar's own condition guarantees the residue is record-class; but the blind spot is structural, so a dry close does not escape it. (Measured: the shop's first post-**dry**-close re-read raised 2, both in closing prose, one claiming what its cited precedent declines to claim — the measurement comes from the DRY branch, which is why the rule may not be scoped to the other one.)
  - **Re-run the finding lens on its own fix.** Treat a fold as a new draft; an accommodation for one edge case often breaks on that exact edge.
+- ⚠️ **A fold that RECLASSIFIES, REORDERS, MERGES or DELETES a branch is a control-flow change, not a wording change — diff it as one.** For every input value, name the branch it took **before** and **after**, and confirm each still terminates the same way. **A stop that disappears is the failure mode and it is invisible in a diff of the sentence**, because the name of a state and the branch for that state live in the same sentence. Measured: five consecutive walks where a correct reclassification silently widened what proceeds.
+- ⚠️ **A COUNT IN PROSE THAT NO ASSERTION READS WILL GO STALE. Declare a set ONCE — a table, a list — and have every other site point at it rather than restate its size.** Measured: eight instances in one cycle, each individually corrected, the eighth contradicting a standing CEO hold.
+- ⚠️ **A CONSTRAINT THAT SPANS STEPS is named as a constraint WITH ITS SITES, never as prose inside one step** — otherwise it is carried by whichever step the author happens to be drafting and the other half is silently dropped. Measured: three half-carried guards in one cycle, one leaving the plan's highest-value check with no independent observer.
+- ⚠️⚠️ **PROVE EVERY POST-CONDITION CAN FAIL, BEFORE THE EDIT.** Run each new assertion's literal against the **pre-edit** state and confirm it returns the failing value. **A post-condition that already passes before the edit is not a post-condition.** Measured: three successive post-conditions in one cycle, each of which would have HALTED a correct run.
  - **Novel lens = provisional fold.** A new lens reliably finds the right window and reliably ships a broken mechanism; sequence a standing lens immediately behind its first fold, aimed at whether the new guard is *executable*.
  - **Parallelism within a lens, never across.** Concurrent readers feeding one fold is fine; concurrent *lenses* sever cumulation (that is a panel pass — label it).
  - **Extraction contract.** Before splitting shared content, diff the regions and move only byte-identical clauses; state what moves, what stays, how it is retrieved, and what the retrieval promises.
@@ -122,6 +141,8 @@ Every plan declares its tier in the header line (`**cycle_tier:** T1`) and — f
 
  The compact form is **load-bearing** — the plan body carries structure, not narrative. Full walk-by-walk analysis lives in a scratchpad file (`scratchpad/`, session-local and ephemeral); only the per-lens summary lines appear in the plan's `## Drafting Cycle` block. Do not keep a running fold-count in the Cycle Log — fold counts belong in the compact per-lens lines (e.g., `w1 2 folded; w2 dry`), not as a separate running tally. The `## Drafting Cycle` section in a deposited plan is a **record, not instructions** — nothing in it is addressed to any executing agent, and the final QA step's gate span absorbs it, so a gate-matching string quoted in the log is evaluated as if the QA step had said it.
 
+⚠️ **The Cycle Log records the walk-0 context pin (§2.0) and the direction verdict with its reasoning.** A cycle that ended in RE-DRAFT records the pin, the verdict and which of the three forcing findings produced it — **that record is the input to the next v0, and it is the whole return on the cycle.**
+
  **The Cycle Log is part of the artifact, and every walk covers it — name it explicitly in the walk's coverage rather than assuming it was swept.** The record is rewritten more often than any other region and read less often: attention follows what each phase changed, never what the changes accumulated into. (Measured: a walk that finally read a Cycle Log no lens had covered returned six of its eight findings there, every one the record decaying while the artifact converged.) **Count record-decay findings separately from artifact findings** in the per-lens lines — they are the class §2's bar reads, and merging them into one total hides exactly the signal it needs. ⚠️ **One bounded exception to the compact form above:** a cycle closing on a judged stop names each residue finding's CLASS in a clause apiece on the Closing line, alongside the origin split. The per-finding detail stays in the scratchpad register; what enters the block is a class list, not narrative.
 
  **The Cycle Log must therefore contain no string a gate matches — describe such strings, never quote them.** This covers Rule 20 banner text, deposit and scope markers, path tokens, and test-name patterns. **The prohibition is scoped to the `## Drafting Cycle` block:** a plan's QA step MUST carry the banner strings, because they are what the gate requires; it is the RECORD that must not repeat them.
@@ -187,6 +208,7 @@ This file is the **base**; lessons refine it without rewriting it.
  - Keep the `plan_lint` self-check (§4) in lockstep with §1/§3 — the gate's tests are part of the change.
 
  ## History
+- **2.1 (2026-08-11):** slug dc-direction-verdict-2026-08-11; CEO-authorized direct amendment, a declared §6 deviation (v1.5/v1.6/v1.7 precedent); ⚠️ a declared DRAFTING-CYCLE deviation: this plan did not run a drafting cycle, by CEO direction, because its subject is the cycle itself (the reasoning and its cost are recorded in the plan's `## Drafting Cycle` block). Evidence: LESSONS 2026-08-11 entries 255–259 and `drafting-cycle-findings-2026-08-11.md`. Units amended: new §2.0 (Walk 0 — the context pin and the direction verdict); §2 (RE-DRAFT bar exemption); §2.7 (four fold rules — control-flow change, count-in-prose, cross-step constraint, pre-edit post-condition); §3 (walk-0 pin and direction verdict in the Cycle Log). §6's coordinate-doctrine-and-gate clause discharged by measurement: `### 2.0`, `DIRECTION VERDICT`, `RE-DRAFT` all return 0 in `plan_lint.py` and `gates.py` (positive control: `Drafting Cycle` in `plan_lint.py` = 11). Inheritors: `gate2-s3-register` re-drafts under these rules, the two queued Gate-2 batches, and the §2 rewrite.
  - **2.0 (2026-08-09):** slug shape-amendment-2026-08-09; ...
```

---

### Ledger Updates

#### Prompt Feedback
