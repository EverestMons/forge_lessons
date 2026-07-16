# Gate 1 Route Disposition QA — Cycle 2026-07-16
**Plan:** 206 | **Step:** 2 (QA) | **Date:** 2026-07-16

## Verification Table

| # | Claim | Result | DB Source |
|---|---|---|---|
| 1 | Routes recorded per CEO table: 146=reference, 147=codify, 148=codify | **PASS** | canonical (read-only) |
| 2 | Gate 1 changed no status — all three `proposed`; distribution unchanged | **PASS** | canonical (read-only) |
| 3 | Blast radius exactly +3 (15→18); no proposal outside {146,147,148} gained a route | **PASS** | canonical (read-only) |
| 4 | Proposals 98/121/130 untouched — all still `stale` | **PASS** | canonical (read-only) |
| 5 | Plan-204 regression watch: 145 `implemented`, `stale` count 3, unclassified `[]` | **PASS** | canonical (read-only) |
| 6 | Targeted tests green: 14 passed, 47 deselected (61 collected) | **PASS** | local pytest |

All queries ran against: `sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro"`

---

### Check 1 — Routes Recorded Per CEO Table

```
sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" \
  "SELECT id, entry_id, status, route FROM lesson_proposals WHERE id IN (146,147,148);"
```

Raw output:
```
146|138|proposed|reference
147|139|proposed|codify
148|140|proposed|codify
```

All three routes match the CEO disposition table exactly. All three remain `status=proposed` (not `reference` — route and status are distinct columns).

---

### Check 2 — Status Distribution Unchanged

```
sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" \
  "SELECT status, COUNT(*) as cnt FROM lesson_proposals GROUP BY status ORDER BY status;"
```

Raw output:
```
implemented|97
proposed|3
reference|2
rejected|15
stale|3
superseded|28
```

Matches the expected distribution: `implemented 97, proposed 3, reference 2, rejected 15, stale 3, superseded 28`. Gate 1 changed no statuses.

---

### Check 3 — Blast Radius

```
sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" \
  "SELECT COUNT(*) FROM lesson_proposals WHERE route IS NOT NULL;"
```

Raw output:
```
18
```

Total is 18: 15 pre-existing from the 2026-07-06 Gate 1 cycle + 3 new from this cycle. Delta is exactly +3.

Full list of proposals with routes (confirming no proposal outside {146,147,148} was modified):

```
sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" \
  "SELECT id, entry_id, status, route FROM lesson_proposals WHERE route IS NOT NULL ORDER BY id;"
```

Raw output:
```
131|123|rejected|codify
132|124|implemented|codify
133|125|implemented|codify
134|126|superseded|codify
135|127|rejected|codify
136|128|implemented|codify
137|129|superseded|codify
138|130|implemented|codify
139|131|implemented|codify
140|132|reference|reference
141|133|reference|reference
142|134|implemented|codify
143|135|superseded|codify
144|136|implemented|codify
145|137|implemented|codify
146|138|proposed|reference
147|139|proposed|codify
148|140|proposed|codify
```

Proposals 131-145 are unchanged from the dev log. Only 146-148 are new.

---

### Check 4 — Proposals 98/121/130 Untouched

```
sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" \
  "SELECT id, entry_id, status, route FROM lesson_proposals WHERE id IN (98,121,130);"
```

Raw output:
```
98|93|stale|
121|116|stale|
130|123|stale|
```

All three remain `stale` with no route assigned, per CEO decision.

---

### Check 5 — Plan-204 Regression Watch

**Proposal 145:**
```
sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" \
  "SELECT id, entry_id, status, route FROM lesson_proposals WHERE id=145;"
```

Raw output:
```
145|137|implemented|codify
```

Still `implemented`.

**Stale count:** 3 (from Check 2 distribution above).

