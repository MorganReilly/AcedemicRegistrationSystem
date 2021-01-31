"""
TITLE: build_database.py
ABOUT: Utility program to create and populate database with data
AUTHOR: Morgan Reilly
"""
import os
from config import db
from models import Professor, Course

# Data to initialise database with
PROFESSORS = [
    {'fname': 'Alice', 'lname': 'Greaney'},
    {'fname': 'Bob', 'lname': 'Murdock'}
]

COURSES = [
    {'title': 'Maths', 'p_id': 1},
    {'title': 'English', 'p_id': 2}
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

for course in COURSES:
    c = Course(title=course['title'], p_id=course['p_id'])
    db.session.add(c)

db.session.commit()
