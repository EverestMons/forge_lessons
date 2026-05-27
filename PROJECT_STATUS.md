# Lessons Forge — Project Status
**Last Updated:** 2026-05-27

---

## Health

Standalone repo fully integrated. Cycle run 2026-05-27 ingested 36 new entries from LESSONS.md (DB had 57 orphan entries from prior LESSONS.md state — zero heading overlap with current content). Phase 2A classifications shipped for all 36 entries across three plans: the original cycle plan (Step 1 + Step 2a, halted at structural failure), the batch 2 recovery plan, and this closeout. Phase 2A complete. Next: CEO Gate 1 review of classifications (separate session).

---

## 2026-05-27 — Plan B (Plan Authoring Checklist + residual scatter) shipped halted-but-shipped

First of the two Phase 2B plans landed. Substance shipped clean; final-step gate_failure on QA Step 3 (32 failures: 1 real Rule 20 omission + 31 enumerative-table gate FPs) resolved via Planner-side post-hoc Rule 20 block run + new Bellows BACKLOG entry for the gate hazard. Plan moved to `Done/halted-but-shipped-*` per 2026-05-22 final-step gate_failure recovery checklist.

**PLANNER_TEMPLATE edits (v4.54, governance root commit `e975e05` + `c420e23`):**
- New `## Plan Authoring Checklist` section (line 917) with 12 mechanical pre-deposit checks (proposals 66, 67, 69, 75, 79, 80, 84, 90, 91, 92, 95, 98). Independent 1-12 numbering scope (not continuous with Orchestration Plan Rules) to signal lifecycle-moment distinction.
- Rules 42-44 under `## Orchestration Plan Rules` (proposals 83, 96, 97): BACKLOG defer re-evaluation when manual fallback gets mechanized; baton "On the horizon" cross-check against PROJECT_STATUS Completed; BACKLOG entry framing — scan Closed section before filing "never done".
- New unnumbered DPE technique "Timing and ordering claim verification" in `### Diagnostic Prompt Engineering` subsection (proposal 76; matches existing DPE convention of bold-paragraph techniques).
- Total file growth: 1504 → 1598 lines (+94 insertions, 0 deletions).

**Archived narratives file shipped:** `lessons-forge/knowledge/archived-narratives-2026-05-27.md` — 4 proposals (64, 87, 93 originally archive-as-context + 72 demoted by SA in Plan B blueprint as Rule 33 overlap).

**SA dispositions for the two residual SA-decision candidates (per Plan B Decision 2):**
- Proposal 72 → archived (substantially overlaps Rule 33 "Phase 1.5 enforcement happens FIRST regardless of how narrow the opening question seems").
- Proposal 74 → folded to Plan A scope (joint-author with proposal 85 — both address how information flows during Bellows-dispatched execution; natural home is the Bellows Operational Workarounds subsection).

**Plan A scope updated:** 12 base proposals + 1 fold-in (74) + 1 prior fold (85 already in scope) → 14 rules total. Plan A queued for next session (see `NEXT_SESSION.md`).

**Gate failure resolution (Step 3):**
- 1 real failure (rule_20_self_check): QA agent built manual verbatim-match table for Check 10 instead of running the canonical Python block from `RULE_20_SELF_CHECK_BLOCK.md`. Banner string missing, gate fired correctly. Planner ran the block post-hoc (evidence_dir=/tmp/empty-evidence-dir/ since governance-edit plan has no evidence artifacts), block exited 0 with PASSED banner present byte-for-byte. stdout appended to QA report under "Appendix: Canonical Rule 20 Python Self-Check".
- 31 false positives (rule_22_verification): gate parses every markdown table in QA reports demanding per-row Status columns; QA report's 5 enumerative content tables (heading list, proposal-ID map, Rules 42-44, archived-proposals, 18-row verbatim-match) all triggered. Filed as new Bellows BACKLOG entry — top of Open section, sibling-symmetric with 2026-05-24 (c) greenness section-scoping fix.

**Deposits:**
- `PLANNER_TEMPLATE.md` (modified, +94 lines)
- `lessons-forge/knowledge/research/plan-authoring-checklist-blueprint-2026-05-27.md` (SA blueprint)
- `lessons-forge/knowledge/archived-narratives-2026-05-27.md` (new file)
- `lessons-forge/knowledge/qa/plan-authoring-checklist-qa-2026-05-27.md` (QA report + Rule 20 appendix)
- `lessons-forge/knowledge/decisions/Done/halted-but-shipped-executable-planner-template-plan-authoring-checklist-2026-05-27.md`
- `bellows/knowledge/BACKLOG.md` (new entry top of Open)

