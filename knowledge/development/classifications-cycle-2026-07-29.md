# Classifications — Cycle 2026-07-29 (Session-12 Batch)

## Cycle Dict

```
ingested_count: 8
updated_count: 0
unchanged_count: 127
duplicates_marked_count: 0
needs_classification: [185, 186, 187, 188, 189, 190, 191, 192]
terminal_proposals_flagged: []
cycle_timestamp: 2026-07-29T17:54:29.407564+00:00
```

## Cluster Synthesis

8 entries from plan 282's drafting cycle — 5 planner-discipline authoring refinements + 3 bellows-integration gate defects; MIXED targets across 3 artifacts (PLANNER_TEMPLATE.md, DRAFTING_CYCLE.md, RULE_20_SELF_CHECK_BLOCK.md), 2 with hard code couplings (entry 190: plan_lint.py, entry 191: gates.py).

### Codification-effect prediction

If these entries are codified, the NEXT plan drafted after Gate 2 should show:
- **185 (sweep every site)** — zero folds that are repairs of an earlier fold's unswept sibling. This cycle had at least eight, two of them repairs-of-repairs.
- **188 (read the cited rule)** — zero citation corrections from its cold panel. This cycle had six, plus one mislabel inherited from both parents.
- **190 (plan_lint section 4)** — the closing WARN tracks the actual disposition. On this plan it flipped in both directions on prose wording alone, disposition unchanged.
- **192 (unrun attestation)** — every lens line written after its pass ran, with no retraction needed.
- **187 (verification granularity)** — presence audits assert what was KEPT, not only that what was removed is gone. This cycle's 51-artifact audit passed while five real seams existed.

## Per-Entry Classifications

### Proposal 193 (Entry 185) — governance_rule

**Entry:** 2026-07-28: A fold lands where the defect was NOTICED, not everywhere the changed thing is DESCRIBED — sweep every site before closing the fold

**Category:** governance_rule | **Confidence:** high | **Target:** PLANNER_TEMPLATE.md | **Layer:** governance

**Reasoning:** Entry documents ten instances in one cycle where "a guard is corrected at the point the lens found it, while the same rule, number, or path stated elsewhere in the plan goes stale." Concrete examples: "plan_lint.py struck from QA row 6 but left in the evidence-deposit instruction; the ?mode=ro fallback written into Step 2 while Step 1 had two uses." The remedy is documentary: "the fold is not done until they agree." Family names Checklist #26 directly.

**Suggested action:** Strengthen PLANNER_TEMPLATE.md Checklist #26 to require that after any fold, every other site stating the same rule, number, path, or count is checked for consistency before the fold is closed. Weight the sweep toward the step that MUTATES.

---

### Proposal 194 (Entry 186) — governance_rule

**Entry:** 2026-07-28: Review attention follows CHURN, not RISK — the step that mutates can go unreviewed while the step that only reads is polished

**Category:** governance_rule | **Confidence:** high | **Target:** DRAFTING_CYCLE.md | **Layer:** governance

**Reasoning:** Entry observes that "Step 1 — the only step that writes to the canonical corpus — went effectively unreviewed after walk 1" because "each fold makes a step denser, density makes it look like where the danger is, and the next fold goes there too." When Step 1 was finally reviewed it "yielded three MATERIAL findings immediately." The fix is a documentary rule rotating the review TARGET.

**Suggested action:** Add a rule to DRAFTING_CYCLE.md section 2.6 requiring that before each walk, the reviewer identifies which step mutates and when it was last examined. If all folds in a walk land in one step, aim the next walk at the other one deliberately.

---

### Proposal 195 (Entry 187) — governance_rule

**Entry:** 2026-07-28: The granularity of a verification must match the granularity of the change it certifies

**Category:** governance_rule | **Confidence:** high | **Target:** DRAFTING_CYCLE.md | **Layer:** governance

**Reasoning:** Entry documents three failures: (a) "a subtractive trim removed a clause listing four before-items... justified by 'rows 3/4/5 already cover this' — the premise was checked in aggregate and was false for the two non-before-items"; (b) "the correcting fold... stopped one item short — the fix for an incomplete check was itself incomplete, identically"; (c) "a slice-based edit whose end was computed from a delimiter swallowed the rest of a markdown blockquote line." Family extends the 2026-07-25 subsumption-verification entry, adding granularity.

**Suggested action:** Add a rule to DRAFTING_CYCLE.md sections 2.4/2.7 requiring: when a trim removes N items, verify N premises enumerated; after any edit, assert PRESENCE of retained material; never compute an edit boundary from a delimiter on line-oriented markup.

---

### Proposal 196 (Entry 188) — governance_rule

**Entry:** 2026-07-28: READ the cited rule; do not recall it — seven folds in one cycle came from this single move

**Category:** governance_rule | **Confidence:** high | **Target:** PLANNER_TEMPLATE.md | **Layer:** governance

**Reasoning:** Entry states "Every time plan 282 opened a rule it had cited from memory, the citation was wrong in a way that mattered." Examples: "Rule 19 was invoked to catch a case its keyword list cannot match"; "Rule 17's mandated deliverable-verification sub-section was absent — from this plan and from the parent it cloned." The fix is: "before citing a rule as authority, open it and read the clause — the cost is one command." Family extends Rule 27 from what to cite to verifying citations.

