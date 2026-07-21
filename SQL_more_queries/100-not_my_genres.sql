-- Script that lists all genres not linked to the show Dexter
-- Uses a subquery to exclude genres attached to Dexter
SELECT name FROM tv_genres
WHERE id NOT IN (
    SELECT tv_genres.id
    FROM tv_genres
    JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
    JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
    WHERE tv_shows.title = 'Dexter'
)
ORDER BY name ASC;
