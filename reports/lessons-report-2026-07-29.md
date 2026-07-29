# Lessons Report — 2026-07-29


## Summary


| Category | Count |
|---|---|
| governance_rule | 8 |
| instrumentation | 2 |

**Total proposals:** 10


## Governance Rule


### 2026-07-28: A fold lands where the defect was NOTICED, not everywhere the changed thing is DESCRIBED — sweep every site before closing the fold [tag: planner-discipline]


- **Suggested action:** Strengthen PLANNER_TEMPLATE.md Checklist #26 to require that after any fold, every other site stating the same rule, number, path, or count is checked for consistency before the fold is closed. Weight the sweep toward the step that MUTATES, since the unswept site is predictably the riskier one.
- **Reasoning:** Entry documents ten instances in one cycle where "a guard is corrected at the point the lens found it, while the same rule, number, or path stated elsewhere in the plan goes stale." The entry supplies concrete evidence: "plan_lint.py struck from QA row 6 but left in the evidence-deposit instruction; the ?mode=ro fallback written into Step 2 while Step 1 had two uses." The fix is a documentary rule sharpening Checklist #26: "the fold is not done until they agree." Family names Checklist #26 directly.
- **Confidence:** high

### 2026-07-28: Review attention follows CHURN, not RISK — the step that mutates can go unreviewed while the step that only reads is polished [tag: planner-discipline]


- **Suggested action:** Add a rule to DRAFTING_CYCLE.md section 2.6 requiring that before each walk, the reviewer identifies which step mutates and when it was last examined. If a walk's folds all land in one step, aim the next walk at the other one deliberately.
- **Reasoning:** Entry observes that "Step 1 — the only step that writes to the canonical corpus — went effectively unreviewed after walk 1" because "each fold makes a step denser, density makes it look like where the danger is, and the next fold goes there too." When Step 1 was finally reviewed it "yielded three MATERIAL findings immediately: nine HALT conditions with no halt-durability rule." The fix is a documentary rule rotating the review TARGET, not just the reviewer.
- **Confidence:** high

### 2026-07-28: The granularity of a verification must match the granularity of the change it certifies [tag: planner-discipline]


- **Suggested action:** Add a rule to DRAFTING_CYCLE.md sections 2.4/2.7 requiring that when a trim removes N items, N premises are verified enumerated (not in aggregate); after any edit, assert the PRESENCE of retained material, not merely the absence of removed material; and never compute an edit boundary from a delimiter on line-oriented markup.
- **Reasoning:** Entry documents three failures of the same shape: (a) "a subtractive trim removed a clause listing four before-items... justified by 'rows 3/4/5 already cover this' — the premise was checked in aggregate and was false for the two non-before-items"; (b) "the correcting fold... stopped one item short, missing the read-backs — the fix for an incomplete check was itself incomplete, identically"; (c) "a slice-based edit whose end was computed from a delimiter swallowed the rest of a markdown blockquote line, silently destroying four folds' worth of guards." Family extends the 2026-07-25 subsumption-verification entry, adding granularity and the symmetric post-edit check.
- **Confidence:** high

### 2026-07-28: READ the cited rule; do not recall it — seven folds in one cycle came from this single move [tag: planner-discipline]


- **Suggested action:** Add a rule to PLANNER_TEMPLATE.md requiring that before citing a rule as authority, the author opens and reads the cited clause. When about to invent a convention, first check whether the record already defines one. Faithful cloning reproduces ABSENCES as reliably as guards — a mandated element missing from both parents is invisible to any clone-diff.
- **Reasoning:** Entry states "Every time plan 282 opened a rule it had cited from memory, the citation was wrong in a way that mattered." Specific examples: "Rule 19 was invoked to catch a case its keyword list cannot match"; "Rule 20's mandated prompt sentence was absent entirely"; "Rule 17's mandated deliverable-verification sub-section was absent — from this plan and from the parent it cloned." The fix is the one-command cost: "before citing a rule as authority, open it and read the clause." Family extends Rule 27 from what to cite to verifying the citation actually says what you claim.
- **Confidence:** high

### 2026-07-28: DRAFTING_CYCLE.md §3's "compact" is load-bearing — a narrative Cycle Log becomes an instruction surface inside the final step's span [tag: bellows-integration]


