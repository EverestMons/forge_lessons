# Classifications Summary — Cycle 2026-07-20

## Cycle Result Dict

```python
{
    'ingested_count': 5,
    'updated_count': 0,
    'unchanged_count': 89,
    'duplicates_marked_count': 0,
    'needs_classification': [147, 148, 149, 150, 151],
    'terminal_proposals_flagged': [],
    'cycle_timestamp': '2026-07-20T20:48:21.765421+00:00'
}
```

## Batch Summary

| Metric | Value |
|---|---|
| Entries ingested | 5 |
| Entries classified | 5 |
| Ambiguous entries | 0 |

## Category Distribution

| Category | Count |
|---|---|
| governance_rule | 5 |

## Confidence Distribution

| Confidence | Count |
|---|---|
| high | 5 |

## Per-Entry Classifications

### Proposal 155 — Entry 147

**Heading:** 2026-07-19: An instruction that is not a numbered row, a named test, or a gate is an instruction that evaporates [tag: planner-discipline]

| Field | Value |
|---|---|
| Category | governance_rule |
| Confidence | high |
| Target Layer | governance |
| Target Artifact | PLANNER_TEMPLATE.md |
| Route | NULL |
| Status | proposed |

**Suggested Action:** Add rule to PLANNER_TEMPLATE.md: requirements must have a structural home — a numbered verification row, a named test, or a gate condition. Prose paragraphs do not survive execution. When a verdict adds a requirement mid-plan, restate it as a numbered row in the plan file, not only in the verdict. Location (in the plan file the agent works from) takes precedence over numbering.

**Reasoning:** Entry 147 states: "every instruction bound to a numbered QA row, a named test, or a mechanical gate was honoured without exception, and every instruction living only in prose was dropped." Three omissions in a single arc are cited — diag-229 Q6/Q7 generalizing from 0 rows, plan 230 Step-1 verdict SENTINEL_CEILING_MIN extraction not done, plan 230 Step-2 verdict fourteenth QA row and Forward Register entry omitted. The refinement (learned from plan 233) adds: "Numbering makes a requirement checkable; location makes it visible. A requirement needs both, and location comes first." The remedy: "a fresh plan carrying both fixes as numbered rows in its OWN step text."

---

### Proposal 156 — Entry 148

**Heading:** 2026-07-19: Grep presence is not effect — a wired call needs an observed behaviour change, not a source-code match [tag: qa-discipline]

| Field | Value |
|---|---|
| Category | governance_rule |
| Confidence | high |
| Target Layer | governance |
| Target Artifact | PLANNER_TEMPLATE.md |
| Route | NULL |
| Status | proposed |

**Suggested Action:** Add rule to PLANNER_TEMPLATE.md: verification of any wired call must observe a behaviour change through the real entry point (before-value, action, after-value). Grep proves wiring exists; a green suite proves it does not throw; only an observed delta proves it works. When designing such a check, verify the construction actually produces the expected delta.

**Reasoning:** Entry 148 states: "the evidence established that the call exists and does not crash, and established nothing at all about whether it does anything. The plan was stopped one row short of closing on a money-affecting write path." The discipline rule: "for any change whose value is that a call now runs somewhere, the verification must observe a behaviour change through the real entry point — a before-value, the action, an after-value." Noted as "sibling to entry 86 (a fresh-built DB reported as a migration): both are evidence that structurally cannot witness the thing it certifies."

---

### Proposal 157 — Entry 149

**Heading:** 2026-07-19: Add an ACID lens to the Drafting Cycle — the four named passes examine requirements individually, none examines them as a system [tag: planner-discipline]

| Field | Value |
|---|---|
| Category | governance_rule |
| Confidence | high |
| Target Layer | governance |
| Target Artifact | PLANNER_TEMPLATE.md |
| Route | NULL |
| Status | proposed |

**Suggested Action:** Amend the Drafting Cycle in PLANNER_TEMPLATE.md to add ACID (atomicity, consistency, isolation, durability) as a fifth named lens, run after the existing four. The lens examines each distinct transaction the plan touches and specifically checks whether requirements accepted in earlier passes contradict one another.

**Reasoning:** Entry 149 states: "None asks whether the plan's own accepted requirements conflict with each other." The CEO directed a fifth pass which "found a genuine contradiction between two requirements folded in earlier passes of the same cycle... No amount of re-running lenses 1-4 would have surfaced it, because each was individually satisfied." The same pass "converted three accidental properties into stated ones" (consistency, isolation, durability). The discipline rule: "add ACID — atomicity, consistency, isolation, durability as a fifth named lens, run after the other four."

---

### Proposal 158 — Entry 150

**Heading:** 2026-07-19: The full Drafting Cycle applies to DIAGNOSTICS, not just executables — its escalation triggers are worded so a read-only plan never trips them [tag: planner-discipline]

| Field | Value |
|---|---|
| Category | governance_rule |
| Confidence | high |
| Target Layer | governance |
| Target Artifact | PLANNER_TEMPLATE.md |
| Route | NULL |
| Status | proposed |

