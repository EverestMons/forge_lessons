BEGIN IMMEDIATE;
SELECT 'PRE='||COUNT(*) FROM lesson_proposals WHERE id IN (315,317,318,319,325) AND status='accepted' AND route='codify';
SELECT 'ACC='||COUNT(*) FROM lesson_proposals WHERE status='accepted' AND route='codify';
SELECT 'MAXID='||MAX(id) FROM lesson_proposals;
ROLLBACK;
