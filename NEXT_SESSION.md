# Lessons Forge — Next Session Baton

**Last session:** 2026-05-27
**Last session focus:** Plan B shipped (`## Plan Authoring Checklist` section + Rules 42-44 + DPE technique + archived narratives). Plan A queued for next session.

---

## In-flight threads (carry forward)

### Plan A — Bellows Operational Workarounds subsection (Plan B's sibling)

Plan A is the second half of the 2026-05-27 Gate 1 Phase 2B work. Scope: new dedicated PLANNER_TEMPLATE subsection under `## Bellows Execution Model` (or as a peer under Orchestration Plan Rules — SA decides during blueprint) collecting 14-15 Bellows operational workaround rules. Each rule cross-referenced to a Bellows BACKLOG entry where applicable. Framed as deprecatable wholesale when daemon fixes ship.

**Source proposals (status='accepted', status_updated_at='2026-05-27' in lessons-forge.db):** 65, 68, 70, 71, 73, 77, 78, 81, 82, 85, 89, 94. Plus proposal **74** folded in from Plan B's residual (SA-decision during Plan B blueprint authoring — "mid-plan communication via verdict text not blueprint edits" overlaps with proposal 85's caching workaround scope, so joint authoring is the right shape).

Final count target: 13 base + 1 folded = 14 rules. Same SA → DEV → QA orchestration via Bellows.

**Pre-blueprint CEO decisions to surface at session start:**
1. Subsection placement: under `## Bellows Execution Model` (peer to other Bellows-specific subsections) vs new top-level `## Bellows Operational Workarounds`. Current lean: under Bellows Execution Model — it's daemon-specific.
2. Cross-reference format: each workaround rule footer pointing to BACKLOG entry (e.g., `Workaround for: bellows/knowledge/BACKLOG.md "Orphan-guard renormalization fires on wrong step" (added 2026-05-27)`). Decide on consistent format up front.
3. Subsection numbering: continuous with Orchestration Plan Rules (would be 45-58) OR independent scope (matches Plan B's checklist choice of independent 1-12). Lean toward independent scope to match Plan B precedent and signal deprecate-wholesale semantics.

---

## Lessons surfaced this session (candidates for next Forge cycle)

1. **QA prompt language ambiguity — "Run the block manually" vs canonical block execution.** Plan B's Step 3 QA prompt said "author the canonical QA self-check Python block per Rule 20 with placeholders filled. Include the block in the QA report. Run the block manually (read PLANNER_TEMPLATE.md section by section against blueprint Markdown) and report PASS/FAIL per check." The QA agent interpreted "manually" as "do the verification manually instead of running the block" — built a verbatim-match table for Check 10, omitted the canonical Python block. Rule 20 banner missing, gate fired. Fix shape: revise plan-side QA template to say "Include the canonical Python block verbatim with placeholders filled, run it via `python3`, and capture stdout in the QA report." Remove the word "manually" entirely. Plan-side patch candidate for next session.

2. **PLANNER_TEMPLATE version drift between session start and SA dispatch.** Plan B Context expected v4.53 (read at session start). SA at Step 1 read v4.54 (was bumped earlier in same day by a separate plan). SA caught and flagged; no impact. But pattern is worth tracking: when session opens with stale memory of template version, plans Context section can mis-reference. Phase 1.5 should re-verify version line before authoring any Context section that names the version.

3. **rule_22_verification (c) enumerative-table FPs — new gate hazard.** Filed as Bellows BACKLOG entry (top of Open as of 2026-05-27). 31 FPs on Step 3 QA. Sibling pattern with 2026-05-22 hedging-detector domain-term FPs. Both gates parse content uniformly without scoping to verification regions. Section-scoping fix (Option a in BACKLOG) is symmetric with 2026-05-24 (c) greenness fix shipped earlier.

---

## DB state

`lesson_proposals` table:
- `status='accepted'`, `status_updated_at='2026-05-27'`: **33 rows** (the Gate 1 accepted set, of which 16 are now structurally accounted for via Plan B). The 17 remaining accepted rows (Plan A scope + the residual 4 actionable rules + DPE technique) are pending status advancement to `implemented`.
- Status advancement to `implemented` deferred to a later session (Gate 2d-style housekeeping). Plan A will ship first; status advancement when both Plan A and Plan B are fully shipped.

---

## Operational notes for next session

- Daemon currently running at `bellows.py @ b9246d0` (post-2026-05-27 session-wrap; latest BACKLOG entries baked into BACKLOG.md but no code change shipped this session — daemon restart NOT required for next session).
- All three repos clean at session end. Submodule status: space-prefix on anvil, bellows, lessons-forge.
- Plan B left v4.54 as the published version. Plan A should NOT bump the version in the plan itself; version bump on session-wrap.
- Phase 1.5 must include: this baton, plus the current Plan B deposit set (`PLANNER_TEMPLATE.md` Plan Authoring Checklist section, archived-narratives file, Plan B QA report) for orientation context.

---

## Bellows BACKLOG additions this session (1 entry)

`rule_22_verification` (c) sub-check false positives on enumerative tables in QA reports. Gate parses every markdown table demanding per-row Status columns; QA reports legitimately contain non-verification enumerative tables. Reproduced on plan-authoring-checklist Step 3 with 31 FPs. Fix shape options: (a) section-scoping (symmetric with 2026-05-24 greenness fix), (b) status-cell heuristic, (c) opt-out marker. Filed at top of `bellows/knowledge/BACKLOG.md` Open section.
