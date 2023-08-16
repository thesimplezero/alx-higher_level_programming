-- List shows from hbtn_0d_tvshows with linked genres.
-- Display: tv_shows.title - tv_show_genres.genre_id.
-- Sort by tv_shows.title and tv_show_genres.genre_id in ascending order.
-- Use only one SELECT statement.

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres
INNER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;