# Classifications — Cycle 2026-08-10, Part 1 (Tranche A: entries 266–279)

## Classification Methodology

All 14 entries classified under ADR-002's six-value taxonomy. Each classification derived from the entry's own `raw_content` body — no entry in this batch carries a `**Family:**` line (0 of 41, measured), so every placement comes from the body alone. The scout table in the plan's front matter provided heading-and-remedy-level guidance, with explicit licence to disagree (Rule 58); divergences recorded below.

Category arm compliance: every classification falls within the expected arm for its entry's tag. No arm-external categories assigned.

## Per-Entry Classification Reasoning

### Entry 266 (proposal 274) — `bellows-integration` → `governance_rule`

**Target:** `PLANNER_TEMPLATE.md` (halt-with-options authoring)

The entry identifies a structural limitation of the verdict channel: a continue/stop bit cannot carry multi-option decisions. The measured mitigation is visibility — bannering the inferred option — rather than channel redesign. The PLANNER_TEMPLATE placement covers the authoring-side rule (how to design halt-with-options); the bellows-owned verdict-channel constraint is a Rule 46 split candidate for Gate 1 to route to the owning register.

The entry's remedy ("Never encode a multi-option CEO decision into a single continue/stop bit"; "banner WHICH option it inferred, at the next gate the CEO reads") prescribes a practice plan authors must remember. No named check, parser, or tool evaluates compliance. **Remedy: discipline.**

### Entry 267 (proposal 275) — `drafting-cycle` → `governance_rule`

**Target:** `DRAFTING_CYCLE.md` (§2/§3, convergence criterion)

Cluster (A) entry. The entry separates the composition bar (no finding changes what an agent will do) from the literal dry bar (zero findings), measuring the divergence for the third time. The prescriptive contribution is requiring confirming-pass yields to be reported by class (machinery vs record) so the two bars can be compared rather than conflated.

The entry's remedy ("Report a confirming pass's yield BY CLASS"; "budget one record culmination before the true dry pass") prescribes editorial judgment calls for cycle authors. No mechanical check or parser named. **Remedy: discipline.**

### Entry 268 (proposal 276) — `drafting-cycle` → `governance_rule`

**Target:** `DRAFTING_CYCLE.md` (§2.8, constraint lifecycle)

The entry identifies a temporal vulnerability: constraints opened from the current batch are the most likely to be breached by later folds, because the folds predate the constraint. Three independent breaches of three independently-opened constraints in one cycle establish this as a systematic class rather than a one-off.

The entry's remedy ("After ANY fold, re-check it against the ledger's newest constraints specifically"; "cite it when pricing mechanization of a constraint over another prose restatement") prescribes a human discipline of post-fold review. No automated check named. **Remedy: discipline.**

### Entry 269 (proposal 277) — `planner-discipline` → `governance_rule`

**Target:** `PLANNER_TEMPLATE.md` (deposit discipline)

The entry documents a near-miss where id_sequence drift between authoring and deposit was caught only because the verify-at-deposit clause enumerated every site. The rule prescribes treating authoring-time ids as predictions and mandating site enumeration.

The entry's remedy ("Treat any authoring-time id as a prediction carrying a verify-at-deposit clause that NAMES every site"; "re-read id_sequence, re-token all sites to the actual id") prescribes a procedure plan authors must follow. No lint or parser automates the enumeration. **Remedy: discipline.**

### Entry 270 (proposal 278) — `drafting-cycle` → `governance_rule`

**Target:** `DRAFTING_CYCLE.md` (§2.7/§3, confirming-pass requirements)

Cluster (A) entry. Flag (D): v2.0 codified the closing-record re-read and the Cycle-Log-as-covered-region; residue is the sweep-the-tracking-lines clause. The entry demonstrates that record decay hides from aimed passes because aim always points at machinery, so the confirming pass must be untargeted.

The entry's remedy ("The confirming pass must be untargeted precisely BECAUSE the record's decay hides from aimed passes"; "sweeps the record lines that TRACK it in the same culmination") prescribes how to scope confirming passes. No tool or check evaluates this. **Remedy: discipline.**

### Entry 271 (proposal 279) — `process-discipline` → `governance_rule`

**Target:** `DRAFTING_CYCLE.md` (cycle methodology)

The entry is a calibration datum: the three-tranche split held classification quality at 3.2× the record batch with no inter-tranche cliff. The scout flagged this as a likely `reference` route; the category is `governance_rule` because the How to apply prescribes future behavior ("prefer tranches-with-manifests over a single saturated step"; "carry the per-tranche depth distribution as the standing instrument"). The file target is `DRAFTING_CYCLE.md` because the cycle methodology section governs tranche architecture. Gate 1 may route this as `reference` if the calibration-datum nature dominates. Divergence from scout's route suggestion noted; the target_artifact divergence from the scout's "likely routed reference" is recorded: the scout named no file target, so the file is independently derived from the entry's subject matter (cycle methodology).

The entry's remedy prescribes a preference and an instrument-carrying convention — human-facing process guidance. No tool or parser named. **Remedy: discipline.**

### Entry 272 (proposal 280) — `process-discipline` → `governance_rule`

**Target:** `PLANNER_TEMPLATE.md` (multi-copy census rule)

The entry identifies the multi-copy enum problem: a recognized-value enum lives in every tool that reads it, and shipping one copy while others drift is a systematic class. The census-first protocol (grep -F across all copies, "both edits or neither" clauses) is the prescribed fix.

The entry's remedy names `grep -F` as the census tool and prescribes "a 'both edits or neither' clause per copy-pair [that] makes the invariant mechanical" — a structural convention a tool could evaluate (verify that all enum copies are updated together). The owner is not named. **Remedy: mechanism | owner: unnamed.**

