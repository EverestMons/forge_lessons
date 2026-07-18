# Classifications Summary — Cycle 2026-07-17

**Plan:** 225 — Lessons Forge Cycle Run 2026-07-17
**Step:** 2 (Lessons Agent — classification)
**Date:** 2026-07-18
**Agent:** Forge Lessons Agent

---

## Classification Count

| Metric | Value |
|--------|-------|
| Total classified | 6 |
| Category: governance_rule | 6 |
| Confidence: high | 6 |
| target_layer: governance | 6 |
| target_artifact: PLANNER_TEMPLATE.md | 6 |
| route | None (all — per plan instructions) |

## Category / Confidence Distribution

| Entry ID | Heading | Category | Confidence | Artifact |
|----------|---------|----------|------------|----------|
| 141 | Never state a bare expected number | governance_rule | high | PLANNER_TEMPLATE.md |
| 142 | High-stakes executables get a drafting cycle | governance_rule | high | PLANNER_TEMPLATE.md |
| 143 | Worktree QA cannot verify a live-DB migration | governance_rule | high | PLANNER_TEMPLATE.md |
| 144 | Drafting cycle pass 4 — integration-vs-record | governance_rule | high | PLANNER_TEMPLATE.md |
| 145 | Region-scoped metric computed unscoped | governance_rule | high | PLANNER_TEMPLATE.md |
| 146 | Schema version bump breaks version-pinned assertions | governance_rule | high | PLANNER_TEMPLATE.md |

## Amendment Linkage

**Entries 142 and 144 form ONE Gate-2 governance item.** Entry 142 proposes the Drafting Cycle as a named process (three adversarial lenses, draft outside decisions/, fold-and-deposit once). Entry 144 amends it by adding a mandatory fourth pass: "integration-vs-record" — scanning the draft against LESSONS.md, knowledge/decisions/Done/, and knowledge/research/ for convention violations, precedent conflicts, and stated-consequence gaps. Both target PLANNER_TEMPLATE.md; the Gate-2 authoring decision (trigger criteria for which plans require a drafting cycle) applies to the combined item.

## Rule 52 — Verification Log

| Cited Identifier | Source Entry | Verification | Result |
|-----------------|-------------|--------------|--------|
| `_normalize_for_hash` | 141 context (plan 204 fix) | `grep -rn "_normalize_for_hash" src/lessons_forge.py` | FOUND at line 34, 89 |
| `insert_proposal()` | Agent guide (ADR-002) | `grep -n "def insert_proposal" src/lessons_forge.py` | FOUND at line 202 |
| `detect_duplicates()` | Agent guide (ADR-002) | `grep -rn "detect_duplicates" src/lessons_forge.py` | FOUND at line 297 |
| `run_full_lessons_cycle()` | Agent guide | `grep -rn "run_full_lessons_cycle" src/lessons_forge.py` | FOUND at line 416 |
| `get_unclassified_entries()` | Agent guide | `grep -rn "get_unclassified_entries" src/lessons_forge.py` | FOUND at line 267 |
| `generate_lessons_report()` | Agent guide | `grep -rn "generate_lessons_report" src/lessons_forge.py` | FOUND at line 514 |
| `ingest_lesson_entries()` | Agent guide | `grep -rn "ingest_lesson_entries" src/lessons_forge.py` | FOUND at line 120 |
| `PLANNER_TEMPLATE.md` | 142, 144, 146 (codification target) | `find /Users/marklehn/Developer/GitHub -maxdepth 2 -name "PLANNER_TEMPLATE.md"` | FOUND at /Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md |
| `LESSONS.md` | 144 (corpus reference) | `find /Users/marklehn/Developer/GitHub -maxdepth 2 -name "LESSONS.md"` | FOUND at /Users/marklehn/Developer/GitHub/LESSONS.md |

No filesystem-state claims were fabricated. All identifiers referenced in reasoning were verified against disk before inclusion.

## Cluster Synthesis for CEO Gate 1

**Dominant cluster: planner-discipline governance rules (5 of 6 entries).** This batch is the most governance-homogeneous since inception — every entry proposes a documentary rule change to PLANNER_TEMPLATE.md. The entries divide into three sub-clusters:

1. **Plan-text discipline (entries 141, 145, 146):** rules about how specific plan elements should be written — bare numbers must carry verify clauses (141), scoped metrics must carry their scope end-to-end (145), schema-bump plans must enumerate and classify version-pinned assertions (146). Each codifies a pattern observed across multiple plans (203–207, 218, 210/219/223 respectively).

