-- Script that displays the max temperature of each state (ordered by State name).
-- WHERE month > 6 AND month < 9 , WHERE month BETWEEN 7 AND 8, WHERE month IN (7, 8)
SELECT `state`, MAX(value) AS max_temp
FROM temperatures
GROUP BY `state`
ORDER BY `state` LIMIT 3;
