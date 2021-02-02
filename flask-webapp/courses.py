"""
TITLE: courses.py
ABOUT: Handler for Course endpoint
AUTHOR: Morgan Reilly
"""
from flask import jsonify
from config import db


def read_all():
    """
        This function responds to a request for /api/courses
        It creates a cursor for connections to MySQL server,
        then executes the SQL statement, whereby retrieving all data.

        :return:        json string of list of courses
        """
    get_courses = '''SELECT * from course'''
    cursor = db.connection.cursor()  # Cursor interacts with MySQL server
    try:
        cursor.execute(get_courses)
        data = cursor.fetchall()  # fetchall() -> Retrieve all items
        return jsonify(data), 200
    except db.connection.Error as e:
        # Using 400 for a general message, bad request
        error_message = 'ERROR: ' + str(e)
        print(error_message)
        return error_message, 400
    finally:
        cursor.close()


def create(course):
    """
    This function creates a new course in the course structure
    based on the passed in course data
    :param course:  course to create in course structure
    :return:        201 on success, Error message on failure
    """
    title = course.get("title")
    p_id = course.get("p_id")

    insert_into_course = '''INSERT INTO course(title, p_id) VALUES (%s, %s)'''
    cursor = db.connection.cursor()
    try:
        cursor.execute(insert_into_course, (title, p_id))
        db.connection.commit()
        data = jsonify(title=title, p_id=p_id)
        return data, 201
    except db.connection.Error as e:
        # Using 409 since it will likely be a conflict error
        # Not great since it could be a missing table...
        error_message = 'ERROR: ' + str(e)
        print(error_message)
        return error_message, 400
    finally:
        cursor.close()
