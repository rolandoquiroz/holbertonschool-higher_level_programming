-- Script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
-- states description:
--  id INT unique, auto generated, can not be null and is a primary key
--  name VARCHAR(256) can’t be null
-- If the database hbtn_0d_usa already exists, this script does not fail
-- If the table states already exists, this script does not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    ID NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
    `name` VARCHAR(256) NOT NULL,
);
