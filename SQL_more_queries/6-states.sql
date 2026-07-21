-- Script that creates the database hbtn_0d_usa and table states
-- Creates database hbtn_0d_usa if missing
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Uses hbtn_0d_usa database
USE hbtn_0d_usa;
-- Creates table states with auto-generated unique primary key
CREATE TABLE IF NOT EXISTS states (
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
