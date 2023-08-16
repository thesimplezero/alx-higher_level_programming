-- List shows by rating.
-- Display each record as: tv_shows.title - rating sum.
-- Sort results by rating in descending order.
-- Use only one SELECT statement.

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;