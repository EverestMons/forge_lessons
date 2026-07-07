# Learning-Loop Routing & Cadence Audit
**Date:** 2026-07-06 | **Plan:** diagnostic-127 | **Status:** complete

---

## Task 1 — Channel State

### Total lesson_entries

123 entries in `lesson_entries` table.

### Unclassified Work List

Invoked `get_unclassified_entries(conn)` per Orchestration Rule #47 (`src/lessons_forge.py:205-229`).

- **Count:** 0
- **Entry IDs:** [] (empty list)
- **Interpretation:** Every ingested entry has at least one non-stale proposal. The classification queue is fully drained.

### Entry Date Range

- **Earliest entry_date:** 2026-04-14
- **Latest entry_date:** 2026-06-06

### Most Recent Cycle Activity

| Metric | Value | Days Elapsed (from 2026-07-06) |
|---|---|---|
| Last ingestion (`MAX(ingested_at)`) | 2026-06-06T21:34:34+00:00 | 30 |
| Last proposal creation (`MAX(proposed_at)`) | 2026-06-06T22:13:05+00:00 | 30 |
| Last status update (`MAX(status_updated_at)`) | 2026-06-08T14:40:16+00:00 | 28 |

**Finding:** The learning loop has been dormant for 28-30 days. No new entries have been ingested and no proposals have been created or dispositioned since the cycle-16 batch (2026-06-06/08). Any lessons captured in LESSONS.md since 2026-06-06 have not been ingested.

---

## Task 2 — Routing Outcomes

### Status Breakdown

| Status | Count |
|---|---|
| implemented | 90 |
| superseded | 25 |
| rejected | 13 |
| stale | 2 |
| proposed | 0 |
| accepted | 0 |
| ambiguous | 0 |

**Total proposals:** 130

### Implemented Proposal Destinations

Destinations reconstructed from `target_artifact` column (no explicit destination/route column exists in schema):

| Destination | Count | % of Implemented |
|---|---|---|
| PLANNER_TEMPLATE.md edit | 72 | 80.0% |
| No target_artifact (unspecified) | 15 | 16.7% |
| bellows.py | 2 | 2.2% |
| runner.py | 1 | 1.1% |

### Implemented by Category

| Category | Count |
|---|---|
| governance_rule | 74 |
| structural | 6 |
| narrative | 5 |
| instrumentation | 5 |

### Destination Schema Gap — FINDING

The `lesson_proposals` schema does **not** record a destination/route column. The columns are (`src/db.py:32-47`):

```
id, entry_id, category, subcategory, suggested_action, reasoning,
confidence, status, target_layer, target_artifact, duplicate_of,
proposed_at, status_updated_at, status_updated_by
```

- **`target_artifact`** is the closest proxy for destination, but it records the *file* to edit (e.g. `PLANNER_TEMPLATE.md`), not the *routing outcome* (codify vs. backlog vs. reference). 15 of 90 implemented proposals have NULL/empty `target_artifact`.
- **`target_layer`** records `structure | governance | language | none` — this is the ADR-002 taxonomy layer, not a routing decision.
- **`status`** tracks proposal lifecycle (`proposed -> accepted -> implemented`), not where the implementation landed.
- **`subcategory`** is reserved for Phase 2 (`src/lessons_forge.py:160`, docstring: "Reserved for Phase 2; pass None in Phase 1"). It has no CHECK constraint. Using it for routing would be a semantic overload — subcategory subdivides the category taxonomy, not routing.

**Could an existing field carry a route value (`codify | backlog | reference`) without schema migration?** No. No existing column has the right semantics or sufficient constraint flexibility. A new column on `lesson_proposals` (e.g. `route TEXT CHECK(route IN ('codify', 'backlog', 'reference'))`) or a new table would require `ALTER TABLE ADD COLUMN` — a schema migration in `src/db.py:init_db()`.

**Evidence for missing routes:** Proposal 129 (entry 122, routed to Bellows BACKLOG by CEO) has `status=implemented` and `target_artifact=NULL`. The BACKLOG routing is not recorded anywhere in the DB — it was a hand-routed CEO decision that left no trace in the schema.

