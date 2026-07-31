# Classifications — Cycle 2026-07-30 (Plan 288)

**Batch:** 6 entries from sessions 13/14 (entry_ids 193-198, proposal_ids 201-206)
**Cycle timestamp:** 2026-07-31T17:54:17.077111+00:00

## Cycle Dict

```
ingested_count: 6
updated_count: 0
unchanged_count: 135
duplicates_marked_count: 0
needs_classification: [193, 194, 195, 196, 197, 198]
terminal_proposals_flagged: []
cycle_timestamp: 2026-07-31T17:54:17.077111+00:00
```

## Per-Entry Classifications

### Entry 193 (proposal 201) — governance_rule → PLANNER_TEMPLATE.md

**Source heading:** 2026-07-29: An artifact a step COPIES at run time has an authoring-vs-runtime drift window — pin its content hash, because a version number is inert [tag: bellows-integration]

**Category:** governance_rule | **Confidence:** high | **Target layer:** governance | **Target artifact:** PLANNER_TEMPLATE.md

**Reasoning:** Entry explicitly proposes planning rules for run-time-copied artifacts, citing the RULE_20_SELF_CHECK_BLOCK.md drift window: "a plan authored against the block as it stands, deposited, and then executed after the block changes." The fix is documentary — recording hashes, distinguishing pin jobs, enumerating blast radius — not a code or tooling change. Family line names Rule 39 as the lineage.

**Suggested action:** Add rule to PLANNER_TEMPLATE.md near Rule 39: for any artifact a step copies at run time, the plan records its content hash at authoring and re-verifies at QA; prefer a hash over a version for anything a machine must trust. Distinguish two jobs a pin can do: unchanged-by-THIS-plan (fail-closed) vs unchanged-since-authoring (drift detection). Before recommending a change to a run-time-copied artifact, enumerate in-flight plans it would land on.

---

### Entry 194 (proposal 202) — governance_rule → DRAFTING_CYCLE.md

**Source heading:** 2026-07-30: When one region keeps getting re-folded, the answer is usually DELETION, not another patch — and every patch feeling correct is exactly why it hides [tag: planner-discipline]

**Category:** governance_rule | **Confidence:** high | **Target layer:** governance | **Target artifact:** DRAFTING_CYCLE.md

**Reasoning:** Entry proposes extending section 2.8 oscillation-signal guidance: "it offers only joint-resolve or escalate; it does not offer cut it, and that is the resolution the evidence actually supports." Cites plan 286 spending ~20 of ~90 folds on four mechanisms later cut wholesale — stash demonstration (6 folds), declared-token apparatus (4), in-plan narrative, snapshot-aside ladder (~5). Family line explicitly names section 2.8.

**Suggested action:** Amend DRAFTING_CYCLE.md section 2.8 to add deletion as a third resolution alongside joint-resolve and escalate: when a region has been folded three or more times across walks, stop patching and ask whether the record or runtime already supplies a simpler method. Treat every-patch-correct as evidence FOR deletion, not against it. A trim still needs the same whole-artifact sweep an addition does.

---

### Entry 195 (proposal 203) — governance_rule → PLANNER_TEMPLATE.md

**Source heading:** 2026-07-30: Verify a guard's NECESSITY against the runtime, not only its correctness — I built a correct ladder for a state that cannot occur [tag: planner-discipline]

**Category:** governance_rule | **Confidence:** high | **Target layer:** governance | **Target artifact:** PLANNER_TEMPLATE.md

**Reasoning:** Entry describes building a correct but unnecessary Rule 56 snapshot-aside ladder in plan 286: "the tree is therefore always clean at step start, the restore can never discard foreign work, and Rule 56's own condition is never triggered." The machinery created a live defect — snapshot commits indistinguishable from real work caused false HALTs. Family line names this as the necessity-side complement to Rule 56.

**Suggested action:** Add rule to PLANNER_TEMPLATE.md near Rule 56: before authoring recovery machinery, establish that the state it recovers from is reachable under the actual dispatch path — read the runtime, do not reason from the general shape of the problem. A doctrine rule with a stated precondition is not owed when the precondition is false. Unreachable-state machinery is not merely inert — it interacts with real mechanisms and can manufacture failures.

---

### Entry 196 (proposal 204) — governance_rule → DRAFTING_CYCLE.md

**Source heading:** 2026-07-30: Check what a command PRINTS on success versus failure, not just what it does — three plan checks were unreadable in one cycle [tag: planner-discipline]

**Category:** governance_rule | **Confidence:** high | **Target layer:** governance | **Target artifact:** DRAFTING_CYCLE.md

**Reasoning:** Entry cites three unreadable checks in plan 286: "git merge-base --is-ancestor signals only through its exit code and prints NOTHING"; a pre-fix linter that "died on import gates and produced EMPTY stdout, byte-identical to the target-WARN-absent result"; and "grep -c prints 0 while exiting 1." The common defect: "the plan never asked what the agent would actually SEE." Family line names section 2.7 as the primary target.

