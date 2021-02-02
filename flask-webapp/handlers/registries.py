"""
TITLE: registries.py
ABOUT: Handler for Registry endpoint
AUTHOR: Morgan Reilly
"""
from flask import jsonify
from config import db


def read_all():
    """
        This function responds to a request for /api/registries
        It creates a cursor for connections to MySQL server,
        then executes the SQL statement, whereby retrieving all data.

        :return:        json string of list of registries
        """
    get_registries = '''SELECT * from registry'''
    cursor = db.connection.cursor()  # Cursor interacts with MySQL server
    try:
        cursor.execute(get_registries)
        data = cursor.fetchall()
        return jsonify(data), 200
    except db.connection.Error as e:
        # Using 400 for a general message, bad request
        error_message = 'ERROR: ' + str(e)
        print(error_message)
        return error_message, 400
    finally:
        cursor.close()


def create(registry):
    """
    This function creates a new registry in the registry structure
    based on the passed in registry data
    :param registry:  student to create in registry structure
    :return:        201 on success, Error message on failure
    """
    c_id = registry.get("c_id")
    s_id = registry.get("s_id")

    insert_into_registry = '''INSERT INTO registry(c_id, s_id) VALUES (%s, %s)'''
    cursor = db.connection.cursor()
    try:
        cursor.execute(insert_into_registry, (c_id, s_id))
        db.connection.commit()
        data = jsonify(c_id=c_id, s_id=s_id)  # Grab the data for the response
        return data, 201
    except db.connection.Error as e:
        # Using 409 since it will likely be a conflict error
        # Not great since it could be a missing table...
        error_message = 'ERROR: ' + str(e)
        print(error_message)
        return error_message, 400
    finally:
        cursor.close()
