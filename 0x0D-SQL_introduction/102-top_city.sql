-- Import in hbtn_0c_0 database the table temperatures.sql
-- Script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
SELECT city, AVG(`value`) AS avg_temp
FROM hbtn_0c_0.temperatures
WHERE `month` >= 7 AND `month` <= 8 -- WHERE `month` = 7 OR `month` = 8, WHERE `month` IN (7, 8), WHERE `month` BETWEEN 7 AND 8
GROUP BY city
ORDER BY avg_temp DESC LIMIT 3;
