-- Script that lists all records with a score >= 10 in second_table
-- Displays score and name ordered by top score first
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
