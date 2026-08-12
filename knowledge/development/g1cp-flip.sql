BEGIN IMMEDIATE;
.output /Users/marklehn/Developer/GitHub/lessons-forge/.bellows-worktrees/360/knowledge/qa/evidence/gate1-write-327-332-2026-08-12/outside-range-ids.txt
SELECT id||'|'||status||'|'||COALESCE(route,'')||'|'||COALESCE(status_updated_at,'') FROM lesson_proposals WHERE id <= 332 AND id NOT IN (327,328,329,330,331,332) ORDER BY id;
.output stdout
UPDATE lesson_proposals SET status='accepted', route='codify', status_updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now'), status_updated_by='ceo' WHERE id IN (327,328,329,330,332) AND status='proposed';
SELECT 'CHANGES_A='||changes();
SELECT 'GLOBOK_A='||COUNT(*) FROM lesson_proposals WHERE id IN (327,328,329,330,332) AND status='accepted' AND route='codify' AND status_updated_at GLOB '20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]T[0-9][0-9]:[0-9][0-9]:[0-9][0-9]Z';
UPDATE lesson_proposals SET status='reference', route='backlog', status_updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now'), status_updated_by='ceo' WHERE id = 331 AND status='proposed';
SELECT 'CHANGES_P='||changes();
SELECT 'GLOBOK_P='||COUNT(*) FROM lesson_proposals WHERE id = 331 AND status='reference' AND route='backlog' AND status_updated_at GLOB '20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]T[0-9][0-9]:[0-9][0-9]:[0-9][0-9]Z';
COMMIT;
