SQL - Additional Queries
In this project, I focused on enhancing my SQL skills by practicing various queries, including permissions, joins, and constraints.

Usage 🐬
The script 3-force_name.sql requires the database to query from as a MySQL command line argument:

bash

Copy
$ cat 3-force_name.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
Tasks 3-101 query from the database defined in hbtn_0d_tvshows.sql, while tasks 102-103 query from hbtn_0d_tvshows_rate.sql.

Tasks 📃
My Privileges
File: 0-privileges.sql
Description: This MySQL script lists all privileges for users user_0d_1 and user_0d_2.
Root User
File: 1-create_user.sql
Description: This script creates the user user_0d_1 with all privileges and the password user_0d_1_pwd.
Read User
File: 2-create_read_user.sql
Description: This script creates the database hbtn_0d_2 and the user user_0d_2 with the password user_0d_2_pwd, granting user_0d_2 only SELECT privileges on hbtn_0d_2.
Always a Name
File: 3-force_name.sql
Description: This script creates a table called force_name with the following structure:
id: INT
name: VARCHAR(256) (not nullable)
ID Can't Be Null
File: 4-never_empty.sql
Description: This script creates the table id_not_null with the following structure:
id: INT (default value = 1)
name: VARCHAR(256)
Unique ID
File: 5-unique_id.sql
Description: This script creates the table unique_id with the following structure:
id: INT (default value = 1, must be unique)
name: VARCHAR(256)
States Table
File: 6-states.sql
Description: This script creates the database hbtn_0d_usa with a states table structured as follows:
id: INT (unique, auto-generated, not nullable, primary key)
name: VARCHAR(256) (not nullable)
Cities Table
File: 7-cities.sql
Description: This script creates the cities table within the hbtn_0d_usa database, structured as follows:
id: INT (unique, auto-generated, not nullable, primary key)
state_id: INT (not nullable, foreign key referencing id in the states table)
name: VARCHAR(256) (not nullable)
Cities of California
File: 8-cities_of_california_subquery.sql
Description: This script lists all cities in California from the hbtn_0d_usa database, ordered by ascending city ID.
Cities by States
File: 9-cities_by_state_join.sql
Description: This script lists all cities in the hbtn_0d_usa database, ordered by ascending city ID.
Genre ID by Show
File: 10-genre_id_by_show.sql
Description: This script lists all shows in hbtn_0d_tvshows that have at least one linked genre, ordered by ascending tv_shows.title and tv_show_genres.genre_id.
Genre ID for All Shows
File: 11-genre_id_all_shows.sql
Description: This script lists all shows in hbtn_0d_tvshows, ordered by ascending tv_shows.title and tv_show_genres.genre_id. If a show lacks a genre, it shows NULL.
No Genre
File: 12-no_genre.sql
Description: This script lists all shows in hbtn_0d_tvshows that do not have a linked genre, ordered by ascending tv_shows.title and tv_show_genres.genre_id.
Number of Shows by Genre
File: 13-count_shows_by_genre.sql
Description: This script lists all genres from hbtn_0d_tvshows, showing the count of linked shows per genre, ordered by descending show count. Genres with no shows are excluded.
My Genres
File: 14-my_genres.sql
Description: This script lists all genres for the show Dexter in the hbtn_0d_tvshows database, ordered by ascending genre name.
Only Comedy
File: 15-comedy_only.sql
Description: This script lists all comedy shows in the hbtn_0d_tvshows database, ordered by ascending show title.
List Shows and Genres
File: 16-shows_by_genre.sql
Description: This script lists all shows and their linked genres from the hbtn_0d_tvshows database, ordered by ascending show title and genre name.
Not My Genre
File: 100-not_my_genres.sql
Description: This script lists all genres not linked to the show Dexter, in the hbtn_0d_tvshows database, ordered by ascending genre name.
No Comedy Tonight!
File: 101-not_a_comedy.sql
Description: This script lists all shows in the hbtn_0d_tvshows database that do not have the comedy genre, ordered by ascending show title.
Rotten Tomatoes
File: 102-rating_shows.sql
Description: This script lists all shows in hbtn_0d_tvshows_rate, ordered by descending rating.
Best Genre
File: 103-rating_genres.sql
Description: This script lists all genres in the hbtn_0d_tvshows_rate database, ordered by descending rating.
