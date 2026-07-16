# Lessons Report — 2026-07-16


## Summary


| Category | Count |
|---|---|
| governance_rule | 2 |
| structural | 1 |

**Total proposals:** 3


## Governance Rule


### 2026-07-07: Classifier file-existence claims must be disk-verified before disposition [tag: planner-discipline]


- **Suggested action:** Add verification discipline rule to PLANNER_TEMPLATE.md or classifier operating procedure: any classifier or report claim about filesystem state (file exists/does not exist/path moved) must be verified against disk (ls/git log) before it informs a disposition or plan shape.
- **Reasoning:** Entry explicitly proposes a documentary discipline rule: "any classifier or report claim about filesystem state is verified against disk before it informs a disposition or plan shape." The fix is a rule addition to governance files (PLANNER_TEMPLATE or specialist procedure), not a code change. The entry draws a parallel to the BACKLOG-lags-code freshness rule, reinforcing governance_rule classification. Disk-verified: FORGE_QA.md EXISTS at forge/agents/FORGE_QA.md, confirming the lesson's premise that the 2026-07-06 classifier carried a stale "file does not exist" flag.
- **Confidence:** high
- ⚠️ **Recently-implemented overlap:** proposal #127 (implemented 2026-06-08T14:40:16.228598+00:00) — tag overlap: planner-discipline; keyword overlap: discipline, planner — verify not already subsumed before codifying.
- ⚠️ **Recently-implemented overlap:** proposal #128 (implemented 2026-06-08T14:40:16.228598+00:00) — tag overlap: planner-discipline; keyword overlap: discipline, file, planner — verify not already subsumed before codifying.

### 2026-07-07: qa_steps header is a step-number list, not a count — copied convention from a degenerate example [tag: planner-discipline]


- **Suggested action:** Clarify qa_steps header semantics in PLANNER_TEMPLATE.md: qa_steps lists the step NUMBERS of QA steps (e.g., qa_steps: 2 for a DEV->QA two-step plan), not a count. Add plan_lint cross-check: lint should verify qa_steps entries against step labels and warn when a step labeled QA is absent from the list.
- **Reasoning:** Entry reports a convention error where qa_steps was misread as a count instead of a step-number list, causing Rule 20 gating to apply to the wrong step. The primary fix is a documentary clarification of the header's semantics in governance files — the convention was "copied from plan 130, a degenerate example that masked the semantics." A secondary plan_lint gap is noted (structural reinforcement), but the root cause is a governance documentation gap. Classified as governance_rule (documentary rule change) with the lint enhancement captured in suggested_action.
- **Confidence:** high
- ⚠️ **Recently-implemented overlap:** proposal #127 (implemented 2026-06-08T14:40:16.228598+00:00) — tag overlap: planner-discipline; keyword overlap: discipline, planner — verify not already subsumed before codifying.
- ⚠️ **Recently-implemented overlap:** proposal #128 (implemented 2026-06-08T14:40:16.228598+00:00) — tag overlap: planner-discipline; keyword overlap: discipline, planner — verify not already subsumed before codifying.

## Structural


### 2026-07-07: Session-limit 429 defeats runner retry-once — pause-and-hold needed [tag: bellows]


- **Suggested action:** Implement session-limit 429 detection in bellows runner: distinguish session-limit exhaustion from transient rate-limiting, and pause-and-hold the step (or park with a resume-after timestamp) instead of surfacing a gate failure.
- **Reasoning:** Entry describes a concrete daemon-behaviour bug: the bellows runner retry-once guard treats session-limit 429s as transient, but session-limit exhaustion persists until a fixed reset time. The proposed fix is mechanical — detect the session-limit message shape and change the runner's error-handling path. This routes to structural (Layer 1 code change). NOTE: disk-verified that this fix has already shipped in bellows/runner.py (functions _check_session_limit, _parse_session_limit_reset now exist with full session-limit handling).
- **Confidence:** high
- ⚠️ **Recently-implemented overlap:** proposal #100 (implemented 2026-06-03) — tag overlap: bellows; keyword overlap: bellows — verify not already subsumed before codifying.
- ⚠️ **Recently-implemented overlap:** proposal #105 (implemented 2026-06-03) — tag overlap: bellows; keyword overlap: bellows — verify not already subsumed before codifying.
- ⚠️ **Recently-implemented overlap:** proposal #108 (implemented 2026-06-03) — tag overlap: bellows; keyword overlap: bellows — verify not already subsumed before codifying.
- ⚠️ **Recently-implemented overlap:** proposal #110 (implemented 2026-06-03) — tag overlap: bellows; keyword overlap: bellows — verify not already subsumed before codifying.
- ⚠️ **Recently-implemented overlap:** proposal #114 (implemented 2026-06-03) — tag overlap: bellows; keyword overlap: bellows — verify not already subsumed before codifying.
- ⚠️ **Recently-implemented overlap:** proposal #117 (implemented 2026-06-03) — tag overlap: bellows; keyword overlap: bellows — verify not already subsumed before codifying.
- ⚠️ **Recently-implemented overlap:** proposal #118 (implemented 2026-06-03) — tag overlap: bellows; keyword overlap: bellows — verify not already subsumed before codifying.
- ⚠️ **Recently-implemented overlap:** proposal #119 (implemented 2026-06-03) — tag overlap: bellows; keyword overlap: bellows — verify not already subsumed before codifying.
- ⚠️ **Recently-implemented overlap:** proposal #128 (implemented 2026-06-08T14:40:16.228598+00:00) — tag overlap: bellows; keyword overlap: bellows — verify not already subsumed before codifying.
- ⚠️ **Recently-implemented overlap:** proposal #129 (implemented 2026-06-08T14:40:16.228598+00:00) — tag overlap: bellows; keyword overlap: bellows — verify not already subsumed before codifying.
