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
    try:
        cursor = db.connection.cursor()  # Get a connection cursor for M
        cursor.execute(get_professors)
        data = cursor.fetchall()  # fetchall() -> Retrieve all items,
        return jsonify(data)
    except db.connection.Error as e:
        return str(e)


def create(professor):
    """
    This function creates a new professor in the professor structure
    based on the passed in professor data
    :param professor:  professor to create in professor structure
    :return:        201 on success, 406 on professor exists
    """
    fname = professor.get("fname")
    lname = professor.get("lname")

    insert_into_professor = '''INSERT INTO professor(fname, lname) VALUES (%s, %s)'''
    try:
        cursor = db.connection.cursor()
        cursor.execute(insert_into_professor, (fname, lname))
        db.connection.commit()
        cursor.close()
        return 201
    except db.connection.Error as e:
        return str(e)
