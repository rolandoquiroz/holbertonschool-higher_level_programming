-- Script that creates the table unique_id on your MySQL server.
SELECT id name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY cities.id;
