"""
TITLE: students.py
ABOUT: Handler for Student endpoint
AUTHOR: Morgan Reilly
"""
from flask import jsonify
from config import db


def read_all():
    """
        This function responds to a request for /api/students
        It creates a cursor for connections to MySQL server,
        then executes the SQL statement, whereby retrieving all data.

        :return:        json string of list of students
        """
    get_students = '''SELECT * from student'''
    try:
        cursor = db.connection.cursor()
        cursor.execute(get_students)
        data = cursor.fetchall()
        return jsonify(data)
    except db.connection.Error as e:
        return str(e)


def create(student):
    """
    This function creates a new student in the student structure
    based on the passed in student data
    :param student:  student to create in student structure
    :return:        201 on success, Error message on failure
    """
    fname = student.get("fname")
    lname = student.get("lname")

    insert_into_student = '''INSERT INTO student(fname, lname) VALUES (%s, %s)'''
    try:
        cursor = db.connection.cursor()
        cursor.execute(insert_into_student, (fname, lname))
        db.connection.commit()
        cursor.close()
        return 201
    except db.connection.Error as e:
        return str(e)
