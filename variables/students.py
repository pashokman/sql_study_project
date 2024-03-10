STUDENTS_TABLE_NAME = 'students'

STUDENTS_TABLE = '''CREATE TABLE students (id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    phone TEXT,
    birthdate TEXT);

INSERT INTO students (first_name, last_name, email, phone, birthdate)
    VALUES ("Peter", "Rabbit", "peter@rabbit.com", "555-6666", "2002-06-24");
INSERT INTO students (first_name, last_name, email, phone, birthdate)
    VALUES ("Alice", "Wonderland", "alice@wonderland.com", "555-4444", "2002-07-04");
'''


STUDENTS_GRADES_TABLE_NAME = 'students_grades'

STUDENTS_GRADES_TABLE = '''CREATE TABLE students_grades (id INTEGER PRIMARY KEY,
    student_id INTEGER,
    test TEXT,
    grade INTEGER);

INSERT INTO students_grades (student_id, test, grade)
    VALUES (1, "Nutrition", 95);
INSERT INTO students_grades (student_id, test, grade)
    VALUES (2, "Nutrition", 92);
INSERT INTO students_grades (student_id, test, grade)
    VALUES (1, "Chemistry", 85);
INSERT INTO students_grades (student_id, test, grade)
    VALUES (2, "Chemistry", 95);
'''

STUDENTS_PROJECTS_TABLE_NAME = 'students_projects'

STUDENTS_PROJECTS_TABLE = '''CREATE TABLE students_projects (id INTEGER PRIMARY KEY,
    student_id INTEGER,
    title TEXT);
    
INSERT INTO students_projects (student_id, title)
    VALUES (1, "Carrotapault");
'''