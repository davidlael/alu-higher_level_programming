-- Script that creates the table force_name on your MySQL server
-- Creates table force_name where name cannot be NULL
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
