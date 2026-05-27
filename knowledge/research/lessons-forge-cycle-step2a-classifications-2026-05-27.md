# Lessons Forge Cycle — Step 2a: Classify First Batch (2026-05-27)

## 1. Batch metadata

- **Entry ID range:** 58–75
- **Count:** 18
- **Source:** Step 1 deposit Section 5 (Step 2a batch)
- **Proposal ID range:** 63–80

## 2. Classification table

| entry_id | category | confidence | target_layer | target_artifact | status | suggested_action |
|---|---|---|---|---|---|---|
| 58 | governance_rule | high | governance | PLANNER_TEMPLATE.md | proposed | Add Rule 26 sub-rule: SA steps >400 words must include distributed liveness anchors |
| 59 | narrative | high | none | — | proposed | Archive as context. Existing Phase 1.5 discipline catches at 100% rate. Tooling retired |
| 60 | governance_rule | high | governance | PLANNER_TEMPLATE.md | proposed | Add methodology rule: use parsed.permission_denials, not grep raw_output |
| 61 | governance_rule | high | governance | PLANNER_TEMPLATE.md | proposed | All Deposits blocks must use canonical multi-line bullet form |
| 62 | governance_rule | high | governance | PLANNER_TEMPLATE.md | proposed | Read literal Files Changed list before authoring follow-up from gate failure |
| 63 | governance_rule | high | governance | PLANNER_TEMPLATE.md | proposed | Serialize same-project plans by default; parallel only cross-project |
| 64 | governance_rule | high | governance | PLANNER_TEMPLATE.md | proposed | Bellows-fix checklist: enumerate lifecycle stages for filename patterns |
| 65 | governance_rule | high | governance | PLANNER_TEMPLATE.md | proposed | Filesystem-ownership rule: four safe Planner rename destinations |
| 66 | governance_rule | high | governance | PLANNER_TEMPLATE.md | proposed | Daemon-fix checklist: in-plan migrations ineffective until restart |
| 67 | governance_rule | high | governance | PLANNER_TEMPLATE.md | proposed | Reinforce Phase 1.5: acknowledge CEO, complete reads before investigation |
| 68 | governance_rule | high | governance | PLANNER_TEMPLATE.md | proposed | Worktree-safety rule: check .bellows-worktrees/ before any project file edit |
| 69 | governance_rule | high | governance | PLANNER_TEMPLATE.md | proposed | Mid-plan CEO addenda flow via verdict, not blueprint edits |
| 70 | governance_rule | high | governance | PLANNER_TEMPLATE.md | proposed | QA step prompt must paste canonical RULE_20_SELF_CHECK_BLOCK.md paragraph |
| 71 | governance_rule | high | governance | PLANNER_TEMPLATE.md | proposed | Verify timing/ordering claims against most recent ordering audit |
| 72 | governance_rule | high | governance | PLANNER_TEMPLATE.md | proposed | Worktree-recovery: git fetch origin before authoring recovery commits |
| 73 | governance_rule | medium | governance | PLANNER_TEMPLATE.md | proposed | Session-start git fetch + divergence check; reset --hard if diffs empty |
| 74 | governance_rule | high | governance | PLANNER_TEMPLATE.md | proposed | Reinforce Rule 35: scan and strip STOP-prose before Bellows plan deposit |
| 75 | governance_rule | high | governance | PLANNER_TEMPLATE.md | proposed | DEV-step rule: specify exact field names/enums for frontend-backend connections |

## 3. Distribution summary

**Category counts (batch 1):**

| Category | Count |
|---|---|
| governance_rule | 17 |
| narrative | 1 |

**Confidence breakdown:**

| Confidence | Count |
|---|---|
| high | 17 |
| medium | 1 |

**Status breakdown:**

| Status | Count |
|---|---|
| proposed | 18 |
| ambiguous | 0 |

## 4. Cross-cutting observations within batch

1. **Heavy governance_rule skew (17/18).** Nearly all entries in this batch propose Planner discipline rules for PLANNER_TEMPLATE.md. This is consistent with the `planner-discipline` tag being dominant across entries 58-75. The batch reflects a mature operational system where most lessons have clear, actionable rule proposals targeting governance artifacts.

2. **"Captured but not internalized" meta-pattern.** Entries 67 (Phase 1.5 skip), 68 (worktree collision despite memory rule), 70 (QA Rule 20 paraphrase), 71 (timing hypothesis re-derived), and 74 (STOP-prose despite Rule 35) all share the same failure shape: the rule exists in context, but cognitive load at the decision point suppresses it. All five propose mechanical checks at the moment of authoring rather than cognitive re-reading. This is the dominant theme of the batch.

3. **Bellows worktree lifecycle cluster.** Entries 63, 64, 65, 66, 68, 69, 72, 73 form a coherent cluster around worktree-related discipline: parallel dispatch conflicts, filename disambiguation, daemon-owned transitions, file-edit safety, verdict-as-channel, recovery procedures, and SHA divergence. These could potentially consolidate into a "Worktree Lifecycle" subsection of PLANNER_TEMPLATE.

4. **Plan-authoring discipline cluster.** Entries 58, 61, 62, 70, 74, 75 focus specifically on how the Planner writes plan step prompts: SA liveness anchors, Deposits block format, Files Changed disambiguation, QA template inclusion, STOP-prose stripping, and interface contract specification.

5. **Single narrative entry (59)** is a well-documented pattern with a tried-and-failed tooling path. The entry explicitly closes the loop — no new action needed, existing discipline sufficient.

## 5. Ambiguous / low-confidence entries

**Entry 73 (medium confidence):** Classified as `governance_rule` rather than `narrative` because it proposes actionable session-start hygiene rules. Medium confidence because the primary recommendation targets the human operator (CEO), not the Planner's governance artifacts directly. The Planner-side discipline rule ("prefer git fetch origin first") substantially overlaps with entry 72's worktree-recovery rule.

No entries classified as `ambiguous`.

## 6. Output Receipt

- **Agent:** Forge Lessons Agent
- **Step:** 2a
- **Status:** Complete
- **What Was Done:** Classified 18 entries (IDs 58-75) via ADR-002 taxonomy, persisted 18 proposals (IDs 63-80) via `insert_proposal`
- **Files Deposited:** `knowledge/research/lessons-forge-cycle-step2a-classifications-2026-05-27.md`
- **Files Created or Modified:** `lessons-forge.db` (committed)
- **Decisions Made:** 18 classification tuples — 17 governance_rule, 1 narrative; 17 high confidence, 1 medium
- **Flags for CEO:** Heavy governance_rule skew (17/18) reflects the planner-discipline nature of this batch. "Captured but not internalized" is the dominant meta-pattern (5 entries). Entry 73 medium-confidence — primary audience is operator, not governance artifact. Worktree lifecycle cluster (8 entries) may warrant consolidation into a PLANNER_TEMPLATE subsection.
- **Flags for Next Step:** Step 2b loads entries 76-93 from Step 1 deposit and applies the same classification procedure