**Suggested Action:** Amend PLANNER_TEMPLATE.md Drafting Cycle escalation triggers to include diagnostic-shaped triggers alongside the executable-shaped ones. A diagnostic escalates when: its findings will be authored from without re-verification; it asks questions whose answers depend on unconfirmed data availability; it scopes a multi-plan arc; or it touches a leak, money, or governance surface. The lens that matters most for a diagnostic is weak spots aimed at the questions themselves.

**Reasoning:** Entry 150 states: "its escalation triggers are written entirely in executable terms — production-data mutation, a CEO-run tool, a money-affecting write path, a cross-machine or irreversible action. A diagnostic is read-only and changes nothing, so by those triggers it essentially never escalates to the full cycle." The cost: "diag-229 received the floor pass only" and "Q6 and Q7 were struck at the verdict gate for answering data questions from data that did not exist." The argument: "a diagnostic changes nothing, but its questions determine what gets built. Bad findings are authored from."

---

### Proposal 159 — Entry 151

**Heading:** 2026-07-20: A drafting-cycle lens is not done at one pass — iterate until the lens runs dry (0 or minor-only), because folding changes the draft [tag: planner-discipline]

| Field | Value |
|---|---|
| Category | governance_rule |
| Confidence | high |
| Target Layer | governance |
| Target Artifact | PLANNER_TEMPLATE.md |
| Route | NULL |
| Status | proposed |

**Suggested Action:** Amend the Drafting Cycle in PLANNER_TEMPLATE.md: a lens iterates (pass, CEO-directed fold, same lens again on folded draft) until it returns 0 or only-minor findings before advancing. The cycle-level terminal condition: the last event before deposit must be a dry pass, never a fold. The cycle is done when it stops finding defects, not when the lens list is exhausted.

**Reasoning:** Entry 151 states: "a lens that just yielded 4 findings is not done — it is interrupted. Each lens repeats — pass, fold, same lens again on the folded draft — until it returns 0 findings or only-minor ones." The structural reason: "folding changes the draft. A pass examines draft N; its accepted findings produce draft N+1 containing new text no pass has ever read." Evidence: plan 240 vulnerabilities pass correcting weak-spots FOLD, plan 239 ACID pass finding contradiction BETWEEN folds. Terminal condition: "the last event before deposit must be a DRY PASS, never a fold — every fold produces a draft no pass has examined."

---

## Cluster Synthesis

### The Drafting-Cycle Cluster (Proposals 157, 158, 159)

Proposals 157, 158, and 159 all amend the SAME template section: `## The Drafting Cycle` (PLANNER_TEMPLATE.md:314, with `### The Full Cycle` at :328). They are a cluster, not three scattered edits:

- **Proposal 157 (entry 149):** Adds a fifth lens (ACID) to the four-lens set at line 330-335.
- **Proposal 158 (entry 150):** Expands the escalation triggers (lines 324-326) to include diagnostic-shaped triggers.
- **Proposal 159 (entry 151):** Rewrites the stop/iteration condition — currently "diminishing returns" at line 337.

All three should be routed coherently at Gate 1; they share a target section and their codifications interact (e.g., adding a fifth lens changes what "exhausting the lens list" means in the stop condition).

Disk-verified: `## The Drafting Cycle` confirmed at PLANNER_TEMPLATE.md:314, `### The Full Cycle` at :328, escalation triggers at :322-326, four lenses at :330-335, "diminishing returns" stop at :337. All verified via `grep -n` and direct read.

### Three-Way Tension on the Stop Condition

Three competing statements exist for the Drafting Cycle's stop condition:

1. **The live template** (PLANNER_TEMPLATE.md:337): "Repeat until a pass honestly reports **diminishing returns** — the signal to stop drafting." (Disk-verified.)
2. **Entry 151 (this batch):** "a lens that just yielded 4 findings is not done — it is interrupted. Each lens repeats — pass, fold, same lens again on the folded draft — until it returns **0 findings or only-minor ones**." The entry explicitly proposes iterating the SAME lens until dry before advancing.
3. **CEO direction, 2026-07-20** (from this plan's CEO Context): "**one pass per lens; walk the whole lens list; a lens is re-run only when the cycle starts the list over.**"

Statement (3) post-dates and corrects entry 151's rule (2): the CEO keeps the lens-list walk but changes iteration to be at the cycle level, not within a single lens. Statement (1) is the current template text. **Gate 2 cannot codify entry 151 verbatim** — the CEO refinement overrides its within-lens iteration model.

This tension is surfaced here for Gate 1 visibility; resolution is a Gate 2 authoring decision. The classification itself is unaffected — all three statements agree that the Drafting Cycle needs a clearer stop condition; they disagree on the mechanism.

### Non-Cluster Entries (Proposals 155, 156)

**Proposal 155 (entry 147):** "An instruction that is not a numbered row, a named test, or a gate evaporates." Standalone governance rule about requirement durability — not part of the Drafting Cycle cluster. Targets PLANNER_TEMPLATE.md generally (plan authoring rules), not the `## The Drafting Cycle` section.

**Proposal 156 (entry 148):** "Grep presence is not effect." Standalone QA discipline rule about verification standards — not part of the Drafting Cycle cluster. Targets PLANNER_TEMPLATE.md (QA/verification rules).
