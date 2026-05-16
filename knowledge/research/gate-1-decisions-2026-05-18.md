# Gate 1 Decisions — Lessons Forge Cycle 2026-05-18

**Cycle:** executable-lessons-forge-cycle-run-2026-05-18 (Done)
**Report:** `lessons-forge/reports/lessons-report-2026-05-18.md` (25 proposals)
**Reviewer:** CEO (Gate 1 protocol per ADR-002)
**Pre-screened by:** Planner
**Decided:** 2026-05-18

---

## Summary

| Disposition | Count |
|---|---|
| Accept | 20 |
| Defer | 2 |
| Reject | 5 |
| **Total** | **27 *(see note)*** |

**Note:** report shows 25 proposals but Gate 1 review touched 27 items because two cases involve pre-existing proposals from prior cycles (entries 16–18, 20, 25) where both old and new proposals were considered. The disposition column above is per-decision, not per-row in the report.

---

## Accepted (20)

These advance to Gate 2 — Planner authors executables that ship the actual governance/code edits. Marked `accepted` in `lesson_proposals.status` by the Gate 2 ratification plan.

### Structural — 2 (Bellows gate fixes)

| # | Entry | Proposal | Target |
|---|---|---|---|
| S1 | 2026-05-18 — `deposit_exists` gate keys on literal staging filename | Fix `deposit_exists` gate: skip `_staging_*` paths during extraction OR restrict extraction to bulleted lists under Deposits headers only | `bellows/src/gates.py` (or wherever extraction regex lives) |
| S2 | 2026-05-17 — Bellows Rule 20 gate keys on a specific stdout pattern | Relax `rule_20_self_check` gate pattern matching to tolerate shell-prompt prefixes and fenced code blocks, OR ship a `bellows.rule_20_check` helper script that prints the exact expected banner | `bellows/src/gates.py` |

Both are Bellows-side code fixes. Likely one combined executable: "Bellows gate false-positive fixes (strikes 4 & 5)."

### Governance Rule — 13 (PLANNER_TEMPLATE edits)

| # | Entry | One-line rule | Confidence |
|---|---|---|---|
| G1 | 2026-05-17 | Pre-cutover unknowns diagnostic before destructive cross-repo work | high |
| G2 | 2026-05-16 | Split destructive cross-cutting plans at natural verification point with verdict gate | high |
| G3 | 2026-05-15 | `Filesystem:write_file` for `/Users/marklehn/` paths, never `create_file` | high |
| G4 | 2026-05-15 | Submodule pointer bump immediately after submodule commit-push | high |
| G6 | 2026-05-14 | Plans with git-internal ops must walk intermediate state; "safe and non-destructive" is not an agent judgment call | high |
| G7 | 2026-05-13 | Phase 1.5 enforcement strengthened — happens FIRST regardless of task size | high |
| G8 | 2026-05-13 | Three-item verdict-file check executed out loud before any Bellows-read write | high |
| G9 | 2026-05-13 | Distinguish manual-bootstrap vs Bellows-dispatch execution modes; `STOP`-prose ignored by Bellows; per-step pause is manual only | high |
| G10 | 2026-05-13 | Negative grep during dormancy ≠ architectural finding (diagnostic methodology) | high |
| G11 | 2026-05-13 | `**Deposits:**` blocks must contain resolvable paths, no placeholders | high |
| G16 | 2026-05-10 | When shipping path-resolution fix, audit ALL gate functions calling shared function | medium |

