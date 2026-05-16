# Dev Log — Gate 2a Step 1 (manifest derivation)

Read: knowledge/research/gate-1-decisions-2026-05-18.md, reports/lessons-report-2026-05-18.md, lessons-forge.db
Mapped: 25 row touches (18 accepted, 2 deferred, 4 rejected, 1 superseded)
Verification:
- all_mapped_ids_exist: true
- all_new_proposals_currently_proposed: true (IDs 39-62 all status=proposed)
- id_38_currently_proposed: true
- ids_34_35_36_37_currently_implemented: true
- g16_duplicate_of_38_consistent: true (G16=ID 62, duplicate_of=38)
- id_38_duplicate_of_g16_consistent: true (ID 38, duplicate_of=62)

Anomalies:
- **G17/ID 38 overlap (count discrepancy):** Plan expects 26 row touches (5 rejected + 1 superseded). Actual distinct row touches: 25 (4 rejected + 1 superseded). Root cause: G17 and pre-existing ID 38 are the same DB row (proposal_id 38, entry_id 25). The cycle pipeline classified entry 25 twice but only created one new proposal (ID 62); the second classification reused the pre-existing ID 38. Plan rule 3 says G17 → rejected; plan rule 4 says ID 38 → superseded; both target the same row. Manifest resolves this by applying rule 4 (superseded) as the final disposition, since it is the more specific handling and the decision matrix's G17 entry itself states "pre-existing proposal ID 38 → superseded by G16."
- **G16 confidence mismatch:** Decision matrix lists G16 as "medium" confidence, but the DB proposal mapped to G16 (ID 62) has confidence "high." The pre-existing ID 38 has confidence "medium." This mismatch arises because G16 corresponds to the new proposal (ID 62, high confidence), not the pre-existing one (ID 38, medium confidence) — G16 must be a new proposal per the plan's explicit instructions ("G16's new proposal is accepted") and its duplicate_of cannot self-reference.

Pre-write status distribution: implemented=14, proposed=25, superseded=23 (total=62)
