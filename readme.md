# SQL training project

Here I practice to interact with the database in SQL using Python.

## List of tests
### Marvels
* `test_connection` - test creates a database file and connect to it;
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
* `test_get_both_tables_left_outer_join` - test gets data from 2 tables (`students`, `stidents_projects`) through LEFT OUTER JOIN;


## What I practice:
* how to create a table (CREATE);
* how to get all data from a table (SELECT *);
* how to get some columns from a table (SELECT [column names]);
* how to create a column and assign values in it, based by the values of another column (CASE);
* how to filter table data by some columns (AND);
* how to sum values on a column and compare it with expected value (SUM);
* how to filter table data by some columns (OR);
* how to count entries of some value in the column (GROUP BY);
* how to join tables (CROSS JOIN);