import pytest
from variables.marvels import marvels_table


def test_connection(database):
    database.test_connection()


def test_create_marvels_table(database):
    database.create_new_table(marvels_table)


def test_get_marvels_table_data(database):
    data = database.get_all_table_data('marvels')
    print(data)

def test_get_smartest_characters(database):
    data = database.sort_characters_by_avg_column_value('marvels', 'name', 'intelligence', 'grade')
    print(data)


# def test_get_characters_by_gender_hometown_energy_Projection(database):
#     data = database.get_characters_by_gender_hometown_energy_Projection('marvels', 'Female', 'USA', 7)
#     print(data)