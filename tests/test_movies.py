import pytest

from variables.movies import MOVIES_NEW_COLUMN_NAME, MOVIES_NEW_ROW, MOVIES_TABLE, MOVIES_TABLE_NAME
from variables.movies_assert_data import *


@pytest.mark.movies
def test_connection(movies):
    # check connection to sqlite
    movies.test_connection()


@pytest.mark.movies
def test_create_students_and_students_grades_tables(movies):
    # if there is no movies file in project root folder, method creates a new file, 
    # if a file exists, we get a proper message
    movies.create_new_table(MOVIES_TABLE)


@pytest.mark.movies
def test_self_join(movies):
    data = movies.get_self_join(MOVIES_TABLE_NAME)
    assert SELF_JOIN_1 in data, 'Movie error in SELF JOIN'
    assert SELF_JOIN_2 in data, 'Movie error in SELF JOIN'
    table = movies.result_with_specific_column_names(data, 'title', 'sequels_title')
    print(table)


@pytest.mark.movies
def test_add_new_movie(movies):
    data = movies.get_all_table_data(MOVIES_TABLE_NAME)
    table = movies.result_with_all_table_columns_names(data, MOVIES_TABLE_NAME)
    print(table)
    assert MOVIE_NEW_ROW_ASSERT not in data, 'Movie error in ADD NEW MOVIE'

    movies.add_new_movie(MOVIES_TABLE_NAME, MOVIES_NEW_ROW)
    data = movies.get_all_table_data(MOVIES_TABLE_NAME)
    table = movies.result_with_all_table_columns_names(data, MOVIES_TABLE_NAME)
    print(table)
    assert MOVIE_NEW_ROW_ASSERT in data, "Movie isn't in the table"


@pytest.mark.movies
def test_delete_movie(movies):
    data = movies.get_all_table_data(MOVIES_TABLE_NAME)
    table = movies.result_with_all_table_columns_names(data, MOVIES_TABLE_NAME)
    print(table)
    assert MOVIE_NEW_ROW_ASSERT in data, "Movie already deleted, or didn't added"

    movies.delete_movie(MOVIES_TABLE_NAME, "The Fast & the Furious")
    data = movies.get_all_table_data(MOVIES_TABLE_NAME)
    table = movies.result_with_all_table_columns_names(data, MOVIES_TABLE_NAME)
    print(table)
    assert MOVIE_NEW_ROW_ASSERT not in data, 'Error in DELETE MOVIE'


@pytest.mark.movies
def test_add_new_column(movies):
    data = movies.get_table_columns_names(MOVIES_TABLE_NAME)
    columns_count = len(data)
    print('\n', data, f'Count of columns = {columns_count}')
    assert columns_count == 4, "Column count isn't as expected in ADD NEW COLUMN (before adding new)"

    movies.add_new_column(MOVIES_TABLE_NAME, MOVIES_NEW_COLUMN_NAME)
    data = movies.get_table_columns_names(MOVIES_TABLE_NAME)
    columns_count = len(data)
    print('\n', data, f'Count of columns = {columns_count}')
    assert columns_count == 5, "Column count isn't as expected in ADD NEW COLUMN (after adding new)"


@pytest.mark.movies
def test_delete_column(movies):
    data = movies.get_table_columns_names(MOVIES_TABLE_NAME)
    columns_count = len(data)
    print('\n', data, f'Count of columns = {columns_count}')
    assert columns_count == 5, "Column count isn't as expected in DELETE COLUMN (before deleting new)"

    movies.delete_column(MOVIES_TABLE_NAME, MOVIES_NEW_COLUMN_NAME)
    data = movies.get_table_columns_names(MOVIES_TABLE_NAME)
    columns_count = len(data)
    print('\n', data, f'Count of columns = {columns_count}')
    assert columns_count == 4, "Column count isn't as expected in DELETE COLUMN (after deleting new)"


@pytest.mark.movies
def test_update_movie_released_year(movies):
    movies.update_movie_year(MOVIES_TABLE_NAME, "Harry Potter and the Philosopher's Stone", 2002)
    data = movies.get_all_table_data(MOVIES_TABLE_NAME)
    print(data)
    table = movies.result_with_all_table_columns_names(data, MOVIES_TABLE_NAME)
    print(table)    
    assert MOVIE_UPDATE_RELEASED_YEAR in data, "Movie year isn't as expected in UPDATE MOVIE YEAR (after update)"

    movies.update_movie_year(MOVIES_TABLE_NAME, "Harry Potter and the Philosopher's Stone", 2001)
    data = movies.get_all_table_data(MOVIES_TABLE_NAME)
    err_msg = "Movie year isn't as expected in UPDATE MOVIE YEAR (after return default)"
    assert MOVIE_UPDATE_RELEASED_YEAR_DEAFULT in data, err_msg