-- Script that lists all the cities of California that can be found in the database hbtn_0d_usa.
-- The states table contains only one record where name = California (but the id can be different, as per the example)
-- Results must be sorted in ascending order by cities.id
-- You are not allowed to use the JOIN keyword
-- The database name will be passed as an argument of the mysql command
-- Subquery solution:
-- SELECT id, `name`
-- FROM cities
-- WHERE state_id =
--	(SELECT id
-- 	 FROM states
--	 WHERE `name` = 'California')
-- ORDER BY id ASC;
-- Theta Join style solution: Projection(Selection(Cartesian product)):
SELECT cities.id, cities.`name`
FROM cities, states
WHERE cities.state_id = 1 AND states.`name` = 'California' 
ORDER BY cities.id ASC;
