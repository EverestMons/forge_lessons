# Archived Narratives — 2026-05-27 Lessons Forge Cycle

This file records Gate 1 archive-as-context dispositions from the 2026-05-27 Lessons Forge cycle. These proposals were reviewed during Gate 1 and classified as narratives or reinforcements that do not warrant new governance rules — either because the pattern is already captured, the structural fix has shipped, or the observation has no actionable intervention. They are preserved here as historical context.

---

## Proposal 64 — Leftover-after-ship tooling retirement

**Source lesson:** 2026-05-27 cycle, entry on leftover-after-ship tooling path
**Why archived:** Existing Phase 1.5 discipline catches the leftover-after-ship pattern at 100% rate. The tooling path (term-matching approach) was tried and retired. No new action until semantic comparison is available.
**Suggested action (verbatim):** Archive as context. Existing Phase 1.5 discipline catches the leftover-after-ship pattern at 100% rate. Tooling path (term-matching) was tried and retired. No new action until semantic comparison is available.

---

## Proposal 72 — Phase 1.5 reinforcement for substantive CEO openings

**Source lesson:** 2026-05-27 cycle, entry on Phase 1.5 skip under urgency
**Why archived:** Substantially overlaps Rule 33 (Phase 1.5 enforcement — happens FIRST regardless of task size), which already mandates Phase 1.5 before any investigation "regardless of how narrow the opening question seems." The incremental value (explicit "acknowledge briefly" instruction) does not warrant a separate rule. SA disposition during blueprint authoring.
**Suggested action (verbatim):** Reinforce PLANNER_TEMPLATE.md Phase 1.5 rule: when CEO opening message is substantive, acknowledge briefly and complete Phase 1.5 reads before any investigation. Protocol exists for high-urgency moments.

---

## Proposal 87 — Runner log step labels unreliable for dispatch tracking

**Source lesson:** 2026-05-27 cycle, entry on runner log `(step N)` label reliability
**Why archived:** Already noted in user memories. File-state (verdict-request filenames, plan filename prefix) is the authoritative dispatch-state tracking mechanism, not runner log labels. Archival captures the narrative without adding a governance rule.
**Suggested action (verbatim):** Archive as operational context — runner log `(step N)` labels are unreliable for dispatch-state tracking; use file-state (verdict-request filenames, plan filename prefix) as ground truth.

---

## Proposal 93 — git diff --stat gate blind spot

**Source lesson:** 2026-05-27 cycle, entry on gate-failure framing for blast-radius evaluation
**Why archived:** Structural fix shipped 2026-05-25 (scope_check gate now uses `--relative -- .` to scope diffs to project subtree). Entry documents the gate-failure framing lesson: evaluate blast radius by gate consumers, not surface output. The lesson is valid context but the fix is already in production code.
**Suggested action (verbatim):** Archive as context — `git diff --stat` gate blind spot is fixed (structural fix shipped 2026-05-25); entry documents the gate-failure framing lesson: evaluate blast radius by gate consumers, not surface output.
