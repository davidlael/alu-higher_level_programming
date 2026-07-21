-- Script that lists all cities of California without using JOIN
-- Selects cities where state_id matches California's state id via subquery
SELECT id, name FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
