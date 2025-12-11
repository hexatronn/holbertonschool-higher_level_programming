-- List all cities of California

-- Select cities with state_id of California
SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id FROM states WHERE name = "California"
)
ORDER BY id;
