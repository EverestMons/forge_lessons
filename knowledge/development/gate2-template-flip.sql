BEGIN IMMEDIATE;
.output /Users/marklehn/Developer/GitHub/lessons-forge/.bellows-worktrees/345/knowledge/qa/evidence/gate2-template-batch-2026-08-11/outside-range-ids.txt
SELECT id||'|'||category||'|'||status||'|'||COALESCE(route,'')||'|'||COALESCE(status_updated_at,'')||'|'||COALESCE(status_updated_by,'') FROM lesson_proposals WHERE id <= 314 AND id NOT IN (223,225,226,228,229,230,236,239,240,242,243,244,250,255,257,264,265,266,267,268,269,274,277,280,281,282,284,288,289,293,297,303,305,306,307,310,314) ORDER BY id;
.output stdout
UPDATE lesson_proposals SET status='implemented', status_updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now'), status_updated_by='ceo' WHERE id IN (223,225,226,228,229,230,236,239,240,242,243,244,250,255,257,264,265,266,267,268,269,274,277,280,281,282,284,288,289,293,297,303,305,306,307,310,314) AND status='accepted';
SELECT 'CHANGES='||changes();
SELECT 'GLOBOK='||COUNT(*) FROM lesson_proposals WHERE id IN (223,225,226,228,229,230,236,239,240,242,243,244,250,255,257,264,265,266,267,268,269,274,277,280,281,282,284,288,289,293,297,303,305,306,307,310,314) AND status_updated_at GLOB '20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]T[0-9][0-9]:[0-9][0-9]:[0-9][0-9]Z' AND status_updated_at NOT IN ('2026-08-09T01:20:01Z','2026-08-11T13:42:09+00:00');
COMMIT;