**Commits shipped:**
- bellows: `b9246d0` (BACKLOG entry + 3 archived processed-verdict files)
- lessons-forge: `e3b0ad9` (SA blueprint, worktree teardown), `28842a5` (DEV+QA + archived narratives, worktree teardown), `738f11c` (QA Rule 20 appendix + Done plan move, session-wrap)
- governance root: `e975e05` (PLANNER_TEMPLATE edits + lessons-forge submodule bump from worktree teardown), `c420e23` (bellows + lessons-forge submodule pointers session-wrap)
- All three repos pushed to origin.

**Lessons for next-session Forge cycle (3 candidates):**
1. QA prompt language: "Run the block manually" interpreted as "do verification manually instead of running the block." Plan-side template should remove "manually" and say "Include the canonical Python block verbatim with placeholders filled, run via `python3`, capture stdout in the QA report."
2. PLANNER_TEMPLATE version drift between session start and SA dispatch (4.53 → 4.54). Phase 1.5 should re-verify version line before authoring Context sections that name the version.
3. New gate hazard: rule_22_verification (c) enumerative-table FPs. Sibling pattern with 2026-05-22 hedging-detector domain-term FPs. Both gates parse content uniformly without scoping to verification regions.

---

## 2026-05-27 — CEO Gate 1 disposition for 36 proposals (cycle 2026-05-27)

All 36 proposals from the 2026-05-27 cycle (IDs 63–98) triaged. Disposition counts: **33 accepted, 2 rejected, 1 superseded, 0 stale, 0 ambiguous.**

**Rejected (2):** proposal 86 (entry 81 — orphan-guard renormalization workaround) and proposal 88 (entry 83 — Rule 22(d) hedging-detector override guidance). Both were medium-confidence Planner-side workarounds for daemon bugs. CEO decision pattern: route the underlying daemon bug to Bellows BACKLOG rather than codify the workaround as governance. Two new Bellows BACKLOG entries shipped this session: orphan-guard step-number predicate gap, and hedging-detector domain-term false positives.

**Superseded (1):** proposal 63 (entry 58 — SA dense-content liveness anchors) — already implemented as Rule 41 in PLANNER_TEMPLATE during the same session that produced the source LESSONS entry.

**Accepted (33):** distributed across two structural clusters identified in cross-batch synthesis plus 7 residual rules. Phase 2B will land via two separate plans:
- **Plan A — Bellows Operational Workarounds subsection (14 rules):** new dedicated PLANNER_TEMPLATE subsection cross-referenced to Bellows BACKLOG entries; deprecatable wholesale when daemon fixes ship.
- **Plan B — Plan Authoring Checklist + residual (12 + 7 rules):** new mechanical pre-deposit checklist section, plus residual rules scattered into Diagnostic Prompt Engineering / Phase 1.5 / BACKLOG-authoring / baton-authoring; 3 narratives archived as context.

**DB state post-write:** `proposed=0`, `accepted=33` (this cycle), `rejected=8` (6 prior + 2 this), `superseded=25` (24 prior + 1 this), `implemented=32` (unchanged). `status_updated_by='ceo'`, `status_updated_at='2026-05-27'` on all 36 dispositioned rows.

**Phase 2B staged for next session:** two plans, dispatched separately. Plan A and Plan B both go through normal SA → DEV → QA orchestration via Bellows. Order TBD at next session start.

**Bellows BACKLOG additions this session (2 entries, Planner-direct edits to `/Users/marklehn/Developer/GitHub/bellows/knowledge/BACKLOG.md`):**
- Orphan-guard renormalization fires on wrong step (small effort, predicate strengthening at `_consume_verdicts` pre-scan site)
- Hedging-detector false positives on domain terminology in QA verification tables (medium effort, three fix shapes named)

---

## 2026-05-27 — Cycle run + Phase 2A classifications shipped (recovery sequence)

Ingested 36 new entries (parser saw 36 in current LESSONS.md). All 36 classified across two batches (entries 58-75 in original plan Step 2a, entries 76-93 in batch-2 recovery plan). Distribution across full cycle: 33 governance_rule (91.7%), 3 narrative (8.3%); 0 structural, 0 instrumentation, 0 language. Confidence: 33 high, 3 medium, 0 low, 0 ambiguous. All 33 governance_rule proposals target PLANNER_TEMPLATE.md.

