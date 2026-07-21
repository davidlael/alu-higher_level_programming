-- Script that lists all records of second_table excluding rows without a name
-- Filters out NULL and empty names, sorted by score descending
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
