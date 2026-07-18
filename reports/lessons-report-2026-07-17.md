# Lessons Report — 2026-07-17


## Summary


| Category | Count |
|---|---|
| governance_rule | 6 |

**Total proposals:** 6


## Governance Rule


### 2026-07-17: A worktree QA step cannot verify a live-DB migration — it fresh-builds and calls it "migrated" [tag: qa-discipline]


- **Suggested action:** Add rule to QA governance (PLANNER_TEMPLATE.md or QA specialist file): for any schema-bump plan, (a) QA row must name the ABSOLUTE canonical DB path and require pre-migration version shown before post-version (fresh-build asymmetry is the tell); (b) Planner verifies canonical DB by absolute path at verdict gate BEFORE composing the verdict; (c) baton records activation as PENDING per machine until real DB app restart confirmed.
- **Reasoning:** The entry identifies a structural gap in worktree-based QA: "a worktree step is STRUCTURALLY INCAPABLE of exercising the migrate-EXISTING path on an untracked canonical DB." It describes plan 223 where QA ran init_db in a worktree that had no canonical DB, creating a fresh database stamped v19 and reporting that as a live migration. The proposed fix is a documentary rule change — three specific governance requirements for schema-bump plans — not a code change to worktree tooling. The entry references the same family as the 2026-07-06 evidence-source entries (worktree-has-no-DB is never a reason to substitute).
- **Confidence:** high

### 2026-07-17: Drafting cycle pass 4 — scan the draft against the project's own record; imagination misses what memory catches [tag: planner-discipline]


- **Suggested action:** Amend the Drafting Cycle process in PLANNER_TEMPLATE.md: add mandatory fourth pass "integration-vs-record" — scan the draft against LESSONS.md, knowledge/decisions/Done/, and knowledge/research/ for convention violations, precedent conflicts, and stated-consequence gaps. Passes 1–3 require adversarial imagination; pass 4 requires institutional memory.
- **Reasoning:** The entry explicitly states it "Amends the drafting-cycle entry (2026-07-16)" and proposes "the cycle's pass set is FOUR named lenses, and the fourth is mandatory before deposit for any plan touching established subsystems: integration-vs-record." It describes how the fuel-review-UI plan (invoice-pulse 224) ran the three original lenses successfully, but a CEO-invoked fourth pass found issues none of the first three could discover — they were facts about the project's accumulated decisions recoverable only from corpus reading, not adversarial imagination. Codification target unchanged: PLANNER_TEMPLATE. NOTE: this is the AMENDMENT to entry 142 — together they form ONE Gate-2 governance item.
- **Confidence:** high

### 2026-07-17: A region-scoped metric computed unscoped poisons the verdict — the config-2 phantom gap [tag: planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: any metric that is semantically scoped (by region, carrier, contract, config, time window) must be computed with that scope applied end-to-end — every aggregate in the chain. When two tools disagree, the one carrying the scope through is the authority. A characterization line feeding an escalation deserves the same scoping scrutiny as the decision itself.
- **Reasoning:** The entry states a "discipline rule" about scoped metrics: "any metric that is semantically scoped must be computed with that scope applied END TO END." It describes a specific incident where a sentinel-repair tool computed "EIA max ever" without a region filter, producing an unscoped aggregate (SCA region max 7.567) compared against an NUS contract table top (7.509), triggering a false escalation. The fix is a documentary rule change for planner verdict discipline — how to verify metric scoping before acting on characterization lines — not a code fix or procedural checklist.
- **Confidence:** high

### 2026-07-17: A CURRENT_SCHEMA_VERSION bump always breaks version-pinned assertions — fix them in the SAME DEV step, preserve migration preconditions [tag: planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: any plan bumping CURRENT_SCHEMA_VERSION MUST, in the same DEV step: (a) grep for all version-pinned assertions and enumerate hits in plan text; (b) classify each as tripwire (update) or migration-precondition (preserve); (c) re-grep after editing to prove none remain. Do not leave version pins for QA to discover.
- **Reasoning:** The entry states an explicit "discipline rule" with three MUST-steps for schema version bump plans, citing three plans (210, 219, 223) that hit the identical trap. Plan 223 finally authored the trap out by enumerating every version-pinned assertion grep-verified line by line. The fix is a documentary rule for plan authoring — a MUST clause in PLANNER_TEMPLATE governing how schema-bump plans are written — not a code change. The entry explicitly differentiates tripwires (bump) from migration-preconditions (preserve, e.g. test_schema_v17_migration.py asserting v_before == 16).
- **Confidence:** high

### 2026-07-16: Never state a bare expected number in plan text — pair every prediction with verify-and-explain [tag: planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: every predicted number in plan text must be paired with a verify-and-report clause ("verify rather than assume — report the actual numbers") and, where the number gates a destructive step, a named catastrophic signature with halt-on-trigger.
- **Reasoning:** The entry explicitly states a "discipline rule" for plan authoring: "Never write a bare expected number — write the prediction, then the clause: 'verify rather than assume and report the actual numbers'." It cites four wrong predictions across plans 203–207, each caught because the plan paired predictions with verify-and-explain clauses. The fix is a documentary rule change to governance text — it prescribes how plan text is written, not a code change or procedural checklist.
- **Confidence:** high

### 2026-07-16: High-stakes executables get a drafting cycle — draft off-queue, analyze under named lenses, fold, repeat to diminishing returns [tag: planner-discipline]


- **Suggested action:** Add named process "the Drafting Cycle" to PLANNER_TEMPLATE.md: for high-stakes plans (production-data mutation, CEO-run tools, irreversible/cross-machine ops), draft outside decisions/, cycle through adversarial analysis under named lenses with severity-ranked verified findings, fold into next draft, repeat until diminishing returns, then deposit once. Gate 2 authoring decision: trigger criteria for which plans require a drafting cycle.
- **Reasoning:** The entry proposes a named governance process — "the Drafting Cycle" — with explicit codification target "PLANNER_TEMPLATE, as a named process." It describes a multi-pass adversarial drafting protocol derived from the fuel-sentinel repair plan (invoice-pulse 216), where three CEO-driven review passes under different named lenses each found real issues the prior pass missed. The fix is a documentary process definition in the governance template, not a tooling change or procedural checklist addition. NOTE: this entry is LINKED with entry 144 (pass 4 amendment) — together they form ONE Gate-2 governance item.
- **Confidence:** high