**Cross-batch synthesis (key signals for CEO Gate 1):**
- 15/36 entries (41.7%) are Bellows operational workarounds — consider dedicated PLANNER_TEMPLATE subsection that can be deprecated when daemon fixes ship
- 13/36 entries (36.1%) propose plan-authoring pre-write checks — consider consolidated "Plan Authoring Checklist" section
- 6/36 entries follow the "captured but not internalized" failure mode — strongest signal for mechanical checklists over prose rules

**Plan sequence (three plans for one cycle):**
1. `Done/executable-lessons-forge-cycle-2026-05-27` (halted) — Step 1 + Step 2a complete; halted at Step 2b due to non-monotonic STEP header labels violating Bellows positional step-parser contract.
2. `Done/executable-lessons-forge-cycle-batch2-recovery-2026-05-27` — Step 2b recovered (entries 76-93 classified as proposals 81-98).
3. `Done/executable-lessons-forge-cycle-closeout-2026-05-27` (this plan) — verification + PROJECT_STATUS update.

**Deposits:**
- `knowledge/research/lessons-forge-cycle-step1-2026-05-27.md`
- `knowledge/research/lessons-forge-cycle-step2a-classifications-2026-05-27.md`
- `knowledge/research/lessons-forge-cycle-batch2-recovery-2026-05-27.md`

Pre-cycle DB state: entries=57, proposals=62 (all terminal). Post-cycle: entries=93, proposals=98 (62 terminal + 36 proposed awaiting Gate 1).

---

## 2026-05-19 — Gate 2d status advancement (18 accepted → implemented)

Advanced 18 `lesson_proposals` rows from `status='accepted'` to `status='implemented'` — housekeeping for gates 2a, 2b, and 2c which shipped earlier this session. Single transaction, all verifications passed.

**Post-write DB state:** accepted=0, implemented=32, rejected=6, superseded=24, total=62.

**Proposal IDs:** 39-40 (gate 2c), 41-47/49-57/62 (gate 2b).

---

## 2026-05-19 — Gate 2b PLANNER_TEMPLATE edits shipped

Applied 16 proposals from cycle 2026-05-18 to `PLANNER_TEMPLATE.md`:
- **11 governance rules** (Rules 28-38) appended to `## Orchestration Plan Rules`
- **6 procedures** (new `## Procedures` section) appended after `## Forge Observations`

QA: 7/7 verification checks PASS. No regressions to existing rules.

**Commits:** `e055c82` (governance root — PLANNER_TEMPLATE.md), `42371a8` (lessons-forge — evidence files)

---

## 2026-05-19 — Gate 2a recovery (schema rollback + worktree teardown)

Gate 2a Step 2 (ratification) successfully wrote 25 ratification rows to `lessons-forge.db` but introduced two unauthorized scope expansions: (a) added `'deferred'` to the `lesson_proposals.status` CHECK constraint, and (b) modified `src/db.py` in a worktree. Recovery plan executed in 3 steps:

1. **Schema rollback + status collapse** — rolled back the CHECK constraint to canonical 7 values, collapsed 2 `deferred` rows (IDs 45, 48) to `rejected` with `status_updated_by='ceo'`. Single transaction, all 6 verifications passed.
2. **Worktree teardown + artifact commit** — removed stale worktree `gate-2a-lessons-forge-ratification-2026-05-19` (commit `d8cb5e5` now unreachable), committed 5 artifact files at `4cd57d6`.
3. **QA verification** — 10/10 checks passed (schema, data distribution, indexes, tests 25/25, no stale worktree, `src/db.py` untouched, working tree clean).

**Final DB state:** 62 proposals — accepted=18, implemented=14, rejected=6, superseded=24. No `deferred` status value in schema or data.

**Commits:** `4cd57d6`, `50cd63e`

---

## 2026-05-18 — Phase B.2 governance wiring shipped

**Plans shipped:** 
1. `executable-lessons-forge-extraction-phase-b2-governance-wiring-2026-05-18` (8 steps, end-to-end, deposited to `bellows/knowledge/decisions/`)
2. `diagnostic-bellows-watch-canary-lessons-forge-2026-05-18` (canary deposited by Step 8 into `lessons-forge/knowledge/decisions/`, dispatched by the newly-watched daemon, all three flags PASS)

**State changes:**
- `lessons-forge/` is now a registered submodule of the governance root (`git@github.com:EverestMons/forge_lessons.git`). `.gitmodules` contains all three submodule blocks (anvil, bellows, lessons-forge).
- Bellows daemon restarted with 9 watched projects (was 8). New entry: `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/decisions`.
- Canary findings deposit at `knowledge/research/canary-lessons-forge-bellows-watch-2026-05-18.md` confirms end-to-end dispatch: `cwd` under `.bellows-worktrees/`, `watched_count=9`, `lessons_forge_watched=True`.
- Canary plan closed cleanly to `knowledge/decisions/Done/`.

