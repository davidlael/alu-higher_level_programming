-- Script that creates the database hbtn_0d_usa and table cities
-- Creates database hbtn_0d_usa if missing
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Uses hbtn_0d_usa database
USE hbtn_0d_usa;
-- Creates table cities with foreign key referencing states(id)
CREATE TABLE IF NOT EXISTS cities (
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