**Suggested action:** Amend DRAFTING_CYCLE.md section 2.7 to require that for every command a plan mandates, the plan states what it prints on success, what it prints on failure, and confirms those differ. If they do not differ, add a positive control that produces visible output. Name the channel explicitly when it is not stdout. A command that can produce empty output on both paths needs a liveness proof.

---

### Entry 197 (proposal 205) — governance_rule → PLANNER_TEMPLATE.md

**Source heading:** 2026-07-30: A fix applied at the site where it was found will be re-created elsewhere — state it as a RULE, not as an edit [tag: planner-discipline]

**Category:** governance_rule | **Confidence:** high | **Target layer:** governance | **Target artifact:** PLANNER_TEMPLATE.md

**Reasoning:** Entry describes fixing QA row 9 (five claims in a one-claim-per-row table) without stating the rule, then reproducing the identical defect in QA row 3 two walks later: "reproducing the identical defect, in the same artifact, in the same cycle, by the same author who had diagnosed it." Notes that Checklist #26 was already strengthened by plan 287 for existing-sibling sweep; this extends to future sites via the Conflict Ledger mechanism from section 2.8.

**Suggested action:** Strengthen PLANNER_TEMPLATE.md Checklist #26 to extend fold-sweep consistency from existing siblings to future ones: after folding a defect that could recur, write the general form into the plan's Conflict Ledger as a constraint so later folds are checked against it. Ask of every fold whether it is a property of this site or of this class of site — only the first is safely fixed in place. A fold that changes a convention must be swept forward as well as sideways.

---

### Entry 198 (proposal 206) — governance_rule → DRAFTING_CYCLE.md

**Source heading:** 2026-07-30: The final step's gate span absorbs the Drafting Cycle block, so a gate-matching string QUOTED in the log is evaluated as if the step had said it [tag: bellows-integration]

**Category:** governance_rule | **Confidence:** high | **Target layer:** governance | **Target artifact:** DRAFTING_CYCLE.md

**Reasoning:** Entry describes a live gates.py mechanism: "gates.py:449 rf ^## STEP {n}\b.*?(?=^## STEP |\Z) — the LAST step's span runs to end-of-file and therefore swallows the trailing Drafting Cycle block." Verified across versions: a quoted path token made a real plan_lint WARN disappear. Worse: the log carried both byte-exact Rule 20 banner strings, satisfying the blocking gate on narrative alone. This is NOT proposal 197 — that addresses agent misreading, this is gate matching with no reader involved.

**Suggested action:** Add rule to DRAFTING_CYCLE.md section 3: the Cycle Log must contain no string a gate matches — describe gate-matching strings, never quote them (banner text, deposits/scope markers, path tokens, test patterns). After compacting or editing the log, re-run the gate and confirm the WARN/PASS set is unchanged. A WARN that disappears when editing the LOG is the signature of this defect. Note: gates.py:449 per-step span regex causes the final step's span to run to end-of-file, absorbing the trailing Drafting Cycle block — Gate 2 should decide whether a paired gate edit is owed.

---

## Cluster Synthesis for Gate 1

6 entries from the 286/287 Gate-2 cycles — 4 planner-discipline authoring refinements + 2 bellows-integration mechanics findings; all classified governance_rule, targets split 3-3 across PLANNER_TEMPLATE.md and DRAFTING_CYCLE.md.

- **PLANNER_TEMPLATE.md targets (proposals 201, 203, 205):** Rule 39 extension (hash pinning for run-time-copied artifacts), Rule 56 complement (verify guard necessity against runtime), Checklist #26 extension (state fixes as rules, not edits). Proposal 201 has a defensible alternative target (RULE_20_SELF_CHECK_BLOCK.md) — the artifact the entry was written about. Proposal 205 has partial overlap with plan 287's Checklist #26 strengthening — extends from existing siblings to future ones.

- **DRAFTING_CYCLE.md targets (proposals 202, 204, 206):** Section 2.8 extension (deletion as third resolution for oscillating regions), section 2.7 extension (state what commands print on success vs failure), section 3 addition (Cycle Log must not contain gate-matching strings). Proposal 206 has a live gates.py coupling — the entry names gates.py:449's per-step span regex as the mechanism. Per DRAFTING_CYCLE.md section 6, a Gate-2 codification touching section 1 or section 4 must pair with a gate edit; section 3 is outside that scope, but the coupling is flagged for Gate 1's decision.

- **No ambiguous classifications.** All 6 are governance_rule with high confidence. The 4 planner-discipline entries propose documentary rule changes; the 2 bellows-integration entries describe live tooling mechanics but their proposed fixes are avoidance rules rather than code changes.
