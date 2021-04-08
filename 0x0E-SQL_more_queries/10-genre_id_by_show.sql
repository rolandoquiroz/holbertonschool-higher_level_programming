-- Script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- Import the database dump from hbtn_0d_tvshows to your MySQL server
--  Each record displays: tv_shows.title - tv_show_genres.genre_id
--  Results are sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
--  You can use only one SELECT statement
--  The database name will be passed as an argument of the mysql command
-- Theta Join style solution: Projection(Selection(Cartesian product)):
-- SELECT tv_shows.title, tv_show_genres.genre_id
-- FROM tv_shows, tv_show_genres
-- WHERE tv_show_genres.genre_id >= 1
-- ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
-- ANSI style solution: 
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id >= 1
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
