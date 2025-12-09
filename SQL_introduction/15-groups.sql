-- Lists the number of records for each score in second_table
-- Displays score and count of records grouped by score
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