---

## Task 3 — Trigger Inventory

### (a) `get_unclassified_entries(conn)` count

- **File:line:** `src/lessons_forge.py:205-229`
- **What exists:** Returns `list[int]` of entry IDs needing (re)classification. Canonical work list per Rule #47. Currently returns 0.
- **What is missing:** This is a query helper, not a trigger. No code calls it on a schedule, evaluates a threshold, or fires a notification when the count exceeds N.
- **Rough cost:** Trivial to wrap in a threshold check; the query itself is production-ready.

### (b) Plans-closed-since-timestamp query against `bellows/lifecycle.db`

- **Table:** `plans` with columns `lifecycle_state` and `closed_at` (schema confirmed via `PRAGMA table_info`)
- **Supported query:** `SELECT COUNT(*) FROM plans WHERE lifecycle_state = 'closed' AND closed_at > ?`
- **Current state:** 111 closed plans; most recent closed 2026-07-03
- **What exists:** The schema fully supports a plans-closed-since query. `lifecycle_state IN ('claimed','in_progress','awaiting_verdict','closed','halted','abandoned')` with `closed_at TEXT` (ISO-8601).
- **What is missing:** No code runs this query as a trigger. No threshold, no notification, no integration with Lessons Forge cycle scheduling.
- **Rough cost:** Low — single SQL query per evaluation against an existing DB with an existing index on lifecycle_state.

### (c) timeline.md trigger mechanics

- **File:** `/Users/marklehn/Developer/GitHub/timeline.md`
- **What exists:** Fully specified trigger grammar with three shapes:
  - **Shape A — tag-count:** fires when N+ `lesson_entries` rows carry a matching tag. Required: tag, threshold, source.
  - **Shape B — evidence-count:** fires when N+ artifacts exist (DB query or filesystem glob). Required: artifact, threshold, source.
  - **Shape C — calendar-date:** fires when current date >= specified date. Required: date.
- **Trigger evaluation status:** Convention-only. The document states triggers are "read on demand via the `task review` command (when implemented in PLANNER_TEMPLATE)" — the evaluator does NOT exist as code. The `(when implemented)` parenthetical confirms no evaluator has been built.
- **Active entries:** 2 active entries (`revisit-verification-tree-2026-05-19`, `eluvian-shop-architecture-articulation`) and 1 resolved entry.
- **What is missing:** An evaluator — code that parses timeline.md entries, dispatches per trigger shape (tag-count -> lessons-forge.db query, evidence-count -> SQL or glob, calendar-date -> datetime comparison), and fires when any trigger matches.
- **Rough cost:** Medium. Requires: (1) a markdown parser for the trigger grammar, (2) query dispatch per shape, (3) integration with a periodic check. The grammar is well-specified enough to parse mechanically, but no code exists.

### (d) Candidate Hook Points for a Nudge

#### Option D1: Bellows daemon rescan loop + `notifier.py` Pushover path

- **What exists:**
  - Daemon main loop at `bellows.py:2070-2073`: `_rescan(handler)` runs every 30 seconds
  - `notifier.py`: full Pushover notification infrastructure with urgency-gated coalescing (`push()`, `_enqueue_deferred()`, named functions for plan lifecycle events)
  - Named notification functions: `notify_plan_complete`, `notify_plan_halted`, `notify_plan_skipped`, `notify_queue_empty`, `notify_failure`, `notify_verdict_request`
- **What is missing:**
  - A `notify_cycle_nudge()` function in `notifier.py`
  - Trigger evaluation logic (either inline in rescan or a parallel periodic check)
  - A cadence separate from the 30s rescan (e.g., hourly or daily) to avoid evaluating triggers 2880 times/day
- **Rough cost:** Medium. Infrastructure exists; requires adding evaluation logic + notification function + cadence control.

#### Option D2: Phase 1.5 session-start check

