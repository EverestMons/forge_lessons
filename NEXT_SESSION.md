# Lessons Forge — Next Session Baton

**Last session:** 2026-07-06 (learning-loop fixes + cycle run — plans 127, 128/130, 131)
**Last session focus:** Diagnostic-127 audited learning-loop routing and cadence (28-day dormancy, no routing capture). Shipped the route column (plan 128, corrected QA via plan 130) and ran the first cycle since 06-06 (plan 131): 14 new + 1 re-queued entries ingested, 15 classified, all proposals `status='proposed'` with `route=NULL`.

---

## In-flight threads (carry forward)

### Gate 1 disposition — 15 proposals from cycle 2026-07-06 [NEXT UP]
Report: `reports/lessons-report-2026-07-06.md`. Classifications summary: `knowledge/development/classifications-summary-2026-07-06.md` (seven-cluster synthesis). First Gate 1 with route assignment available — record `codify | backlog | reference` per disposition via `set_proposal_route(conn, proposal_id, route)`.
Classifier flags to weigh at disposition:
- Cluster 1 consolidation candidate: entries 125/126/129/135 all prescribe "derive scope mechanically, not by hand" — consider one umbrella Gate 2 rule.
- Entry 136 targets `FORGE_QA.md`, a specialist file that does NOT exist yet (carried gap since 06-06 cycle) — Gate 2 either authors it or re-targets.
- Dedup against LIVE PLANNER_TEMPLATE (v4.70) at Gate 1, with git blame on cited lines (2026-06-07 discipline) — classifier does not dedup.

### Route-field conventions (Gate 2 candidates, not direct edits)
- Capture-time route hint convention for LESSONS.md entries (Planner writes at session wrap) — pending Gate 2 ratification.
- Entry 137's evidence-source contract for DB-out-of-git QA steps — Plan Authoring Checklist candidate (plan 130's per-row DB-source rule is the model).

---

## What shipped this session (2026-07-06)

- **diagnostic-127** — learning-loop routing & cadence audit. Findings: ingestion (not classification) was the dormancy bottleneck; no routing capture in schema; timeline.md trigger grammar has no evaluator.
- **Route column (128 + 130):** `route TEXT CHECK(codify|backlog|reference)` on `lesson_proposals`, PRAGMA-guarded ALTER migration, `insert_proposal(route=...)` + `set_proposal_route()`, conditional report render. Commit `643e9e7`. Plan 128 halted at QA (evidence-source substitution — QA presented fresh-init_db PRAGMA as canonical); plan 130 superseded with corrected verification. Canonical DB migrated during plan 131 Step 1 (route at PRAGMA index 14, verified).
- **Cycle 2026-07-06 (131):** entries 123-137 classified (12 governance_rule / 2 structural / 1 instrumentation, all high). Post-cycle DB: 137 entries, 145 proposals (15 proposed, 89 implemented, 25 superseded, 13 rejected, 3 stale). QA 11/11 with per-row DB-source declarations.
- **Cross-project:** bellows cycle-nudge trigger (plan 129) fires on plans-closed-since-`MAX(ingested_at)` ≥ 10 — live-canary green (fired on 114 at daemon restart). Suppressed until ingestion advances; this cycle's ingestion advanced it, so the counter is reset as of 2026-07-06.

---

## DB state (post-cycle 2026-07-06)

`lesson_entries`: **137**. `lesson_proposals`: **145** — proposed 15, implemented 89, superseded 25, rejected 13, stale 3. `get_unclassified_entries(conn)` = []. Route column live; all values NULL pending Gate 1.

---

## Operational notes for next session

- PLANNER_TEMPLATE at v4.70 (Rules through #49, Checklist through #24, Scope blocks + plan_lint contract in force).
- Route assignment criteria are NOT codified — Gate 1 assigns by CEO judgment this first time; observe and codify at Gate 2.
- LESSONS.md 2026-07-06 entries (136, 137) are already ingested and classified — do not re-capture at next wrap.
