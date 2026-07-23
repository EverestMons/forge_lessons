# Gate 1 Route Disposition QA — cycle 2026-07-22

**Plan:** executable-258 | **Step:** 2 (QA) | **Date:** 2026-07-23

## Rule 20 — QA Self-Check Results

**PASSED — SELF-CHECK PASSED**

## Verification Table

| # | Check | Result | DB Source |
|---|---|---|---|
| 1 | All fifteen dispositions applied | **PASS** | canonical (`lessons-forge.db?mode=ro`) |
| 2 | Fourteen codify proposals still `status='proposed'` | **PASS** | canonical |
| 3 | Proposal 183 terminal status landed | **PASS** | canonical |
| 4 | Status distribution matches target | **PASS** | canonical |
| 5 | Blast radius within bounds | **PASS** | canonical |
| 6 | No proposal outside 172-186 changed | **PASS** | canonical |
| 7 | `PLANNER_TEMPLATE.md` unchanged | **PASS** | root repo git |
| 8 | `src/` untouched and suite green | **PASS** | canonical + pytest |
| 9 | `get_unclassified_entries` returns `[]` | **PASS** | canonical |

### Check 1 — All fifteen dispositions applied

```
sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" \
  "SELECT id, entry_id, status, route FROM lesson_proposals WHERE id BETWEEN 172 AND 186 ORDER BY id;"
```

```
172|164|proposed|codify
173|165|proposed|codify
174|166|proposed|codify
175|167|proposed|codify
176|168|proposed|codify
177|169|proposed|codify
178|170|proposed|codify
179|171|proposed|codify
180|172|proposed|codify
181|173|proposed|codify
182|174|proposed|codify
183|175|reference|reference
184|176|proposed|codify
185|177|proposed|codify
186|178|proposed|codify
```

Fourteen rows show `route='codify'`, one row (183) shows `route='reference'`. Matches disposition table exactly. **PASS.**

### Check 2 — Fourteen codify proposals still `status='proposed'`

From the same query above: proposals 172-182, 184-186 all show `status='proposed'`. None at a non-`proposed` status. **PASS.**

### Check 3 — Proposal 183 terminal status landed

```
sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" \
  "SELECT id, status, status_updated_by, status_updated_at FROM lesson_proposals WHERE id=183;"
```

```
183|reference|ceo|2026-07-23T16:08:21Z
```

`status='reference'`, `status_updated_by='ceo'`, `status_updated_at` non-NULL. Route and status both present. **PASS.**

### Check 4 — Status distribution matches target

```
sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" \
  "SELECT status, COUNT(*) FROM lesson_proposals GROUP BY status ORDER BY COUNT(*) DESC;"
```

```
implemented|119
superseded|28
rejected|15
proposed|14
reference|7
stale|3
```

Total: 186. Matches target exactly: `proposed 14, reference 7, implemented 119, superseded 28, rejected 15, stale 3`. **PASS.**

Reconciliation with Step 1 A0 before-snapshot: Step 1 reported `proposed 15 / reference 6` before writes. Movement: `proposed −1`, `reference +1`. Fresh run (not resume). **PASS.**

### Check 5 — Blast radius

```
sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" \
  "SELECT COUNT(*) FROM lesson_proposals;"
  -- 186

sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" \
  "SELECT COUNT(*) FROM lesson_proposals WHERE route IS NOT NULL;"
  -- 56

sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" \
  "SELECT COUNT(*) FROM lesson_proposals WHERE status='reference';"
  -- 7
```

- Total proposals: **186** (unchanged).
- Route-NOT-NULL: **56** (Step 1 before-count: 41, rose by 15 — exactly 15). **PASS.**
- `status='reference'`: **7** (before: 6, rose by 1). **PASS.**

### Check 6 — No proposal outside 172-186 changed

```
sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" \
  "SELECT COUNT(*) FROM lesson_proposals WHERE route IS NOT NULL AND id < 172;"
  -- 41

sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" \
  "SELECT COUNT(*) FROM lesson_proposals WHERE status='reference' AND id < 172;"
  -- 6
```

Route-NOT-NULL for id < 172: **41** (matches Step 1 A0 before-total). Reference for id < 172: **6** (the pre-existing 140/141/146/161/164/169). No unscoped writes. **PASS.**

### Check 7 — `PLANNER_TEMPLATE.md` unchanged

```
git -C /Users/marklehn/Developer/GitHub diff --exit-code -- PLANNER_TEMPLATE.md
```

Exit code: **0**. No diff. **PASS.**

### Check 8 — `src/` untouched and suite green

```
git -C /Users/marklehn/Developer/GitHub/lessons-forge status --porcelain -- src/
```

(empty — no changes)

```
python3 -m pytest src/ -q
```

```
.......................................................                  [100%]
55 passed in 0.09s
```

```
python3 -m pytest src/ --collect-only -q
```

```
55 tests collected
```

Baseline reconciliation: prior QA (cycle-qa-2026-07-22) recorded 55. Current: 55. 0 regressions. **PASS.**

### Check 9 — `get_unclassified_entries` returns `[]`

```python
from src.lessons_forge import get_unclassified_entries
conn = sqlite3.connect('file:/.../lessons-forge.db?mode=ro', uri=True)
result = get_unclassified_entries(conn)
# []
```

Empty list. Proposal 183 (`status='reference'`) keeps its entry classified. **PASS.**

---

### Output Receipt

| Field | Value |
|---|---|
| Plan | executable-258 |
| Step | 2 (QA) |
| Status | **Complete** |
| Checks | 9/9 PASS |
| Proposals verified | 15 (14 codify, 1 reference) |
| Status distribution | implemented 119, superseded 28, proposed 14, rejected 15, reference 7, stale 3 (total 186) |
| Route-NOT-NULL | 56 (before 41, +15) |
| Test suite | 55 passed, 0 regressions (baseline 55) |

### Ledger Updates

#### Project Status

Gate 1 complete for cycle 2026-07-22 — 14 codify / 1 reference / 0 backlog. The fourteen codify proposals remain `proposed` (Gate-2-bound). Proposal 183 ("read the record before deriving") is terminal at `reference` — the rule is already codified in the Drafting Cycle's integration-vs-record pass. Gate 2 owes the execute-before-deposit cluster [172/173/178/179], the halted-triage pair [174/175], the #26 extension [178], the path-role split [184], and the conformance pass [185].

#### Prompt Feedback

The Step 2 verification matrix was well-structured with clear pass/fail criteria and DB-source requirements. The vacuous-pass warning on Check 7 (PLANNER_TEMPLATE.md via root repo git, not worktree) correctly prevented a false pass — running `git -C` against the root repo is the right approach. The before-snapshot reconciliation in Check 4 (requiring cross-reference to Step 1's A0 deposit) ensures resume-invariant verification rather than assuming fresh-run deltas.