- **What exists:** Documented as governance discipline in PLANNER_TEMPLATE (read LESSONS, PROJECT_STATUS, etc. at session start). No code.
- **What is missing:**
  - Code to evaluate triggers at session start
  - A mechanism to surface a nudge (e.g., write to `NEXT_SESSION.md` or print to stdout)
- **Rough cost:** Low-to-Medium. Could be a Planner-side script querying `get_unclassified_entries()` + `lifecycle.db` closed-count-since. Only fires on session start, not between sessions — lacks the daemon’s periodic evaluation.

---

## Task 4 — Gap Assessment

| Candidate Change | Current Behavior | Gap | Evidence | Affected Components |
|---|---|---|---|---|
| **Route field on `lesson_proposals`** (`codify \| backlog \| reference`) | Implemented proposals have no recorded routing destination. `target_artifact` records edit target, not routing outcome. 15/90 implemented proposals have NULL target_artifact. | Routing outcome (PLANNER_TEMPLATE edit vs. BACKLOG route vs. reference archive) is not captured in the DB. Hand-routed decisions (e.g. proposal 129 -> Bellows BACKLOG) leave no trace. | `src/db.py:32-47` (schema); DB query: 15 implemented proposals with NULL target_artifact; `src/lessons_forge.py:155-202` (insert_proposal has no route param) | `src/db.py:init_db()`, `src/lessons_forge.py:insert_proposal()`, Gate 2 codification workflow, `generate_lessons_report()` |
| **Evidence-count trigger for cycle nudge** | No automatic nudge when unclassified entries accumulate or plans close without a cycle running. The 28-day dormancy gap demonstrates the failure mode. | No code evaluates `get_unclassified_entries()` count or plans-closed-since-cycle threshold on any schedule. `timeline.md` defines trigger grammar (Shapes A/B/C) but the evaluator is convention-only ("when implemented"). | `src/lessons_forge.py:205-229` (helper exists, no trigger wrapper); `bellows/lifecycle.db` plans table (closed_at column exists, no trigger query); `timeline.md:1-4` ("when implemented" parenthetical) | `src/lessons_forge.py`, `bellows/bellows.py` (rescan loop), `bellows/notifier.py`, `timeline.md` |
| **Destination column on `lesson_proposals`** (if route field finding confirms need) | `target_artifact` partially records where the implementation went, but 16.7% of implemented proposals have no target_artifact. No column distinguishes codify-to-governance vs. route-to-BACKLOG vs. archive-as-reference. | Identical to route field gap. Separated here because the diagnostic scope distinguishes capture-time route (classifier emits) from post-implementation destination (Gate 2 records). Both are absent. | `src/db.py:32-47` (schema has no destination column); DB query: `SELECT status, target_artifact FROM lesson_proposals WHERE status = 'implemented' AND target_artifact IS NULL OR target_artifact = ''` returns 15 rows | `src/db.py:init_db()`, Gate 2 codification workflow, `generate_lessons_report()`, future reporting/analytics |

---

## Output Receipt

| Field | Value |
|---|---|
| **Plan** | diagnostic-learning-loop-routing-audit-2026-07-06 |
| **Step** | 1 (SA) |
| **Status** | complete |
| **Deposit** | `knowledge/research/learning-loop-routing-audit-2026-07-06.md` |
| **Agent** | Forge Lessons Agent (diagnostic mode) |
| **Date** | 2026-07-06 |

### Ledger Updates

#### Prompt Feedback

- Lessons Forge learning loop has a 28-day dormancy gap (last cycle activity 2026-06-08, today 2026-07-06) with 0 unclassified entries — the backlog is drained but no new ingestion has occurred since 2026-06-06
- 80% of implemented proposals route to PLANNER_TEMPLATE edits; the remaining 20% route to structural fixes, reference archives, or untracked destinations — the routing outcome is NOT recorded in the DB schema
- timeline.md trigger grammar (Shapes A/B/C) is fully specified but the evaluator is convention-only — no code parses or evaluates triggers
- Two candidate hook points for a cycle nudge exist: Bellows daemon rescan loop (infrastructure ready, needs evaluation logic) and Phase 1.5 session-start check (no code, simpler but non-periodic)
