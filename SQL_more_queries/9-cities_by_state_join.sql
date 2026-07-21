-- Script that lists all cities contained in database hbtn_0d_usa
-- Displays cities.id, cities.name, and states.name sorted by cities.id
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
