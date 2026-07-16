# Hash Normalization Backfill — Step 2 Dev Log (Plan 204)

**Date:** 2026-07-16
**Plan:** 204 — Fix whitespace-only hash flips silently staling implemented proposals
**Step:** 2 (DEV — canonical DB backfill + restore + audit)

## Task A — Backup

| Field | Value |
|---|---|
| Backup path | `/tmp/lessons-forge-backup-2026-07-16.db` |
| Byte size | 798,720 bytes |
| lesson_entries rows | 140 |
| lesson_proposals rows | 145 |

## Task B — Backfill (hash column only)

Script: `scripts/backfill_normalized_hashes_2026-07-16.py`

For each of the 83 currently-parsed LESSONS.md entries (matched by `source_heading`), recomputes `content_hash` via `_normalize_for_hash` and issues `UPDATE lesson_entries SET content_hash = ? WHERE id = ?`. Direct SQL only — no call to `ingest_lesson_entries` or `run_full_lessons_cycle`.

### Hard constraint verification

- **No lesson_proposals statements:** script issues only SELECT against lesson_proposals (for distribution snapshots). No UPDATE/INSERT/DELETE.
- **No raw_content modification:** only `content_hash` is updated.
- **Idempotent:** second run reports 0 changes.
- **Archived entries untouched:** only the 83 parsed entries are updated; the 57 archived entries retain their stored hashes.

### Results

```
Backfill results: updated=83, unchanged=0, not_found=0
```

### Proposal status distribution — before and after (THE critical evidence)

```
BEFORE: {'implemented': 96, 'reference': 2, 'rejected': 15, 'stale': 4, 'superseded': 28}
AFTER:  {'implemented': 96, 'reference': 2, 'rejected': 15, 'stale': 4, 'superseded': 28}
```

**Distributions are identical. No proposals touched.**

### Idempotency re-run

```
Idempotency check: 0 rows would change on re-run
ASSERTION PASSED: backfill is idempotent.
```

## Task C — Restore proposal 145

Proposal 145 (entry 137) was staled at `2026-07-16T13:15:46Z` by a whitespace-only hash flip (proven in plan CEO Context). Restored:

```sql
UPDATE lesson_proposals
SET status='implemented', status_updated_by='ceo', status_updated_at=datetime('now')
WHERE id=145;
```

Note: `status_updated_by='ceo'` used because the CHECK constraint only allows `('planner', 'ceo', 'auto', NULL)`. The plan specified `'ceo-plan-203-recovery'` but that violates the constraint. `'ceo'` is correct — this is CEO-directed recovery.

Note: proposal 145's pre-corruption `status_updated_at` is unrecoverable (overwritten at `2026-07-16T13:15:46Z` by the auto stale update).

### Verification

```
Entry 137 proposals: {145: implemented, status_updated_by='ceo', status_updated_at='2026-07-16 13:34:26'}
```

### Post-restore proposal distribution

```
implemented: 97  (was 96, +1 from proposal 145 restore)
reference:    2
rejected:    15
stale:        3  (was 4, -1 from proposal 145 restore)
superseded:  28
```

## Task D — Loop closure proof

### get_unclassified_entries

```
Unclassified entries: [138, 139, 140]
Entry 137 in work list: False
```

Entry 137 is no longer in the work list — its proposal 145 is `implemented` again.

### run_full_lessons_cycle

```
updated_count: 0
needs_classification: [138, 139, 140]
terminal_proposals_flagged: []
ingested_count: 0
unchanged_count: 83
```

All hashes match. Zero updates, zero stales. Work list is exactly `[138, 139, 140]` — the three genuine new entries from cycle 203.

## Task E — Audit of proposals 98/121/130 (REPORT ONLY)

| Entry | Staled proposal | Current status | status_updated_at | Reclassified twin | Twin disposition | Twin rationale |
|---|---|---|---|---|---|---|
| 93 | 98 | stale | 2026-06-03T22:04:57Z | 122 | rejected (ceo, 2026-06-07) | Already covered by Checklist #12 (schema init_db+PRAGMA), added in 06-03 Gate 2 |
| 116 | 121 | stale | 2026-06-06T21:34:34Z | 123 | rejected (ceo, 2026-06-07) | Superseded by Checklist #14's inline-paths fix |
| 123 | 130 | stale | 2026-07-07T01:22:28Z | 131 | rejected (planner, 2026-07-07) | Already codified — the baton/root-cause rule is present in PLANNER_TEMPLATE.md's recurring-bug Guardrail bullet |

### Key facts

- **Pre-stale status is unrecoverable from the DB** for all three. The `status` and `status_updated_at` fields were overwritten by the `auto` stale mechanism.
- **External evidence:** all three underlying rules are already codified in PLANNER_TEMPLATE.md (via the 06-03 and 06-07 Gate 2 ratifications). The reclassified twins were correctly rejected as duplicates.
- **All three completed reclassification cycles ended as rejected duplicates** — 100% waste rate from this bug, confirming the plan's CEO Context.

### Recommendation for CEO Gate 1

Leave proposals 98, 121, and 130 as `stale`. Their reclassified twins (122, 123, 131) were all correctly rejected — the underlying rules were already implemented before the reclassification even occurred. Restoring them would create three `proposed` or `implemented` proposals for rules that are already codified, adding noise rather than value. The `stale` status accurately reflects that they were victims of the whitespace bug, and the rejection of their twins confirms no governance gap exists.

## Output Receipt

| Field | Value |
|---|---|
| Status | **Complete** |
| Plan | 204 Step 2 |
| Backup | `/tmp/lessons-forge-backup-2026-07-16.db` (798,720 bytes) |
| Entries re-hashed | 83 (all currently-parsed) |
| Proposal distribution change | None (96→96 implemented pre-restore; 96→97 post-restore from proposal 145) |
| Proposal 145 | Restored to `implemented` |
| Loop closed | `updated == 0`, work list = `[138, 139, 140]`, entry 137 absent |
| Idempotent | Second run: 0 changes |
| Files changed | `scripts/backfill_normalized_hashes_2026-07-16.py` |
| DB touched | Yes — canonical `lessons-forge.db` (hash backfill + proposal 145 restore) |

### Ledger Updates

#### Prompt Feedback

The plan specified `status_updated_by='ceo-plan-203-recovery'` for the proposal 145 restore, but the `lesson_proposals` table has a CHECK constraint restricting `status_updated_by` to `('planner', 'ceo', 'auto', NULL)`. Used `'ceo'` instead — the semantically closest valid value for CEO-directed recovery. The plan's `stale_proposals_marked` key was expected in `run_full_lessons_cycle`'s return dict but isn't surfaced there (it's only in `ingest_lesson_entries`'s return); however, `updated_count == 0` proves no stale path fired.
