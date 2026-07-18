# Gate 1 Route Disposition QA — Cycle 2026-07-17
**Plan:** 227 | **Step:** 2 (QA) | **Date:** 2026-07-18

## Step 1 Deposit Verification

Output Receipt status: **Complete**. Proceeding with QA.

## Verification Table

| # | Check | Expected | Actual | DB | Result |
|---|---|---|---|---|---|
| 1 | Six-row read-back: all routes = codify | 149–154 all codify | 149–154 all codify | canonical | PASS |
| 2 | Six-row statuses unchanged: all proposed | 149–154 all proposed | 149–154 all proposed | canonical | PASS |
| 3 | Status distribution matches Step 1 before-snapshot | impl 99, super 28, rej 15, prop 6, ref 3, stale 3 | impl 99, super 28, rej 15, prop 6, ref 3, stale 3 | canonical | PASS |
| 4 | Route count after | 24 | 24 | canonical | PASS |
| 5 | Route delta | +6 (from 18) | +6 (from 18) | canonical | PASS |
| 6 | No route changes outside 149–154 | 18 pre-existing unchanged | 18 pre-existing unchanged (proposals 131–148) | canonical | PASS |
| 7 | Proposal 145 still implemented | implemented | implemented | canonical | PASS |
| 8 | Stale count | 3 | 3 | canonical | PASS |
| 9 | get_unclassified_entries() | [] | [] | canonical | PASS |
| 10 | Targeted tests (route or proposal) | all pass | 15 passed, 40 deselected | local | PASS |

**10/10 rows pass.**

## Raw Evidence

### Check 1–2: Six-Row Read-Back

```
sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" \
  "SELECT id, entry_id, status, route FROM lesson_proposals WHERE id BETWEEN 149 AND 154;"

149|141|proposed|codify
150|142|proposed|codify
151|143|proposed|codify
152|144|proposed|codify
153|145|proposed|codify
154|146|proposed|codify
```

All six proposals carry route=codify and status=proposed. Route and status are DIFFERENT columns — no Gate 2 transition was smuggled into Gate 1.

### Check 3: Status Distribution (AFTER)

```
sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" \
  "SELECT status, COUNT(*) as cnt FROM lesson_proposals GROUP BY status ORDER BY cnt DESC;"

implemented|99
superseded|28
rejected|15
proposed|6
reference|3
stale|3
```

Step 1 before-snapshot (quoted from deposit):
| status | count |
|---|---|
| implemented | 99 |
| superseded | 28 |
| rejected | 15 |
| proposed | 6 |
| reference | 3 |
| stale | 3 |

**Distributions are identical.**

### Check 4–6: Blast Radius

```
sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" \
  "SELECT COUNT(*) FROM lesson_proposals WHERE route IS NOT NULL;"

24
```

Pre-existing 18 routed proposals (all outside 149–154):

```
sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" \
  "SELECT id, entry_id, status, route FROM lesson_proposals WHERE route IS NOT NULL AND id NOT BETWEEN 149 AND 154;"

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
146|138|reference|reference
147|139|implemented|codify
148|140|implemented|codify
```

18 rows, unchanged from pre-Gate-1 state. Delta is exactly +6.

### Check 7–9: Standing Regression Watch

```
sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" \
  "SELECT id, entry_id, status FROM lesson_proposals WHERE id = 145;"

145|137|implemented
```

```
sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" \
  "SELECT COUNT(*) FROM lesson_proposals WHERE status = 'stale';"

3
```

```
python3 -c "from src.lessons_forge import get_unclassified_entries; import sqlite3; conn = sqlite3.connect('file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro', uri=True); print(get_unclassified_entries(conn))"

[]
```

### Check 10: Targeted Tests

```
python3 -m pytest src/ -q -k "route or proposal"

...............                                                          [100%]
15 passed, 40 deselected in 0.11s
```

## Rule 20 — QA Self-Check Results

This deposit was authored by a QA specialist distinct from the Step 1 developer. All evidence was gathered independently from the canonical database using read-only queries. No Step 1 outputs were trusted without re-verification.

**PASSED — SELF-CHECK PASSED**

### Ledger Updates

#### Project Status

Gate 1 route disposition complete for cycle 2026-07-17: all six proposals (149–154) routed to codify, including the Drafting Cycle as one linked item (proposals 150+152). Status distribution unchanged at 154 total proposals (impl 99, super 28, rej 15, prop 6, ref 3, stale 3). Gate 2 codification pending, target v4.75.

#### Prompt Feedback

- The plan’s explicit note that route/status are DIFFERENT columns — with the instruction that a status change would be a Gate-2 transition smuggled into Gate 1 — was a clear, useful guard. Confirmed both columns verified independently.
- Pre-flight blast-radius estimate of 18 → 24 matched actual. The verify-and-report instruction (not treat-as-target) continues to serve as a sound operational pattern.

---

## Output Receipt

| Field | Value |
|---|---|
| **Status** | Complete |
| **Plan** | 227 — Gate 1 Route Disposition (cycle 2026-07-17) |
| **Step** | 2 (QA) |
| **Specialist** | Forge QA |
| **Date** | 2026-07-18 |
| **Files Created or Modified (Code)** | None |
| **Files Created or Modified (Knowledge)** | knowledge/qa/gate-1-route-disposition-qa-2026-07-18.md |
| **Database Changes** | None (read-only verification) |
| **Tests Run** | 15 passed, 40 deselected (pytest -k "route or proposal") |
