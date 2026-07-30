# Gate 1 Route — Session 12 QA (2026-07-29)

## Verification Table

| # | Claim | Status | Measured value | DB source | Evidence |
|---|-------|--------|----------------|-----------|----------|
| 0 | Deliverable verification (Rule 17) | ✅ | Deposit exists, committed at 967f0a5, porcelain empty; Receipt items (iii) backup path+verification and (iv) B/C read-backs all present | git log + git status | db-invariants.txt ROW-0 |
| 1 | All 8 routed with correct fields | ✅ | 8 rows: each route=codify, status=proposed, confidence=high, category and target_artifact match disposition table per row (198/199 instrumentation, rest governance_rule) | canonical DB read-only | db-invariants.txt ROW-1 |
| 2 | No status moved | ✅ | (a) All 8 targets status=proposed; (b) distribution byte-identical to before-item (1): implemented 137, superseded 28, rejected 15, proposed 10, reference 7, stale 3 | canonical DB read-only | db-invariants.txt ROW-2 |
| 3 | Blast radius total (same-instant) | ✅ | total=70, outside-range=62, identity 70==62+8; rise over before-item (2): 8 | canonical DB read-only | db-invariants.txt ROW-3 |
| 4 | Blast radius outside range | ✅ | 62, unchanged from before-item (4) = 62 | canonical DB read-only | db-invariants.txt ROW-4 |
| 5 | Parked pair 191/192 untouched | ✅ | 191: proposed, codify, DRAFTING_CYCLE.md; 192: proposed, codify, PLANNER_TEMPLATE.md — unchanged from before-item (4b) | canonical DB read-only | db-invariants.txt ROW-5 |
| 5b | Classification unchanged | ✅ | get_unclassified_entries = [], unchanged from before-item (3) = [] | canonical DB read-only | db-invariants.txt ROW-5b |
| 6 | Full suite regression | ✅ | 55 passed | pytest src/ -v | pytest_targeted.txt |
| 7 | Gate-2 target artifacts unchanged | ✅ | porcelain empty, exit 0; all 3 shasum pins match authoring values; root HEAD 881ec60 matches | git status + shasum | db-invariants.txt ROW-7 |

## Evidence and Narrative

### Row 0 — Deliverable Sub-Table (Rule 17)

| Deliverable | Expected | Status | Evidence |
|-------------|----------|--------|----------|
| knowledge/development/gate-1-route-session-12-captures-2026-07-29.md | Committed, porcelain empty | ✅ | git log: 967f0a5; porcelain: empty |

Receipt item (iii): backup path `/Users/marklehn/Developer/GitHub/lessons-forge/data/backups/lessons-forge-pre-gate1-284-20260730T001726Z.db` with PRAGMA integrity_check = ok, counts match (192/200).

Receipt item (iv): B1/B2/B3/C2/C3/C4 read-backs all present with raw output in the Step 1 deposit.

### Row 1 — Raw Read-Back

```
193|185|proposed|codify|governance_rule|high|PLANNER_TEMPLATE.md
194|186|proposed|codify|governance_rule|high|DRAFTING_CYCLE.md
195|187|proposed|codify|governance_rule|high|DRAFTING_CYCLE.md
196|188|proposed|codify|governance_rule|high|PLANNER_TEMPLATE.md
197|189|proposed|codify|governance_rule|high|DRAFTING_CYCLE.md
198|190|proposed|codify|instrumentation|high|DRAFTING_CYCLE.md
199|191|proposed|codify|instrumentation|high|RULE_20_SELF_CHECK_BLOCK.md
200|192|proposed|codify|governance_rule|high|DRAFTING_CYCLE.md
```

### Row 2 — Status Distribution

(a) All 8 targets confirmed `status='proposed'` from row 1 query.

(b) Current distribution vs before-item (1):
```
implemented|137
superseded|28
rejected|15
proposed|10
reference|7
stale|3
```
Byte-identical.

### Row 3 — Same-Instant Identity

```
total_route_not_null|70
outside_range_route_not_null|62
```
Identity: 70 == 62 + 8. Rise over before-item (2): 70 - 62 = 8.

### Row 4 — Outside-Range Count

```
62
```
Before-item (4) from Step 1 Receipt: 62. Unchanged.

### Row 5 — Parked Pair

```
191|proposed|codify|DRAFTING_CYCLE.md
192|proposed|codify|PLANNER_TEMPLATE.md
```
Before-item (4b) from Step 1 Receipt: identical.

### Row 5b — Unclassified Entries

```
[]
```
Before-item (3) from Step 1 Receipt: `[]`. Unchanged.

### Row 6 — Pytest

55 collected, 55 passed. Baseline from prior QA (cycle-qa-2026-07-29.md): 55. 0 regressions. `git status --porcelain -- src/`: empty (src/ untouched).

### Row 7 — Gate-2 Target Artifacts

Porcelain: empty, exit 0.

Shasum pins (first 16 hex chars):
- DRAFTING_CYCLE.md: d8f17394c08d7dc7 matches d8f17394c08d7dc7
- PLANNER_TEMPLATE.md: 49b726447498d0c5 matches 49b726447498d0c5
- RULE_20_SELF_CHECK_BLOCK.md: c90ffb4bea0063e9 matches c90ffb4bea0063e9

Root HEAD: 881ec60 (matches authoring value 881ec60).

### Evidence File Self-Grep

- `db-invariants.txt`: `grep -c '^ROW-'` = 8 (expected 8)
- `pytest_targeted.txt`: contains `55 passed`

## Rule 20 — QA Self-Check Results

```
============================================================
Rule 20 — QA Self-Check Results
============================================================
PASSED — SELF-CHECK PASSED — all evidence files present, no hedging keywords found.
Evidence folder: /Users/marklehn/Developer/GitHub/lessons-forge/.bellows-worktrees/284/knowledge/qa/evidence/gate-1-route-session-12-captures-2026-07-29/
Files verified: 2
```

Self-grep: `grep "Rule 20 — QA Self-Check Results" <this file>` — banner present.

## Output Receipt

Status: Complete

All 9 verification rows (0, 1, 2, 3, 4, 5, 5b, 6, 7) pass.

#### Files Created or Modified

- `knowledge/qa/gate-1-route-qa-2026-07-29.md`
- `knowledge/qa/evidence/gate-1-route-session-12-captures-2026-07-29/db-invariants.txt`
- `knowledge/qa/evidence/gate-1-route-session-12-captures-2026-07-29/pytest_targeted.txt`

### Ledger Updates

#### Project Status

Gate 1 complete for the session-12 batch: 8 codify / 0 backlog / 0 reference. All 8 remain `status='proposed'` and are Gate-2-bound. The parked pair 191/192 is unharmed (both still `proposed|codify`, target artifacts unchanged).

#### Forward Register

Gate 2 owes:
- The doc+gate pairing for proposals 198 (DRAFTING_CYCLE.md section 4 defects) and 199 (RULE_20_SELF_CHECK_BLOCK.md documentation) per DRAFTING_CYCLE.md section 6.
- The un-codified 2026-07-25 subtractive-trim parent lesson (the "verify the subsumption against live data" entry) noted in CEO Context — Gate 2 can land the parent principle and proposal 195's refinement together.

#### Prompt Feedback

No prompt feedback for this step.
