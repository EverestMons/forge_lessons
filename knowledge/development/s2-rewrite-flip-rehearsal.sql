BEGIN IMMEDIATE;
SELECT 'PRE='||COUNT(*) FROM lesson_proposals WHERE id IN (233,238,246,247,258,259,271,275,278,292,302,308) AND status='reference' AND route='backlog';
SELECT 'PRE_OLD='||COUNT(*) FROM lesson_proposals WHERE id IN (233,238,246,247,258,259,271) AND status='reference' AND route='backlog';
SELECT 'PRE_NEW='||COUNT(*) FROM lesson_proposals WHERE id IN (275,278,292,302,308) AND status='reference' AND route='backlog';
SELECT 'RB='||COUNT(*) FROM lesson_proposals WHERE status='reference' AND route='backlog';
SELECT 'MAXID='||MAX(id) FROM lesson_proposals;
.output /Users/marklehn/Developer/GitHub/lessons-forge/.bellows-worktrees/348/knowledge/qa/evidence/s2-rewrite-2026-08-11/pre-flip-state.txt
SELECT id||'|'||category||'|'||status||'|'||COALESCE(route,'')||'|'||COALESCE(status_updated_by,'')||'|'||COALESCE(status_updated_at,'') FROM lesson_proposals WHERE id IN (233,238,246,247,258,259,271,275,278,292,302,308) ORDER BY id;
.output stdout
ROLLBACK;
