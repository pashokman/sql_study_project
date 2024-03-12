# SQL training project

Here I practice to interact with the database in SQL using Python.

## List of tests
### Marvels
* `test_connection` - test creates a database file and connects to it;
* `test_create_marvels_table` - test creates a table with data from an external file - `marvels.py`;
* `test_get_marvels_table_data` - test gets all table data and checks if some characters in it;
* `test_assign_to_characters_intelligence_text_value` - test gets a table with columns `name`, `inteligence`, and creates a `grade` column in which I assign the text value for an inteligence value range;
* `test_filter_characters_by_gender_hometown_energy_Projection` - test filters all table by `gender`, `hometown`, `energy_Projection` values, and checks if there are expected characters in it;
* `test_can_all_characters_defeat_one_strong_badguy` - test checks if all characters can defeat the badguy (if their sum of every passed parameter is greater than same parameter of a badguy). By default using parameters - `intelligence`, `strength`, `speed`, `energy_Projection`, `fighting_Skills`;
* `test_characters_with_popularity_or_weight` - test filter characters by popularity or weight;
* `test_group_characters_by_param` - test grouped characters by parameter. By default using `alignment`.

### Students
* `test_create_students_and_students_grades_tables` - test creates 2 tables - `students`, `students_grades`;
* `test_get_both_tables_data` - test gets all data from 2 tables (`students`, `students_grades`) and checks if there a few expected rows;
* `test_get_both_tables_data_cross_join` - test gets data from 2 tables through CROSS JOIN;
* `test_get_both_tables_implicit_inner_join` - test gets data from 2 tables through IMPLICIT INNER JOIN;
* `test_get_both_tables_explicit_inner_join` - test gets data from 2 tables through EXPLICIT INNER JOIN;
* `test_create_students_projects_table` - test creates a table `students_projects`;
* `test_get_both_tables_left_outer_join` - test gets data from 2 tables (`students`, `students_projects`) through LEFT OUTER JOIN (return all rows from left table even if there is no match vs the right table).

### Movies
* `test_self_join` - test gets data from one table and JOIN them with the same table;
* `test_add_new_movie` - test checks if a new movie is in the base and then adds it into the base;
* `test_delete_movie` - test checks if a new movie is in the base and then deletes it;
* `test_add_new_column` - test checks columns count and then adds a new one, and checks columns count one more time;
* `test_delete_column` - test checks if a new columns already in the table and then deletes it;
* `test_update_movie_released_year` - test updates released year of the movie and returns default value.


## What I practice:
* how to create a table (CREATE TABLE); 
```
CREATE TABLE table_name (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                         name TEXT, 
                         age INTEGER, 
                         height REAL);
```

* how to get all data from a table (SELECT);
```
SELECT * FROM table_name;
```

* how to get some columns from a table (SELECT); 
```
SELECT [list of columns names] FROM table_name;
```

* how to create a column and assign values in it, based by the values of another column (CASE);
```
SELECT column_name1, column_name2,\
    CASE\
        WHEN column_name2 > value THEN 'Best'\
        WHEN column_name2 = value THEN 'Common'\
        ELSE 'Silly'
    END as 'new_column_name'
FROM table_name;
```

* how to filter table data by some columns (AND);
```
SELECT * FROM table_name 
WHERE column1_value = 'some_value1' AND column2_value = 'some_value2';
```

* how to sum values of a column and compare it with expected value (SUM);
```
SELECT SUM(column_name) FROM table_name;
```

* how to filter table data by some columns (OR);
```
SELECT * FROM table_name 
WHERE column1_name > 'some_value1' OR column2_name < 'some_value2';
```

* how to count entries of some value in the column (GROUP BY);
```
SELECT column1_name, COUNT(*) FROM table_name GROUP BY column1_name;
```

* how to join tables (CROSS JOIN, IMPLICIT INNER JOIN, EXPLICIT INNER JOIN, LEFT OUTER JOIN, LEFT OUTER SELF JOIN);  
```CROSS JOIN``` - return all data from 2 tables;
```
SELECT * FROM table1_name, table2_name;
```

```IMPLICIT INNER JOIN``` - returns only rows that have mached in 2 tables;
```
SELECT * FROM table1_name, table2_name
WHERE table1_name.id = table2_name.student_id;
```

```EXPLICIT INNER JOIN``` (best practice) - returns only rows that have mached in 2 tables;
```
SELECT * FROM table1_name
JOIN table2_name
ON table1_name.id = table2_name.student_id
```

```LEFT OUTER JOIN``` - returns all rows from left table, even if they does not have a match with right table (NULL values returns in cells where their is no match)
```
SELECT * FROM table1_name
LEFT OUTER JOIN table2_name
ON table1_name.id = table2_name.student_id
```

```LEFT OUTER SELF JOIN``` - the same as previous, but only with 1 table
```
SELECT table1_name.title, new_table1_name.title as new_title
FROM table1_name
LEFT OUTER JOIN table1_name new_table1_name
ON table1_name.sequals_id = sequals_id;
```

* how to separate methods between different database classes, to make classes more readable and simple;

* how to add a new record into the table (INSERT INTO);
```
INSERT INTO table_name (id, name, age, height) VALUES (167, 'Jack Riecher', 37, 208);
```

* how to delete a record from the database (DELETE FROM);
```
DELETE FROM table1_name WHERE column_name = 'some_value';
```

* how to add a new column into the table (ALTER);
```
ALTER TABLE table_name ADD column_name column_data_type
```

* how to delete a column from the table (ALTER);
```
ALTER TABLE table_name DROP COLUMN column_name;
```

* how to update a record into the table (UPDATE).
```
UPDATE table_name SET column1_name = 'some_value1'
WHERE table_name.column2_name = 'some_value2';
```



## Commands to run tests:
* run all tests and get all output data in console: 
```
python -m pytest -v -s
```

* run tests with specific marker (run only marvels tests):
```
python -m pytest -m marvels -v -s
```
* run all tests and make allure report. First command should run in VS Code bash terminal, second one in cmd from root folder:
```
python -m pytest -v -s --alluredir="./Reports"
allure serve "./Reports"
```