# Dev Log — Gate 2a Recovery Step 1 (schema rollback + status collapse)

Transaction start ISO: 2026-05-16T16:47:44.717691+00:00
Transaction end ISO: 2026-05-16T16:47:44.723247+00:00

Pre-rollback DB state:
- CHECK constraint values: 8 (includes 'deferred')
- Distribution: accepted=18, deferred=2, implemented=14, rejected=4, superseded=24 (total=62)

Operations:
1. UPDATE: 2 rows (IDs 45, 48) deferred -> rejected (status_updated_by='ceo', status_updated_at='2026-05-16T16:47:44.717691+00:00')
2. CREATE TABLE lesson_proposals_new with canonical 7-value CHECK
3. INSERT ... SELECT * FROM lesson_proposals (62 rows copied)
4. DROP TABLE lesson_proposals
5. ALTER TABLE lesson_proposals_new RENAME TO lesson_proposals
6. CREATE INDEX (3 indexes recreated)

Post-rollback DB state:
- CHECK constraint values: 7 (no 'deferred')
- Distribution: accepted=18, implemented=14, rejected=6, superseded=24 (total=62)
- IDs 45, 48 status: rejected (status_updated_by='ceo')
- Deferred count: 0
- Indexes present: idx_lesson_proposals_category, idx_lesson_proposals_entry, idx_lesson_proposals_status
- FK integrity: PRAGMA foreign_key_check returned 0 rows

Verifications:
- V1 (schema 7 values, no deferred): PASS
- V2 (distribution matches expected): PASS
- V3 (IDs 45, 48 rejected by ceo): PASS
- V4 (no deferred rows): PASS
- V5 (3 indexes present): PASS
- V6 (FK integrity clean): PASS

Result: COMMIT

## Output Receipt

- Agent: Forge Developer
- Step: 1
- Status: Complete (all verifications passed, transaction committed)
- What Was Done: rolled back schema CHECK constraint and collapsed 2 deferred rows to rejected
- Files Deposited: `lessons-forge/knowledge/development/dev-log-gate-2a-recovery-step-1-2026-05-19.md`
- Files Created or Modified: `lessons-forge.db` (gitignored, no commit)
- Decisions Made: rollback completed
- Flags for CEO: none — all verifications passed, pre-rollback state matched plan expectations exactly
- Flags for Next Step: Planner Rule 22 reads dev log, verifies state, authorizes Step 2
