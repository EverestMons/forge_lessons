BEGIN IMMEDIATE;
.output /Users/marklehn/Developer/GitHub/lessons-forge/.bellows-worktrees/353/knowledge/qa/evidence/gate2-dc5-2026-08-11/outside-range-ids.txt
SELECT id||'|'||category||'|'||status||'|'||COALESCE(route,'')||'|'||COALESCE(status_updated_at,'')||'|'||COALESCE(status_updated_by,'') FROM lesson_proposals WHERE id <= 326 AND id NOT IN (315,317,318,319,325) ORDER BY id;
.output stdout
UPDATE lesson_proposals SET status='implemented', status_updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now'), status_updated_by='ceo' WHERE id IN (315,317,318,319,325) AND status='accepted';
SELECT 'CHANGES='||changes();
SELECT 'GLOBOK='||COUNT(*) FROM lesson_proposals WHERE id IN (315,317,318,319,325) AND status_updated_at GLOB '20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]T[0-9][0-9]:[0-9][0-9]:[0-9][0-9]Z' AND status_updated_at NOT IN ('2026-08-12T00:29:31Z');
COMMIT;
