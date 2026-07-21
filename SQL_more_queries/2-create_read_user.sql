-- Script that creates the database hbtn_0d_2 and the user user_0d_2
-- Creates database hbtn_0d_2 if missing
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Creates user user_0d_2 if missing
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Grants SELECT privilege on hbtn_0d_2 database to user_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
