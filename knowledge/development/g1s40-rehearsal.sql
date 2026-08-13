BEGIN IMMEDIATE;
SELECT 'PRE='||COUNT(*) FROM lesson_proposals WHERE id BETWEEN 333 AND 336 AND status='proposed' AND status_updated_at IS NULL;
ROLLBACK;
