import pytest
from variables.marvels import *
from variables.marvels_assert_data import *

TABLE_NAME = MARVELS_TABLE_NAME

@pytest.mark.marvels
def test_connection(database):
    # check connection to sqlite
    database.test_connection()


@pytest.mark.marvels
def test_create_marvels_table(database):
    # if there is no database file in project root folder, method creates a new file, 
    # if a file exists, we get a proper message
    database.create_new_table(MARVELS_TABLE)


@pytest.mark.marvels
def test_get_marvels_table_data(database):
    # get all data from a table
    data = database.get_all_table_data(TABLE_NAME)
    
    assert len(data) == ALL_CHARACTERS_COUNT, 'Some character is missing (all table)'
    assert WOLVERINE in data, 'Wolverine is epsent in all table data'
    assert LOKI in data, 'Loki is epsent in all table data'
    
    table = database.result_with_all_table_columns_names(data, TABLE_NAME)
    print(table)


@pytest.mark.marvels
def test_assign_to_characters_intelligence_text_value(database):
    # here I get a table with columns `name`, `inteligence`,
    # and create a `grade` column in which I assign the text value for an inteligence value range
    data = database.sort_characters_by_avg_column_value(TABLE_NAME, 'name', 'intelligence', 'grade')
    
    assert len(data) == ALL_CHARACTERS_COUNT, 'Some character is missing (intelligence text value)'
    assert GREEN_GOBLIN_TEXT_VALUE in data, 'Green Goblin is epsent in inteligence text value'
    assert ROGUE_TEXT_VALUE in data, 'Rogue is epsent in inteligence text value'
    assert STORM_TEXT_VALUE in data, 'Storm is epsent in inteligence text value'
    
    table = database.result_with_specific_column_names(data, 'name', 'intelligence', 'grade')
    print(table)


@pytest.mark.marvels
def test_filter_characters_by_gender_hometown_energy_Projection(database):
    # filters all table by `gender`, `hometown`, `energy_Projection` values, 
    # and checks if there are expected characters in it
    data = database.get_characters_by_gender_hometown_energy_Projection(TABLE_NAME, 'Female', 'USA', 7)
    
    assert len(data) == 2, 'Some character is missing (gender, hometown, energy projection)'
    assert JEAN_GREY in data, 'Jean Grey is epsent in gender, hometown, energy protection'
    assert ROGUE in data, 'Rogue is epsent in gender, hometown, energy protection'
    
    table = database.result_with_all_table_columns_names(data, TABLE_NAME)
    print(table)


@pytest.mark.marvels
def test_can_all_characters_defeat_one_strong_badguy(database):
    # checks if all characters can defeat the badguy 
    # (if their sum of every passed parameter is greater than same parameter of a badguy)
    all_characters = database.get_few_parameters_sum_of_all_characters(TABLE_NAME, 'intelligence', 'strength', 
                                                                       'speed', 'energy_Projection', 'fighting_Skills')
    print('\n', all_characters)
    print(BADGUY)
    
    assert database.can_all_characters_defeat_badguy(all_characters, BADGUY), "All characters can't defeat the badguy"


@pytest.mark.marvels
def test_characters_with_popularity_or_weight(database):
    # test filter characters by popularity or weight
    data = database.get_characters_with_more_popularity_or_more_weight(TABLE_NAME, 10, 100)

    assert len(data) == 18, 'Some character is missing in popularity or weight'
    assert LOKI in data, 'Loki is epsent in popularity or weight'
    assert WOLVERINE in data, 'Green Goblin is epsent in popularity or weight'
    
    table = database.result_with_all_table_columns_names(data, TABLE_NAME)
    print(table)


@pytest.mark.marvels
def test_group_characters_by_param(database):
    data = database.group_characters_by_param(TABLE_NAME, 'alignment')
    print('\n', data)
    
    assert data['Bad'] == 4, 'Bad characters count is incorrect in group characters by param'
    assert data['Good'] == 15, 'Good characters count is incorrect in group characters by param'
    assert data['Neutral'] == 7, 'Bad characters count is incorrect in group characters by param'