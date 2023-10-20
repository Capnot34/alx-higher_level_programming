-- Lists all shows not of the genre "Comedy"
SELECT ts.title
FROM tv_shows ts
WHERE ts.id NOT IN (
    SELECT tsg.show_id
    FROM tv_show_genres tsg
    WHERE tsg.genre_id = (
        SELECT tg.id
        FROM tv_genres tg
        WHERE tg.name = 'Comedy'
    )
)
ORDER BY ts.title ASC;
