# Classifications Summary — Cycle 2026-07-16 (Plan 205, re-dispatch)
**Date:** 2026-07-16 | **Plan:** 205 | **Step:** 1 (Lessons Agent)
**DB:** canonical `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db`
**Work list:** [138, 139, 140] — derived via `get_unclassified_entries(conn)` (Orchestration Rule #47)
**Overlap advisory:** 14 hits across 3 entries (all tag-equality noise per CEO Context; none informative — ignored)

---

## Classification Count

| Metric | Value |
|---|---|
| Entries classified | 3 |
| Proposals inserted | 3 (IDs 146, 147, 148) |
| All routes | NULL (Gate 1 CEO disposition) |

## Category / Confidence Distribution

| Category | Count | Confidence |
|---|---|---|
| structural | 1 | high |
| governance_rule | 2 | high |

---

## Per-Entry Classification

### Entry 138 — Session-limit 429 defeats runner retry-once
- **Proposal ID:** 146
- **Category:** structural | **Confidence:** high
- **Target layer:** structure | **Target artifact:** bellows/runner.py
- **Suggested action:** Implement session-limit 429 detection in bellows runner: distinguish session-limit exhaustion from transient rate-limiting, and pause-and-hold the step (or park with a resume-after timestamp) instead of surfacing a gate failure.
- **Reasoning:** Entry describes a concrete daemon-behaviour bug: the bellows runner retry-once guard treats session-limit 429s as transient, but session-limit exhaustion persists until a fixed reset time. The proposed fix is mechanical — detect the session-limit message shape and change the runner's error-handling path. This routes to structural (Layer 1 code change).
- **Fix-shipped note:** Disk-verified that this fix has already shipped in bellows/runner.py — functions `_check_session_limit`, `_parse_session_limit_reset` now exist with full session-limit detection, pause-and-hold, and park-with-resume-after-timestamp handling.
- **Overlap advisory:** 10 hits, all `tag overlap: bellows; keyword overlap: bellows` — tag-equality degeneration, no semantic subsumption. Ignored per CEO directive.

### Entry 139 — Classifier file-existence claims must be disk-verified
- **Proposal ID:** 147
- **Category:** governance_rule | **Confidence:** high
- **Target layer:** governance | **Target artifact:** PLANNER_TEMPLATE.md
- **Suggested action:** Add verification discipline rule to PLANNER_TEMPLATE.md or classifier operating procedure: any classifier or report claim about filesystem state (file exists/does not exist/path moved) must be verified against disk (ls/git log) before it informs a disposition or plan shape.
- **Reasoning:** Entry explicitly proposes a documentary discipline rule: "any classifier or report claim about filesystem state is verified against disk before it informs a disposition or plan shape." The fix is a rule addition to governance files, not a code change. The entry draws a parallel to the BACKLOG-lags-code freshness rule, reinforcing governance_rule classification.
- **Disk-verification (entry 139 IS this lesson):** Verified FORGE_QA.md EXISTS at `/Users/marklehn/Developer/GitHub/forge/agents/FORGE_QA.md`. The 2026-07-06 classifier's "file does not exist" flag was stale — the file has existed since plan 8 (2026-06-12). Verified via `find` against disk.
- **Overlap advisory:** 2 hits (proposals 127, 128), tag-equality on `planner-discipline`. Ignored.

### Entry 140 — qa_steps header is a step-number list, not a count
- **Proposal ID:** 148
- **Category:** governance_rule | **Confidence:** high
- **Target layer:** governance | **Target artifact:** PLANNER_TEMPLATE.md
- **Suggested action:** Clarify qa_steps header semantics in PLANNER_TEMPLATE.md: qa_steps lists the step NUMBERS of QA steps (e.g., qa_steps: 2 for a DEV->QA two-step plan), not a count. Add plan_lint cross-check: lint should verify qa_steps entries against step labels and warn when a step labeled QA is absent from the list.
- **Reasoning:** Entry reports a convention error where qa_steps was misread as a count instead of a step-number list, causing Rule 20 gating to apply to the wrong step. The primary fix is a documentary clarification of the header's semantics in governance files. A secondary plan_lint gap is noted (structural reinforcement), but the root cause is a governance documentation gap. Classified as governance_rule with the lint enhancement captured in suggested_action.
- **Overlap advisory:** 2 hits (proposals 127, 128), tag-equality on `planner-discipline`. Ignored.

---

## Cluster Synthesis (CEO Gate 1 Context)

### Cluster 1: Planner Discipline (entries 139, 140)
Both entries are verification-discipline lessons from 2026-07-07. Entry 139 targets classifier filesystem claims (verify before disposition); entry 140 targets plan-header semantic copying (verify semantics from a non-degenerate example). Both route to governance_rule edits in PLANNER_TEMPLATE.md. They are distinct rules but share the meta-pattern: generated or copied artifacts describe the world as of generation/copy time — ground truth must be verified before action.

### Cluster 2: Bellows Daemon Behaviour (entry 138)
Standalone entry. Session-limit 429 handling in the bellows runner. The fix has already shipped (disk-verified: `_check_session_limit` and `_parse_session_limit_reset` exist in bellows/runner.py). Gate 1 disposition should note the implemented status — this may qualify for `implemented` rather than needing a new codification route.
