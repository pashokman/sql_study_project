# SQL training project

Here I trained to interact with the database in SQL using Python.

## List of tests
* `test_connection` - test creates a database file and connect to it;
* `test_create_marvels_table` - test creates a table with data from an external file - `marvels.py`;
* `test_get_marvels_table_data` - test gets all table data and checks if some characters in it;
* `test_assign_to_characters_intelligence_text_value` - test gets a table with columns `name`, `inteligence`, and creates a `grade` column in which I assign the text value for an inteligence value range;
* `test_filter_characters_by_gender_hometown_energy_Projection` - test filters all table by `gender`, `hometown`, `energy_Projection` values, and checks if there are expected characters in it;
* `test_can_all_characters_defeat_one_strong_badguy` - test checks if all characters can defeat the badguy (if their sum of every passed parameter is greater than same parameter of a badguy). By default using parameters - `intelligence`, `strength`, `speed`, `energy_Projection`, `fighting_Skills`;
* `test_characters_with_popularity_or_weight` - test filter characters by popularity or weight;
* `test_group_characters_by_param` - test grouped characters by parameter. By default using `alignment`.