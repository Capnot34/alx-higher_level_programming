-- This query lists all TV shows from the hbtn_0d_tvshows database 
-- that do not have an associated genre. For each TV show, 
-- the title and genre_id (which will be NULL) are displayed.
-- The results are sorted by the TV show title in ascending order.

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC;

