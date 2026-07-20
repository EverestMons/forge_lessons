# Lessons Report — 2026-07-20


## Summary


| Category | Count |
|---|---|
| governance_rule | 5 |

**Total proposals:** 5


## Governance Rule


### 2026-07-20: A drafting-cycle lens is not done at one pass — iterate until the lens runs dry (0 or minor-only), because folding changes the draft [tag: planner-discipline]


- **Suggested action:** Amend the Drafting Cycle in PLANNER_TEMPLATE.md: a lens iterates (pass, CEO-directed fold, same lens again on folded draft) until it returns 0 or only-minor findings before advancing. The cycle-level terminal condition: the last event before deposit must be a dry pass, never a fold. The cycle is done when it stops finding defects, not when the lens list is exhausted.
- **Reasoning:** Entry 151 states: "a lens that just yielded 4 findings is not done — it is interrupted. Each lens repeats — pass, fold, same lens again on the folded draft — until it returns 0 findings or only-minor ones." The structural reason: "folding changes the draft. A pass examines draft N; its accepted findings produce draft N+1 containing new text no pass has ever read." Evidence: plan 240 vulnerabilities pass correcting weak-spots FOLD, plan 239 ACID pass finding contradiction BETWEEN folds. Terminal condition: "the last event before deposit must be a DRY PASS, never a fold — every fold produces a draft no pass has examined."
- **Confidence:** high

### 2026-07-19: An instruction that is not a numbered row, a named test, or a gate is an instruction that evaporates [tag: planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: requirements must have a structural home — a numbered verification row, a named test, or a gate condition. Prose paragraphs do not survive execution. When a verdict adds a requirement mid-plan, restate it as a numbered row in the plan file, not only in the verdict. Location (in the plan file the agent works from) takes precedence over numbering.
- **Reasoning:** Entry 147 states: "every instruction bound to a numbered QA row, a named test, or a mechanical gate was honoured without exception, and every instruction living only in prose was dropped." Three omissions in a single arc are cited — diag-229 Q6/Q7 generalizing from 0 rows, plan 230 Step-1 verdict SENTINEL_CEILING_MIN extraction not done, plan 230 Step-2 verdict fourteenth QA row and Forward Register entry omitted. The refinement (learned from plan 233) adds: "Numbering makes a requirement checkable; location makes it visible. A requirement needs both, and location comes first." The remedy: "a fresh plan carrying both fixes as numbered rows in its OWN step text."
- **Confidence:** high

### 2026-07-19: Grep presence is not effect — a wired call needs an observed behaviour change, not a source-code match [tag: qa-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: verification of any wired call must observe a behaviour change through the real entry point (before-value, action, after-value). Grep proves wiring exists; a green suite proves it does not throw; only an observed delta proves it works. When designing such a check, verify the construction actually produces the expected delta.
- **Reasoning:** Entry 148 states: "the evidence established that the call exists and does not crash, and established nothing at all about whether it does anything. The plan was stopped one row short of closing on a money-affecting write path." The discipline rule: "for any change whose value is that a call now runs somewhere, the verification must observe a behaviour change through the real entry point — a before-value, the action, an after-value." Noted as "sibling to entry 86 (a fresh-built DB reported as a migration): both are evidence that structurally cannot witness the thing it certifies."
- **Confidence:** high

### 2026-07-19: Add an ACID lens to the Drafting Cycle — the four named passes examine requirements individually, none examines them as a system [tag: planner-discipline]


- **Suggested action:** Amend the Drafting Cycle in PLANNER_TEMPLATE.md to add ACID (atomicity, consistency, isolation, durability) as a fifth named lens, run after the existing four. The lens examines each distinct transaction the plan touches and specifically checks whether requirements accepted in earlier passes contradict one another.
- **Reasoning:** Entry 149 states: "None asks whether the plan's own accepted requirements conflict with each other." The CEO directed a fifth pass which "found a genuine contradiction between two requirements folded in earlier passes of the same cycle... No amount of re-running lenses 1–4 would have surfaced it, because each was individually satisfied." The same pass "converted three accidental properties into stated ones" (consistency, isolation, durability). The discipline rule: "add ACID — atomicity, consistency, isolation, durability as a fifth named lens, run after the other four."
- **Confidence:** high

### 2026-07-19: The full Drafting Cycle applies to DIAGNOSTICS, not just executables — its escalation triggers are worded so a read-only plan never trips them [tag: planner-discipline]


- **Suggested action:** Amend PLANNER_TEMPLATE.md Drafting Cycle escalation triggers to include diagnostic-shaped triggers alongside the executable-shaped ones. A diagnostic escalates when: its findings will be authored from without re-verification; it asks questions whose answers depend on unconfirmed data availability; it scopes a multi-plan arc; or it touches a leak, money, or governance surface. The lens that matters most for a diagnostic is weak spots aimed at the questions themselves.
- **Reasoning:** Entry 150 states: "its escalation triggers are written entirely in executable terms — production-data mutation, a CEO-run tool, a money-affecting write path, a cross-machine or irreversible action. A diagnostic is read-only and changes nothing, so by those triggers it essentially never escalates to the full cycle." The cost: "diag-229 received the floor pass only" and "Q6 and Q7 were struck at the verdict gate for answering data questions from data that did not exist." The argument: "a diagnostic changes nothing, but its questions determine what gets built. Bad findings are authored from."
- **Confidence:** high
