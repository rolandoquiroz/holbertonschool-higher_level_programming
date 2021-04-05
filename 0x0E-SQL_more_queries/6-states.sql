-- Script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
-- states description:
--  id INT unique, auto generated, can not be null and is a primary key
--  name VARCHAR(256) can not be null
-- If the database hbtn_0d_usa already exists, this script does not fail
-- If the table states already exists, this script does not fail
-- SERIAL DEFAULT VALUE = NOT NULL AUTO_INCREMENT UNIQUE = UNIQUE AUTO_INCREMENT NOT NULL
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT SERIAL DEFAULT VALUE PRIMARY KEY,
    `name` VARCHAR(256) NOT NULL
);
