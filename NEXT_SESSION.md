# Lessons Forge — Next Session Baton

**Last session:** 2026-07-07 (Gate 1 route disposition — plans 132 halted / 133)
**Last session focus:** First route-assignment Gate 1 completed for cycle 2026-07-06. All 15 proposals dispositioned and recorded via first live `set_proposal_route()` use: 13 codify, 2 reference (entries 132/133 — fixes already shipped in plans 62/63), 0 backlog. QA verified 15/15 against canonical DB with per-row source declarations plus independent Planner re-query; zero mismatches, zero collateral writes.

---

## In-flight threads (carry forward)

### Gate 2 codification — 13 codify-routed proposals [NEXT UP]
Disposition record: `knowledge/development/gate1-dispositions-2026-07-06.md`. QA: `knowledge/qa/gate1-route-disposition-qa-2026-07-06.md`.
Authoring decisions locked at Gate 1, execution at Gate 2:
- **Cluster-1 umbrella:** entries 125/126/129/135 (proposals 133/134/137/143) consolidate into ONE scope-derivation rule with sub-bullets; mark constituent proposals per established supersede/implement pattern.
- **Entry 136 target:** existing `forge/agents/FORGE_QA.md` (created 2026-06-12, plan 8 — the "does not exist" classifier flag was stale). Verify at authoring whether lessons-forge QA dispatches actually read forge's QA specialist; if not, note that entry 137's plan-text contract is the reaching layer.
- **Entry 137:** PLANNER_TEMPLATE Plan Authoring Checklist — plan 130's per-row DB-source rule is the model.
- Dedup with git blame against LIVE PLANNER_TEMPLATE (v4.70) per 2026-06-07 discipline — flagged risks: 128 (occurrence-grep vs existing convention-string rules), 130 (verdict-prose vs existing verdict rules).
- After codification: mark 13 proposals `implemented` (or superseded within Cluster-1), decide terminal status convention for the 2 reference-routed proposals (first reference-routed items ever — no precedent; surface to CEO).

### Route-field conventions (Gate 2 candidates, not direct edits)
- Capture-time route hint convention for LESSONS.md entries (Planner writes at session wrap) — pending Gate 2 ratification.
- Route assignment criteria: first Gate 1 assigned by CEO judgment — codify observed criteria (shipped-fix → reference; generic-discipline → codify) if stable.

---

## What shipped this session (2026-07-07)

- **Plan 133 (executable-gate1-route-disposition):** 15/15 routes recorded via `set_proposal_route()` module API, QA 5/5 with per-entry detail table, independent Planner verification. Plan 132 = identical plan, halted on environmental failure (see below).
- **Session-limit 429 incident:** plan 132 step 1 never ran (`claude -p` exit 1 on Claude Code session limit); runner retry-once fired and re-hit the limit. Recovery: `verdict: stop` → re-deposit (continue would have advanced past the never-run step, Precondition Failure false). LESSONS captured; Bellows pause-and-hold candidate.
- **qa_steps semantics trap:** `qa_steps: 1` parsed as step-number list (gates.py:724), not count — step 1 (DEV) gated as QA (false-positive FAIL, CEO override A), step 2 ran without mechanical Rule 20/22 gates (full manual Planner verification performed instead). Correct form for DEV→QA: `qa_steps: 2`. LESSONS captured; plan_lint cross-check gap filed.

---

## DB state (post-Gate 1 2026-07-07)

`lesson_entries`: **137**. `lesson_proposals`: **145** — proposed 15 (all routed: 13 codify / 2 reference), implemented 89, superseded 25, rejected 13, stale 3. Session-end full suite: **40 passed**.

---

## Operational notes for next session

- PLANNER_TEMPLATE at v4.70. `qa_steps` header = list of QA step numbers, NOT a count.
- Session-end suite evidence-file convention (`session-YYYY-MM-DD/pytest_session_end.txt`, template line ~593) has no on-disk precedent anywhere — location convention undefined; suite result recorded here instead. Decide convention or drop the rule.
- LESSONS.md 2026-07-07 entries (session-limit 429, classifier disk-verification, qa_steps trap) are NOT yet ingested — next cycle picks them up.
