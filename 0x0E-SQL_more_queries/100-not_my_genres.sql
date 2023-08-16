-- List genres not linked to the show Dexter.
-- Retrieve from tv_genres table excluding genres linked to show Dexter (id may vary).
-- Display each record as: tv_genres.name.
-- Sort results by genre name in ascending order.
-- Use a maximum of two SELECT statements.

SELECT name 
FROM tv_genres
WHERE name NOT IN (
    SELECT name 
    FROM tv_genres
    LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
    LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
    WHERE tv_shows.title = 'Dexter'
  )
GROUP BY name
ORDER BY name ASC;