-- List shows without linked genres.
-- Sort by tv_shows.title and tv_show_genres.genre_id in ascending order.
-- Display each record as: tv_shows.title - tv_show_genres.genre_id.
-- Use only one SELECT statement.

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres
RIGHT JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.show_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;