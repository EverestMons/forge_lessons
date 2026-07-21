# Gate 1 Route Disposition — QA Report (cycle 2026-07-21)

**Plan:** 248 | **Step:** 2 (QA) | **Date:** 2026-07-21

---

## Verification Table

| # | Check | Result | DB Source |
|---|-------|--------|-----------|
| 1 | All twelve dispositions applied | **PASS** | `lessons-forge.db` (ro) |
| 2 | Nine codify proposals still `status='proposed'` | **PASS** | `lessons-forge.db` (ro) |
| 3 | Three terminal statuses landed with `status_updated_by='ceo'` | **PASS** | `lessons-forge.db` (ro) |
| 4 | Status distribution matches absolute target | **PASS** | `lessons-forge.db` (ro) |
| 5 | Blast radius within bounds | **PASS** | `lessons-forge.db` (ro) |
| 6 | No proposal outside 160–171 changed | **PASS** | `lessons-forge.db` (ro) |
| 7 | `PLANNER_TEMPLATE.md` unchanged | **PASS** | git (root repo) |
| 8 | `src/` untouched and suite green | **PASS** | git + pytest |
| 9 | `get_unclassified_entries` returns `[]` | **PASS** | `lessons-forge.db` (ro) |

**All 9 checks PASS.**

---

## Raw Evidence

### Check 1 — All twelve dispositions applied

```
$ sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" \
  "SELECT id, entry_id, status, route FROM lesson_proposals WHERE id BETWEEN 160 AND 171 ORDER BY id;"
160|152|proposed|codify
161|153|reference|backlog
162|154|proposed|codify
163|155|proposed|codify
164|156|reference|reference
165|157|proposed|codify
166|158|proposed|codify
167|159|proposed|codify
168|160|proposed|codify
169|161|reference|backlog
170|162|proposed|codify
171|163|proposed|codify
```

Assertion: `codify` on 160/162/163/165/166/167/168/170/171 (9), `reference` on 164 (1), `backlog` on 161/169 (2). All match disposition table. **PASS.**

### Check 2 — Nine codify proposals still `status='proposed'`

From Check 1 raw output: ids 160, 162, 163, 165, 166, 167, 168, 170, 171 all show `status=proposed`. None has a non-`proposed` status. **PASS.**

### Check 3 — Three terminal statuses landed

```
$ sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" \
  "SELECT id, status, status_updated_by, status_updated_at FROM lesson_proposals WHERE id IN (161, 164, 169) ORDER BY id;"
161|reference|ceo|2026-07-21T23:05:25Z
164|reference|ceo|2026-07-21T23:05:25Z
169|reference|ceo|2026-07-21T23:05:25Z
```

All three show `status='reference'`, `status_updated_by='ceo'`, and non-NULL `status_updated_at`. Route AND status both set — durability argument holds. **PASS.**

### Check 4 — Status distribution matches absolute target

```
$ sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" \
  "SELECT status, COUNT(*) FROM lesson_proposals GROUP BY status ORDER BY COUNT(*) DESC;"
implemented|110
superseded|28
rejected|15
proposed|9
reference|6
stale|3
```

Total: 110 + 28 + 15 + 9 + 6 + 3 = **171**. Matches absolute target exactly: `proposed 9, reference 6, implemented 110, superseded 28, rejected 15, stale 3`. **PASS.**

**Delta reconciliation (fresh-run):** Step 1 A0 before-snapshot showed `proposed 12 / reference 3`. This was a fresh run. Movement: `proposed −3`, `reference +3`; all other statuses unchanged. Consistent with the three proposals (161, 164, 169) moving from `proposed` to `reference`. **PASS.**

### Check 5 — Blast radius

| Metric | Before (Step 1 A0) | After | Delta | Max Allowed | Result |
|--------|---------------------|-------|-------|-------------|--------|
| Total proposals | 171 | 171 | 0 | 0 | **PASS** |
| route-NOT-NULL | 29 | 41 | +12 | +12 | **PASS** |
| status='reference' | 3 | 6 | +3 | +3 | **PASS** |

```
$ sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" "SELECT COUNT(*) FROM lesson_proposals;"
171
$ sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" "SELECT COUNT(*) FROM lesson_proposals WHERE route IS NOT NULL;"
41
$ sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" "SELECT COUNT(*) FROM lesson_proposals WHERE status='reference';"
6
```

### Check 6 — No proposal outside 160–171 changed

```
$ sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" \
  "SELECT COUNT(*) FROM lesson_proposals WHERE route IS NOT NULL AND id < 160;"
29
$ sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" \
  "SELECT COUNT(*) FROM lesson_proposals WHERE status='reference' AND id < 160;"
3
```

Route-NOT-NULL for id < 160: **29** — equals Step 1 A0 before-total (29). No pre-existing routes altered. **PASS.**
Reference count for id < 160: **3** — equals pre-existing 140/141/146. No unscoped status write. **PASS.**

### Check 7 — `PLANNER_TEMPLATE.md` unchanged

```
$ git -C /Users/marklehn/Developer/GitHub diff --exit-code -- PLANNER_TEMPLATE.md
EXIT_CODE=0
```

Exit 0 — no diff. Codification is Gate 2. **PASS.**

### Check 8 — `src/` untouched and suite green

```
$ git -C /Users/marklehn/Developer/GitHub/lessons-forge status --porcelain -- src/
(empty — no changes)
```

```
$ python3 -m pytest src/ --collect-only -q 2>&1 | tail -1
55 tests collected in 0.01s

$ python3 -m pytest src/ -q 2>&1 | tail -1
55 passed in 0.09s
```

Baseline reconciliation: `--collect-only` reports 55 tests. Prior QA (`cycle-qa-2026-07-21.md`) recorded 55. 0 regressions. **PASS.**

### Check 9 — `get_unclassified_entries` returns `[]`

```
$ python3 -c "
import sqlite3
from src.lessons_forge import get_unclassified_entries
conn = sqlite3.connect('file:///Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro', uri=True)
result = get_unclassified_entries(conn)
print(f'get_unclassified_entries: {result}')
conn.close()
"
get_unclassified_entries: []
```

No orphaned entries. **PASS.**

---

## Rule 20 — QA Self-Check Results

All nine verification rows evaluated. Zero failures. All raw outputs deposited above with DB-source attribution.

**PASSED — SELF-CHECK PASSED**

---

### Ledger Updates

#### Project Status

Gate 1 complete for cycle 2026-07-21 (plan 248): 9 proposals routed `codify`, 1 routed `reference`, 2 routed `backlog`. The nine codify proposals (160/162/163/165/166/167/168/170/171) are Gate-2-bound and remain `status='proposed'`. Proposals 161, 164, and 169 are terminal at `status='reference'` with `status_updated_by='ceo'`. Gate 2 owes the conflict-serializability FORM decision (proposal 160: named lens vs. ACID Isolation widening) and the paired-codification strategy (163+170, 165+167).

#### Prompt Feedback

No new prompt feedback. The QA step executed all nine checks cleanly; the evidence-source rule and vacuous-pass guards (Checks 6 and 7) correctly directed queries to the canonical DB and root repo respectively.

---

## Output Receipt

- **Status:** Complete
- **Plan:** 248, Step 2 (QA)
- **Scope Adherence:** Verification and reporting only — no DB writes, no `src/` changes, no `PLANNER_TEMPLATE.md` changes.
- **Verification:** All 9 QA checks PASS.
- **Files Created (Deposits):**
  - `knowledge/qa/gate-1-route-disposition-qa-2026-07-21.md` (this file)
