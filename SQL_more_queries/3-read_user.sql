-- Creates database user_2_db, gives user_0d_2 only SELECT and INSERT on it
CREATE DATABASE IF NOT EXISTS user_2_db;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT, INSERT ON user_2_db.* TO 'user_0d_2'@'localhost';