2. **The Drafting Cycle (entries 142 + 144):** a single governance item spanning two entries. Entry 142 defines the process (three adversarial lenses, draft off-queue, fold-and-deposit once). Entry 144 amends it with a mandatory fourth pass (integration-vs-record: scan against the project's own corpus). Together they target PLANNER_TEMPLATE as a named process with an open Gate-2 trigger-criteria decision.

3. **QA-discipline governance (entry 143):** the sole `qa-discipline`-tagged entry, but classified as governance_rule because the fix is a documentary rule about how QA rows and verdict gates are authored for schema-bump plans, not a tooling change.

**Gate 1 note:** all 6 are high-confidence governance_rule with no ambiguity flags. The CEO's disposition decision is straightforward — the question is which rules to accept for codification, not which categories to reassign.

## Per-Entry Classification Detail

### Entry 141 — Never state a bare expected number (proposal 149)

- **Category:** governance_rule | **Confidence:** high
- **Reasoning:** The entry explicitly states a "discipline rule" for plan authoring: "Never write a bare expected number — write the prediction, then the clause: 'verify rather than assume and report the actual numbers'." It cites four wrong predictions across plans 203–207, each caught because the plan paired predictions with verify-and-explain clauses. The fix is a documentary rule change to governance text — it prescribes how plan text is written, not a code change or procedural checklist.
- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: every predicted number in plan text must be paired with a verify-and-report clause and, where the number gates a destructive step, a named catastrophic signature with halt-on-trigger.

### Entry 142 — High-stakes executables get a drafting cycle (proposal 150)

- **Category:** governance_rule | **Confidence:** high
- **Reasoning:** The entry proposes a named governance process — "the Drafting Cycle" — with explicit codification target "PLANNER_TEMPLATE, as a named process." It describes a multi-pass adversarial drafting protocol derived from the fuel-sentinel repair plan (invoice-pulse 216), where three CEO-driven review passes under different named lenses each found real issues the prior pass missed. The fix is a documentary process definition in the governance template, not a tooling change or procedural checklist addition. LINKED with entry 144 — together they form ONE Gate-2 governance item.
- **Suggested action:** Add named process "the Drafting Cycle" to PLANNER_TEMPLATE.md with the full protocol and Gate-2 trigger criteria.

### Entry 143 — Worktree QA cannot verify a live-DB migration (proposal 151)

- **Category:** governance_rule | **Confidence:** high
- **Reasoning:** The entry identifies a structural gap in worktree-based QA: "a worktree step is STRUCTURALLY INCAPABLE of exercising the migrate-EXISTING path on an untracked canonical DB." It describes plan 223 where QA ran init_db in a worktree that had no canonical DB, creating a fresh database and reporting it as a live migration. The proposed fix is a documentary rule change — three specific governance requirements for schema-bump plans — not a code change to worktree tooling.
- **Suggested action:** Add rule for schema-bump plans: QA must name absolute canonical path, show pre-migration version, Planner verifies canonical DB at verdict gate, baton records activation PENDING per machine.

### Entry 144 — Drafting cycle pass 4: integration-vs-record (proposal 152)

- **Category:** governance_rule | **Confidence:** high
- **Reasoning:** The entry explicitly "Amends the drafting-cycle entry (2026-07-16)" and proposes the cycle's pass set is FOUR named lenses with a mandatory fourth: "integration-vs-record — scan the draft against LESSONS.md, knowledge/decisions/Done/, and knowledge/research/." It cites the fuel-review-UI plan where the CEO's fourth pass found issues (stale-marking invariant, FROZEN files convention, consistency with staging arc) that no adversarial-imagination pass could discover. AMENDMENT to entry 142 — ONE Gate-2 governance item.
- **Suggested action:** Amend the Drafting Cycle in PLANNER_TEMPLATE.md: add mandatory pass 4 "integration-vs-record" scanning the draft against the project's corpus.

### Entry 145 — Region-scoped metric computed unscoped (proposal 153)

- **Category:** governance_rule | **Confidence:** high
- **Reasoning:** The entry states a "discipline rule" about scoped metrics: "any metric that is semantically scoped must be computed with that scope applied END TO END." It describes a specific incident where a sentinel-repair tool computed an unscoped "EIA max ever" aggregate (SCA region max 7.567) compared against an NUS contract table top (7.509), triggering a false escalation. The fix is a documentary rule for planner verdict discipline — how to verify metric scoping before acting on characterization lines.
- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: scoped metrics must carry scope end-to-end; when two tools disagree, the scoped one is the authority.

### Entry 146 — Schema version bump breaks version-pinned assertions (proposal 154)

- **Category:** governance_rule | **Confidence:** high
- **Reasoning:** The entry states an explicit "discipline rule" with three MUST-steps for schema version bump plans, citing three plans (210, 219, 223) that hit the identical trap. Plan 223 authored the trap out by enumerating every version-pinned assertion grep-verified line by line. The fix is a documentary MUST clause for plan authoring, differentiating tripwires (bump) from migration-preconditions (preserve).
- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: schema-bump plans MUST grep, classify, and re-grep version-pinned assertions in the same DEV step.
