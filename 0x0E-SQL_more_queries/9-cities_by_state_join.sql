-- List all cities in hbtn_0d_usa database.
-- Each record: cities.id - cities.name - states.name.
-- Sort results by cities.id in ascending order.
-- Use only one SELECT statement.

SELECT cities.id, cities.name, states.name
FROM cities
LEFT JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;