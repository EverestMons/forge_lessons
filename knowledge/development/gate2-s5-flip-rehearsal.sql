BEGIN IMMEDIATE;
SELECT 'PRE='||COUNT(*) FROM lesson_proposals WHERE id IN (232,245) AND status='accepted' AND route='codify';
ROLLBACK;
