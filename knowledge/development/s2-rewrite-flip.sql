BEGIN IMMEDIATE;
.output /Users/marklehn/Developer/GitHub/lessons-forge/.bellows-worktrees/348/knowledge/qa/evidence/s2-rewrite-2026-08-11/outside-range-ids.txt
SELECT id||'|'||category||'|'||status||'|'||COALESCE(route,'')||'|'||COALESCE(status_updated_at,'')||'|'||COALESCE(status_updated_by,'') FROM lesson_proposals WHERE id <= 314 AND id NOT IN (233,238,246,247,258,259,271,275,278,292,302,308) ORDER BY id;
.output stdout
UPDATE lesson_proposals SET status='implemented', route='codify', status_updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now'), status_updated_by='ceo' WHERE id IN (233,238,246,247,258,259,271,275,278,292,302,308) AND status='reference' AND route='backlog';
SELECT 'CHANGES='||changes();
SELECT 'GLOBOK='||COUNT(*) FROM lesson_proposals WHERE id IN (233,238,246,247,258,259,271,275,278,292,302,308) AND status_updated_at GLOB '20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]T[0-9][0-9]:[0-9][0-9]:[0-9][0-9]Z' AND status_updated_at NOT IN ('2026-08-09T01:20:01Z','2026-08-11T13:42:09+00:00');
COMMIT;
