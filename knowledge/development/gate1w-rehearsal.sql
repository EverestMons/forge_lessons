BEGIN IMMEDIATE;
SELECT 'PRE='||COUNT(*) FROM lesson_proposals WHERE id BETWEEN 315 AND 326 AND status='proposed' AND status_updated_at IS NULL;
SELECT 'PRE_A='||COUNT(*) FROM lesson_proposals WHERE id IN (315,316,317,318,319,324,325,326) AND status='proposed';
SELECT 'PRE_R='||COUNT(*) FROM lesson_proposals WHERE id IN (320,321,322,323) AND status='proposed';
ROLLBACK;
