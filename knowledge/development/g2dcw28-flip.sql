BEGIN IMMEDIATE;
CREATE TEMP TABLE g_pre(x INTEGER CHECK(x=8));
INSERT INTO g_pre VALUES((SELECT COUNT(*) FROM lesson_proposals WHERE id IN (426,427,428,429,432,439,440,441) AND status='accepted' AND route='codify'));
SELECT 'PRE_F='||x FROM g_pre;
.output knowledge/qa/evidence/gate2-dc-w28-2026-09-01/flip-capture.txt
SELECT id||'|'||status||'|'||COALESCE(route,'')||'|'||category||'|'||COALESCE(status_updated_by,'')||'|'||COALESCE(status_updated_at,'') FROM lesson_proposals WHERE id <= 441 AND id NOT IN (426,427,428,429,432,439,440,441) ORDER BY id;
.output stdout
UPDATE lesson_proposals SET status='implemented', status_updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now'), status_updated_by='ceo' WHERE id IN (426,427,428,429,432,439,440,441) AND status='accepted' AND route='codify';
SELECT 'CHANGES_F='||changes();
SELECT 'EXCL_F='||COUNT(*) FROM lesson_proposals WHERE id IN (426,427,428,429,432,439,440,441) AND status='implemented' AND status_updated_at GLOB '20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]T[0-9][0-9]:[0-9][0-9]:[0-9][0-9]Z' AND status_updated_at NOT IN ('2026-09-01T22:03:28Z','2026-09-01T21:58:31Z');
SELECT 'ACC_POST='||COUNT(*) FROM lesson_proposals WHERE status='accepted';
SELECT 'IMPL_POST='||COUNT(*) FROM lesson_proposals WHERE status='implemented';
COMMIT;
