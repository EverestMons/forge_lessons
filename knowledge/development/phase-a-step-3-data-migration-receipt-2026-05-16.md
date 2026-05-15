# Phase A Step 3 — Data Migration Receipt

**Date:** 2026-05-16
**Source:** `forge/forge.db` (read-only)
**Target:** `lessons-forge/lessons-forge.db`
**Method:** `.dump` → grep INSERT → `.read` (entries first, proposals second)

## Verification Results

### Row Counts
| Table | forge.db | lessons-forge.db |
|---|---|---|
| lesson_entries | 38 | 38 |
| lesson_proposals | 38 | 38 |

### PRAGMA foreign_key_check
Empty (no violations).

### ID Range Comparison
| Table | forge.db MIN(id) | forge.db MAX(id) | lessons-forge.db MIN(id) | lessons-forge.db MAX(id) |
|---|---|---|---|---|
| lesson_entries | 1 | 38 | 1 | 38 |
| lesson_proposals | 1 | 38 | 1 | 38 |

### Spot-Check JOIN (top 3 proposals by ID DESC)
```
38|25|governance_rule|2026-05-10 — When shipping a path-resolution fix, audit ALL gate functions that call _resolve_deposit_path
37|20|governance_rule|2026-05-12 — Dev-log self-reference SHA loop is structurally impossible
36|18|governance_rule|2026-05-12 — "queue empty — all plans complete" means paused-or-done, NOT completed
```
Identical in both databases.

## Verdict
Migration complete. All verifications passed. forge.db untouched (read-only access only).
