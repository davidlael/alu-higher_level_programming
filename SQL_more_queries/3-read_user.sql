-- Creates database user_2_db; user_0d_2 only gets SELECT and INSERT on it
CREATE DATABASE IF NOT EXISTS user_2_db;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'user_0d_2'@'localhost';
GRANT SELECT, INSERT ON user_2_db.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
