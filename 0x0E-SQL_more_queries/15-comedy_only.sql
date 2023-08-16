-- List all comedy shows from hbtn_0d_tvshows.
-- Retrieve from tv_genres table with name = Comedy (id may vary).
-- Display each record as: tv_shows.title.
-- Sort results by show title in ascending order.
-- Use only one SELECT statement.

SELECT tv_shows.title
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = "comedy"
ORDER BY tv_shows.title;