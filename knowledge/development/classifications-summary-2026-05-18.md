# Classifications Summary — 2026-05-18

**Plan:** executable-lessons-forge-cycle-run-2026-05-18, Step 2
**Specialist:** Forge Lessons Agent
**Date:** 2026-05-16
**Wall-clock time:** <1s (all classifications computed in a single batch)

---

## Totals

- **Total entries classified:** 24
- **New proposals inserted:** 24 (proposal IDs 39-62)

## Distribution by Category

| Category | Count |
|---|---|
| governance_rule | 16 |
| instrumentation | 6 |
| structural | 2 |

## Distribution by Confidence

| Confidence | Count |
|---|---|
| high | 21 |
| medium | 3 |

## Entries with Medium Confidence

| Entry ID | Category | Heading (truncated) | Reasoning for medium |
|---|---|---|---|
| 45 | governance_rule | Canary "captured cwd" flag... | Recommended technique rather than hard rule; entry frames it as a directive but the strength is advisory |
| 48 | instrumentation | Files already tracked by git... | Basic git knowledge; actionable procedure but may not warrant formal instrumentation |
| 49 | instrumentation | Existing gitlinks without .gitmodules... | Rare edge case; recovery procedure useful if situation recurs but unlikely to be needed |

## Ambiguous Entries

None. All 24 entries classified cleanly within the six-value taxonomy.

## Entries Flagged for Potential Duplication (deterministic check missed)

None flagged. No entries appeared to be duplicates that `detect_duplicates()` missed.

## Entries with Pre-existing Proposals

5 entries in `needs_classification` already had proposals from prior cycles:

| Entry ID | Existing Proposal | Existing Status | New Proposal ID |
|---|---|---|---|
| 16 | #34 (governance_rule) | implemented | #58 |
| 17 | #35 (governance_rule) | implemented | #59 |
| 18 | #36 (governance_rule) | implemented | #60 |
| 20 | #37 (governance_rule) | implemented | #61 |
| 25 | #38 (governance_rule) | proposed | #62 |

These entries were included in `needs_classification` because the cycle logic excludes only entries with `category='duplicate'` proposals. New classifications were inserted per plan instruction. Gate 1 review should note the duplicated coverage.

## Classification Rationale Summary

**Structural (2):** Both Bellows gate false positives (IDs 39, 40) — root cause is gate code that pattern-matches plan prose incorrectly. Requires code-level fix to gate logic.

**Governance Rule (16):** Planner discipline entries proposing new rules or amendments to PLANNER_TEMPLATE (execution mode distinction, Phase 1.5 enforcement, verdict format/directory, diagnostic methodology, plan authoring heuristics, agent improvisation prohibition, submodule pointer bumps). Majority target PLANNER_TEMPLATE.md specifically.

**Instrumentation (6):** New checklists and procedural safeguards (git filter-repo checklist, gitignore update procedure, submodule recovery, push-bisect diagnostic, iCloud dataless check, filename truthfulness check at deposit).
