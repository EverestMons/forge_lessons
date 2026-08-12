BEGIN IMMEDIATE;
.output /Users/marklehn/Developer/GitHub/lessons-forge/.bellows-worktrees/350/knowledge/qa/evidence/gate1-write-315-326-2026-08-11/outside-range-ids.txt
SELECT id||'|'||status||'|'||COALESCE(route,'')||'|'||COALESCE(status_updated_at,'') FROM lesson_proposals WHERE id <= 326 AND id NOT IN (315,316,317,318,319,320,321,322,323,324,325,326) ORDER BY id;
.output stdout
UPDATE lesson_proposals SET status='accepted', route='codify', status_updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now'), status_updated_by='ceo' WHERE id IN (315,316,317,318,319,324,325,326) AND status='proposed';
SELECT 'CHANGES_A='||changes();
SELECT 'GLOBOK_A='||COUNT(*) FROM lesson_proposals WHERE id IN (315,316,317,318,319,324,325,326) AND status_updated_at IS NOT NULL AND status_updated_at GLOB '20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]T[0-9][0-9]:[0-9][0-9]:[0-9][0-9]Z';
UPDATE lesson_proposals SET target_artifact='DRAFTING_CYCLE.md' WHERE id = 325 AND target_artifact='PLANNER_TEMPLATE.md';
SELECT 'CHANGES_T='||changes();
UPDATE lesson_proposals SET status='reference', route='reference', status_updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now'), status_updated_by='ceo' WHERE id IN (320,321,322,323) AND status='proposed';
SELECT 'CHANGES_R='||changes();
SELECT 'GLOBOK_R='||COUNT(*) FROM lesson_proposals WHERE id IN (320,321,322,323) AND status_updated_at IS NOT NULL AND status_updated_at GLOB '20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]T[0-9][0-9]:[0-9][0-9]:[0-9][0-9]Z';
COMMIT;
