BEGIN IMMEDIATE;
SELECT 'PRE_A='||COUNT(*) FROM lesson_proposals WHERE id IN (347,348,350,352) AND status='proposed';
SELECT 'PRE_R='||COUNT(*) FROM lesson_proposals WHERE id IN (349,351) AND status='proposed';
.output /Users/marklehn/Developer/GitHub/lessons-forge/.bellows-worktrees/416/knowledge/qa/evidence/gate1-write-347-352-2026-08-14/route-capture.txt
SELECT id||'|'||status||'|'||COALESCE(route,'')||'|'||category||'|'||COALESCE(status_updated_by,'')||'|'||COALESCE(status_updated_at,'') FROM lesson_proposals WHERE id <= 352 AND id NOT IN (347,348,349,350,351,352) ORDER BY id;
.output stdout
UPDATE lesson_proposals SET status='accepted', route='codify', status_updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now'), status_updated_by='ceo' WHERE id IN (347,348,350,352) AND status='proposed';
SELECT 'CHANGES_A='||changes();
UPDATE lesson_proposals SET status='reference', route='reference', status_updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now'), status_updated_by='ceo' WHERE id IN (349,351) AND status='proposed';
SELECT 'CHANGES_R='||changes();
SELECT 'STAMP_A='||COUNT(*) FROM lesson_proposals WHERE id IN (347,348,350,352) AND status_updated_at IS NOT NULL AND status_updated_at GLOB '20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]T[0-9][0-9]:[0-9][0-9]:[0-9][0-9]Z';
SELECT 'STAMP_R='||COUNT(*) FROM lesson_proposals WHERE id IN (349,351) AND status_updated_at IS NOT NULL AND status_updated_at GLOB '20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]T[0-9][0-9]:[0-9][0-9]:[0-9][0-9]Z';
SELECT 'ACC_POST='||COUNT(*) FROM lesson_proposals WHERE status='accepted';
SELECT 'PROP_POST='||COUNT(*) FROM lesson_proposals WHERE status='proposed';
SELECT 'REF_POST='||COUNT(*) FROM lesson_proposals WHERE status='reference';
SELECT 'IMPL_POST='||COUNT(*) FROM lesson_proposals WHERE status='implemented';
COMMIT;
