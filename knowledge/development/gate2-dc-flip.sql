BEGIN IMMEDIATE;
.output /Users/marklehn/Developer/GitHub/lessons-forge/.bellows-worktrees/346/knowledge/qa/evidence/gate2-dc-batch-2026-08-11/outside-range-ids.txt
SELECT id||'|'||category||'|'||status||'|'||COALESCE(route,'')||'|'||COALESCE(status_updated_at,'')||'|'||COALESCE(status_updated_by,'') FROM lesson_proposals WHERE id <= 314 AND id NOT IN (224,227,231,234,235,237,241,248,249,251,252,253,254,256,260,261,262,263,270,272,273,276,279,283,285,286,287,290,295,296,298,300,304,309,311,313) ORDER BY id;
.output stdout
UPDATE lesson_proposals SET status='implemented', status_updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now'), status_updated_by='ceo' WHERE id IN (224,227,231,234,235,237,241,248,249,251,252,253,254,256,260,261,262,263,270,272,273,276,279,283,285,286,287,290,295,296,298,300,304,309,311,313) AND status='accepted';
SELECT 'CHANGES='||changes();
SELECT 'GLOBOK='||COUNT(*) FROM lesson_proposals WHERE id IN (224,227,231,234,235,237,241,248,249,251,252,253,254,256,260,261,262,263,270,272,273,276,279,283,285,286,287,290,295,296,298,300,304,309,311,313) AND status_updated_at GLOB '20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]T[0-9][0-9]:[0-9][0-9]:[0-9][0-9]Z' AND status_updated_at NOT IN ('2026-08-09T01:20:01Z','2026-08-11T13:42:09+00:00');
COMMIT;
