BEGIN IMMEDIATE;
SELECT 'PRE='||COUNT(*) FROM lesson_proposals WHERE id BETWEEN 327 AND 332 AND status='proposed' AND status_updated_at IS NULL;
SELECT 'PRE_A='||COUNT(*) FROM lesson_proposals WHERE id IN (327,328,329,330,332) AND status='proposed';
SELECT 'PRE_P='||COUNT(*) FROM lesson_proposals WHERE id = 331 AND status='proposed';
ROLLBACK;
