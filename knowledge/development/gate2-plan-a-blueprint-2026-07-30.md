# Gate 2 Plan A — SA Blueprint

**Plan:** 287
**Date:** 2026-07-30
**Step:** 1 (SA — read-only)

---

## Task A — Pre-edit State

### SHA-256 hashes (full 64-hex)

| File | SHA-256 | Pin prefix | Match |
|------|---------|------------|-------|
| `DRAFTING_CYCLE.md` | `d8f17394c08d7dc72e550df133baba28ae897f1faf89ab2d5c78ab7efcd111ea` | `d8f17394c08d…` | ✅ |
| `PLANNER_TEMPLATE.md` | `49b726447498d0c5375c1986e3beca2d7bd435dd49ee98d452e171482d3cbe96` | `49b726447498…` | ✅ |
| `RULE_20_SELF_CHECK_BLOCK.md` | `c90ffb4bea0063e994f4b85e56df80c1653de59cb0124a1bbd982df9d52f8711` | `c90ffb4bea00…` | ✅ |

All three match the authoring-time pins in CEO Context by 12-hex prefix.

### plan_lint.py liveness confirmation

```
$ git -C /Users/marklehn/Developer/GitHub/bellows diff a59200b..HEAD --stat -- scripts/plan_lint.py
(empty)
exit=0
```

SHA `a59200b` is still what is live on bellows main. `exit=0` confirms the SHA is reachable. The shipped code is the authority for §4's description.

---

## Task B — Seven DRAFTING_CYCLE.md Edits

All edits target `/Users/marklehn/Developer/GitHub/DRAFTING_CYCLE.md`.

---

### Edit B1 — Proposal 191 (clone-against-newest cold-panel discipline)

**Gap row:** 1
**Action:** APPEND (new paragraph within §2.6)
**Anchor:** `"Author-verify cold findings; a cold reader can misread deliberate design as a defect."`
**Anchor uniqueness:** `grep -Fc 'Author-verify cold findings; a cold reader can misread deliberate design as a defect.' DRAFTING_CYCLE.md` → **1** ✅

**BEFORE:**
```
Author-verify cold findings; a cold reader can misread deliberate design as a defect.
```
(End of the §2.6 paragraph, currently at line 73.)

**AFTER:**
```
Author-verify cold findings; a cold reader can misread deliberate design as a defect.

When cloning a plan, diff the machinery against the **newest** same-class plan already shipped — not only the clone origin. Hand cold readers the newest same-class plan and ask what the clone dropped or mis-adapted. A "bounded" or "proven-clone" framing is not licence to down-tier or skip the cold panel — it is a statement about the plan's structure, not its risk.
```

**Must-survive after edit:**
- The §2.6 opening sentence (`"run the five lenses **cold**"`) — UNCHANGED, on the same line 73 as the anchor.
- `grep -Fc 'run the five lenses' <file>` must return 1.

**Required final order:** 191's paragraph appears BEFORE 194's paragraph (see Edit B2).

---

### Edit B2 — Proposal 194 (review-target rotation)

