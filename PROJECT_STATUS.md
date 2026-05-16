# Lessons Forge — Project Status
**Last Updated:** 2026-05-17

---

## Health

Standalone repo operational. Phase A (stand-up) complete 2026-05-16. Phase B.1 (forge-side cutover + remote push) complete 2026-05-17. Phase B.2 (governance edits, submodule registration, Bellows watch wiring) pending next session. Bellows is NOT yet watching this repo's `knowledge/decisions/`.

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
