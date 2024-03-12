import pytest

from variables.students import *
from variables.students_assert_data import *


@pytest.mark.students
def test_connection(students):
    # check connection to sqlite
    students.test_connection()


@pytest.mark.students
def test_create_students_and_students_grades_tables(students):
    # if there is no students file in project root folder, method creates a new file, 
    # if a file exists, we get a proper message
    students.create_new_table(STUDENTS_TABLE)
    students.create_new_table(STUDENTS_GRADES_TABLE)


@pytest.mark.students
def test_get_both_tables_data_cross_join(students):
    data = students.get_cross_join(STUDENTS_TABLE_NAME, STUDENTS_GRADES_TABLE_NAME)
    
    assert CROSS_JOIN_ALICE in data, 'Some Alice data is incorrect in CROSS JOIN'
    assert CROSS_JOIN_PETER in data, 'Some Peter data is incorrect in CROSS JOIN'
    
    table = students.result_with_few_tables_columns_names(data, STUDENTS_TABLE_NAME, STUDENTS_GRADES_TABLE_NAME)
    print(table)


@pytest.mark.students
def test_get_both_tables_implicit_inner_join(students):
    data = students.get_implicit_inner_join(STUDENTS_TABLE_NAME, STUDENTS_GRADES_TABLE_NAME)
    
    assert IMPL_EXPL_INNER_JOIN_PETER in data, 'Some Peter data is incorrect in IMPLICIT INNER JOIN'
    assert IMPL_EXPL_INNER_JOIN_ALICE in data, 'Some Alice data is incorrect in IMPLICIT INNER JOIN'
    assert IMPL_EXPL_INNER_JOIN_ALICE2 in data, 'Some Peter data is incorrect in IMPLICIT INNER JOIN'
    assert IMPL_EXPL_INNER_JOIN_PETER in data, 'Some Alice data is incorrect in IMPLICIT INNER JOIN'
    
    table = students.result_with_few_tables_columns_names(data, STUDENTS_TABLE_NAME, STUDENTS_GRADES_TABLE_NAME)
    print(table)


@pytest.mark.students
def test_get_both_tables_explicit_inner_join(students):
    data = students.get_explicit_inner_join(STUDENTS_TABLE_NAME, STUDENTS_GRADES_TABLE_NAME)
    
    assert IMPL_EXPL_INNER_JOIN_PETER in data, 'Some Peter data is incorrect in IMPLICIT INNER JOIN'
    assert IMPL_EXPL_INNER_JOIN_ALICE in data, 'Some Alice data is incorrect in IMPLICIT INNER JOIN'
    assert IMPL_EXPL_INNER_JOIN_ALICE2 in data, 'Some Peter data is incorrect in IMPLICIT INNER JOIN'
    assert IMPL_EXPL_INNER_JOIN_PETER in data, 'Some Alice data is incorrect in IMPLICIT INNER JOIN'
    
    table = students.result_with_few_tables_columns_names(data, STUDENTS_TABLE_NAME, STUDENTS_GRADES_TABLE_NAME)
    print(table)


@pytest.mark.students
def test_create_students_projects_table(students):
    # if there is no students file in project root folder, method creates a new file, 
    # if a file exists, we get a proper message
    students.create_new_table(STUDENTS_PROJECTS_TABLE)


@pytest.mark.students
def test_get_both_tables_left_outer_join(students):
    data = students.get_left_outer_join(STUDENTS_TABLE_NAME, STUDENTS_PROJECTS_TABLE_NAME)
    
    assert LEFT_OUTER_JOIN_PETER in data, 'Some Peter data is incorrect in LEFT OUTER JOIN'
    assert LEFT_OUTER_JOIN_ALICE in data, 'Some Alice data is incorrect in LEFT OUTER JOIN'
    
    table = students.result_with_specific_column_names(data, 'first_name', 'last_name', 'title')
    print(table)
