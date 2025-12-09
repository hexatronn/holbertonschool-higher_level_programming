-- Removes all records from second_table with a score less than or equal to 5
-- Cleans low-scoring students from the table
DELETE FROM second_table
WHERE score <= 5;