**Gap row:** 5
**Action:** APPEND (new paragraph after 191's insertion)
**Sequenced anchor:** The closing text of 191's newly-inserted clause: `"it is a statement about the plan's structure, not its risk."`
**Note:** This anchor does NOT exist in the pre-edit file — it is created by Edit B1. The DEV must apply B1 first, then anchor B2 on B1's closing sentence.

**BEFORE:** (post-B1 state)
```
A "bounded" or "proven-clone" framing is not licence to down-tier or skip the cold panel — it is a statement about the plan's structure, not its risk.
```

**AFTER:**
```
A "bounded" or "proven-clone" framing is not licence to down-tier or skip the cold panel — it is a statement about the plan's structure, not its risk.

Before each walk, identify which step mutates and when it was last examined. If a walk's folds all land in one step, aim the next walk at the other step deliberately — review-target rotation prevents the quiet step from accumulating unexamined risk while the noisy one absorbs all attention.
```

**Required final order in §2.6:** Original paragraph → 191's clone-diff paragraph → 194's target-rotation paragraph → (blank line) → `### 2.7` heading.

---

### Edit B3 — Proposal 195 + parent (subtractive-trim verification)

**Gap row:** 6
**Action:** APPEND (new bullet in §2.7)
**Anchor:** The ACTUAL last §2.7 bullet — the **Sequential-fold rule**.
**Anchor string:** `"Sequential-fold rule (extends §2.7"`
**Anchor uniqueness:** `grep -Fc 'Sequential-fold rule' DRAFTING_CYCLE.md` → **1** ✅

**⚠️ MAP DEVIATION (declared — sixth):** The map says the anchor is `"Sketch one real block."` and calls it "the last bullet in §2.7" at authoring-time `:82`. In the live file, "Sketch one real block." is at `:81` and the Sequential-fold rule is at `:82` — the Sequential-fold rule IS the last §2.7 bullet. The map's line-number-to-text association is internally inconsistent (`:82` = Sequential-fold rule, not "Sketch one real block."). This does not affect the edit: the new bullet goes after ALL existing bullets regardless of which is nominally "last." I anchor on the actual last bullet.

**BEFORE:**
```
- **Sequential-fold rule (extends §2.7 "Parallelism" and §2.6 "cumulation lives in the draft").** Run each lens against the draft **as folded by all prior lenses in this walk** — never analyze all lenses against one draft and batch the folds (a batched fork is never seen by the later lenses). The rationalization "this pass is just confirmation, so cumulation doesn't matter here" is a self-check target: it is the same false reasoning that applies to an expected-dry confirming walk (you do not know it is dry until you have run it lens-by-lens).
```

**AFTER:**
```
- **Sequential-fold rule (extends §2.7 "Parallelism" and §2.6 "cumulation lives in the draft").** Run each lens against the draft **as folded by all prior lenses in this walk** — never analyze all lenses against one draft and batch the folds (a batched fork is never seen by the later lenses). The rationalization "this pass is just confirmation, so cumulation doesn't matter here" is a self-check target: it is the same false reasoning that applies to an expected-dry confirming walk (you do not know it is dry until you have run it lens-by-lens).
- **Subtractive-trim verification.** Before removing a check on the premise that another check covers it, verify the subsumption against live data — per item, not in aggregate. When a trim removes N items, verify N premises enumerated; a claim that "the other check covers these" is not evidence until each item has been tested through the surviving check. After any edit, assert the PRESENCE of retained material, not merely the absence of removed material — a deletion is invisible to a check that greps only for new strings. Never compute an edit boundary from a delimiter on line-oriented markup (a delimiter-based split silently bisects a line that contains the delimiter as content).
```

**Required final order:** 195+parent's bullet appears BEFORE 200's bullet (see Edit B4).

---

### Edit B4 — Proposal 200, §2.7 (lens attestation integrity)

**Gap row:** 12 (§2.7 component)
**Action:** APPEND (new bullet after 195+parent's insertion)
**Sequenced anchor:** The closing text of 195+parent's bullet: `"a delimiter-based split silently bisects a line that contains the delimiter as content)."`
**Note:** This anchor does NOT exist in the pre-edit file — it is created by Edit B3. The DEV must apply B3 first.

**BEFORE:** (post-B3 state)
```
Never compute an edit boundary from a delimiter on line-oriented markup (a delimiter-based split silently bisects a line that contains the delimiter as content).
```

**AFTER:**
```
Never compute an edit boundary from a delimiter on line-oriented markup (a delimiter-based split silently bisects a line that contains the delimiter as content).
- **Lens attestation integrity.** A lens result is written only after the lens has actually run — never in the same edit as the fold it reports on. A dry pass must show evidence examined, not reconstructed justification. A false attestation discovered after the fact must be retracted in the artifact (struck with a note), not quietly corrected in place — the retraction is the record that the original was wrong, and without it a later reader trusts an attestation that was never honest.
```

**Required final order in §2.7 (last three bullets):** Sequential-fold rule → Subtractive-trim verification (195+parent) → Lens attestation integrity (200) → (blank line) → `### 2.8` heading.

---

### Edit B5 — Proposal 197 (compact Cycle Log form load-bearing)

**Gap row:** 8
**Action:** MODIFY (insert new paragraph within §3)
**Anchor:** `"The Cycle Log (compact, in the plan)"`
**Anchor uniqueness:** `grep -Fc 'The Cycle Log (compact, in the plan)' DRAFTING_CYCLE.md` → **1** ✅

The edit INSERTS a new paragraph after the existing introductory paragraph and before the fenced code example. No existing text is changed.

**BEFORE:** (lines 99–100, the introductory paragraph)
```
Every plan declares its tier in the header line (`**cycle_tier:** T1`) and — for T1+ — carries a `## Drafting Cycle` block. The block is the auditable proof the cycle ran and the anchor lessons attach to. It records **what ran and what it found**, not the findings in full (those live in the plan's evolution). One line per lens is the floor. A dry pass is an honestly reportable success — manufacturing minor findings to look diligent is the same Goodhart failure as forcing a predicted number.
```

**AFTER:**
```
Every plan declares its tier in the header line (`**cycle_tier:** T1`) and — for T1+ — carries a `## Drafting Cycle` block. The block is the auditable proof the cycle ran and the anchor lessons attach to. It records **what ran and what it found**, not the findings in full (those live in the plan's evolution). One line per lens is the floor. A dry pass is an honestly reportable success — manufacturing minor findings to look diligent is the same Goodhart failure as forcing a predicted number.

The compact form is **load-bearing** — the plan body carries structure, not narrative. Full walk-by-walk analysis lives in a scratchpad file (`scratchpad/`, session-local and ephemeral); only the per-lens summary lines appear in the plan's `## Drafting Cycle` block. Do not keep a running fold-count in the Cycle Log — fold counts belong in the compact per-lens lines (e.g., `w1 2 folded; w2 dry`), not as a separate running tally. The `## Drafting Cycle` section in a deposited plan is a **record, not instructions** — nothing in it is addressed to any executing agent, and the final QA step's gate span absorbs it, so a gate-matching string quoted in the log is evaluated as if the QA step had said it.
```

**Must-survive after edit:**
1. The fenced canonical Cycle Log example block (lines 101–113) — UNCHANGED
   - Post-edit grep: `grep -Fc '**Tier:** T2 — triggers fired: T-6 (governance surface), T-8 (novel).' <file>` must return 1
2. The T0 collapsed form sentence (line 115) — UNCHANGED
   - Post-edit grep: `grep -Fc 'the block collapses to a single line in the header context' <file>` must return 1
3. The opening sentence `"Every plan declares its tier"` — preserved verbatim in the AFTER text
   - Post-edit grep: `grep -Fc 'Every plan declares its tier in the header line' <file>` must return 1

---

### Edit B6 — Proposal 198-doc (§4 defect documentation — CORRECTION)

**Gap row:** 9
**Action:** MODIFY (correct §4's bullet list to describe shipped behaviour)
**Anchor:** `"The Self-Check (mechanical, enforced by plan_lint)"`
**Anchor uniqueness:** `grep -Fc 'The Self-Check (mechanical, enforced by plan_lint)' DRAFTING_CYCLE.md` → **1** ✅

**⚠️ This is a CORRECTION, not merely a supplement.** Plan 286 shipped code that contradicts `:126`'s description. The shipped code (`a59200b:scripts/plan_lint.py`) has four fixes: (a) `vulnerabilit\w*` matches all inflections; (b) negation-aware `dry` detection strips `not/no/never dry` before word-boundary check; (c) Closing-presence check moved outside the if/else — runs unconditionally; (d) cold-panel check uses line-anchored structural pattern. The current `:126` mandates the pre-fix rule. This edit corrects `:126` to describe the shipped behaviour and adds the Closing-presence check as a new bullet.

**BOUND from 286:** Document the negation-aware `dry` handling ONLY. The fold side is the incumbent substring check (`'fold' in ll_lower`) and is deliberately unchanged — this plan is not authorised to narrow it.

**⚠️ `:126` is a must-CHANGE pin:** Leaving it intact while appending defect descriptions would ship §4 that documents the fix and mandates its opposite.

**BEFORE:** (lines 125–126)
```
- for **T2**: a cold-panel line is present;
- the check finds the **last lens result line** (the last `- <Lens>: …` line in the Drafting Cycle block before the `**Closing:**` line) and reads its whole-line status: it WARNs iff that line contains a fold-token (`fold`) but not `dry` — reading the structured last lens line, not keyword-matching the closing prose. The closing-line prose check is retained only as a legacy fallback when no structured lens line is parseable.
```

**AFTER:**
```
- for **T2**: a cold-panel line is present, matched by a **line-anchored** structural pattern (bold-keyword `**Cold…` or dash-prefixed `- Cold…`), not a whole-block substring search — a prose mention of "cold panel" elsewhere in the block does not satisfy the check;
- the check finds the **last lens result line** (the last `- <Lens>: …` line matching the lens-name regex — which recognises all inflections via `vulnerabilit\w*`, etc. — in the Drafting Cycle block before the `**Closing:**` line) and reads its status: it WARNs iff that line contains a fold-token (substring `fold`) and lacks a genuine `dry` token — the `dry` detection is **negation-aware**, stripping negation phrases (`not dry`, `no dry`, `never dry`) before checking for `\bdry\b` as a word boundary, so a line reading "NOT dry" does not satisfy the dry condition. The closing-line prose check is retained as a legacy fallback when no structured lens line is parseable;
- the check WARNs if the Drafting Cycle block has no `**Closing:**` line, regardless of whether structured lens lines exist.
```

**Must-survive after edit (§4 paragraphs NOT touched by this edit):**
1. `**Landing posture — warn-first (deliberate).**` paragraph (line 128) — UNCHANGED
   - Post-edit grep: `grep -Fc '**Landing posture — warn-first (deliberate).**' <file>` must return 1
2. `"The gate reads structure, not truth"` paragraph (line 130) — UNCHANGED (200's §4 edit appends to it separately)
   - Post-edit grep: `grep -Fc 'The gate reads structure, not truth' <file>` must return 1
3. Lines 123–124 (the `cycle_tier` and T1+ lens-count bullets) — UNCHANGED
   - Post-edit grep: `grep -Fc 'the plan header declares' <file>` must return 1
   - Post-edit grep: `grep -Fc 'all five for T1/T2, ACID included' <file>` must return 1
4. The `"The self-check never gates on the Conflict Ledger (§2.8)"` clause — UNCHANGED
   - Post-edit grep: `grep -Fc 'never gates on the Conflict Ledger' <file>` must return 1

**Must-CHANGE confirmations:**
- `grep -Fc 'negation-aware' <file>` must return ≥1 (new text)
- `grep -Fc 'line-anchored' <file>` must return ≥1 (new text)
- `grep -Fc 'regardless of whether structured lens lines exist' <file>` must return 1 (new Closing-presence bullet)
- `grep -Fc 'reads its whole-line status: it WARNs iff that line contains a fold-token' <file>` must return **0** (old text removed)

---

### Edit B7 — Proposal 200, §4 (attestation integrity note)

**Gap row:** 12 (§4 component)
**Action:** APPEND (sentence added to integrity paragraph)
**Anchor:** `"The gate reads structure, not truth"`
**Anchor uniqueness:** `grep -Fc 'The gate reads structure, not truth' DRAFTING_CYCLE.md` → **1** ✅

**BEFORE:** (line 130, the final sentence of the integrity paragraph)
```
The gate reads structure, not truth — a Planner who writes "dry" without looking defeats it, exactly as a QA agent who hedges defeats Rule 20; that residual trust is deliberate and is why Planner verification (the second layer) still exists.
```

**AFTER:**
```
The gate reads structure, not truth — a Planner who writes "dry" without looking defeats it, exactly as a QA agent who hedges defeats Rule 20; that residual trust is deliberate and is why Planner verification (the second layer) still exists. The §2.7 lens attestation integrity rule codifies the obligation the gate cannot enforce — a lens result is written only after the lens has actually run, and a false attestation is retracted rather than quietly corrected.
```

---

## Task C — Version + History for DRAFTING_CYCLE.md

### C1 — Version bump (surgical substring swap on line 5)

**Anchor:** `"1.1 (2026-07-25). Amended only through the Iteration Protocol (§6)."`
**Anchor uniqueness:** `grep -Fc '1.1 (2026-07-25). Amended only through the Iteration Protocol (§6).' DRAFTING_CYCLE.md` → **1** ✅

**⚠️ The SHORT substring `1.1 (2026-07-25)` is NOT unique** — `grep -Fc '1.1 (2026-07-25)' DRAFTING_CYCLE.md` → **2** (`:5` version line AND `:157` History row). The lengthened anchor including the trailing clause IS unique.

**BEFORE:**
```
**Version:** 1.1 (2026-07-25). Amended only through the Iteration Protocol (§6).
```

**AFTER:**
```
**Version:** 1.2 (2026-07-30). Amended only through the Iteration Protocol (§6).
```

**⚠️ MAP DEVIATION (declared — third, per CEO Context):** The map writes `1.2 (2026-07-29)` — that is the map's authoring date. Ship date is 2026-07-30, per the 1.1 precedent (1.1 shipped 2026-07-25 and is dated 2026-07-25).

**Must-survive:** The trailing clause `Amended only through the Iteration Protocol (§6).` MUST survive — plan 278's M1 nearly destroyed it with a whole-line replace.
- Post-edit grep: `grep -Fc 'Amended only through the Iteration Protocol (§6).' <file>` must return 1

### C2 — History row (PREPEND above the 1.1 row)

**⚠️ MAP DEVIATION (declared — second, per CEO Context):** The map says "APPEND after `:157`." The `## History` table is newest-first: `:157` = 1.1 above `:158` = 1.0. The 1.2 row is PREPENDED directly above the 1.1 row to maintain newest-first order. The live order is authority.

**⚠️ §6:148 discrepancy (for the record):** §6 says a Gate-2 codification "appends a dated row." This wording is stale against the file's own newest-first table. The live order is authority; PREPEND is correct. This discrepancy does not halt execution — the plan explicitly instructs PREPEND and documents the stale wording. §6 is amendable only through the same Gate-2 route; a future batch should correct it.

**Anchor:** The `## History` heading and the 1.1 row.
**Insert:** One row directly ABOVE the `- **1.1 (2026-07-25):**` row. The 1.1 row is NOT modified.

**BEFORE:**
```
## History
- **1.1 (2026-07-25):** Codified proposals 187–190.
```

**AFTER:**
```
## History
- **1.2 (2026-07-30):** Codified proposals 191, 194, 195 (+parent), 197, 198, 200. §2.6: clone-against-newest cold-panel discipline (191), review-target rotation (194). §2.7: subtractive-trim verification with enumerated premises (195+parent), lens attestation integrity (200). §3: compact Cycle Log form load-bearing (197). §4: four shipped plan_lint defect fixes documented — negation-aware dry check, Closing-presence check unconditional, cold-panel check line-anchored, Vulnerabilities regex fixed (198). **The lens count deliberately stays five** — all additions are sub-rules of existing lenses or cross-cutting rules, not new lenses. Paired with Plan B (286, bellows).
- **1.1 (2026-07-25):** Codified proposals 187–190.
```

(The 1.1 row's full text is preserved — only its first few words are shown here for the anchor; the DEV inserts above it.)

---

## Task D — Four PLANNER_TEMPLATE.md Edits + Version + Changelog

All edits target `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md`.

---

### D0 — Version bump (lines 5 and 6)

**D0a — Version line (line 5):**
**Anchor:** `"**Version:** 4.80"`
**Anchor uniqueness:** `grep -Fc '**Version:** 4.80' PLANNER_TEMPLATE.md` → **1** ✅

**⚠️ The bare `4.80` is NOT unique** — `grep -Fc '4.80' PLANNER_TEMPLATE.md` → **3** (`:5` version, `:6` Last Updated, `:1866` Lessons Learned row). Never use replace-all on `4.80`.

**BEFORE:**
```
**Version:** 4.80
```

**AFTER:**
```
**Version:** 4.81
```

**D0b — Last Updated line (line 6):**
**Anchor:** `"**Last Updated:** 2026-07-23 (v4.80)"`
**Anchor uniqueness:** `grep -Fc '**Last Updated:** 2026-07-23 (v4.80)' PLANNER_TEMPLATE.md` → **1** ✅

**BEFORE:**
```
**Last Updated:** 2026-07-23 (v4.80)
```

**AFTER:**
```
**Last Updated:** 2026-07-30 (v4.81)
```

---

### D1 — Proposal 196 → NEW Rule 59 (read the cited rule)

**Gap row:** 7
**Action:** INSERT new rule section after Rule 58's closing `Source:` line, before the `---` separator
**Anchor:** `"Source: proposal 186, lesson 2026-07-22"`
**Anchor uniqueness:** `grep -Fc 'Source: proposal 186, lesson 2026-07-22' PLANNER_TEMPLATE.md` → **1** ✅
**Position:** After Rule 58's Source line (line 1097), before the `---` at line 1099. Rule 59 is first, Rule 60 follows — ascending order at the END of the Orchestration Plan Rules.

**BEFORE:**
```
Source: proposal 186, lesson 2026-07-22

---
```

**AFTER:**
```
Source: proposal 186, lesson 2026-07-22

### 59. Read the cited rule before citing it

Before citing a rule, convention, line number, or prior decision as authority, the author opens and reads the cited clause — never cites from memory. When about to invent a convention (a naming pattern, a format, a version line), first check whether the record already defines one. Faithful cloning reproduces ABSENCES as faithfully as guards — a mandated element missing from both parents is invisible to any clone-diff.

Source: proposal 196, lesson 2026-07-30

### 60. Rule 20 self-check form selected by plan class

When authoring a QA step's Rule 20 self-check, select the form by plan class:
- **Full canonical block** — for plans whose QA produces evidence files (doc/DB plans, code plans with test output). The block runs with adapted real evidence files (`evidence_dir` and `required_evidence_files` both non-empty). When cloning a QA step that mandates the full form, verify the plan supplies its own `required_evidence_files` set and `evidence_dir`; never clone another plan's specific evidence set blindly.
- **Simple banner** — for move-only or trivial plans with no evidence artifacts. The banner string and PASSED line are the block's ACTUAL stdout — run the canonical block with an empty `required_evidence_files` list and a real `evidence_dir`, never hand-author the output.

Both forms pass the gate identically: `gates.py` requires only the banner + PASSED line.

Source: proposal 192, lesson 2026-07-30

---
```

**Number assignment derivation:** §Q3(b) pins 196 → Rule 59. Both 192 and 196 are new Orchestration Rules that APPEND after Rule 58 (highest existing). Therefore 192 → Rule 60. Position: ascending order at END of Orchestration Plan Rules — Rule 59 (196) then Rule 60 (192). This is NOT the Checklist section — Rules and Checklist number independently (§Q3(b)).

---

### D2 — Proposal 193 → MODIFY Checklist #26 (fold-sweep sibling consistency)

**Gap row:** 4
**Action:** MODIFY
**Anchor:** `"After fixing an anti-pattern instance, sweep the whole artifact for siblings"`
**Anchor uniqueness:** `grep -Fc 'After fixing an anti-pattern instance, sweep the whole artifact for siblings' PLANNER_TEMPLATE.md` → **1** ✅

**BEFORE:**
```
### 26. After fixing an anti-pattern instance, sweep the whole artifact for siblings

After fixing any instance of an anti-pattern — a convention violation, a bare hardcoded number, a vacuous check, a wrong-signal guard, an un-isolated read — sweep the whole artifact for the same pattern and confirm zero siblings remain. The sweep must explicitly include places that merely QUOTE the pattern: negative examples, rationale text, documentation, and the fix's own illustration, where the pattern most often survives. A fix reported without a sibling-sweep is unverified.

**Worked example — convention changes.** When a plan redefines a convention — renaming a field, reformatting a header, changing a string pattern — the DEV step must grep for all occurrences of the old convention string rather than relying on a Planner-enumerated site list. The QA step must re-run the same grep and classify every hit as edited or deliberate-survivor (a site that intentionally retains the old form, e.g., a historical reference or backward-compatibility alias). Structural enumeration of the places that define a convention predictably misses the places that quote it — embedded copies, examples, documentation, test fixtures. An occurrence-grep catches both.

Source: proposals 136 + 162, lessons 2026-07-06 / 2026-07-20
```

**AFTER:**
```
### 26. After fixing an anti-pattern instance, sweep the whole artifact for siblings

After fixing any instance of an anti-pattern — a convention violation, a bare hardcoded number, a vacuous check, a wrong-signal guard, an un-isolated read — sweep the whole artifact for the same pattern and confirm zero siblings remain. The sweep must explicitly include places that merely QUOTE the pattern: negative examples, rationale text, documentation, and the fix's own illustration, where the pattern most often survives. A fix reported without a sibling-sweep is unverified. After any fold, every other site stating the same rule, number, path, or count must be checked for consistency before the fold is closed. Weight the sweep toward the step that MUTATES — the unswept site is predictably the riskier one, since the swept site already has the author's attention. The fold is not done until all sites agree.

**Worked example — convention changes.** When a plan redefines a convention — renaming a field, reformatting a header, changing a string pattern — the DEV step must grep for all occurrences of the old convention string rather than relying on a Planner-enumerated site list. The QA step must re-run the same grep and classify every hit as edited or deliberate-survivor (a site that intentionally retains the old form, e.g., a historical reference or backward-compatibility alias). Structural enumeration of the places that define a convention predictably misses the places that quote it — embedded copies, examples, documentation, test fixtures. An occurrence-grep catches both.

Source: proposals 136 + 162 + 193, lessons 2026-07-06 / 2026-07-20 / 2026-07-30
```

**Must-survive after edit:**
1. `"must explicitly include places that merely QUOTE the pattern"` clause — PRESERVED in the AFTER text
   - Post-edit grep: `grep -Fc 'merely QUOTE the pattern' <file>` must return 1
2. `"**Worked example — convention changes.**"` block — PRESERVED verbatim
   - Post-edit grep: `grep -Fc 'Worked example — convention changes.' <file>` must return 1

---

### D3 — Proposal 192-coupled → MODIFY Checklist #4 (conditional form)

**Gap row:** 3
**Action:** MODIFY
**Anchor:** `"QA step includes exact canonical Rule 20 self-check reference"`
**Anchor uniqueness:** `grep -Fc 'QA step includes exact canonical Rule 20 self-check reference' PLANNER_TEMPLATE.md` → **1** ✅

**BEFORE:**
```
### 4. QA step includes exact canonical Rule 20 self-check reference

Grep the plan file for every step identified as QA (per the `qa_steps` header field). Each QA step must contain the exact canonical template paragraph from `RULE_20_SELF_CHECK_BLOCK.md` with four placeholders filled (`plan_slug`, `qa_report_path`, `evidence_dir`, `required_evidence_files`). No paraphrasing, no "review the file" pointers, no agent-discretion language. If the template paragraph is missing or paraphrased, copy it verbatim from `RULE_20_SELF_CHECK_BLOCK.md` and fill the placeholders.

Source: proposal 75, lesson 2026-05-27
```

**AFTER:**
```
### 4. QA step includes exact canonical Rule 20 self-check reference

Grep the plan file for every step identified as QA (per the `qa_steps` header field). Each QA step must include the canonical Rule 20 self-check in the form appropriate to its plan class (per Rule 60 — form by plan class). Full-form plans: the exact canonical template paragraph from `RULE_20_SELF_CHECK_BLOCK.md` with four placeholders filled (`plan_slug`, `qa_report_path`, `evidence_dir`, `required_evidence_files`). Simple-banner plans: the banner string and PASSED line, produced by running the canonical block with an empty `required_evidence_files` list and a real `evidence_dir` — never hand-authored. No paraphrasing in either form, no "review the file" pointers, no agent-discretion language. If the template paragraph is missing or paraphrased in a full-form plan, copy it verbatim from `RULE_20_SELF_CHECK_BLOCK.md` and fill the placeholders.

Source: proposals 75 + 192, lessons 2026-05-27 / 2026-07-30
```

**⚠️ Compensating clause present:** The simple-banner form requires the block's ACTUAL stdout (`"produced by running the canonical block … never hand-authored"`), preventing unverified hand-written PASSED lines from clearing the gate.

**Must-survive after edit:**
1. `"Grep the plan file for every step identified as QA"` — PRESERVED
   - Post-edit grep: `grep -Fc 'Grep the plan file for every step identified as QA' <file>` must return 1
2. `"no agent-discretion language"` — PRESERVED
   - Post-edit grep: `grep -Fc 'no agent-discretion language' <file>` must return 1

**Cross-references:**
- `grep -Fc 'Rule 60' <file>` must return ≥1 (Checklist #4 → Rule 60 cross-reference)
- `grep -Fc 'never hand-authored' <file>` must return ≥1 (compensating clause)

---

### D4 — Lessons Learned row (PREPEND)

**Action:** PREPEND one row after the table header separator (line 1865), before the first data row (line 1866 — the v4.80 row).

**⚠️ The v4.80 Lessons Learned row at `:1866` must NOT be modified.** A replace-all on `4.80` would rewrite this row — the version edits at D0a/D0b use exact unique anchors, never bare `4.80`.

**Anchor:** The table separator row `|---|---|` at line 1865.

**BEFORE:**
```
|---|---|
| 2026-07-23 | v4.80: The Drafting Cycle extracted
```

**AFTER:**
```
|---|---|
| 2026-07-30 | v4.81: Gate 2 codification, 2026-07-30 cycle. Four edits from three proposals (192, 193, 196) plus one coupled edit. New Rule 60 for Rule 20 form-by-class selection (192). New Rule 59 — read the cited rule before citing it (196). Checklist #26 strengthened with fold-sweep sibling consistency (193). Checklist #4 amended to conditional form cross-referencing Rule 60 (192-coupled). Three proposals (192, 193, 196) → implemented. |
| 2026-07-23 | v4.80: The Drafting Cycle extracted
```

(Only the first few words of the v4.80 row are shown for anchoring; the full row is untouched.)

---

## Task E — RULE_20_SELF_CHECK_BLOCK.md Edit

Target: `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md`

---

### E1 — Proposal 199 (verification scope documentation — prose section)

**Gap row:** 11
**Action:** INSERT new `## What This Block Verifies` section
**Position:** Between the `---` separator after `## How Plans Reference This Block` (line 26) and `## Canonical Python Block` (line 28)
**Anchor:** `"## Canonical Python Block"`
**Anchor uniqueness:** `grep -Fc '## Canonical Python Block' RULE_20_SELF_CHECK_BLOCK.md` → **1** ✅

The new section documents ALL FOUR points §Q4(a) enumerates: (1) verification scope, (2) heading requirement, (3) status column glyph constraint, (4) heading coupling + FAILED-run placement.

**BEFORE:**
```
---

## Canonical Python Block
```

**AFTER:**
```
---

## What This Block Verifies

The canonical Python block below enforces two narrow structural checks — nothing more:

1. **Evidence-file presence.** Every file listed in `required_evidence_files` must exist in `evidence_dir` and be non-empty. A missing or empty evidence file is a CRITICAL failure.
2. **Hedging-keyword absence in positive-status rows.** Any markdown table row marked with a positive-status token (✅, OK, PASS, done, complete, verified) is scanned for hedging keywords (pending, inferred, extrapolated, estimated, approximate, skipped, assumed, close enough, should pass, would pass, not run). A hedge in a positive row is a CRITICAL failure.

The block does **not** verify verdicts, fail-glyphs, row counts, or the substance of any verification claim. It reads structure, not truth.

**Report format coupling.** The QA report must use a heading containing "verification" (case-insensitive) to scope the section `gates.py` reads. `gates.py::_gate_rule_20_self_check` matches headings via `"verification" in stripped.lower()` and scopes its banner/PASSED search to that section. A QA report using a different heading name for its verification table is invisible to the gate.

**Status column.** Positive-status rows use pass/fail glyphs (✅/❌) or the token equivalents listed in `POSITIVE_STATUS_TOKENS`. The block's `is_positive_row` function matches these tokens by cell equality (not substring), so a cell containing "completed" does not match "complete" — the token must be the entire cell value.

**On a FAILED run.** When the block prints `FAILED — SELF-CHECK FAILED`, the raw stdout goes into the evidence file, not the QA report body. The QA agent halts and reports to the CEO rather than proceeding with closure.

---

## Canonical Python Block
```

**⚠️ The executable Python block (lines 32–100) is UNCHANGED.** Every QA step copies it verbatim at run time. CEO Decision 1: NO `**Version:**` line is added.

**Must-survive after edit:**
1. `"## Canonical Python Block"` heading — PRESERVED
   - Post-edit grep: `grep -Fc '## Canonical Python Block' <file>` must return 1
2. `"Copy the block below verbatim"` instruction — UNCHANGED (line 30)
   - Post-edit grep: `grep -Fc 'Copy the block below verbatim' <file>` must return 1
3. The approach path: `## Canonical Python Block` → "Copy the block below verbatim" → opening ` ```python ` fence must remain adjacent, in that order, with nothing inserted between them.

---

### E2 — History row (PREPEND)

**⚠️ MAP DEVIATION (declared — fourth, per CEO Context):** The map says "APPEND after `:122`." The file has only one History row (the 2026-05-10 creation entry). Both sibling doctrine files use newest-first. This row SETS the convention for every future one by PREPENDING above the existing entry.

**Anchor:** The `## History` heading (line 120) and the existing 2026-05-10 row (line 122).

**BEFORE:**
```
## History

- **2026-05-10:** Created as the single-source canonical location.
```

**AFTER:**
```
## History

- **2026-07-30:** Documented the block's verification scope (evidence-file presence and hedging-keyword absence in positive-status rows; never verdicts or fail-glyphs), the verification-heading coupling with `gates.py`, the status-column glyph constraint (cell-equality matching), and the FAILED-run stdout placement rule. Codified from proposal 199.
- **2026-05-10:** Created as the single-source canonical location.
```

(The 2026-05-10 row's full text is preserved — only the opening is shown for anchoring.)

**CEO Decision 1:** NO `**Version:**` line added. Post-edit grep: `grep -Fc '**Version:**' RULE_20_SELF_CHECK_BLOCK.md` must return **0**.

---

## Task F — Lens-Count Guard

The three count phrases in `DRAFTING_CYCLE.md`, located by live grep (NOT from the map or plan 278):

| Phrase | Line | Full line text | Touched by any edit? |
|--------|------|----------------|---------------------|
| `full five-lens walk` | `:29` | `- **T1 — Standard cycle.** Any of T-1, T-3, T-4, T-7, T-8 fires → run the **full five-lens walk** (§2.1–§2.5).` | NO — §1 is not edited by any proposal in this batch |
| `run the five lenses` | `:73` | `After the sequential walk goes dry, rotate the **reviewer**, not the lens: run the five lenses **cold** — …` | NO — 191 and 194 APPEND after this line, they do not modify it |
| `all five` | `:124` | `- for **T1+**: a \`## Drafting Cycle\` block is present, with one result line per **required** lens (all five for T1/T2, ACID included);` | NO — §4's edit targets `:125–126`, not `:124` |

**⚠️ Confirmed: `:124`, NOT `:123`.** Plan 278's Task B3 cites `:123` and is wrong; the session-13 baton records the correction.

**No blueprinted edit modifies any of the three count phrases.** The lens count stays five.

---

## Task G — Status Flip Blueprint

### Parameterised UPDATE statement

```bash
TS="$(date -u +%Y-%m-%dT%H:%M:%SZ)" && \
sqlite3 "/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db" \
  "UPDATE lesson_proposals
   SET status = 'implemented',
       status_updated_at = '$TS',
       status_updated_by = 'ceo'
   WHERE id IN (191,192,193,194,195,196,197,198,199,200)
     AND status = 'proposed';"
```

### Three pinned columns

| Column | Value | Basis |
|--------|-------|-------|
| `status` | `'implemented'` | Target state |
| `status_updated_at` | `$TS` (format `YYYY-MM-DDTHH:MM:SSZ`) | ISO-Z form — plurality at ~34% of populated rows; lexically sortable, space-free. Computed into `$TS` FIRST, then referenced — never inline `$(date …)` into the sqlite3 argument. |
| `status_updated_by` | `'ceo'` | Plurality (121 of 200 rows) plus every prior Gate-2 codification precedent. |

### Timestamp format

`YYYY-MM-DDTHH:MM:SSZ` — ISO-Z. The corpus has no dominant convention (ISO-Z 64, `+00:00` 58, other 49, space-separated 19, NULL 10). This is a deliberate choice for the plurality + lexical-sort form.

### `.backup` restore point

```bash
BK="/Users/marklehn/Developer/GitHub/lessons-forge/data/backups/lessons-forge-pre-gate2-flip-$(date -u +%Y%m%dT%H%M%SZ).db" && \
sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" ".backup '$BK'" && \
ls -la "$BK" && \
sqlite3 "file:$BK?immutable=1" "SELECT count(*) FROM lesson_proposals WHERE id BETWEEN 191 AND 200 AND status='proposed';"
```

Expected: `ls -la` shows non-zero size; the count query returns **10**.

**⚠️ `?immutable=1`, NOT `?mode=ro`** — the live DB is WAL, so a `.backup` has no `-shm`/`-wal` sidecars; `mode=ro` cannot create them and returns error 14.

### Per-id read-back

```sql
SELECT id, status, route, status_updated_at, status_updated_by
FROM lesson_proposals
WHERE id BETWEEN 191 AND 200
ORDER BY id;
```

All ten must read `status='implemented'`, `route='codify'`, a populated `status_updated_at` in `…Z` form, and `status_updated_by='ceo'`.

### Post-flip counts

- `SELECT count(*) FROM lesson_proposals WHERE status='proposed' AND id BETWEEN 191 AND 200` → **0** (HARD assertion)
- `SELECT count(*) FROM lesson_proposals WHERE status='proposed' AND id NOT BETWEEN 191 AND 200` → expected **0** at authoring, but a non-zero value from a new proposal created during a verdict gate is legitimate and NOT a failure

### Load-bearing ordering

**Every doc edit and its COMMIT lands BEFORE the flip.** If docs land and the DB fails, the corpus says `proposed` while the doctrine carries the rules — recoverable and obvious at the gate. If the DB flipped first and a doc edit failed, the corpus asserts ten `implemented` with no codification behind them — a false permanent claim no later gate re-checks.

---

## `## When this file changes` Determinations

### Which in-flight plans inherit the amendment?

**None.** Checked all four `knowledge/decisions/` directories:
- `/Users/marklehn/Developer/GitHub/governance/knowledge/decisions/` — no non-Done files (empty of `executable-` or `diagnostic-` files)
- `/Users/marklehn/Developer/GitHub/bellows/knowledge/decisions/` — none
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/decisions/` — none
- `/Users/marklehn/Developer/GitHub/anvil/knowledge/decisions/` — none

No deposited-but-unrun plans exist in any project. No plans inherit the amended doctrine.

### Does 197's §3 change require a paired `plan_lint` edit?

**No.** 197 strengthens §3 with four prose conventions:
1. Compact form is load-bearing — PROSE (describes intent, not a structural check)
2. Full narrative lives in scratchpad — PROSE (organizational, not enforceable mechanically)
3. RECORD-not-instructions banner — PROSE (a convention for authors, not a gate check)
4. No running fold-count in the log — PROSE (a prohibition, not a structural pattern plan_lint could detect)

None of these add or alter a structural requirement that `plan_lint` enforces. The existing `plan_lint` checks (`cycle_tier` declaration, `## Drafting Cycle` block, required lens lines, cold-panel line, fold/dry status, `**Closing:**` line) are unchanged by 197's additions.

**§4 IS amended by 198-doc, but that amendment corrects §4 to match the ALREADY SHIPPED code from plan 286.** The code shipped first; the doc now catches up. There is no new gate behaviour to implement — the gate already behaves as the corrected §4 describes.

**This plan is NOT chartered for a gate edit.** If the analysis above were wrong — if 197's §3 change DID alter what `plan_lint` enforces — the correct action would be to HALT and report, not to proceed with a gate edit.

---

## Declared Deviations from the Map (Summary)

| # | Deviation | Reason |
|---|-----------|--------|
| 1 | §4 is a CORRECTION, not an append | Plan 286 supersedes map row 9's framing — `:126` mandates the pre-fix rule |
| 2 | `## History` rows PREPEND (DRAFTING_CYCLE.md) | The live table is newest-first; appending inverts the convention |
| 3 | Version dated `2026-07-30`, not `2026-07-29` | Ship date, per the 1.1 precedent |
| 4 | `## History` row PREPENDS (RULE_20_SELF_CHECK_BLOCK.md) | File has one row so nothing establishes order; sibling files are newest-first — this row sets the convention |
| 5 | Seven edits enumerated as 191, 194, 195+parent, 197, 198-doc, 200×2 sites | Map counts the parent as "the 7th edit"; this plan counts 200's two sites. Both total seven. |
| 6 | §2.7 last-bullet anchor is the Sequential-fold rule, not "Sketch one real block." | Map error — in the live file, line 81 = "Sketch one real block." and line 82 = Sequential-fold rule. The map claims `:82` = "Sketch one real block." which is internally inconsistent. The edit lands in the same place either way. |

---

## 192's Assigned Rule Number

**192 → Rule 60.**

Derivation: The highest existing Orchestration Plan Rule is 58. §Q3(b) pins 196 → Rule 59. Therefore 192 → Rule 60. Both are new rules appended at the END of the Orchestration Plan Rules, in ascending order: Rule 59 (196) then Rule 60 (192).

The Checklist #4 coupled edit (D3) cross-references `Rule 60`.

---

## Output Receipt

**Status:** Complete

### Deposits
- `knowledge/development/gate2-plan-a-blueprint-2026-07-30.md` (this file)

### Ledger Updates

#### Prompt Feedback
- **(SA, plan 287, Step 1):** The diagnostic map's line-number-to-text associations should be verified at the point of use rather than trusted — the map associated `:82` with "Sketch one real block." when line 82 in the live file is actually the Sequential-fold rule. Line numbers drift between authoring and execution; quoted unique strings do not.
