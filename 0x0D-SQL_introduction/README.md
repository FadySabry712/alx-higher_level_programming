# SQL Project - Introduction

This project marks my initial venture into the world of SQL and relational databases. Throughout this journey, I practiced key concepts in data definition and data manipulation languages, crafted subqueries, and utilized various functions to interact with the database.

## Usage 🐬

The scripts provided in this project are designed to be executed in a MySQL environment. For instance, the script `3-list_tables.sql` can be run from the command line, taking the target database as an argument:

```bash
$ cat 3-list_tables.sql | mysql -h localhost -u root -p mysql

Tasks 📃
The following tasks represent the progression of my learning and the functionalities implemented in this project:

List Databases
File: 0-list_databases.sql
Description: MySQL script that lists all databases on the server.
Create a Database
File: 1-create_database.sql
Description: MySQL script that creates a new database named hbtn_0c_0.
Delete a Database
File: 2-remove_databases.sql
Description: MySQL script that deletes the database hbtn_0c_0.
List Tables
File: 3-list_tables.sql
Description: MySQL script that lists all tables in the current database.
Create First Table
File: 4-first_table.sql
Description: MySQL script that creates a table called first_table.
Schema:
id: INT
name: VARCHAR(256)
Full Table Description
File: 5-full_table.sql
Description: MySQL script that retrieves the full structure of first_table.
List All Values
File: 6-list_values.sql
Description: MySQL script that lists all rows from the first_table.
Insert First Value
File: 7-insert_value.sql
Description: MySQL script that inserts a new row into first_table.
Data:
id = 89
name = "Holberton School"
Count Records with ID 89
File: 8-count_89.sql
Description: MySQL script that counts the number of records with id = 89 in first_table.
Create and Populate Second Table
File: 9-full_creation.sql
Description: MySQL script that creates and populates a new table named second_table.
Schema:
id: INT
name: VARCHAR(256)
score: INT
Sample Records:
id = 1, name = "John", score = 10
id = 2, name = "Alex", score = 3
id = 3, name = "Bob", score = 14
id = 4, name = "George", score = 8
List Scores in Descending Order
File: 10-top_score.sql
Description: MySQL script that lists each record's score and name from second_table, ordered by score in descending order.
Select High-Scoring Records
File: 11-best_score.sql
Description: MySQL script that lists the score and name of records with a score of 10 or higher from second_table.
Update Bob's Score
File: 12-no_cheating.sql
Description: MySQL script that updates Bob's score to 10 in second_table.
Remove Low Scores
File: 13-change_class.sql
Description: MySQL script that deletes all records with a score of 5 or lower from second_table.
Compute Average Score
File: 14-average.sql
Description: MySQL script that calculates the average score of all entries in second_table.
Count Records by Score
File: 15-groups.sql
Description: MySQL script that counts and lists the number of records for each score in second_table, sorted by count in descending order.
Exclude Records without Names
File: 16-no_link.sql
Description: MySQL script that lists the score and name of records in second_table, excluding those without a name.
Convert Database to UTF8
File: 100-move_to_utf8.sql
Description: MySQL script that converts the hbtn_0c_0 database to UTF8 encoding.
Average Temperatures
File: 101-avg_temperatures.sql
Description: MySQL script displaying average temperatures (in Fahrenheit) by city, ordered in descending order.
Top Cities by Average Temperature
File: 102-top_city.sql
Description: MySQL script that displays the three cities with the highest average temperatures from July to August, sorted in descending order.
Maximum Temperature by State
File: 103-max_state.sql
Description: MySQL script that shows the maximum temperature recorded in each state, ordered by state name.
