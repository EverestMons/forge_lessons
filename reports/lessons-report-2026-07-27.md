# Lessons Report — 2026-07-27


## Summary


| Category | Count |
|---|---|
| governance_rule | 2 |

**Total proposals:** 2


## Governance Rule


### 2026-07-27: When cloning a plan, diff its machinery against the NEWEST same-class plan, not just the origin you copied — clone-drift accrues against the latest hardening [tag: planner-discipline]


- **Suggested action:** Amend DRAFTING_CYCLE.md to extend the cold-panel/clone-review discipline: when cloning a plan, diff its machinery against the NEWEST same-class plan (not just the clone origin), and aim the cold panel at that diff explicitly — hand the fresh readers the newest same-class plan and ask "what did the clone DROP or MIS-ADAPT relative to the latest hardening?". A "bounded"/"proven-clone" framing is not licence to down-tier or skip the cold panel.
- **Reasoning:** The entry describes how "Gate 2 Plan A (plan 278) was cloned from plan 259 (the prior Gate 2), but plan 275 — a more-recent same-batch sibling — had independently hardened three things 259 did more weakly, and cloning 259 silently REVERTED all three." It identifies the root cause: "Only a diff against the newest same-class plan surfaces it" — a warm fold-review or diff against the direct origin cannot see dropped hardenings. The fix is a documentary rule: "before or while cloning, find the LATEST plan of the same class — not just the parent you happened to copy — and diff the machinery against IT." The entry also refines cold-panel guidance: "hand the fresh readers the newest same-class plan (plus the real code/schema) and ask 'what did the clone DROP or MIS-ADAPT relative to the latest hardening?'". Its Family section places it as sharpening "the 2026-07-20 cold-read family ('rotate the reviewer, not the lens')" — the cold-panel practice in DRAFTING_CYCLE.md. This is a governance_rule: a documentary rule change to how plans are cloned and cold-panel reviewed, not a code fix (structural) or a new procedural mechanism (instrumentation).
- **Confidence:** high

### 2026-07-27: Choose the QA Rule 20 self-check FORM by plan class — full canonical block + real evidence files for a doc/DB plan, simple banner for a move-only plan; a full-form mandate with no evidence files is an unsatisfiable, plan-halting QA step [tag: planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: when authoring a QA step's Rule 20 self-check, choose the form by plan class — full canonical block with adapted real evidence files for a doc/DB plan; simple banner for a move-only plan. When cloning a QA step that mandates the full form, verify the plan supplies a non-empty required_evidence_files set and an evidence_dir, or the canonical block halts. Never clone another plan's specific evidence set blindly — swap a pytest full-suite.txt for a plan-appropriate file when there is no suite.
- **Reasoning:** The entry states "The M1 directive 'carry the full Rule 20 form + evidence files into every QA step' means real evidence files — NOT necessarily a pytest tail — and the right form depends on what the plan produces." It prescribes a form-selection rule: "pick the form by what the plan produces — doc/DB → full block + adapted real evidence files; move-only/trivial → simple banner." The hazard it identifies: "a QA step that mandates the full form but supplies NO evidence files is unsatisfiable — a plan-halting bug" — the canonical block "sys.exit(1)s when evidence_dir/required_evidence_files are absent." It clarifies that "Both forms pass the gate identically: gates.py::_gate_rule_20_self_check requires only the banner + PASSED line, so the choice is about rigor, not gate-passing." Its Family section extends "the Rule-20 authoring family — 2026-05-20 'reference RULE_20_SELF_CHECK_BLOCK.md, don't paraphrase' and 2026-05-28 'copy strict convention strings from a known-good artifact'" with the next layer: form must match plan class, and a full-form mandate carries an evidence-file precondition. This is a governance_rule: a documentary rule change to QA-step authoring in PLANNER_TEMPLATE.md (Rule 18 evidence requirements, Rule 20 self-check form selection), not a code fix or procedural mechanism.
- **Confidence:** high