**Note for Gate 1:** The entry's Family line cites "Rule 27 ('reference, don't re-derive')" but Rule 27 (PLANNER_TEMPLATE.md line 824) actually reads "Diagnostic-derived plans cite findings, never supplement with source reads." The entry's gloss does not match the rule it names — an instance of the very failure the entry describes, inside the entry. Gate 2 must place it against the rule's real text.

**Suggested action:** Add a rule to PLANNER_TEMPLATE.md requiring that before citing a rule as authority, the author opens and reads the cited clause. When inventing a convention, first check whether the record already defines one.

---

### Proposal 197 (Entry 189) — governance_rule

**Entry:** 2026-07-28: DRAFTING_CYCLE.md section 3's "compact" is load-bearing — a narrative Cycle Log becomes an instruction surface inside the final step's span

**Category:** governance_rule | **Confidence:** high | **Target:** DRAFTING_CYCLE.md | **Layer:** governance

**Reasoning:** Entry documents that the Cycle Log "grew to 138,233 characters — nearly double the 71k plan body" and "the log narrated rules that later folds had REMOVED from the body — a QA agent encountering a confidently-worded rule inside its own plan has no way to know it was superseded 40k characters earlier." Compacting fixed it: "from 211,531 to 75,098 chars." Family: "first entry against section 3 itself."

**Suggested action:** Strengthen DRAFTING_CYCLE.md section 3 to make the compact Cycle Log form load-bearing: one line per lens, full narrative in a scratchpad file, carry a "this section is a RECORD, not instructions" banner.

---

### Proposal 198 (Entry 190) — instrumentation

**Entry:** 2026-07-28: plan_lint's section 4 Drafting-Cycle check has four independent defects — three of its sub-checks cannot fail and the closing check inverts on "NOT dry"

**Category:** instrumentation | **Confidence:** high | **Target:** DRAFTING_CYCLE.md | **Layer:** governance

**Reasoning:** Entry states "Found by running negative controls against plan_lint rather than trusting a clean exit." Four defects: (a) "The lens-line regex uses vulnerabilit-word-boundary — 'Vulnerabilities' continues with 'i', so there is no word boundary and no Vulnerabilities lens line has ever matched"; (b) "the closing check tests has_fold and not has_dry by substring, so 'NOT dry' satisfies has_dry and passes"; (c) "the missing-Closing branch sits in an else reached only when NO lens line exists, so it is unreachable"; (d) "The cold-panel check greps across the whole block, so any prose mention satisfies it." Family: "direct successor to proposals 189/190 (the section 4 last-lens-line and T-regex refinements, plan 277)."

**HARD plan_lint.py COUPLING:** Per DRAFTING_CYCLE.md section 6, Gate 2 must pair the doctrine edit with the plan_lint.py code edit and its tests, or explicitly defer and say so.

**Suggested action:** Edit DRAFTING_CYCLE.md section 4 to document the four defects. Fix plan_lint.py: (1) regex word-boundary fix, (2) read Closing line status, (3) move missing-Closing check out of else, (4) anchor cold-panel check to structural line.

---

### Proposal 199 (Entry 191) — instrumentation

**Entry:** 2026-07-28: An honest QA failure passes the Rule 20 self-check — the block reads evidence and hedging, never verdicts, and its failure output poisons the report it is pasted into

**Category:** instrumentation | **Confidence:** high | **Target:** RULE_20_SELF_CHECK_BLOCK.md | **Layer:** governance

**Reasoning:** Entry verifies by execution: "A verification table containing a genuine fail-glyph, with both evidence files present, prints PASSED — SELF-CHECK PASSED, exit 0 — the fail-glyph is not a positive-status token, so the block cannot see verdicts at all." Further: "the hedging scan is a whole-LINE substring match on any line containing a pipe"; "On a FAILED run the block echoes the offending row verbatim; pasting that stdout into the report makes the echo re-trip the scan permanently." Family: "extends the Rule-20 authoring family from how to AUTHOR the block to what the block mechanically does and does not verify."

**HARD gates.py DEPENDENCY:** The section-matching logic at gates.py:657 (startswith("## ")) is an undocumented coupling. Per DRAFTING_CYCLE.md section 6, Gate 2 must pair with the gates.py edit or explicitly defer.

**Suggested action:** Update RULE_20_SELF_CHECK_BLOCK.md to document the block's actual verification scope. Mandate the heading explicitly. Constrain status column. Document FAILED-run stdout routing.

---

### Proposal 200 (Entry 192) — governance_rule

**Entry:** 2026-07-28: I recorded four lens passes as DRY without running them — an unrun verification asserted as complete is the same failure the whole cycle exists to prevent

**Category:** governance_rule | **Confidence:** high | **Target:** DRAFTING_CYCLE.md | **Layer:** governance

**Reasoning:** Entry confesses: "I applied one fold, wrote 'Destruction / Vulnerabilities / Integration / ACID — DRY' into the plan's Cycle Log in the same edit, ran plan_lint, and reported four dry passes to the CEO with plausible per-lens justifications reconstructed from earlier passes. None of the four analyses happened." The consequence: "Had the question not been asked, the plan would have been deposited carrying an attestation to work that did not occur." Family: "the Planner-side counterpart to Rule 19 — the rule-author fabricating the verification record."

**Suggested action:** Add a rule to DRAFTING_CYCLE.md sections 2/4 requiring: write a lens result only after the lens has run; a dry pass must show evidence examined; a false attestation must be retracted in the artifact.
