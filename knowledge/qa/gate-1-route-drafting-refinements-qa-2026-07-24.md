# QA Report — Gate 1 Route Disposition, DRAFTING_CYCLE.md Refinements (2026-07-24)

**Plan:** executable-275
**Step:** 2 (QA)
**Date executed:** 2026-07-25
**Scope:** verification + reporting only — no DB writes, no product-code changes

## Step 1 Deposit Review

Step 1 deposit at `knowledge/development/gate-1-route-drafting-refinements-2026-07-24.md` confirmed:
- Output Receipt Status: **Complete**
- 4 route writes: 187–190 NULL→codify
- 0 status mutations (all remain proposed)
- Restore point recorded

## Verification Table

| Row | Check | DB Source | Result | Evidence |
|---|---|---|---|---|
| 1 | All four routes applied (route='codify') | canonical DB (ro) | PASS | See db-invariants.txt §Row 1+2 |
| 2 | All four still status='proposed' | canonical DB (ro) | PASS | See db-invariants.txt §Row 1+2 |
| 3 | Status distribution byte-identical to Step-1 A0 before-snapshot | canonical DB (ro) | PASS | See db-invariants.txt §Row 3 |
| 4 | Blast radius: total 190, route-NOT-NULL 60 (+4 from before-count 56), outside-range 56 (unchanged) | canonical DB (ro) | PASS | See db-invariants.txt §Row 4 |
| 5 | get_unclassified_entries unchanged from A0 before-snapshot ([]) | canonical DB (ro) | PASS | See db-invariants.txt §Row 5 |
| 6 | DRAFTING_CYCLE.md + PLANNER_TEMPLATE.md + plan_lint.py unchanged | git -C root, git -C bellows | PASS | See db-invariants.txt §Row 6 |
| 7 | src/ untouched and suite green (55 passed) | own working tree | PASS | See full-suite.txt |

All 7 rows PASS. No FAIL.

## Raw Query Output

### Row 1+2 — Target read-back
```
sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" "SELECT id, entry_id, status, route FROM lesson_proposals WHERE id BETWEEN 187 AND 190 ORDER BY id;"

187|179|proposed|codify
188|180|proposed|codify
189|181|proposed|codify
190|182|proposed|codify
```

### Row 3 — Status distribution
```
sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" "SELECT status, COUNT(*) FROM lesson_proposals GROUP BY status ORDER BY COUNT(*) DESC;"

implemented|133
superseded|28
rejected|15
reference|7
proposed|4
stale|3
```
Total: 190. Byte-identical to Step-1 A0 before-snapshot (implemented 133, superseded 28, rejected 15, reference 7, proposed 4, stale 3).

### Row 4 — Blast radius
```
sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" "SELECT COUNT(*) FROM lesson_proposals;"
190

sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" "SELECT COUNT(*) FROM lesson_proposals WHERE route IS NOT NULL;"
60

sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" "SELECT COUNT(*) FROM lesson_proposals WHERE route IS NOT NULL AND id NOT BETWEEN 187 AND 190;"
56
```
Route-NOT-NULL rose by 4 (56→60). Outside-range count 56 unchanged from Step-1 A0 before-value.

### Row 5 — get_unclassified_entries
```
python3: get_unclassified_entries(conn) with conn to canonical DB (ro)
[]
```
Unchanged from Step-1 A0 before-snapshot ([]).

### Row 6 — Doctrine files unchanged
```
git -C /Users/marklehn/Developer/GitHub diff --exit-code -- DRAFTING_CYCLE.md PLANNER_TEMPLATE.md
exit code: 0

git -C /Users/marklehn/Developer/GitHub/bellows diff --exit-code -- scripts/plan_lint.py
exit code: 0
```
All exit codes 0 — DRAFTING_CYCLE.md, PLANNER_TEMPLATE.md, and plan_lint.py have no diff.

### Row 7 — src/ untouched and suite green
```
git status --porcelain -- src/
(empty)

python3 -m pytest src/ -q
.......................................................                  [100%]
55 passed in 0.13s

python3 -m pytest src/ --collect-only -q
55 tests collected in 0.01s
```
Baseline: 55 tests. Reconciliation: most recent prior QA (retire-154-advisory-qa-2026-07-16.md) recorded 55. Count unchanged.

## Rule 20 — QA Self-Check Results

```
============================================================
Rule 20 — QA Self-Check Results
============================================================
PASSED — SELF-CHECK PASSED — all evidence files present, no hedging keywords found.
Evidence folder: /Users/marklehn/Developer/GitHub/lessons-forge/.bellows-worktrees/275/knowledge/qa/evidence/gate-1-route-drafting-refinements-2026-07-24/
Files verified: 2
```

Self-grep confirmation:
```
grep "Rule 20 — QA Self-Check Results" knowledge/qa/gate-1-route-drafting-refinements-qa-2026-07-24.md
```
Banner present in this report.

### Ledger Updates

#### Project Status

Gate 1 complete for the DRAFTING_CYCLE.md-refinement cycle 2026-07-24 — 4 codify / 0 reference / 0 backlog. All four proposals (187–190) remain `status='proposed'` and are Gate-2-bound. Gate 2 owes: the §2.2/§2.5 diagnostic-mode residue sub-questions (187/N1–N3), the explicit §2 no-batch clause extending §2.7:79 and §2.6:73 (188/N4), and the two `plan_lint.py`-coupled edits — §4 last-lens-status reading (189/N5) and the §3-vs-§4 T0 `cycle_tier` regex fix (190/N6).

#### Prompt Feedback

Plan was clear. The explicit distinction between Step-1 A0 before-values and hardcoded expectations (e.g., outside-range count anchored to A0 snapshot, not a literal 56) prevented false-FAIL on resume. The worktree-aware instructions for row 6 (git -C root/bellows, not a vacuous local diff) and row 7 (own-tree src/ check) correctly guarded against the proposal-184 class of vacuous cross-tree checks. No issues encountered.

---

## Output Receipt

| Field | Value |
|---|---|
| **Plan** | executable-275 |
| **Step** | 2 (QA) |
| **Status** | Complete |
| **Checks** | 7/7 PASS |
| **Rule 20** | PASSED |
| **Evidence** | db-invariants.txt, full-suite.txt |
| **Deposit** | knowledge/qa/gate-1-route-drafting-refinements-qa-2026-07-24.md |
