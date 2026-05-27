# Lessons Forge Cycle — Batch 2 Recovery: Classify Entries 76-93 (2026-05-27)

## 1. Batch metadata

- **Entry ID range:** 76–93
- **Count:** 18
- **Source:** Step 1 deposit Section 5 (Step 2b batch) from halted cycle plan
- **Proposal ID range:** 81–98
- **Recovery context:** Original cycle plan halted at Bellows-step-3 due to non-monotonic STEP labels violating Bellows's positional step-parser contract. Step 2a (entries 58-75) completed as proposals 63-80. This plan recovers Step 2b (entries 76-93).

## 2. Classification table

| entry_id | category | confidence | target_layer | target_artifact | status | suggested_action |
|---|---|---|---|---|---|---|
| 76 | governance_rule | high | governance | PLANNER_TEMPLATE.md | proposed | Add verdict-response filename discipline rule: copy request filename, no suffixes |
| 77 | governance_rule | high | governance | PLANNER_TEMPLATE.md | proposed | Add three worktree lifecycle rules: pre-flight prune, halt on 2nd teardown-empty, fresh-claim stop |
| 78 | governance_rule | high | governance | PLANNER_TEMPLATE.md | proposed | Add rule: scan BACKLOG defers for manual-fallback rationales when mechanizing checks |
| 79 | governance_rule | high | governance | PLANNER_TEMPLATE.md | proposed | Add rule: multi-step diagnostics needing per-step CEO review use `always` or split |
| 80 | governance_rule | high | governance | PLANNER_TEMPLATE.md | proposed | Add rule: verdict-time overrides target fresh-read documents, not cached plan file |
| 81 | governance_rule | medium | governance | PLANNER_TEMPLATE.md | proposed | Add rule: archive prior processed-verdict files before issuing verdict for step N>1 |
| 82 | narrative | high | none | — | proposed | Archive as context — runner log step labels unreliable; use file-state for ground truth |
| 83 | governance_rule | medium | governance | PLANNER_TEMPLATE.md | proposed | Add Rule 22(d) override guidance for domain-terminology hedging false positives |
| 84 | governance_rule | high | governance | PLANNER_TEMPLATE.md | proposed | Add final-step gate_failure 5-step recovery checklist (verify, stop, Done move, archive) |
| 85 | governance_rule | high | governance | PLANNER_TEMPLATE.md | proposed | Add rule: QA-step Deposits blocks declare exactly one `.md` file (the QA report) |
| 86 | governance_rule | high | governance | PLANNER_TEMPLATE.md | proposed | Add rule: new-data-source mechanization must ship governance edit in same session |
| 87 | governance_rule | high | governance | PLANNER_TEMPLATE.md | proposed | Add Rule 21 supplement: grep test files for function refs before declaring targeted scope |
| 88 | narrative | high | none | — | proposed | Archive as context — `git diff --stat` blind spot fixed; documents gate-failure framing |
| 89 | governance_rule | high | governance | PLANNER_TEMPLATE.md | proposed | Add rule: `pause_for_verdict` must be exactly `always`, `after_step_1`, or `after_qa_step` |
| 90 | governance_rule | high | governance | PLANNER_TEMPLATE.md | proposed | Add rule: all deposits must use Rule 26 `**Deposits:**` block format, not inline prose |
| 91 | governance_rule | high | governance | PLANNER_TEMPLATE.md | proposed | Add baton rule: cross-check "On the horizon" items against PROJECT_STATUS Completed |
| 92 | governance_rule | high | governance | PLANNER_TEMPLATE.md | proposed | Add BACKLOG rule: scan Closed section before filing "X is missing" entries |
| 93 | governance_rule | high | governance | PLANNER_TEMPLATE.md | proposed | Add rule: migration plans must include `init_db` run against production DB with PRAGMA verify |

## 3. Distribution summary

**Category counts (batch 2):**

| Category | Count |
|---|---|
| governance_rule | 16 |
| narrative | 2 |

**Confidence breakdown:**

| Confidence | Count |
|---|---|
| high | 16 |
| medium | 2 |

**Status breakdown:**

| Status | Count |
|---|---|
| proposed | 18 |
| ambiguous | 0 |

## 4. Cross-cutting observations within batch

1. **Continued governance_rule dominance (16/18).** Similar to batch 1 (17/18), nearly all entries propose Planner discipline rules for PLANNER_TEMPLATE.md. The batch reflects lessons learned from operational friction with Bellows mechanics — the fixes are governance rules because the Planner is the agent whose behavior needs to change to work around daemon-side limitations.

2. **Bellows-workaround cluster (entries 76, 77, 80, 81, 82, 84, 89).** Seven entries are Planner-side workarounds for Bellows daemon behaviors: verdict filename matching (76), worktree lifecycle gaps (77), plan-content caching (80), verdict renormalization loop (81), runner log unreliability (82), final-step gate_failure stuck state (84), and silent no-pause on invalid header values (89). The workarounds exist because the underlying daemon bugs aren't fixed yet. When daemon-side fixes ship, these governance rules become unnecessary.

3. **Plan-authoring discipline cluster (entries 79, 85, 86, 87, 89, 90, 93).** Seven entries propose pre-write checks at plan-authoring time: `pause_for_verdict` value selection (79, 89), QA deposit count (85), code-governance coupling (86), test-scope scoping (87), Deposits block format (90), and migration-plan shape (93). All follow the same pattern: mechanical check at authoring time prevents downstream failure that is expensive to recover from.

4. **Session-handoff discipline cluster (entries 91, 92).** Two entries address the integrity of cross-session artifacts: stale baton claims (91) and misframed BACKLOG entries (92). Both propose the same fix shape: cross-reference against existing Closed/Completed history before propagating or filing.