### Entry 273 (proposal 281) — `verification` → `governance_rule`

**Target:** `PLANNER_TEMPLATE.md` (trade-off argumentation)

The entry establishes a measurement rule: headline rates must be computed over the in-population (the rows the change actually affects), not a cross-population average that dilutes the signal. The strongest counterexample must be named and argued against.

The entry's remedy ("compute the rate over the IN-population"; "Name the strongest single counterexample from the IN-population and argue against it specifically") prescribes analytical discipline for plan authors. No mechanical check named. **Remedy: discipline.**

### Entry 274 (proposal 282) — `verification` → `governance_rule`

**Target:** `PLANNER_TEMPLATE.md` (doc-correction rule)

The entry establishes that truth-restoration edits are held to their own standard in both directions: overstating and understating enforcement are the same defect. The remedy requires reading the enforcement implementation first and stating its exact tier.

The entry's remedy ("read the ENFORCEMENT implementation first and state its exact tier"; "Sweep the correcting plan's own prose for the banned claims") prescribes a human verification process. No automated check named. **Remedy: discipline.**

### Entry 275 (proposal 283) — `drafting` → `governance_rule`

**Target:** `DRAFTING_CYCLE.md` (§2.6, evidence coherence)

Flag (D): the evidence-attack brief exists at v1.7; residue is the after-every-fold cadence. The entry demonstrates that a narrowing fold can destroy its own evidence base: the Why-table citations looked honest but traced through the shipped filter revealed silencing.

The entry's remedy ("re-trace every cited evidence case through the NARROWED spec and confirm each can still fire"; "re-verify the pairing whenever either side moves") prescribes a human re-trace after narrowing folds. No automated check named. **Remedy: discipline.**

### Entry 276 (proposal 284) — `verification` → `governance_rule`

**Target:** `PLANNER_TEMPLATE.md` (test authoring)

The entry identifies the test-fixture guard-weakening class: a fixture asserting the wrong expected output forces a developer to weaken the guard to make the test pass. The fix: assert the current measured behaviour first, then carve out only the intended delta.

The entry's remedy ("run the CURRENT implementation on the input first and assert its measured behaviour"; "Treat a fixture no correct implementation can satisfy as a defect in the PLAN") prescribes a test-authoring discipline. No automated check named. **Remedy: discipline.**

### Entry 277 (proposal 285) — `instrumentation` → `governance_rule`

**Target:** `DRAFTING_CYCLE.md` (§3, earned-phrasing clause)

The entry establishes that the gap between a checker's mechanics and its intended condition fires in both directions: over-match and under-match. Three specimens demonstrate the three shapes: early clearing, narration-triggered false match, and deliberate broadness over-matching.

The entry's remedy ("state the check's exact matching semantics beside the earned-clear condition, and never satisfy or dodge it by wording the state has not earned"; "expect and pre-classify the over-match band") prescribes documentation and classification conventions for check authors. No named tool or parser. **Remedy: discipline.**

### Entry 278 (proposal 286) — `drafting-cycle` → `governance_rule`

**Target:** `DRAFTING_CYCLE.md` (§2.6, panel methodology)

Flag (D): the seat-brief registry landed at v1.7; residue is the residue-battery cadence and the metering convention. The entry presents the first metered panel run (563k tokens, 45 findings) and identifies the composition pattern: aimed briefs produce HIGHs, replication seats produce MEDIUM hardening, and ~40% of late findings are residue a script could drain.

The entry's remedy ("Aim panel seats at deletion premises and the clone-diff explicitly"; "Run the mechanical residue battery after every culmination"; "Meter every panel") prescribes panel configuration and timing. The residue battery names existing tools (lint + sweeps) but the prescription is about WHEN to run them — a cadence decision. **Remedy: discipline.**

### Entry 279 (proposal 287) — `verification` → `governance_rule`

**Target:** `DRAFTING_CYCLE.md` (§2.7, count verification)

The entry measures a systematic failure: close-commit counts were wrong or absent 4-for-4. The remedy prescribes mechanical enumeration (git log --follow by PATH, SELECT by key range) instead of narrated counts, and reconciliation lines at authoring.

The entry's remedy ("enumerated mechanically (git log --follow by PATH, SELECT by key range)"; "emit the reconciliation line at authoring") prescribes a practice of using tools rather than narrating. The tools named (git, SQL) are used manually by the author. No automated lint verifies the reconciliation. **Remedy: discipline.**

## Summary

| Tag | Count | Categories assigned |
|---|---|---|
| `bellows-integration` | 1 | governance_rule |
| `drafting-cycle` | 4 | governance_rule (4) |
| `planner-discipline` | 1 | governance_rule |
| `process-discipline` | 2 | governance_rule (2) |
| `verification` | 4 | governance_rule (4) |
| `instrumentation` | 1 | governance_rule |
| `drafting` | 1 | governance_rule |

All 14 classified as `governance_rule`. One mechanism remedy identified (entry 272, proposal 280). Thirteen discipline remedies.

**Cluster (A) entries in this tranche:** 267 (proposal 275) and 270 (proposal 278), both routed to `DRAFTING_CYCLE.md` with the §2 rewrite flag in `suggested_action`.

**Rule 46 candidate:** entry 266 (proposal 274), noted in `suggested_action`.

**Flag (D) entries:** 270 (proposal 278, sweep-the-tracking-lines residue) and 275 (proposal 283, after-every-fold cadence residue) and 278 (proposal 286, residue-battery cadence and metering convention residue).

**No `ambiguous` proposals in this tranche.**
