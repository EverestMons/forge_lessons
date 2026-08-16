# Lessons Report — 2026-08-15


## Summary


| Category | Count |
|---|---|
| governance_rule | 1 |

**Total proposals:** 1


## Governance Rule


### 2026-08-14: A residual "everything else" bucket silently absorbs the class that deserved its own bin [tag: governance-design]


- **Suggested action:** Add a third destination to PLANNER_TEMPLATE.md Session Wrap step 7 for project-domain knowledge (facts about a project's data, schema, or execution environment), alongside the existing shop-level lessons (LESSONS.md) and Planner-memory routes.
- **Reasoning:** [DEDUP] This extends wrap step 7's existing two-destination rule rather than creating a new one. The routing already names two bins — shop-level lessons to LESSONS.md and everything else to the Planner's memory repo — and entry 345 proposes adding a third bin for project-domain knowledge that currently falls into the residual 'everything else' arm by elimination.

[REMEDY-GATED] The remedy is drafted (PLANNER_TEMPLATE 4.88 -> 4.89, three logical edits: step 7 gains a third destination, Source B gains a standing read, version + History), its builder is committed, and it cannot dispatch until this proposal is routed accepted or codify — the proposal and entry ids are required builder arguments.

[AUTHOR-CONFLICT] The proposal's author (the Planner) also authored its evidence (the measurement of invoice-pulse's misfiled domain facts and the diagnostic arc that exposed the routing gap) and its drafted remedy (the PLANNER_TEMPLATE edit), and benefits from the outcome — the rule change governs what lands in the Planner's own memory versus a shared project bin. This disclosure is an input for Gate 1's routing decision, not a verdict.

Entry 345 explicitly describes a governance routing defect: the session-wrap lessons sweep's two-destination rule lacks a label for project-domain knowledge, so that class of material takes the residual door by elimination. The entry quotes measurement evidence — all 5 invoice-pulse project-lessons-bin entries were shop-class, while roughly half of the 26 Planner-memory files naming that project are genuine domain facts — demonstrating that the material was misfiled, not missing. The proposed fix is documentary: add a named destination to the governance routing rule so the residual arm no longer absorbs a class that has its own identity. This is a governance_rule classification with high confidence because the entry proposes a specific rule edit to a governance file (PLANNER_TEMPLATE.md), not a tooling change or procedural checklist.
- **Confidence:** high
