# Dev Log — Classifier Recently-Implemented Dedup (Advisory)

**Plan:** 154 — Surface recently-implemented-proposal overlaps in classifier review
**Date:** 2026-07-09
**Step:** 1 (DEV)

---

## Detection Design

### Function: `detect_recently_implemented_overlaps(conn, entry_ids, recency_days=45)`

**Approach:** Keyword-overlap heuristic with tag-match boost.

1. **Implemented-proposal query:** `WHERE status='implemented' AND status_updated_at >= date('now', '-' || recency_days || ' days')`. Default 45-day window covers ~2 cycles.

2. **Tokenization:** `_tokenize_for_overlap(text)` extracts 3+ character alphabetic tokens, removing stop words. Applied to both entry (heading + tags) and proposal (suggested_action + reasoning + category + target_artifact) sides.

3. **Tag handling:** Entry tags are stripped of backticks (`` ` ``), lowered, and split by comma. Full compound tags (e.g. `planner-discipline`) are checked as substring matches against the proposal's concatenated text for high-signal boost.

4. **Scoring:**
   - Base score: Jaccard similarity of keyword sets (`|intersection| / |union|`)
   - Tag-match boost: if any full compound tag is found in proposal text, score is raised to at least 0.15
   - Threshold: 0.08 (recall-oriented; a false surface costs one glance, a miss costs a wasted Gate-2 cycle)

5. **Overlap reason string:** Reports tag overlaps and up to 5 keyword overlaps for reviewer context.

### Advisory-only contract

- Function performs **zero DB writes** — SELECT queries only
- `run_full_lessons_cycle` stores results in returned dict under `recently_implemented_overlaps` key but does NOT insert proposals or change statuses
- `generate_lessons_report` renders advisory lines inline under affected proposals; proposals with no overlap render identically to before

---

## Task D — Live-DB Validation (entries 123/127)

**Command:** `detect_recently_implemented_overlaps(conn, [123, 127], recency_days=60)`

**Results:**

| Entry | Caught? | Overlapping Proposals | Match Mechanism |
|---|---|---|---|
| 123 (proposal 131) | **YES** | #1, #127, #128 | tag overlap: planner-discipline; keyword overlap: discipline, planner |
| 127 (proposal 135) | **YES** | #1, #127, #128 | tag overlap: planner-discipline; keyword overlap: discipline, planner |

**Evidence:** Both entries are tagged `` `planner-discipline` ``. Multiple implemented proposals (notably #1: "Add plan-write-time discipline to PLANNER_TEMPLATE... re-read recent LESSONS.md entries tagged planner-discipline") contain the compound tag "planner-discipline" in their text, triggering the tag-match boost (score ≥ 0.15, well above the 0.08 threshold).

**Conclusion:** The recall-oriented heuristic catches the known 131/135 misses. The tag-match pathway is the primary detection mechanism for entries sharing tags with implemented proposals. Keyword Jaccard provides additional coverage for entries with distinctive heading vocabulary but no tag match.

---

## Full Suite

```
52 passed in 0.13s
```

New tests added:
- `test_overlap_recent_match` — recently-implemented overlap surfaced
- `test_overlap_old_not_surfaced` — old proposal outside recency window NOT surfaced
- `test_overlap_non_overlapping` — unrelated entry NOT surfaced
- `test_overlap_advisory_only_no_writes` — zero DB mutations verified
- `test_report_renders_overlap_advisory` — advisory line rendered in report
- `test_report_no_overlap_unchanged` — report unchanged when no overlaps
- `test_overlap_131_135_shape` — synthetic 131/135-shaped test passes

All 45 pre-existing tests remain green. 7 new tests added (52 total).

---

## Commit

**Hash:** (pending)
**Message:** `feat(forge): surface recently-implemented-proposal overlaps in classifier review (advisory) [154]`

---

### Ledger Updates

#### Prompt Feedback

- The plan's instruction to strip backticks from tags was not explicit but was necessary — live DB stores tags with backtick delimiters (`` `planner-discipline` ``). Tokenizers processing raw tag fields should account for formatting characters.
- `date('now', '-N days')` in SQLite works correctly against ISO 8601 timestamps with timezone offsets for lexicographic comparison, but this should be tested explicitly if timestamp formats ever change.

---

## Output Receipt

| Field | Value |
|---|---|
| **Plan** | 154 — Classifier recently-implemented dedup (advisory) |
| **Step** | 1 (DEV) |
| **Status** | COMPLETE |
| **Tests** | 52 passed, 0 failed, 0 regressions |
| **Task D** | PASS — entries 123/127 both caught (3 overlapping proposals each) |
| **Commit** | pending |
| **Deposits** | `knowledge/development/classifier-recently-implemented-dedup-2026-07-09.md`, `src/lessons_forge.py`, `src/test_lessons_forge.py` |
