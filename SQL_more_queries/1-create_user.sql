-- Script that creates the MySQL server user user_0d_1
-- Creates user_0d_1 with all privileges and password user_0d_1_pwd if not exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Grants all privileges on all databases to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
