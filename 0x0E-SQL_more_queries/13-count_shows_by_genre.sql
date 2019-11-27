-- Lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT tv_genres.name AS genre, COUNT(*) AS number_shows FROM tv_genres
LEFT OUTER JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id WHERE tv_show_genres.genre_id = tv_show_genres.genre_id
GROUP BY genre ORDER BY number_shows DESC;
