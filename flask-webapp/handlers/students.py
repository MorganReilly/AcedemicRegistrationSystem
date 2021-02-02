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
    cursor = db.connection.cursor()
    try:
        cursor.execute(get_students)
        data = cursor.fetchall()
        return jsonify(data), 200
    except db.connection.Error as e:
        # Using 400 for a general message, bad request
        error_message = 'ERROR: ' + str(e)
        print(error_message)
        return error_message, 400
    finally:
        cursor.close()


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
    cursor = db.connection.cursor()
    try:
        cursor.execute(insert_into_student, (fname, lname))
        db.connection.commit()
        data = jsonify(fname=fname, lname=lname)
        return data, 201
    except db.connection.Error as e:
        # Using 409 since it will likely be a conflict error
        # Not great since it could be a missing table...
        error_message = 'ERROR: ' + str(e)
        print(error_message)
        return error_message, 400
    finally:
        cursor.close()