**Bellows gate false positive (strike 4):** Step 8 verdict request showed `deposit_exists` gate failure on the literal staging filename `_staging_diagnostic-bellows-watch-canary-lessons-forge-2026-05-18.md` mentioned in step prose. Rule 22 verification confirmed the work was substantively correct — all 8 steps verified clean. Captured to LESSONS.md as the 4th documented Bellows gate false positive; mitigation noted (don't list staging/transient filenames in Deposits blocks). Cross-cutting fix: Bellows backlog candidate for `_staging_*` heuristic in gate extraction.

---

## 2026-05-17 — Phase B.1 cutover shipped

**Plans shipped:** `executable-lessons-forge-extraction-phase-b1-cutover-2026-05-17` (dispatched through forge, deposited there by historical Bellows watch config).

**State changes:**
- Fixed stale `/Desktop/GitHub/` paths in `src/lessons_forge.py`:
  - Line 235 docstring default for `detect_duplicates` reference_files: `/Desktop/GitHub/PLANNER_TEMPLATE.md` → `/Developer/GitHub/PLANNER_TEMPLATE.md`
  - Line 246 default argument for `detect_duplicates`: same fix
  - Line 328 default argument for `run_full_lessons_cycle` `lessons_md_path`: `/Desktop/GitHub/LESSONS.md` → `/Developer/GitHub/LESSONS.md`
  - Root cause: 2026-05-14 governance-root relocation commit `26b964f` missed this file
- Added `knowledge/decisions/.gitkeep` (Bellows watch directory prereq for Phase B.2)
- Added `origin` remote: `git@github.com:EverestMons/forge_lessons.git`
- Pushed all 4 commits to new remote (3 from Phase A + 1 from B.1 step 1)
- Test suite: 25/25 passing post-path-fix

**Commit:** `f06a2ec` — fix: relocate /Desktop/GitHub/ paths to /Developer/GitHub/; scaffold knowledge/decisions/ (Phase B.1 step 1)

**Naming note:** GitHub remote is `EverestMons/forge_lessons` (underscore); local directory is `lessons-forge` (hyphen). Asymmetry is intentional and standard.

---

## 2026-05-16 — Phase A stand-up complete

Repo scaffold + code/data migrated from forge:
- Directory structure: `src/`, `agents/`, `knowledge/{decisions,research,development,qa}/`, `reports/`, `Done/`
- Project metadata: `CLAUDE.md`, `PROJECT_BRIEF.md`, `PROJECT_STATUS.md`, `.gitignore`, `requirements.txt`
- Code copied byte-identically from forge: `src/lessons_forge.py`, `src/test_lessons_forge.py`, `agents/FORGE_LESSONS_AGENT.md`
- New `src/db.py` containing ONLY lesson DDL (2 tables + 6 indexes)
- `lessons-forge.db` populated via sqlite3 `.dump` → `.read` (38 rows in both tables, FK integrity preserved)
- QA verdict: PASS (25/25 tests, live parse+ingest works, forge.db untouched)

Commits `047476f`, `e1c9825`, `8e618b4`.

---

## In Progress

*(none)*

## Pending — Phase B.2 (next session)

1. Edit `governance/adr/ADR-002-lessons-forge-design.md` (lines 32, 34, 76, 145 — stale `forge/src/lessons_forge.py` / `forge/agents/FORGE_LESSONS_AGENT.md` references)
2. Edit `governance/adr/ADR-003-orchestrator-plan-pattern.md` (line 196 — same stale path)
3. Edit `ARCHITECTURE.md` (line 116 drop "(proposed)" label, line 124 reference update)
4. Register lessons-forge as submodule of governance root: `git submodule add git@github.com:EverestMons/forge_lessons.git lessons-forge`
5. Append `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/decisions` to `bellows/config.json` watched_projects
6. Restart Bellows daemon (load new watch)
7. Two-commit pattern at governance root (.gitmodules + ADR edits + bellows submodule pointer bump if bellows touched anything)
8. Canary: deposit no-op decision to `lessons-forge/knowledge/decisions/`, verify Bellows dispatches

---

## Open Operational Notes

- The first Bellows-dispatched plan to lessons-forge will be the B.2 canary (item 8 above).
- Until B.2 is complete, any executable touching lessons-forge must still be deposited through forge's `knowledge/decisions/` (only watched project so far).
- Bellows BACKLOG: `rule_20_self_check` gate false-positive pattern (see LESSONS.md 2026-05-17 entry).
