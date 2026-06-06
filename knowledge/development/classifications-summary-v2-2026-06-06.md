# Classifications Summary — Cycle v2 2026-06-06

## Distribution

| Category | Count |
|---|---|
| governance_rule | 8 |
| structural | 1 |
| **Total** | **9** |

| Confidence | Count |
|---|---|
| high | 7 |
| medium | 2 |

## Per-Entry Classifications

| Entry | Category | Confidence | Target |
|---|---|---|---|
| 93 | governance_rule | high | PLANNER_TEMPLATE.md |
| 116 | governance_rule | medium | PLANNER_TEMPLATE.md |
| 117 | governance_rule | high | PLANNER_TEMPLATE.md |
| 118 | governance_rule | high | PLANNER_TEMPLATE.md |
| 119 | governance_rule | medium | PLANNER_TEMPLATE.md |
| 120 | governance_rule | high | PLANNER_TEMPLATE.md |
| 121 | governance_rule | high | PLANNER_TEMPLATE.md |
| 122 | structural | high | (code — marker walk-up resolver) |
| 123 | governance_rule | high | PLANNER_TEMPLATE.md |

## Cross-Batch Synthesis

**Dominant cluster: governance_rule targeting PLANNER_TEMPLATE.md (8 of 9).** The 2026-06-06 batch is almost entirely planner-discipline and qa-discipline governance rules. This is the strongest single-category concentration seen in any cycle. Seven of the eight governance_rule entries carry the `planner-discipline` tag; two also carry `qa-discipline`; three carry `bellows-architecture` as a secondary tag.

**06-06 sub-batch (entries 119-123):** 4 governance_rule + 1 structural. All five are from a single session and all carry `planner-discipline`. Entries 120 and 121 form a tight qa-discipline pair (gate-enforced QA placement and full-suite-green enforcement). Entry 122 is the lone structural entry (worktree root resolution) — third instance of a known worktree-root-confusion class.

**Entry 117 query-correction flag:** Entry 117 prescribes the work-list query `WHERE NOT EXISTS (SELECT 1 FROM lesson_proposals p WHERE p.entry_id=e.id)` which is the non-stale-aware form. This query drops entries whose only proposal is `stale` (the edit-requeue path). The correct implementation is now `get_unclassified_entries(conn)` in `src/lessons_forge.py`, which uses `p.status != 'stale'` in the NOT EXISTS clause. **Gate 2 codification of entry 117 MUST reference the helper function, not the buggy SQL from the entry text.** The reasoning field on proposal 124 carries this flag.

**Entries 93 and 116 — re-classified after stale.** Both entries had prior proposals staled by content edits in earlier cycles. The new `proposed` proposals (122, 123) coexist with the stale rows as history. Entry 93 was previously classified as governance_rule with high confidence (consistent). Entry 116 was previously classified as governance_rule with medium confidence (consistent).

**No ambiguous entries.** All 9 entries mapped cleanly to the taxonomy. No `status='ambiguous'` proposals were needed.

## Flags for CEO

1. **Entry 117 buggy query:** the prescribed SQL in entry 117's raw_content is the non-stale-aware form. Codification at Gate 2 must use `get_unclassified_entries(conn)` instead. Flagged in proposal 124's reasoning.
2. **Heavy governance_rule concentration:** 8 of 9 entries route to PLANNER_TEMPLATE.md. Gate 2 will be a large governance edit session. Consider batching related rules (e.g., 120+121 as a qa-discipline pair).
3. **Entry 119 structural shadow:** the `pause_for_verdict` enum validation gap is framed as a governance rule (authoring-time check), but the root cause is that `gates._parse_plan_header` does not validate the enum. A structural BACKLOG item for parser-side validation may be warranted.
4. **Entry 122 structural fix:** worktree-root resolution via marker walk-up. Third instance of same class. Anvil, bellows, and forge all affected. Routes to Anvil/structural, not PLANNER_TEMPLATE.
