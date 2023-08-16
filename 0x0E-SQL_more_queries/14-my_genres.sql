-- List genres of the show Dexter.
-- Retrieve from tv_shows table with title = Dexter (id may vary).
-- Display each record as: tv_genres.name.
-- Sort results by genre name in ascending order.
-- Use only one SELECT statement.

SELECT tv_genres.name
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;