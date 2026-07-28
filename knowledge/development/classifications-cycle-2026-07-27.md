# Classifications — Cycle 2026-07-27

## Cycle Result Dict

```
ingested_count: 2
updated_count: 0
unchanged_count: 125
duplicates_marked_count: 0
needs_classification: [183, 184]
terminal_proposals_flagged: []
cycle_timestamp: 2026-07-28T01:09:03.283056+00:00
```

## Classifications

### Entry 183 → Proposal 191

- **entry_id:** 183
- **source_heading:** 2026-07-27: When cloning a plan, diff its machinery against the NEWEST same-class plan, not just the origin you copied — clone-drift accrues against the latest hardening [tag: planner-discipline]
- **category:** governance_rule
- **confidence:** high
- **target_layer:** governance
- **target_artifact:** DRAFTING_CYCLE.md
- **suggested_action:** Amend DRAFTING_CYCLE.md to extend the cold-panel/clone-review discipline: when cloning a plan, diff its machinery against the NEWEST same-class plan (not just the clone origin), and aim the cold panel at that diff explicitly — hand the fresh readers the newest same-class plan and ask "what did the clone DROP or MIS-ADAPT relative to the latest hardening?". A "bounded"/"proven-clone" framing is not licence to down-tier or skip the cold panel.
- **reasoning:** The entry describes how "Gate 2 Plan A (plan 278) was cloned from plan 259 (the prior Gate 2), but plan 275 — a more-recent same-batch sibling — had independently hardened three things 259 did more weakly, and cloning 259 silently REVERTED all three." It identifies the root cause: "Only a diff against the newest same-class plan surfaces it" — a warm fold-review or diff against the direct origin cannot see dropped hardenings. The fix is a documentary rule: "before or while cloning, find the LATEST plan of the same class — not just the parent you happened to copy — and diff the machinery against IT." The entry also refines cold-panel guidance: "hand the fresh readers the newest same-class plan (plus the real code/schema) and ask 'what did the clone DROP or MIS-ADAPT relative to the latest hardening?'". Its Family section places it as sharpening "the 2026-07-20 cold-read family ('rotate the reviewer, not the lens')" — the cold-panel practice in DRAFTING_CYCLE.md. This is a governance_rule: a documentary rule change to how plans are cloned and cold-panel reviewed, not a code fix (structural) or a new procedural mechanism (instrumentation).
- **target_artifact divergence from scout:** None — the Planner's Rule-27 scout placed this on DRAFTING_CYCLE.md (§2.6 cold-panel pass, §1 Rigor-Tier Gate), and the entry's content independently supports this: it refines the cold-panel/clone-review practice, citing the "2026-07-20 cold-read family ('rotate the reviewer, not the lens')" which lives in DRAFTING_CYCLE.md §2.6.

### Entry 184 → Proposal 192

- **entry_id:** 184
- **source_heading:** 2026-07-27: Choose the QA Rule 20 self-check FORM by plan class — full canonical block + real evidence files for a doc/DB plan, simple banner for a move-only plan; a full-form mandate with no evidence files is an unsatisfiable, plan-halting QA step [tag: planner-discipline]
- **category:** governance_rule
- **confidence:** high
- **target_layer:** governance
- **target_artifact:** PLANNER_TEMPLATE.md
- **suggested_action:** Add rule to PLANNER_TEMPLATE.md: when authoring a QA step's Rule 20 self-check, choose the form by plan class — full canonical block with adapted real evidence files for a doc/DB plan; simple banner for a move-only plan. When cloning a QA step that mandates the full form, verify the plan supplies a non-empty required_evidence_files set and an evidence_dir, or the canonical block halts. Never clone another plan's specific evidence set blindly — swap a pytest full-suite.txt for a plan-appropriate file when there is no suite.
- **reasoning:** The entry states "The M1 directive 'carry the full Rule 20 form + evidence files into every QA step' means real evidence files — NOT necessarily a pytest tail — and the right form depends on what the plan produces." It prescribes a form-selection rule: "pick the form by what the plan produces — doc/DB → full block + adapted real evidence files; move-only/trivial → simple banner." The hazard it identifies: "a QA step that mandates the full form but supplies NO evidence files is unsatisfiable — a plan-halting bug" — the canonical block "sys.exit(1)s when evidence_dir/required_evidence_files are absent." It clarifies that "Both forms pass the gate identically: gates.py::_gate_rule_20_self_check requires only the banner + PASSED line, so the choice is about rigor, not gate-passing." Its Family section extends "the Rule-20 authoring family — 2026-05-20 'reference RULE_20_SELF_CHECK_BLOCK.md, don't paraphrase' and 2026-05-28 'copy strict convention strings from a known-good artifact'" with the next layer: form must match plan class, and a full-form mandate carries an evidence-file precondition. This is a governance_rule: a documentary rule change to QA-step authoring in PLANNER_TEMPLATE.md (Rule 18 evidence requirements, Rule 20 self-check form selection), not a code fix or procedural mechanism.
- **target_artifact divergence from scout:** None — the Planner's Rule-27 scout placed this on PLANNER_TEMPLATE.md (Rule 18:557 evidence requirements, Rule 20:565 self-check block), and the entry's content independently supports this: it refines how QA steps are authored (which Rule 20 form + which evidence files), a Plan Authoring Checklist matter.

## Cluster Synthesis for Gate 1

**2 planner-discipline authoring refinements — SPLIT target:**
1. Entry 183 / Proposal 191 — cold-panel/clone-drift refinement → `DRAFTING_CYCLE.md` (governance_rule, high confidence)
2. Entry 184 / Proposal 192 — Rule-20-form by plan class → `PLANNER_TEMPLATE.md` (governance_rule, high confidence)

Both are `governance_rule` / `governance` layer, but they refine DIFFERENT artifacts. Neither entry has a `plan_lint.py` code coupling — both are pure doctrine. The two may route to different artifacts and/or different Gate-2 plans.

No ambiguous entries. No entries skipped or downgraded.
