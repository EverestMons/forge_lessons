BEGIN IMMEDIATE;
SELECT 'PRE='||COUNT(*) FROM lesson_proposals WHERE id BETWEEN 337 AND 346 AND status='proposed';
.output /Users/marklehn/Developer/GitHub/lessons-forge/.bellows-worktrees/402/knowledge/qa/evidence/gate1-write-337-346-2026-08-13/flip-capture.txt
SELECT id||'|'||status||'|'||COALESCE(route,'')||'|'||category||'|'||COALESCE(status_updated_by,'')||'|'||COALESCE(status_updated_at,'') FROM lesson_proposals WHERE id <= 336 ORDER BY id;
.output stdout
UPDATE lesson_proposals SET status='implemented', status_updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now'), status_updated_by='ceo' WHERE id IN (337,338,339) AND status='proposed';
SELECT 'CH_I='||changes();
UPDATE lesson_proposals SET status='reference', route='reference', status_updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now'), status_updated_by='ceo' WHERE id IN (343,344,345) AND status='proposed';
SELECT 'CH_R='||changes();
UPDATE lesson_proposals SET status='accepted', route='codify', status_updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now'), status_updated_by='ceo' WHERE id IN (340,341,342,346) AND status='proposed';
SELECT 'CH_A='||changes();
SELECT 'GLOBOK='||COUNT(*) FROM lesson_proposals WHERE id BETWEEN 337 AND 346 AND status_updated_at GLOB '20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]T[0-9][0-9]:[0-9][0-9]:[0-9][0-9]Z';
SELECT 'PROP_POST='||COUNT(*) FROM lesson_proposals WHERE status='proposed';
SELECT 'ACC_POST='||COUNT(*) FROM lesson_proposals WHERE status='accepted';
SELECT 'IMPL_POST='||COUNT(*) FROM lesson_proposals WHERE status='implemented';
SELECT 'REF_POST='||COUNT(*) FROM lesson_proposals WHERE status='reference';
SELECT 'TOT='||COUNT(*) FROM lesson_proposals;
COMMIT;
