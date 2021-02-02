"""
TITLE: professors.py
ABOUT: Handler for Professor endpoint
AUTHOR: Morgan Reilly
"""
from flask import jsonify
from config import db


def read_all():
    """
        This function responds to a request for /api/professors
        It creates a cursor for connections to MySQL server,
        then executes the SQL statement, whereby retrieving all data.

        :return:        json string of list of professors
        """
    get_professors = '''SELECT * from professor'''
    cursor = db.connection.cursor()  # Get a connection cursor for M
    try:
        cursor.execute(get_professors)
        data = cursor.fetchall()  # fetchall() -> Retrieve all items,
        return jsonify(data), 200
    except db.connection.Error as e:
        # Using 400 for a general message, bad request
        error_message = 'ERROR: ' + str(e)
        print(error_message)
        return error_message, 400
    finally:
        cursor.close()


def create(professor):
    """
    This function creates a new professor in the professor structure
    based on the passed in professor data
    :param professor:  professor to create in professor structure
    :return:        201 on success, Error message on failure
    """
    fname = professor.get("fname")
    lname = professor.get("lname")

    insert_into_professor = '''INSERT INTO professor(fname, lname) VALUES (%s, %s)'''
    cursor = db.connection.cursor()
    try:
        cursor.execute(insert_into_professor, (fname, lname))
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
