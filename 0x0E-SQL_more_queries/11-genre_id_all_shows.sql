-- List all shows from hbtn_0d_tvshows.
-- Display each record as: tv_shows.title - tv_show_genres.genre_id.
-- Sort results by tv_shows.title and tv_show_genres.genre_id in ascending order.
-- Show NULL for shows without a genre.
-- Use only one SELECT statement.

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres
RIGHT JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;