5. **Two narrative entries document closed loops.** Entry 82 (runner log labels) is a "know this limitation" observation without an actionable governance change. Entry 88 (git diff blind spot) documents a structural fix that already shipped — the remaining value is the framing lesson about evaluating gate blast radius by consumer analysis.

## 5. Cross-batch observations

Spanning Step 2a batch (proposals 63-80, entries 58-75) and this batch (proposals 81-98, entries 76-93):

1. **Overwhelming governance_rule skew across the full 36-entry cycle: 33/36 (91.7%).** Only 3 entries classified as narrative (entries 59, 82, 88). Zero entries classified as structural, instrumentation, or language. This batch continues the pattern from batch 1 and is consistent with the `planner-discipline` tag being dominant across the cycle. The lesson corpus from this period is almost entirely Planner-discipline governance rules targeting PLANNER_TEMPLATE.md.

2. **"Captured but not internalized" meta-pattern extends across batches.** Batch 1 identified 5 entries (67, 68, 70, 71, 74) with this failure shape. Batch 2 adds entry 85 (QA deposit count rule in BACKLOG but not applied at authoring time) as the same pattern: discipline exists as text-in-context but doesn't fire at the authoring moment. Combined: 6 entries across the 36-entry cycle share this root cause. The implied meta-fix is mechanical checklists at plan-authoring time rather than prose rules hoping for cognitive recall.

3. **Bellows workaround governance rules form the largest cluster.** Combining batch 1's worktree lifecycle cluster (entries 63-66, 68-69, 72-73 = 8 entries) with batch 2's Bellows-workaround cluster (entries 76-77, 80-82, 84, 89 = 7 entries) yields 15 entries — 41.7% of the full cycle — that are governance workarounds for Bellows daemon-side limitations. These rules are explicitly noted as temporary mitigations that become unnecessary when the underlying daemon fixes ship. This cluster may warrant a dedicated "Bellows Operational Workarounds" subsection in PLANNER_TEMPLATE that can be deprecated wholesale when the daemon is hardened.

4. **Plan-authoring pre-write checks are the dominant fix shape.** Batch 1 had 6 entries in its plan-authoring cluster (58, 61, 62, 70, 74, 75). Batch 2 has 7 (79, 85, 86, 87, 89, 90, 93). Combined: 13 entries (36.1%) propose mechanical checks at plan-authoring time. The meta-pattern suggests a "Plan Authoring Checklist" section in PLANNER_TEMPLATE that consolidates these checks into a single pre-flight list rather than scattering them across individual rules.

5. **Confidence is uniformly high.** Batch 1: 17 high, 1 medium. Batch 2: 16 high, 2 medium. Combined: 33 high (91.7%), 3 medium (8.3%). The two medium-confidence entries in batch 2 (entries 81, 83) are both Planner-side workarounds for daemon bugs — medium because the real fix is structural/code-side, not governance. No low-confidence entries in either batch. No ambiguous entries in either batch.

6. **PLANNER_TEMPLATE.md is the universal target artifact.** All 33 governance_rule entries across both batches target PLANNER_TEMPLATE.md. No entries target COMPANY.md, specialist files, or other governance artifacts. The full 36-entry cycle is essentially a PLANNER_TEMPLATE hardening exercise.

## 6. Ambiguous / low-confidence entries

**Entry 81 (medium confidence):** Classified as `governance_rule` rather than `narrative` because it proposes a concrete Planner-side workaround (archive prior processed-verdict files before issuing new verdict). Medium confidence because the entry explicitly states "The real fix is Bellows-side" — the governance rule is a temporary workaround for a daemon bug, not a permanent Planner discipline. If the daemon fix ships, this proposal should be marked `stale`.

**Entry 83 (medium confidence):** Classified as `governance_rule` rather than `narrative` because it proposes a concrete override discipline ("override-with-Rule-22 with explicit reasoning is the correct path"). Medium confidence because the entry frames this as a "discipline workaround" for a Bellows-side bug (hedging detector needs context awareness). The governance rule is a temporary workaround; the real fix is code-side in the hedging detector.

No entries classified as `ambiguous`. No low-confidence entries.

## 7. Output Receipt

- **Agent:** Forge Lessons Agent
- **Step:** 1
- **Status:** Complete (18 proposals inserted with non-duplicate category)
- **What Was Done:** Classified 18 entries (IDs 76-93) via ADR-002 taxonomy, persisted 18 proposals (IDs 81-98) via `insert_proposal`, produced cross-batch synthesis spanning the full 36-entry cycle
- **Files Deposited:** `knowledge/research/lessons-forge-cycle-batch2-recovery-2026-05-27.md`
- **Files Created or Modified:** `lessons-forge.db` (committed)
- **Decisions Made:** 18 classification tuples — 16 governance_rule, 2 narrative; 16 high confidence, 2 medium; 0 ambiguous
- **Flags for CEO:** (1) Heavy governance_rule skew continues (16/18, consistent with batch 1's 17/18). Full cycle: 33/36 governance_rule, all targeting PLANNER_TEMPLATE.md. (2) Two medium-confidence entries (81, 83) are Planner-side workarounds for daemon bugs — will become stale when Bellows fixes ship. (3) Cross-batch meta-pattern: 15/36 entries (41.7%) are Bellows operational workarounds; consider dedicated PLANNER_TEMPLATE subsection. (4) 13/36 entries (36.1%) propose plan-authoring pre-write checks; consider consolidated "Plan Authoring Checklist" section. (5) "Captured but not internalized" pattern has 6 entries across the cycle — strongest signal for mechanical checklist at authoring time.
- **Flags for Next Step:** Closeout plan (separate, follow-up) will update PROJECT_STATUS and verify all 36 entries have proposals
