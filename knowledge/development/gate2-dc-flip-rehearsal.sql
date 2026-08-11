BEGIN IMMEDIATE;
SELECT 'PRE='||COUNT(*) FROM lesson_proposals WHERE id IN (224,227,231,234,235,237,241,248,249,251,252,253,254,256,260,261,262,263,270,272,273,276,279,283,285,286,287,290,295,296,298,300,304,309,311,313) AND status='accepted' AND route='codify';
SELECT 'ACC='||COUNT(*) FROM lesson_proposals WHERE status='accepted' AND route='codify';
SELECT 'MAXID='||MAX(id) FROM lesson_proposals;
ROLLBACK;
