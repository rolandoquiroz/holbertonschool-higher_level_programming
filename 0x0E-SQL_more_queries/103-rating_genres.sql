-- Script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Import the database dump from hbtn_0d_tvshows_rate to your MySQL server
--  Each record should display: tv_genres.name - rating sum
--  Results must be sorted in descending order by their rating
--  You can use only one SELECT statement
--  The database name will be passed as an argument of the mysql command
SELECT tv_genres.`name`, SUM(tv_show_ratings.rate) AS rating
FROM tv_show_ratings
NATURAL JOIN tv_show_genres
INNER JOIN tv_genres
ON genre_id = tv_genres.id
GROUP BY tv_genres.`name`
ORDER BY rating DESC;
