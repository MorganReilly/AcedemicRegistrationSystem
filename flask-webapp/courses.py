"""
TITLE: courses.py
ABOUT: Handler for Course endpoint
AUTHOR: Morgan Reilly
"""
import mysql.connector
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
    try:
        # Cursor interacts with MySQL server
        cursor = db.connection.cursor()
        cursor.execute(get_courses)
        data = cursor.fetchall()  # fetchall() -> Retrieve all items
        return jsonify(data)
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))


def create(course):
    """
    This function creates a new course in the course structure
    based on the passed in course data
    :param course:  course to create in course structure
    :return:        201 on success, 406 on course exists
    """
    title = course.get("title")
    p_id = course.get("p_id")

    insert_into_course = '''INSERT INTO course(title, p_id) VALUES (%s, %s)'''
    try:
        cur = db.connection.cursor()
        cur.execute(insert_into_course, (title, p_id))
        db.connection.commit()
        cur.close()
        return 201
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
