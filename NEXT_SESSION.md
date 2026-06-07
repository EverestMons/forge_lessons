# Lessons Forge — Next Session Baton

**Last session:** 2026-06-06 (cycle v2 — Gate 1 run + work-list-query root-cause fix)
**Last session focus:** Ran a fresh Gate 1 cycle. First dispatch halted at Step 1: the DB work-list query `NOT EXISTS (SELECT 1 FROM lesson_proposals p WHERE p.entry_id=e.id)` — prescribed verbatim by entry 117 and copied into every cycle plan — silently drops entries whose only proposal is `stale` (the edit-requeue state). Re-dispatched as v2 with a stale-aware helper `get_unclassified_entries(conn)`; classified the correct 9 entries; shipped clean end-to-end through Bellows (QA 4/4).

---

## In-flight threads (carry forward)

*(none in orchestration — cycle v2 closed to `Done/` through QA 4/4)*

**Next queued task: Gate 1 disposition of the 9 proposed proposals** (entries 93, 116, 117-123). Decision-heavy review — accept/reject each, then author a Gate 2 codification plan for the accepted set. This is a fresh session, not a tail-on.

---

## What shipped this session (2026-06-06 cycle v2)

- **Root-cause fix:** `get_unclassified_entries(conn)` at `src/lessons_forge.py:205` — stale-aware work list (`... AND status != 'stale'`) + unit test `test_get_unclassified_entries`. Suite 25 -> 26 green. This is now the canonical work list; consumers call the helper instead of copying SQL, killing both the over-reporting (`needs_classification` returns every parsed entry) and the stale-only undercount.
- **9 entries classified** (8 governance_rule + 1 structural), `status='proposed'`, staged for Gate 1. 7 high / 2 medium confidence, no ambiguous.
- **Report** `reports/lessons-report-2026-06-06.md`; **QA** 4/4 PASS (suite, DB invariants stale-aware, schema drift none, Rule 20 byte-exact).
- **Closed the prior baton's "1 stale row, minor anomaly, not blocking":** that was entry 93 (a real schema-migration governance_rule lesson), dropped every cycle by the buggy query. Now caught and classified. The "not blocking" framing was itself the inherited-framing failure (this batch's entry 123).
- First dispatch committed halted at `knowledge/decisions/Done/halted-executable-lessons-forge-cycle-2026-06-06.md`.

---

## CRITICAL caveats for Gate 1 / Gate 2

1. **Entry 117 (proposal 124) — codify the helper, not the quoted SQL.** 117's note text quotes the buggy no-stale-guard query. When accepted and codified into PLANNER_TEMPLATE, the rule MUST reference `get_unclassified_entries(conn)`, NOT the SQL in the entry text. Flag is persisted in proposal 124's reasoning. This is the one place a careless codification re-introduces today's bug.
2. **Entry 116 (proposal 123) is a REVISION, not net-new.** Its prior proposal 121 was implemented at the 06-03 Gate 2 (scope_check blueprint-delegation inline-file-list rule) and was re-staled this cycle by an edit to the lesson. Gate 2 must UPDATE the existing codified rule, not add a duplicate. Reconcile 123 against what 121 already placed in the template.
3. **Entry 93 (proposal 122) is effectively first-time codification.** Its prior proposal 98 was stale before 06-03 and never implemented — no existing template rule to reconcile against.

---

## On the horizon (open items, none in-flight)

### New — `run_full_lessons_cycle` `needs_classification` over-report refactor (BACKLOG candidate)
The function still returns every parsed entry in `needs_classification`. The new helper is the consumer-side fix and is sufficient for correctness, but the function's return shape is the deeper root (entry 117's "candidate code fix, separate"). File in Bellows/lessons-forge BACKLOG; not blocking.

### Recommended next reliability cut — Bellows teardown Gap 3 (dirty-tree auto-stash) [carried]
`worktree_teardown_dirty_tree` pre-check is the recurring failure source. Auto-stash of dirty non-lifecycle files before teardown cherry-pick would remove the manual commit/stash recovery cycle (~5-10 min each, documented in Workaround #8). Next Bellows reliability session.

### `lessons-forge.db` git tracking disposition [carried]
DB is tracked; de-facto commit-on-state-change. Decision still open: keep committing vs `git rm --cached` + bootstrap. Not blocking. Filed in Bellows BACKLOG (2026-05-27).

### Cross-project (not lessons-forge) [carried]
- **invoice-pulse T0.5.1 reconciliation** — next ungated step in fuel-bracket extrapolation work.
- **email-PRO -> assigned-user feature** — gated on the two Windows prod-DB queries in `email-pro-user-lookup-prod-queries-2026-06-03.sql`.

### Forge cycle #14 + canary follow-ups [carried]
`forge.db` 50MB warning, retire-the-queue decision. Not blocking. Run `bash ~/Developer/GitHub/forge/scripts/pre-scan-sync.sh` before any Mac Forge work.

---

## DB state (post-cycle-v2 2026-06-06)

`lesson_proposals` ground-truth:
- `implemented`: **84** (was 85; proposal 121/entry 116 re-staled by edit this cycle)
- `superseded`: **25**
- `rejected`: **10**
- `proposed`: **9** (NEW — entries 93, 116, 117-123; await Gate 1)
- `stale`: **2** (proposal 98/entry 93 pre-existing; proposal 121/entry 116 newly staled)
- `accepted`: **0** (clean)
- Total: **130**

`lesson_entries`: **123**. The 2 stale rows are retained as history; their entries are cleared from the work list by the new `proposed` rows.

---

## Operational notes for next session

- Daemon: bellows submodule advanced this session for verdict-artifact lifecycle commits only (no daemon code change, no restart required). Running binary `bellows.py @ 5c45295` (proc started 14:52, after the 14:19 bellows.py commit).
- PLANNER_TEMPLATE.md at **v4.59**.
- Phase 1.5 next session: this baton + PROJECT_STATUS top entry + the horizon items above. Cycle v2 fully closed; no in-flight orchestration to carry.
- **Use the helper:** any future cycle's work list comes from `get_unclassified_entries(conn)` — never from `needs_classification`, never from a hand-copied `NOT EXISTS` query.