(G16 also supersedes the pre-existing `proposed` proposal ID 38; Gate 2 plan must update that row's status to `superseded`.)

### Instrumentation — 5 (checklists/procedures)

| # | Entry | Procedure | Confidence |
|---|---|---|---|
| I1 | 2026-05-15 | `.gitignore` at commit 1 for new repos; push-bisect runbook for "inflate / bad object" errors | high |
| I2 | 2026-05-15 | `git filter-repo` 5-step recovery checklist | high |
| I4 | 2026-05-15 | Submodule recovery: hand-write `.gitmodules`, `git submodule init`, verify clean prefix | medium |
| I5 | 2026-05-14 | iCloud `dataless` flag check (`ls -lO`) before git-corruption diagnosis; hard rule: no git repos in iCloud-synced folders | high |
| I6 | 2026-05-13 | Filename truthfulness check at staging before atomic deposit | high |

---

## Deferred (2)

Captured for revisit; no Gate 2 action.

| # | Entry | Rationale for deferral |
|---|---|---|
| G5 | 2026-05-15 — Canary "captured cwd" / runtime-fact flag pattern | The agent's own reasoning admits "recommended technique rather than a hard rule." Captures planning craft, not a hard rule. Defer until we figure out where Planner techniques live (separate from PLANNER_TEMPLATE rules). |
| I3 | 2026-05-15 — `.gitignore` update procedure with `git ls-files \| grep` + `git rm --cached` | Agent flagged: "basic git behavior that may not warrant formal instrumentation." Procedure is sound but feels too elementary for a formal runbook entry. Revisit if we hit this failure mode again. |

Mark `deferred` in `lesson_proposals.status`. These do NOT close; they wait.

---

## Rejected (5)

Reject reasoning + status transitions.

| # | Entry | Rejection reason | Status transition |
|---|---|---|---|
| G12 | 2026-05-12 — Verdict response files go to `verdicts/resolved/` | Already `implemented` from prior cycle (proposal ID 34). New duplicate proposal is redundant. | New proposal → `rejected` (status_updated_by `ceo`, reason "duplicate of implemented ID 34") |
| G13 | 2026-05-12 — Verdict response format `verdict: continue\n<reason>` | Already `implemented` (proposal ID 35) | Same as G12, referencing ID 35 |
| G14 | 2026-05-12 — "queue empty" means paused-or-done | Already `implemented` (proposal ID 36) | Same as G12, referencing ID 36 |
| G15 | 2026-05-12 — Dev-log self-reference SHA loop | Already `implemented` (proposal ID 37) | Same as G12, referencing ID 37 |
| G17 | 2026-05-10 — Audit shared-dependency call sites (second proposal) | Internal duplicate of G16; same entry classified twice. | New proposal → `rejected`; G16 advances to Gate 2; pre-existing proposal ID 38 → `superseded` by G16 |

---

## Implications for Gate 2

Three executables to author next session:

1. **Gate 2a — Lessons Forge ratification.** DB-only plan: updates `lesson_proposals.status` for all 27 dispositioned items. Marks 20 `accepted`, 2 `deferred`, 5 `rejected`, plus the 1 superseded pre-existing proposal. Single-step against `lessons-forge.db`. Specialist: Forge Developer.

2. **Gate 2b — PLANNER_TEMPLATE governance edits.** 11 governance_rule rules + 5 instrumentation procedures, all targeting `PLANNER_TEMPLATE.md`. Likely combined into one executable with multiple Edit operations. Some accepted proposals overlap on rule subject (e.g., G7 strengthens existing Phase 1.5 rule); Planner must reconcile overlaps at plan-write time. Specialist: Planner-authored, executed via Desktop Commander or Filesystem edit_file under Rule 22 verification.

3. **Gate 2c — Bellows gate false-positive fixes.** S1 + S2 combined: code edits to `bellows/src/gates.py` (or equivalent) + tests + canary verification of both gate behaviors. Specialist: Bellows Developer (if exists; otherwise Forge Developer).

**Suggested order:** 2a first (cheap DB writes, closes the cycle bookkeeping). Then 2c (Bellows fixes reduce friction for all future plans). Then 2b (PLANNER_TEMPLATE edits — the biggest cognitive lift, deserves a clean session).

---

## Output Receipt

**Deposit:** `lessons-forge/knowledge/research/gate-1-decisions-2026-05-18.md` (this file)
**Status:** Complete
**Authored by:** Planner (pre-screen) + CEO (Gate 1 approval)
**Date:** 2026-05-18

**Database state changes pending (deferred to Gate 2a ratification plan):**
- 20 proposals → `accepted`
- 2 proposals → `deferred`
- 5 proposals → `rejected`
- 1 pre-existing proposal (ID 38) → `superseded`

No DB writes performed by this deposit. Gate 2a will execute the writes against `lessons-forge.db`.
