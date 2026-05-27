# Lessons Forge — Next Session Baton

**Last session:** 2026-05-27
**Last session focus:** Both Phase 2B plans shipped. Plan A (Bellows Operational Workarounds subsection — 12 workarounds) shipped clean; Plan B (Plan Authoring Checklist + residual scatter) shipped halted-but-shipped earlier in the session.

---

## In-flight threads (carry forward)

*(none — Phase 2B complete)*

---

## On the horizon (open items, none in-flight)

### Status advancement to `implemented` (Gate 2d-style housekeeping)

All 33 accepted proposals from cycle 2026-05-27 (IDs 63–98, minus 2 rejected / 1 superseded) are now structurally accounted for via shipped governance edits — Plan A (13 proposals) + Plan B (17 actionable proposals + 3 archived narratives + 1 demoted DPE addition + the 3 already-shipped via Rule 41 supersession). DB rows still carry `status='accepted'` and need advancement to `status='implemented'`.

Suggested approach: single housekeeping plan with a Python script that flips `status` to `implemented` and sets `status_updated_at` / `status_updated_by` for all 33 rows in one transaction. Same shape as the 2026-05-19 Gate 2d advancement (18 rows). No SA blueprint needed; this is mechanical DB work.

### 4 lessons captured this session (candidates for next Forge cycle)

1. **QA prompt language ambiguity — "Run the block manually" vs canonical block execution.** From Plan B's Step 3 QA prompt. The QA agent interpreted "manually" as "do verification manually instead of running the block" — built a verbatim-match table for Check 10, omitted the canonical Python block. Fix shape: revise plan-side QA template to say "Include the canonical Python block verbatim with placeholders filled, run via `python3`, capture stdout in the QA report." Remove the word "manually" entirely. Plan A's Step 3 QA prompt avoided this by saying "Run the block via `python3`" directly — and indeed Plan A's QA ran the block correctly first time. The pattern is confirmed.

2. **PLANNER_TEMPLATE version drift between session start and SA dispatch.** Plan B Context expected v4.53 (read at session start). SA at Step 1 read v4.54 (bumped earlier in the day by a separate plan). SA caught and flagged; no impact. Phase 1.5 should re-verify version line before authoring any Context section that names the version.

3. **`rule_22_verification` (c) enumerative-table FPs.** Already filed as Bellows BACKLOG entry. 31 FPs on Plan B Step 3 QA.

4. **`ceo_flags` gate FP on "None"-as-declaration content (NEW this session).** Filed as Bellows BACKLOG entry top-of-Open. Reproduced on Plan A Step 2 DEV — the agent's textbook clean-execution declaration ("None. All SA-cited anchor lines matched verbatim. No blueprint-vs-file mismatches. No prose adjustments needed.") was treated as a flag. Same root-cause shape as the 2026-05-27 enumerative-table FPs (Plan B) and the 2026-05-22 hedging-detector domain-term FPs: gate parses field content uniformly without semantic scoping. **Pattern call-out:** three gate FPs filed this session, all the same root-cause class. When daemon-side fixes ship, the three gates (`ceo_flags`, `rule_22_verification` (c), hedging-detector) should probably share a `_is_null_declaration()` / section-scoping helper rather than three independent fixes — single audit-and-fix session would close all three.

### Forge cycle #14 + canary follow-ups

Still parked from prior sessions: `forge.db` 50MB warning, retire-the-queue decision. Not blocking.

### Forge pre-scan sync workflow before each Mac run

`bash ~/Developer/GitHub/forge/scripts/pre-scan-sync.sh` — run if any Forge work is in scope next session.

---

## DB state

`lesson_proposals` table:
- `status='accepted'`, `status_updated_at='2026-05-27'`: **33 rows** (all of cycle 2026-05-27's Gate 1 accepted set). Now ALL structurally accounted for via Plan A and Plan B shipped governance edits. Next session should run Gate 2d advancement.
- `status='implemented'`: 32 rows (unchanged this session).

---

## Operational notes for next session

- Daemon at `bellows.py @ b9246d0` (unchanged this session — BACKLOG-only edits, no code changes). No daemon restart required.
- All three repos clean at session-wrap. Submodule status: space-prefix on anvil, bellows, lessons-forge (confirm during session-wrap commit sequence).
- PLANNER_TEMPLATE.md at v4.55 after this session's bump (Plan A's substantive content shipped at v4.54; version bump applied at session-wrap).
- Phase 1.5 next session must include: this baton + PROJECT_STATUS top entry (Plan A shipped) + the 4 lessons captured above. The Plan B + Plan A pair is closed; no in-flight context to carry beyond housekeeping.

---

## Bellows BACKLOG additions this session (3 entries — top of Open)

1. **2026-05-27 — `ceo_flags` gate FP on null-declaration content.** Filed during Plan A Step 2 DEV. Fix shape options (a)/(b)/(c) — null-token allowlist suggested first. Sibling-pattern context with entries 2 and 3 below.
2. **2026-05-27 — `rule_22_verification` (c) FPs on enumerative tables.** Filed during Plan B Step 3 QA. 31 FPs on a single QA report.
3. **2026-05-27 — Orphan-guard renormalization fires on wrong step.** Filed during Plan B/Plan A planning context (carryover from prior session, not session-new but documented this session).
4. **2026-05-27 — Hedging-detector FPs on domain terminology.** Same.

The three FP entries (#1, #2, and 2026-05-22 hedging-detector) are siblings worth a coordinated daemon-side fix session — see "4 lessons captured" section above.
