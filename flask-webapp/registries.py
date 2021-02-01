"""
TITLE: registries.py
ABOUT: Handler for Registry endpoint
AUTHOR: Morgan Reilly
"""
from flask import make_response, abort, jsonify
from config import db


# from models import Registry, RegistrySchema


# Create handler for GET request on Registries
# def read_all():
#     """
#         This function responds to a request for /api/registries
#
#         :return:        json string of list of registries
#         """
#     # Create the list of registries from our data
#     registries = Registry.query.order_by(Registry.c_id).all()
#
#     # Serialise data for response
#     registry_schema = RegistrySchema(many=True)
#     data = registry_schema.dump(registries)
#     return data
def read_all():
    """
        This function responds to a request for /api/registries

        :return:        json string of list of registries
        """
    cur = db.connection.cursor()
    cur.execute('''SELECT * from registry''')
    rv = cur.fetchall()
    resp = jsonify(rv)
    return resp


# def create(registry):
#     """
#     This function creates a new registry in the registry structure
#     based on the passed in registry data
#     :param registry:  student to create in registry structure
#     :return:        201 on success, 406 on registry exists
#     """
#     c_id = registry.get("c_id")
#     s_id = registry.get("s_id")
#
#     existing_registry = (
#         Registry.query.filter(Registry.c_id == c_id)
#             .filter(Registry.s_id == s_id)
#             .one_or_none()
#     )
#
#     # Possible insertion?
#     if existing_registry is None:
#         # Create registry instance using schema and passed-in registry
#         schema = RegistrySchema()
#         new_registry = schema.load(registry, session=db.session)
#
#         # Add registry to database
#         db.session.add(new_registry)
#         db.session.commit()
#
#         # Serialise and return newly created professor in response
#         data = schema.dump(new_registry)
#         return data, 201
#     else:
#         # Otherwise registry exists
#         abort(409, f'Registry of course[{c_id}] and student[{s_id}] exists already')
def create(registry):
    """
    This function creates a new registry in the registry structure
    based on the passed in registry data
    :param registry:  student to create in registry structure
    :return:        201 on success, 406 on registry exists
    """
    c_id = registry.get("c_id")
    s_id = registry.get("s_id")

    cur = db.connection.cursor()
    cur.execute("INSERT INTO registry(c_id, s_id) VALUES (%s, %s)", (c_id, s_id))
    db.connection.commit()
    cur.close()
    return 'success'