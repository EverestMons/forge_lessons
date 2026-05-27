# Lessons Forge Cycle — Step 1: Deterministic Cycle Run (2026-05-27)

## 1. Pre-state snapshot (sub-step 1.0)

```
lesson_entries total: 57
lesson_proposals total: 62
  status=proposed: 0
  status=accepted: 0
max_entry_id: 57
max_proposal_id: 62
```

## 2. Cycle result JSON (sub-step 1.1)

```json
{
  "ingested_count": 36,
  "updated_count": 0,
  "unchanged_count": 0,
  "duplicates_marked_count": 0,
  "needs_classification": [
    58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73,
    74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
    90, 91, 92, 93
  ],
  "cycle_timestamp": "2026-05-27T18:49:00.677967+00:00"
}
```

## 3. Post-state snapshot + delta table

```
lesson_entries total: 93
lesson_proposals total: 62
  status=proposed: 0
  status=accepted: 0
max_entry_id: 93
max_proposal_id: 62
```

| Metric | Pre | Post | Delta |
|---|---|---|---|
| lesson_entries | 57 | 93 | +36 |
| lesson_proposals | 62 | 62 | 0 |
| status=proposed | 0 | 0 | 0 |
| status=accepted | 0 | 0 | 0 |
| max_entry_id | 57 | 93 | +36 |
| max_proposal_id | 62 | 62 | 0 |

## 4. `needs_classification` queue listing

| ID | Date | Heading (truncated) | Tags |
|---|---|---|---|
| 58 | 2026-05-27 | SA dense-content blueprint steps need explicit early-output anchors to avoid ~600-730s idle... | (no tags) |
| 59 | 2026-05-26 | "Leftover after ship" pattern — 5th recurrence in 3 days; the discipline catch rate is 1... | (no tags) |
| 60 | 2026-05-26 | When mining agent step logs for tool-denial events, parse JSON structure; don't grep ra... | (no tags) |
| 61 | 2026-05-26 | Inline `**Deposits:**` blocks with un-prefixed backticked paths silently fail `_extract_`... | (no tags) |
| 62 | 2026-05-26 | scope_check trip identified the WRONG file in CEO context, leading to a diagnostic that... | (no tags) |
| 63 | 2026-05-22 | Parallel diagnostics against the same project conflict at teardown on shared bookkeeping... | (no tags) |
| 64 | 2026-05-22 | Pre-scan-style fix-ups must disambiguate filename-overloaded lifecycle states... | (no tags) |
| 65 | 2026-05-22 | Planner manually renamed in-progress-* → verdict-pending-* and triggered re-dispatch loo... | (no tags) |
| 66 | 2026-05-22 | Bellows-side fix-plan with in-plan filesystem migration is ineffective until daemon rest... | (no tags) |
| 67 | 2026-05-20 | Phase 1.5 Source 0 (shop_next_session.md) skipped at session start | (no tags) |
| 68 | 2026-05-20 | Worktree collision — Planner edited a project file while a worktree was active on the sa... | planner-discipline, worktree, bellows-integration |
| 69 | 2026-05-20 | CEO addenda routed downstream via verdict, not upstream via file edit | planner-discipline, worktree, bellows-integration, ve... |
| 70 | 2026-05-20 | QA-step prompts must reference RULE_20_SELF_CHECK_BLOCK.md, not paraphrase Rule 20 | planner-discipline, rule-20, bellows-integration, qa-... |
| 71 | 2026-05-27 | Timing/ordering hypotheses must be verified against the most recent ordering audit befor... | planner-discipline, bellows-integration, diagnostic-aut... |
| 72 | 2026-05-27 | "Empty cherry-pick" during worktree teardown is not always a teardown failure — fetch or... | planner-discipline, bellows-integration, worktree, re... |
| 73 | 2026-05-27 | Local-vs-origin parallel-SHA divergence is a routine outcome of worktree teardown, not a... | bellows-integration, worktree, operator-discipline, g... |
| 74 | 2026-05-21 | STOP-prose recurrence in Bellows-dispatched plans | planner-discipline, bellows-integration, stop-prose... |
| 75 | 2026-05-21 | Planner specified the WHAT without the WHERE-IT-CONNECTS (field-invention pattern) | planner-discipline, prompt-authoring, interface-contrac... |
| 76 | 2026-05-21 | Verdict response filename must mirror request filename byte-for-byte | planner-discipline, bellows-integration, verdict-format... |
| 77 | 2026-05-21 | Worktree lifecycle hygiene — three discipline rules from a high-friction session | planner-discipline, operator-discipline, bellows-integr... |
| 78 | 2026-05-22 | BACKLOG defers grounded in Planner-side fallback can be silently invalidated by gate mec... | (no tags) |
| 79 | 2026-05-22 | Multi-step diagnostic with `pause_for_verdict: after_step_1` skips intermediate-step CEO... | planner-discipline, plan-authoring, diagnostic-shape |
| 80 | 2026-05-22 | Bellows plan-content cache is claim-time snapshot; post-claim plan edits do not propagat... | (no tags) |
| 81 | 2026-05-22 | processed-verdict-* renormalization loop on advanced plans... | (no tags) |
| 82 | 2026-05-22 | Bellows runner log "(step N)" label lags actual dispatch state... | (no tags) |
| 83 | 2026-05-22 | Rule 22 (d) hedging-keyword detector false-positive on domain terminology... | (no tags) |
| 84 | 2026-05-22 | Final-step gate_failure leaves plan stuck — Planner-direct Done move is the recovery... | (no tags) |
| 85 | 2026-05-25 | QA-step deposits blocks must declare exactly one `.md` file or the gate misfires... | planner-discipline, bellows-integration, gate-deposit-h... |
| 86 | 2026-05-25 | Mechanizing a new authoritative data source requires shipping the governance edit that o... | planner-discipline, orchestration-pattern, mechanizatio... |
| 87 | 2026-05-25 | Targeted-scope QA can miss regressions in test files outside the targeted bucket... | planner-discipline, rule-21, test-scope |
| 88 | 2026-05-25 | `git diff --stat` working-tree-vs-index is blind to committed changes; agents commit dur... | bellows-architecture, gate-design |
| 89 | 2026-05-26 | `pause_for_verdict` accepts only three values; inventing a fourth gets a WARN, not an er... | planner-discipline, bellows-architecture |
| 90 | 2026-05-26 | Use `**Deposits:**` blocks for ALL agent deposits including QA reports; the prose-fallba... | planner-discipline, rule-26 |
| 91 | 2026-05-26 | Stale priority claims propagate across batons without PROJECT_STATUS cross-check... | planner-discipline, baton-discipline |
| 92 | 2026-05-26 | BACKLOG entries authored from current-state grep without scanning Closed history can mis... | planner-discipline, backlog-discipline |
| 93 | 2026-05-27 | Schema migrations shipped in `src/db.py` are not applied to production DB by code commit... | schema-discipline, forge-architecture |