**Unclassified entries:**
```python
import sqlite3
conn = sqlite3.connect('/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db')
from src.lessons_forge import get_unclassified_entries
result = get_unclassified_entries(conn)
print(repr(result))
# Output: []
```

All three indicators healthy — plan-204 fix holds.

---

### Check 6 — Targeted Tests

```
python3 -m pytest src/ -v -k "route or proposal"
```

Raw output:
```
============================= test session starts ==============================
platform darwin -- Python 3.9.6, pytest-8.4.2, pluggy-1.6.0 -- /Library/Developer/CommandLineTools/usr/bin/python3
cachedir: .pytest_cache
rootdir: /Users/marklehn/Developer/GitHub/lessons-forge
plugins: anyio-4.12.1, xdist-3.8.0, timeout-2.4.0, cov-7.0.0
collecting ... collected 61 items / 47 deselected / 14 selected

src/test_lessons_forge.py::test_lesson_proposals_schema PASSED           [  7%]
src/test_lessons_forge.py::test_ingest_stale_proposals PASSED            [ 14%]
src/test_lessons_forge.py::test_insert_proposal_basic PASSED             [ 21%]
src/test_lessons_forge.py::test_insert_proposal_minimal_fields PASSED    [ 28%]
src/test_lessons_forge.py::test_insert_proposal_with_valid_route[codify] PASSED [ 35%]
src/test_lessons_forge.py::test_insert_proposal_with_valid_route[backlog] PASSED [ 42%]
src/test_lessons_forge.py::test_insert_proposal_with_valid_route[reference] PASSED [ 50%]
src/test_lessons_forge.py::test_insert_proposal_route_none_default PASSED [ 57%]
src/test_lessons_forge.py::test_insert_proposal_invalid_route_raises PASSED [ 64%]
src/test_lessons_forge.py::test_route_check_constraint_rejects_invalid_sql PASSED [ 71%]
src/test_lessons_forge.py::test_migration_adds_route_to_pre_existing_db PASSED [ 78%]
src/test_lessons_forge.py::test_set_proposal_route_persists PASSED       [ 85%]
src/test_lessons_forge.py::test_set_proposal_route_invalid_raises PASSED [ 92%]
src/test_lessons_forge.py::test_report_renders_route_where_present PASSED [100%]

====================== 14 passed, 47 deselected in 0.03s =======================
```

14 passed (of 61 collected), 0 failures. Baseline reference: 61 total tests.

---

## Rule 20 — QA Self-Check Results

**PASSED — SELF-CHECK PASSED**

---

### Ledger Updates

#### Project Status

Gate 1 2026-07-16 complete: 3 proposals dispositioned — 2 codify (147, 148), 1 reference (146); proposals 98/121/130 left stale per CEO decision; plan-154 advisory retirement queued separately; Gate 2 codification pending.

#### Prompt Feedback

- Plan Step 2 check 3 states "SELECT COUNT(*) FROM lesson_proposals WHERE route IS NOT NULL returns 3" — actual count is 18 (15 from 2026-07-06 cycle + 3 new). The Step 1 dev log already flagged this same discrepancy. The plan's phrasing should have said "delta is exactly +3" rather than "returns 3." Consistent with the Step 1 prompt feedback about the route-count expectation.
- The expected status distribution in the plan is correct and matches the actual DB state.

---

## Output Receipt

| Field | Value |
|---|---|
| **Status** | Complete |
| **Plan** | 206 — Gate 1 Route Disposition (cycle 2026-07-16) |
| **Step** | 2 (QA) |
| **Specialist** | Forge QA |
| **Date** | 2026-07-16 |
| **Files Created or Modified (Code)** | None (verification only) |
| **Files Created or Modified (Knowledge)** | knowledge/qa/gate-1-route-disposition-qa-2026-07-16.md |
| **Database Changes** | None (read-only verification) |
| **Tests Run** | `python3 -m pytest src/ -v -k "route or proposal"` — 14 passed, 0 failed |
