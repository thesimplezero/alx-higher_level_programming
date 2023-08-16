-- List all genres and their linked show counts.
-- Display: <TV Show genre> - <Number of shows linked to this genre>.
-- Column names: genre, number_of_shows.
-- Exclude genres without linked shows.
-- Sort results by the number of linked shows in descending order.
-- Use only one SELECT statement.

SELECT tv_genres.name AS 'genre', COUNT(tv_show_genres.genre_id)
AS 'number_of_shows'
FROM tv_genres
INNER JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY genre
ORDER BY number_of_shows DESC;