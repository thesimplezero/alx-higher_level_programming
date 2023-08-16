-- List all cities of California from hbtn_0d_usa database.
-- Retrieve cities using the states table's single record where name is California; id may vary.
-- Prohibited from using the JOIN keyword.

SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'california'
)
ORDER BY id ASC;