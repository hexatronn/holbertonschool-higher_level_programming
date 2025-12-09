-- Lists records from second_table with score greater than or equal to 10
-- Displays score and name ordered by highest score first
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
