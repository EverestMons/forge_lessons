# Dev Log — `needs_classification` Return-Shape Fix
**Date:** 2026-07-02 | **Plan:** 116 | **Commit:** `4235f85`

## Changes

### Change 1 — Delegate `needs_classification` to canonical helper

**Old (lines 436–444):**
```python
    # Compute needs_classification: all entry IDs minus those with duplicate proposals
    needs_classification = []
    for eid in candidate_ids:
        has_dup = conn.execute(
            "SELECT 1 FROM lesson_proposals WHERE entry_id = ? AND category = 'duplicate'",
            (eid,),
        ).fetchone()
        if not has_dup:
            needs_classification.append(eid)
```

**New (single line, same position after Step 4 loop):**
```python
    needs_classification = get_unclassified_entries(conn)
```

Also removed the unused `duplicate_entry_ids` set — grep confirmed it was only `.add()`-ed, never read.

### Change 2 — Docstring updates

**`get_unclassified_entries` — old warning:**
```
This is the canonical work list. Do NOT derive a work list from
run_full_lessons_cycle().needs_classification — it over-reports every
parsed entry.
```

**New:**
```
This is the canonical work list. As of 2026-07-02, run_full_lessons_cycle()
delegates its needs_classification field to this helper, so the two are
consistent. This helper remains the canonical source (Rule #47).
```

**`run_full_lessons_cycle` — `needs_classification` return-key description:**
```
- needs_classification: list[int] — entry IDs requiring classification,
  computed via get_unclassified_entries(conn) after duplicate-proposal
  insertion. DB-wide (not parse-scoped); matches the canonical Rule #47
  work list.
```

### Change 3 — New tests

| Test | Rationale |
|---|---|
| `test_needs_classification_excludes_dispositioned_entry` | Over-report regression: entry with `implemented` proposal must be absent from `needs_classification` on next cycle |
| `test_needs_classification_includes_stale_only_entry` | Re-queued-edit path: stale-only proposal entry must still appear |
| `test_needs_classification_plus_duplicates_equals_total` | Fresh-DB invariant: `len(needs_classification) + duplicates_marked_count == total parsed` |

## Full Suite Tail (verbatim)

```
src/test_lessons_forge.py::test_run_full_lessons_cycle_fresh PASSED      [ 72%]
src/test_lessons_forge.py::test_run_full_lessons_cycle_with_duplicates PASSED [ 75%]
src/test_lessons_forge.py::test_run_full_lessons_cycle_idempotent PASSED [ 79%]
src/test_lessons_forge.py::test_needs_classification_excludes_dispositioned_entry PASSED [ 82%]
src/test_lessons_forge.py::test_needs_classification_includes_stale_only_entry PASSED [ 86%]
src/test_lessons_forge.py::test_needs_classification_plus_duplicates_equals_total PASSED [ 89%]
src/test_lessons_forge.py::test_generate_lessons_report_empty PASSED     [ 93%]
src/test_lessons_forge.py::test_generate_lessons_report_multi_category PASSED [ 96%]
src/test_lessons_forge.py::test_generate_lessons_report_writes_file PASSED [100%]

============================== 29 passed in 0.21s ==============================
```

### Output Receipt

| Field | Value |
|---|---|
| **Status** | Complete |
| **Commit** | `4235f85` |
| **Tests** | 29 passed, 0 failed |
| **Files changed** | `src/lessons_forge.py`, `src/test_lessons_forge.py` |
| **Pre-existing tests modified** | None (additions only) |

### Ledger Updates

#### Prompt Feedback

No prompt feedback this session.
