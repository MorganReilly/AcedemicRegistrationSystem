"""
TITLE: professors.py
ABOUT: Handler for Professor endpoint
AUTHOR: Morgan Reilly
"""
from flask import make_response, abort

# Data to serve with API
PROFESSORS = {
    'P001': {
        'p_id': 'P001',
        'fname': 'Alice',
        'lname': 'Greaney'
    },
    'P002': {
        'p_id': 'P002',
        'fname': 'Bob',
        'lname': 'Murdock'
    },
}


# Create handler for GET request on Professors
def read_all():
    """
        This function responds to a request for /api/professors
        with the complete lists of professors

        :return:        sorted list of professors
        """
    # Create the list of professors from our data
    return [PROFESSORS[key] for key in sorted(PROFESSORS.keys())]


def create(professor):
    """
    This function creates a new professor in the professor structure
    based on the passed in professor data
    :param professor:  professor to create in professor structure
    :return:        201 on success, 406 on professor exists
    """
    p_id = professor.get("p_id", None)
    fname = professor.get("fname", None)
    lname = professor.get("lname", None)

    # Does the professor exist already?
    if p_id not in PROFESSORS and p_id is not None:
        PROFESSORS[p_id] = {
            "p_id": p_id,
            "fname": fname,
            "lname": lname
        }
        return make_response(
            "Professor {p_id} successfully created".format(p_id=p_id), 201
        )

    # Otherwise, they exist, that's an error
    else:
        abort(
            406,
            "Professor with {p_id} already exists".format(p_id=p_id),
        )