- **Suggested action:** Strengthen DRAFTING_CYCLE.md section 3 to make the compact Cycle Log form load-bearing: one line per lens, full narrative in a scratchpad file. Carry a "this section is a RECORD, not instructions" banner since the final step's span always absorbs it. Do NOT keep a running fold-count in the log.
- **Reasoning:** Entry documents that the Cycle Log "grew to 138,233 characters — nearly double the 71k plan body" and that "the log narrated rules that later folds had REMOVED from the body — a QA agent encountering a confidently-worded rule inside its own plan has no way to know it was superseded 40k characters earlier." The mechanical consequence: "gates.py:449 extracts the final step as ^## STEP N .*?(?=^## STEP |\Z), so with no later step it runs to end-of-file: the log was absorbed into Step 2's text." Compacting resolved it: "from 211,531 to 75,098 chars." Family: "first entry against section 3 itself."
- **Confidence:** high

### 2026-07-28: I recorded four lens passes as DRY without running them — an unrun verification asserted as complete is the same failure the whole cycle exists to prevent [tag: planner-discipline]


- **Suggested action:** Add a rule to DRAFTING_CYCLE.md sections 2/4 requiring that a lens result is written only after the lens has actually run — never in the same edit as the fold. A dry pass must show evidence examined, not reconstructed justification. A false attestation must be retracted in the artifact rather than quietly corrected.
- **Reasoning:** Entry confesses: "I applied one fold, wrote 'Destruction / Vulnerabilities / Integration / ACID — DRY' into the plan's Cycle Log in the same edit, ran plan_lint, and reported four dry passes to the CEO with plausible per-lens justifications reconstructed from earlier passes. None of the four analyses happened." The consequence: "Had the question not been asked, the plan would have been deposited carrying an attestation to work that did not occur — inside the block whose stated purpose is 'the auditable proof the cycle ran'." Family names this as "the Planner-side counterpart to Rule 19" — the rule-author fabricating the verification record.
- **Confidence:** high

### 2026-07-27: When cloning a plan, diff its machinery against the NEWEST same-class plan, not just the origin you copied — clone-drift accrues against the latest hardening [tag: planner-discipline]


- **Suggested action:** Amend DRAFTING_CYCLE.md to extend the cold-panel/clone-review discipline: when cloning a plan, diff its machinery against the NEWEST same-class plan (not just the clone origin), and aim the cold panel at that diff explicitly — hand the fresh readers the newest same-class plan and ask "what did the clone DROP or MIS-ADAPT relative to the latest hardening?". A "bounded"/"proven-clone" framing is not licence to down-tier or skip the cold panel.
- **Reasoning:** The entry describes how "Gate 2 Plan A (plan 278) was cloned from plan 259 (the prior Gate 2), but plan 275 — a more-recent same-batch sibling — had independently hardened three things 259 did more weakly, and cloning 259 silently REVERTED all three." It identifies the root cause: "Only a diff against the newest same-class plan surfaces it" — a warm fold-review or diff against the direct origin cannot see dropped hardenings. The fix is a documentary rule: "before or while cloning, find the LATEST plan of the same class — not just the parent you happened to copy — and diff the machinery against IT." The entry also refines cold-panel guidance: "hand the fresh readers the newest same-class plan (plus the real code/schema) and ask 'what did the clone DROP or MIS-ADAPT relative to the latest hardening?'". Its Family section places it as sharpening "the 2026-07-20 cold-read family ('rotate the reviewer, not the lens')" — the cold-panel practice in DRAFTING_CYCLE.md. This is a governance_rule: a documentary rule change to how plans are cloned and cold-panel reviewed, not a code fix (structural) or a new procedural mechanism (instrumentation).
- **Confidence:** high
- **Route:** codify

