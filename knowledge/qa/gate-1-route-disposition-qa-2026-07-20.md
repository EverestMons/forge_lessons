# Gate 1 Route Disposition QA — Cycle 2026-07-20
**Plan:** 244 | **Step:** 2 (QA) | **Date:** 2026-07-20

## Verification Table

| # | Claim | Result | DB Source |
|---|---|---|---|
| 1 | Routes recorded exactly per CEO table (155–159 all codify) | **PASS** | canonical (ro) |
| 2 | Gate 1 changed no status (before == after identity) | **PASS** | canonical (ro) + Step 1 deposit |
| 3 | Blast radius — route-NOT-NULL count rose ≤5 | **PASS** | canonical (ro) + Step 1 deposit |
| 4 | 204 fix still holds | **PASS** | canonical (ro) |
| 5 | Template untouched | **PASS** | git -C root repo |
| 6 | Targeted tests green, selector non-vacuous | **PASS** | worktree pytest |

All rows PASS. No blockers.

---

### Row 1 — Routes Recorded

Raw output of `SELECT id, entry_id, status, route FROM lesson_proposals WHERE id BETWEEN 155 AND 159` on canonical DB:

```
155|147|proposed|codify
156|148|proposed|codify
157|149|proposed|codify
158|150|proposed|codify
159|151|proposed|codify
```

DB: `file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro`

All five proposals carry `route='codify'` and `status='proposed'`. Matches CEO disposition table exactly.

### Row 2 — Status Distribution Identity

**A0 before-snapshot (from Step 1 deposit):**

| status | count |
|---|---|
| implemented | 105 |
| proposed | 5 |
| reference | 3 |
| rejected | 15 |
| stale | 3 |
| superseded | 28 |

**Current distribution (read now):**

```
implemented|105
proposed|5
reference|3
rejected|15
stale|3
superseded|28
```

DB: `file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro`

Distributions are **identical**. No status changed. No `status='codify'` anywhere (codify is a route value, not a status). All five of {155–159} remain `status='proposed'`.

### Row 3 — Blast Radius

- **Route-NOT-NULL count BEFORE (A0 deposit):** 24
- **Route-NOT-NULL count NOW:** 29
- **Delta:** +5 (exactly 5, clean run)

All five of {155–159} carry `route='codify'` (confirmed in Row 1). Delta ≤5 holds. No proposal outside {155–159} had its route changed.

DB: `file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro`

### Row 4 — 204 Fix Still Holds

```
get_unclassified_entries() = []
```

DB: `file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro`

No unclassified entries. Stale count unchanged at 3 (proven by Row 2's status-distribution identity — `stale` is one of the distribution buckets, and the distribution is identical before and after). No proposal moved off a terminal status.

### Row 5 — Template Untouched

```
$ git -C /Users/marklehn/Developer/GitHub diff --exit-code -- PLANNER_TEMPLATE.md
EXIT_CODE=0
```

`PLANNER_TEMPLATE.md` has no changes in the root repo. Gate 1 correctly made no template edits (Gate 2's job).

### Row 6 — Targeted Tests Green

```
$ python3 -m pytest src/ -k "route or proposal" -v
15 passed, 40 deselected in 0.06s
```

Selector `-k "route or proposal"` collected **15 tests** (non-vacuous; confirmed via `--collect-only`). All 15 passed. Full suite not required for a routes-only DB-disposition plan.

---

## Rule 20 — QA Self-Check Results

**PASSED — SELF-CHECK PASSED**

---

### Ledger Updates

#### Project Status

Gate 1 for cycle 2026-07-20 is complete: all 5 proposals (155–159) dispositioned as `codify` per CEO direction; statuses unchanged at `proposed`. Gate 2 codification is pending — the three Drafting-Cycle amendments (157/158/159) must be codified coherently, with proposal 159 in its C1/walk-the-list corrected form (not the verbatim within-lens iterate-to-dry model from entry 151). Proposal 156 codifies the general grep-presence-vs-effect rule, with the existing line-1539 canary becoming its worked example.

#### Prompt Feedback

- The plan's precondition requiring the A0 before-snapshots to be present in the Step 1 deposit (not just a "Complete" Output Receipt) was the right guard — it ensures QA can independently verify the status-identity and blast-radius claims rather than trusting the DEV step's conclusion.
- The explicit instruction to diff before vs after distributions (not hardcode expected values) correctly avoids the checklist-#29 anti-pattern; the identity check is robust regardless of corpus size.
- Row 4's instruction to derive stale-count constancy from Row 2's distribution identity was an efficient design — no redundant query needed.

---

## Output Receipt

| Field | Value |
|---|---|
| **Status** | Complete |
| **Plan** | 244 — Gate 1 Route Disposition (cycle 2026-07-20) |
| **Step** | 2 (QA) |
| **Specialist** | Forge QA |
| **Date** | 2026-07-20 |
| **Files Created or Modified (Code)** | None (verification only) |
| **Files Created or Modified (Knowledge)** | knowledge/qa/gate-1-route-disposition-qa-2026-07-20.md |
| **Database Changes** | None (read-only verification) |
| **Tests Run** | 15 passed (selector: route or proposal) |
