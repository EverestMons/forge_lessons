-- Gate 1, cycle W=28 (plan 100007), the CEO's four author-conflict rulings 2026-09-01 ("go for it" on the Planner's coverage table)
-- 438 -> reference|backlog (plan_lint checks: QA .txt deposit; one-.md-first QA Deposits) ; 439, 440, 441 -> accepted|codify target DRAFTING_CYCLE.md
BEGIN IMMEDIATE;
CREATE TEMP TABLE g_pre(x INTEGER CHECK(x=4));
INSERT INTO g_pre SELECT COUNT(*) FROM lesson_proposals WHERE id IN (438,439,440,441) AND status='proposed' AND route IS NULL;
UPDATE lesson_proposals SET status='reference', route='backlog', target_artifact='bellows/scripts/plan_lint.py', status_updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now'), status_updated_by='ceo' WHERE id = 438 AND status='proposed';
UPDATE lesson_proposals SET status='accepted', route='codify', target_artifact='DRAFTING_CYCLE.md', status_updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now'), status_updated_by='ceo' WHERE id IN (439,440,441) AND status='proposed';
SELECT 'CHANGES_F='||changes();
CREATE TEMP TABLE g_post(x INTEGER CHECK(x=0));
INSERT INTO g_post SELECT COUNT(*) FROM lesson_proposals WHERE id IN (438,439,440,441) AND status='proposed';
SELECT 'ACC='||COUNT(*) FROM lesson_proposals WHERE status='accepted';
SELECT 'REF_BACKLOG='||COUNT(*) FROM lesson_proposals WHERE id=438 AND status='reference' AND route='backlog';
COMMIT;