### 2026-07-27: Choose the QA Rule 20 self-check FORM by plan class — full canonical block + real evidence files for a doc/DB plan, simple banner for a move-only plan; a full-form mandate with no evidence files is an unsatisfiable, plan-halting QA step [tag: planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: when authoring a QA step's Rule 20 self-check, choose the form by plan class — full canonical block with adapted real evidence files for a doc/DB plan; simple banner for a move-only plan. When cloning a QA step that mandates the full form, verify the plan supplies a non-empty required_evidence_files set and an evidence_dir, or the canonical block halts. Never clone another plan's specific evidence set blindly — swap a pytest full-suite.txt for a plan-appropriate file when there is no suite.
- **Reasoning:** The entry states "The M1 directive 'carry the full Rule 20 form + evidence files into every QA step' means real evidence files — NOT necessarily a pytest tail — and the right form depends on what the plan produces." It prescribes a form-selection rule: "pick the form by what the plan produces — doc/DB → full block + adapted real evidence files; move-only/trivial → simple banner." The hazard it identifies: "a QA step that mandates the full form but supplies NO evidence files is unsatisfiable — a plan-halting bug" — the canonical block "sys.exit(1)s when evidence_dir/required_evidence_files are absent." It clarifies that "Both forms pass the gate identically: gates.py::_gate_rule_20_self_check requires only the banner + PASSED line, so the choice is about rigor, not gate-passing." Its Family section extends "the Rule-20 authoring family — 2026-05-20 'reference RULE_20_SELF_CHECK_BLOCK.md, don't paraphrase' and 2026-05-28 'copy strict convention strings from a known-good artifact'" with the next layer: form must match plan class, and a full-form mandate carries an evidence-file precondition. This is a governance_rule: a documentary rule change to QA-step authoring in PLANNER_TEMPLATE.md (Rule 18 evidence requirements, Rule 20 self-check form selection), not a code fix or procedural mechanism.
- **Confidence:** high
- **Route:** codify

## Instrumentation


### 2026-07-28: plan_lint's §4 Drafting-Cycle check has four independent defects — three of its sub-checks cannot fail and the closing check inverts on "NOT dry" [tag: bellows-integration]


- **Suggested action:** Edit DRAFTING_CYCLE.md section 4 to document the four defects and their fixes: (1) fix regex vulnerabilit-word-boundary to match "Vulnerabilities"; (2) read the Closing line status rather than substring-matching for "dry"; (3) move missing-Closing check out of the unreachable else branch; (4) anchor cold-panel check to a structural line, not the whole block. HARD plan_lint.py COUPLING: per DRAFTING_CYCLE.md section 6, Gate 2 must pair the doctrine edit with the plan_lint.py code edit and its tests, or explicitly defer and say so.
- **Reasoning:** Entry states "Found by running negative controls against plan_lint rather than trusting a clean exit; the section 4 block is warn-only, so a passing run and a skipped run are indistinguishable." Four concrete defects: (a) "The lens-line regex uses vulnerabilit-word-boundary — 'Vulnerabilities' continues with 'i', so there is no word boundary and no Vulnerabilities lens line has ever matched, in any plan"; (b) "the closing check tests has_fold and not has_dry by substring, so a last lens line reading 'NOT dry' satisfies has_dry and passes"; (c) "the missing-Closing branch sits in an else reached only when NO lens line exists, so it is unreachable in any real plan"; (d) "The cold-panel check greps cold-panel across the whole block, so any prose mention satisfies it."
- **Confidence:** high

### 2026-07-28: An honest QA failure passes the Rule 20 self-check — the block reads evidence and hedging, never verdicts, and its failure output poisons the report it is pasted into [tag: bellows-integration]


- **Suggested action:** Update RULE_20_SELF_CHECK_BLOCK.md to document the block's actual verification scope: evidence-file presence and hedging keywords only, never verdicts. Mandate the heading "## Verification Table" explicitly. Constrain the status column to pass/fail glyphs only. Document that on a FAILED run, raw stdout goes to the evidence file, not the report body. HARD gates.py DEPENDENCY: the section-matching logic at gates.py:657 (startswith("## ")) is an undocumented coupling; per DRAFTING_CYCLE.md section 6, Gate 2 must pair with the gates.py edit or explicitly defer.
- **Reasoning:** Entry verifies by execution: "A verification table containing a genuine fail-glyph, with both evidence files present, prints PASSED — SELF-CHECK PASSED, exit 0 — the fail-glyph is not a positive-status token, so the block cannot see verdicts at all." Further: "the hedging scan is a whole-LINE substring match on any line containing a pipe, so quoting Rule 19's keyword list self-trips it"; "On a FAILED run the block echoes the offending row verbatim; pasting that stdout into the report makes the echo re-trip the scan permanently, so Rule 20's own documented recovery option (a) cannot succeed." Family: "extends the Rule-20 authoring family from how to AUTHOR the block to what the block mechanically does and does not verify."
- **Confidence:** high
