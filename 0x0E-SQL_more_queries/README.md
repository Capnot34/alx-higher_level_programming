# 🌟 0x0E. SQL - More queries 🌟

## 📚 Learning Objectives

- 🔐 How to create a new MySQL user
- ⚙️ How to manage privileges for a user to a database or table
- 🗝️ Comprehend the significance and use of `PRIMARY KEY` and `FOREIGN KEY` in relational databases.🔗
- ❗Understand the importance and application of `NOT NULL` and `UNIQUE` constraints.
- 🌐 Learn to retrieve data from multiple tables in one single request leveraging SQL capabilities.
- 🤔 Dive deep into the nuances of subqueries.
- 🤝 Grasp the concepts and differences of `JOIN` and `UNION` operations in SQL.

## 📜 Tasks

### [0. My privileges!](./0-privileges.sql)
Write a script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on your server (in localhost).

### [1. Root user](./1-create_user.sql)
Write a script that creates the MySQL server user `user_0d_1`.

### [2. Read user](./2-create_read_user.sql)
Write a script that creates the database `hbtn_0d_2` and the user `user_0d_2`.

### [3. Always a name](./3-force_name.sql)
Write a script that creates the table `force_name` on your MySQL server.

### [4. ID can't be null](./4-never_empty.sql)
Write a script that creates the table `id_not_null` on your MySQL server.

### [5. Unique ID](./5-unique_id.sql)
Write a script that creates the table `unique_id` on your MySQL server.

### [6. States table](./6-states.sql)
Write a script that creates the database `hbtn_0d_usa` and the table `states` on your MySQL server.

### [7. Cities table](./7-cities.sql)
Write a script that creates the database `hbtn_0d_usa` and the table `cities` on your MySQL server.

### [8. Cities of California](./8-cities_of_california_subquery.sql)
Write a script that lists all the cities of California that can be found in the database `hbtn_0d_usa`.

### [9. Cities by States](./9-cities_by_state_join.sql)
Write a script that lists all cities contained in the database `hbtn_0d_usa`.

### [10. Genre ID by show](./10-genre_id_by_show.sql)
Write a script that lists all shows contained in `hbtn_0d_tvshows` that have at least one genre linked.

### [11. Genre ID for all shows](./11-genre_id_all_shows.sql)
Write a script that lists all shows contained in the database `hbtn_0d_tvshows`.

### [12. No genre](./12-no_genre.sql)
Write a script that lists all shows contained in `hbtn_0d_tvshows` without a genre linked.

### [13. Number of shows by genre](./13-count_shows_by_genre.sql)
Write a script that lists all genres from `hbtn_0d_tvshows` and displays the number of shows linked to each.

### [14. My genres](./14-my_genres.sql)
Write a script that lists all genres of the show Dexter.

### [15. Only Comedy](./15-comedy_only.sql)
Write a script that lists all Comedy shows in the database `hbtn_0d_tvshows`.

### [16. List shows and genres](./16-shows_by_genre.sql)
Write a script that lists all shows, and all genres linked to that show, from the database `hbtn_0d_tvshows`.

### [17. Not my genre](./100-not_my_genres.sql)
Write a script that lists all genres not linked to the show Dexter.

### [18. No Comedy tonight!](./101-not_a_comedy.sql)
Write a script that lists all shows without the genre Comedy in the database `hbtn_0d_tvshows`.

### [19. Rotten tomatoes](./102-rating_shows.sql)
Write a script that lists all shows from `hbtn_0d_tvshows_rate` by their rating.

### [20. Mystery task!](./103-mystery_task.sql)
🔍 Write a script for this mysterious task. Find out what's hidden!

## 👤 Author
- Gift Amachree
