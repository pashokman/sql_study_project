import pytest

from variables.movies import MOVIES_TABLE, MOVIES_TABLE_NAME
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