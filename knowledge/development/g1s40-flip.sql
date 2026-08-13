BEGIN IMMEDIATE;
.output /Users/marklehn/Developer/GitHub/lessons-forge/.bellows-worktrees/384/knowledge/qa/evidence/gate1-write-333-336-2026-08-13/outside-range-ids.txt
SELECT id||'|'||status||'|'||COALESCE(route,'')||'|'||COALESCE(status_updated_at,'') FROM lesson_proposals WHERE id <= 336 AND id NOT IN (333,334,335,336) ORDER BY id;
.output stdout
UPDATE lesson_proposals SET status='accepted', route='codify', status_updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now'), status_updated_by='ceo' WHERE id IN (333,334,335,336) AND status='proposed';
SELECT 'CHANGES_A='||changes();
SELECT 'GLOBOK_A='||COUNT(*) FROM lesson_proposals WHERE id IN (333,334,335,336) AND status='accepted' AND route='codify' AND status_updated_at GLOB '20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]T[0-9][0-9]:[0-9][0-9]:[0-9][0-9]Z';
COMMIT;
