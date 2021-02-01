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
    try:
        cursor = db.connection.cursor()
        cursor.execute(get_registries)
        data = cursor.fetchall()
        return jsonify(data)
    except db.connection.Error as e:
        return str(e)


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
    try:
        cursor = db.connection.cursor()
        cursor.execute(insert_into_registry, (c_id, s_id))
        db.connection.commit()
        cursor.close()
        return 201
    except db.connection.Error as e:
        return str(e)
