"""
TITLE: build_database.py
ABOUT: Utility program to create and populate database with data
AUTHOR: Morgan Reilly
"""
import os
from config import db
from models import Professor, Course, Student, Registry

# Data to initialise database with
PROFESSORS = [
    {'fname': 'Alice', 'lname': 'Greaney'},
    {'fname': 'Bob', 'lname': 'Murdock'}
]

COURSES = [
    {'title': 'Maths', 'p_id': 1},
    {'title': 'English', 'p_id': 2}
]

STUDENTS = [
    {'fname': 'Roger', 'lname': 'Cullina'},
    {'fname': 'Megan', 'lname': 'Greenwood'}
]

REGISTRIES = [
    {'c_id': 100, 's_id': 1},
    {'c_id': 100, 's_id': 2},
    {'c_id': 101, 's_id': 1},
    {'c_id': 101, 's_id': 2}
]

# Delete database file if it exits currently
if os.path.exists('academic.db'):
    os.remove('academic.db')

# Create the database
db.create_all()

# Iterate over PROFESSORS structure and populate database
for professor in PROFESSORS:
    p = Professor(lname=professor['lname'], fname=professor['fname'])
    db.session.add(p)

# Iterate over COURSES structure and populate database
for course in COURSES:
    c = Course(title=course['title'], p_id=course['p_id'])
    db.session.add(c)

# Iterate over STUDENTS structure and populate database
for student in STUDENTS:
    s = Student(lname=student['lname'], fname=student['fname'])
    db.session.add(s)

# Iterate over REGISTRIES structure and populate database
for registry in REGISTRIES:
    r = Registry(c_id=registry['c_id'], s_id=registry['s_id'])
    db.session.add(r)

db.session.commit()
