# Lessons Forge — Next Session Baton

**Last session:** 2026-05-27 (continuation)
**Last session focus:** Gate 2d-style housekeeping — advanced 33 accepted proposals to implemented for cycle 2026-05-27. Diagnostic + executable both shipped clean end-to-end via Bellows.

---

## In-flight threads (carry forward)

*(none — cycle 2026-05-27 housekeeping complete)*

---

## On the horizon (open items, none in-flight)

### `lessons-forge.db` git tracking disposition

The DB file is tracked but `*.db` is in `.gitignore` — grandfathered tracking from before the ignore rule. Two paths to resolve:
- (a) Commit the DB on every state change (current de-facto behavior, was inconsistent across sessions — 2026-05-19 gate 2d did NOT commit; 2026-05-27 gate 2d DID commit).
- (b) Un-track and treat disk file as state of record. Requires `git rm --cached lessons-forge.db`, a one-time commit, and an operational decision about how fresh clones bootstrap their DB.

Not blocking next session, but worth a decision before another gate 2d or schema migration. Filed as Bellows BACKLOG entry this session.

### Verdict filename matching tolerance (vs. README convention)

README at `bellows/verdicts/README.md` specifies verdict response filename strips leading prefix from plan slug:
- `diagnostic-foo-bar-2026-04-16.md` → `verdict-foo-bar-2026-04-16-step-1.md`
- `executable-foo-bar-2026-04-16.md` → `verdict-foo-bar-2026-04-16-step-1.md`

Observed this session: Bellows consumed `verdict-diagnostic-gate-2d-mapping-v2-2026-05-27-step-1.md` and `verdict-executable-gate-2d-status-advancement-2026-05-27-step-1.md` correctly — both with the prefix NOT stripped. Either Bellows matching is more tolerant than the README documents, or the consumption succeeded by some other matching path (suffix match on `-step-N`?). Worth a daemon-side investigation to confirm matching logic, then either tighten Planner authoring discipline or update the README to document the observed tolerance.

### 4 lessons captured 2026-05-27 morning session (candidates for next Forge cycle)

Unchanged from prior baton — still candidates for next Forge cycle:
1. QA prompt language ambiguity — "Run the block manually" vs canonical block execution.
2. PLANNER_TEMPLATE version drift between session start and SA dispatch.
3. `rule_22_verification` (c) enumerative-table FPs (filed as Bellows BACKLOG).
4. `ceo_flags` gate FP on "None"-as-declaration content (filed as Bellows BACKLOG).

### 2 lessons captured this session (continuation; candidates for next Forge cycle)

5. **`Dispatch Mode: standard` rejection on first deposit.** Authored `**Dispatch Mode:** standard` despite Rule 35 specifying `bellows` or `manual_bootstrap`. BACKLOG already carries Rule 35 dispatch-mode hazard (four prior rejections across three days). Pattern: Planner authoring discipline still relies on memory rather than mechanized check. Plan Authoring Checklist item 3 (proposal 79) exists but didn't fire. Either checklist isn't being consulted in session, or its phrasing doesn't make the hazard sharp enough. Lesson shape: PLANNER_TEMPLATE checklist needs an explicit enumerated allowlist at the head of the item, not just a "valid values" reference.

6. **Verdict filename prefix tolerance.** See "On the horizon" above. Two verdict files this session matched against requests despite extra prefix segments. Lesson shape: either Bellows matching is documented incorrectly in README, or the matching logic should be tightened to enforce README spec. Daemon-side investigation needed.

### Forge cycle #14 + canary follow-ups

Still parked from prior sessions: `forge.db` 50MB warning, retire-the-queue decision. Not blocking.

### Forge pre-scan sync workflow before each Mac run

`bash ~/Developer/GitHub/forge/scripts/pre-scan-sync.sh` — run if any Forge work is in scope next session.

---

## DB state

`lesson_proposals` table (post-gate-2d 2026-05-27):
- `status='implemented'`: **65 rows** (32 prior + 33 advanced this cycle).
- `status='accepted'`: **0 rows** (clean).
- `status='rejected'`: 8 rows.
- `status='superseded'`: 25 rows.
- Total: 98 rows.

---

## Operational notes for next session

- Daemon at `bellows.py @ b9246d0` (unchanged this session — BACKLOG-only edits, no code changes). No daemon restart required.
- All three repos clean at session-wrap (anvil, bellows, lessons-forge all space-prefix on `git submodule status`).
- PLANNER_TEMPLATE.md at v4.55 (unchanged this session).
- Phase 1.5 next session must include: this baton + PROJECT_STATUS top entry (gate 2d) + the 6 lesson candidates above. Cycle 2026-05-27 closed across DB, governance, and bookkeeping; no in-flight context to carry.

---

## Bellows BACKLOG additions this session (2 entries — top of Open)

1. **2026-05-27 — `lessons-forge.db` tracked-but-gitignored disposition.** Decision needed: commit-on-state-change vs un-track. Sibling-class to nothing prior — this is governance hygiene, not a daemon hazard.
2. **2026-05-27 — Verdict filename prefix tolerance vs README convention.** Daemon-side investigation: confirm verdict-consumer matching logic, then either tighten or update README.

---

## Bellows BACKLOG additions from morning session (4 entries — unchanged, still Open)

1. **2026-05-27 — `ceo_flags` gate FP on null-declaration content.** Sibling-class with #2 and the 2026-05-22 hedging-detector entry. All three same root-cause shape (uniform field parsing without semantic scoping). Coordinated daemon-side fix session is the right next step.
2. **2026-05-27 — `rule_22_verification` (c) FPs on enumerative tables.** Same sibling-class.
3. **2026-05-27 — Orphan-guard renormalization fires on wrong step.** Carryover from prior session, documented this session.
4. **2026-05-27 — Hedging-detector FPs on domain terminology.** Same sibling-class as #1 and the 2026-05-27 `rule_22_verification` (c) entry.

Three FP entries (`ceo_flags`, `rule_22_verification` (c), hedging-detector) worth a coordinated daemon-side fix session — single `_is_null_declaration()` / section-scoping helper rather than three independent fixes.
