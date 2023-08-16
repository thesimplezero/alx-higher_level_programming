-- List all shows and their linked genres.
-- Display each record as: tv_shows.title - tv_genres.name.
-- Show NULL in genre column if a show has no genre.
-- Sort results by show title and genre name in ascending order.
-- Use only one SELECT statement.

SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title, tv_genres.name;