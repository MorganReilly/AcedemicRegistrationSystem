"""
TITLE: registries.py
ABOUT: Handler for Registry endpoint
AUTHOR: Morgan Reilly
"""
from flask import make_response, abort

# Data to serve with API
COURSE_REGISTRIES = {
    'R001': {
        'r_id': 'R001',
        'c_id': 100,
        's_id': 'S001'
    },
    'R002': {
        'r_id': 'R002',
        'c_id': 100,
        's_id': 'S002'
    },
    'R003': {
        'r_id': 'R003',
        'c_id': 101,
        's_id': 'S001'
    },
    'R004': {
        'r_id': 'R004',
        'c_id': 101,
        's_id': 'S002'
    }
}


# Create handler for GET request on Registries
def read_all():
    """
        This function responds to a request for /api/registries
        with the complete lists of registries

        :return:        sorted list of registries
        """
    # Create the list of registries from our data
    return [COURSE_REGISTRIES[key] for key in sorted(COURSE_REGISTRIES.keys())]


def create(registry):
    """
    This function creates a new registry in the registry structure
    based on the passed in registry data
    :param registry:  student to create in registry structure
    :return:        201 on success, 406 on registry exists
    """
    r_id = registry.get("r_id", None)
    c_id = registry.get("c_id", None)
    s_id = registry.get("s_id", None)

    # Does the registry exist already?
    if r_id not in COURSE_REGISTRIES and r_id is not None:
        COURSE_REGISTRIES[r_id] = {
            "r_id": r_id,
            "c_id": c_id,
            "s_id": s_id
        }
        return make_response(
            "Registry {r_id} successfully created".format(r_id=r_id), 201
        )

    # Otherwise, they exist, that's an error
    else:
        abort(
            406,
            "Registry with {r_id} already exists".format(r_id=r_id),
        )