## 5. Batch split: Step 2a IDs and Step 2b IDs

**Step 2a batch (entries 1-18):** `[58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]`

**Step 2b batch (entries 19-36):** `[76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93]`

## 6. Interpretation

- **Ingested count:** Exactly 36, matching the pre-cycle diagnostic's parser count. All 36 LESSONS.md entries were new (zero heading overlap with the 57 existing DB entries).
- **Duplicates:** `duplicates_marked_count = 0`. The deterministic `detect_duplicates()` found no cross-entry duplicates. This is expected given the headings are all distinct and cover different topics.
- **Updated/unchanged:** Both 0, confirming all 36 entries were genuinely new ingestions (no heading matches to update or skip).
- **Anomalies:** None. The cycle ran cleanly — 36 in, 0 updated, 0 unchanged, 0 duplicates. Entry IDs are contiguous (58-93) starting right after the prior max_entry_id of 57.

## 7. Output Receipt

- **Agent:** Forge Lessons Agent
- **Step:** 1
- **Status:** Complete
- **What Was Done:** Ran `run_full_lessons_cycle`, captured ingestion deltas, inspected and split `needs_classification` queue for Steps 2a/2b
- **Files Deposited:** `knowledge/research/lessons-forge-cycle-step1-2026-05-27.md`
- **Files Created or Modified:** `lessons-forge.db` (committed)
- **Decisions Made:** Batch split — entries 58-75 (Step 2a) / entries 76-93 (Step 2b)
- **Flags for CEO:** None. Ingestion count is exactly 36 as expected. `duplicates_marked_count` is 0 — no cross-entry duplication detected.
- **Flags for Next Step:** Step 2a loads the first-18 batch (IDs 58-75) from this deposit Section 5
