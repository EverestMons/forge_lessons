# Lessons Forge — Next Session Baton

**Last session:** 2026-07-07 (Gate 2 codification + reference-status migration — plans 134 / 135)
**Last session focus:** Closed the 2026-07-06 cycle end-to-end. Gate 2 (plan 134) codified 8 rules into PLANNER_TEMPLATE (now **v4.71**) from the 13 codify-routed proposals; reference-status migration (plan 135) gave the 2 reference-routed proposals an honest terminal state. `status='proposed'` is now 0 — every proposal from the cycle is dispositioned.

---

## In-flight threads (carry forward)

### plan_lint qa_steps cross-check [NEXT UP — not started]
Guard against the plan-133 trap: warn when a QA-labeled step is absent from the `qa_steps` list, or when `qa_steps` names a non-QA step. `qa_steps` is a step-number list (gates.py:724), not a count — `qa_steps: 1` silently gated the DEV step as QA. No lint logic exists yet (grep-confirmed). Small; deposit as a Bellows plan.

### Session-end-suite evidence-file convention [CEO decision, still open]
Template ~line 593 prescribes `session-YYYY-MM-DD/pytest_session_end.txt` but no such file has ever been written anywhere. Decide the convention (and location) or drop the rule. Suite results keep getting recorded in batons instead.

### Carried from Gate 2 ratification (flagged in v4.71 changelog)
- **Workaround #3 factual tension:** verdict reasoning does NOT reach agents — the Workaround text implies it can. Diagnostic-first before correcting.
- **Classifier-side dedup:** dedup candidates against *recently-implemented* proposals, not just live template text — Gate 2 caught 2 already-covered proposals (131/135) only via manual git blame.

### FORGE_QA dispatch wiring [verify when relevant]
Gate 2 added a FORGE_QA.md evidence-source guardrail (entry 136 → existing `forge/agents/FORGE_QA.md`). Still worth confirming lessons-forge QA dispatches actually read forge's QA specialist; entry 137's plan-text contract is the reaching layer if they don't.

---

## What shipped this session (2026-07-07)

- **Plan 134 (Gate 2 codification):** 8 rules into PLANNER_TEMPLATE v4.71 — Rules 50 (Cluster-1 scope-derivation umbrella; proposals 133/134/137/143 → 1 implemented + 3 superseded) and 51 (verdict prose ≠ instruction channel), Checklist 25-28, Workaround #15 (post-activation live canary), FORGE_QA.md guardrail. 2 proposals (131/135) rejected as already-covered with blame evidence. QA 10/10 units PASS (`knowledge/qa/gate2-codification-qa-2026-07-06.md`).
- **Plan 135 (reference-status migration):** added `reference` to the `lesson_proposals.status` CHECK constraint (guarded table-rebuild migration against canonical DB), applied to proposals 140/141 (entries 132/133; fixes shipped in plans 62/63). QA 7/7 verifications PASS. First-ever reference terminal status.
- **Precursors (context):** plan 133 = Gate 1 route disposition (15/15 recorded); plan 132 halted on session-limit 429.

---

## DB state (post-Gate 2 2026-07-07)

`lesson_entries`: **137**. `lesson_proposals`: **145** — implemented 97, superseded 28, rejected 15, stale 3, **reference 2**, proposed **0**. Session-end full suite: verify at next session start.

---

## Operational notes for next session

- PLANNER_TEMPLATE at **v4.71** (was v4.70). `qa_steps` header = list of QA step numbers, NOT a count.
- LESSONS.md 2026-07-07 entries (session-limit 429, classifier disk-verification, qa_steps trap) are the last 3 entries and are **NOT yet ingested** — no classifier cycle has run since 2026-07-06. Next cycle picks them up (and will re-test the classifier dedup thread above).
- Session-end suite evidence-file convention: see In-flight threads — undecided.
