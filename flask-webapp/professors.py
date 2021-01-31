"""
TITLE: professors.py
ABOUT: Handler for Professor endpoint
AUTHOR: Morgan Reilly
"""
from flask import make_response, abort
from config import db
from models import Professor, ProfessorSchema


# Create handler for GET request on Professors
def read_all():
    """
        This function responds to a request for /api/professors

        :return:        json string of list of professors
        """
    # Create the list of professors from our data
    professors = Professor.query.order_by(Professor.lname).all()

    # Serialise data for response
    professor_schema = ProfessorSchema(many=True)
    data = professor_schema.dump(professors)
    return data


def create(professor):
    """
    This function creates a new professor in the professor structure
    based on the passed in professor data
    :param professor:  professor to create in professor structure
    :return:        201 on success, 406 on professor exists
    """
    fname = professor.get("fname")
    lname = professor.get("lname")

    existing_professor = (
        Professor.query.filter(Professor.fname == fname)
            .filter(Professor.lname == lname)
            .one_or_none()
    )

    # Insertion possible?
    if existing_professor is None:
        # Create professor instance using schema and passed-in professor
        schema = ProfessorSchema()
        new_professor = schema.load(professor, session=db.session)

        # Add professor to database
        db.session.add(new_professor)
        db.session.commit()

        # Serialise and return newly created professor in response
        data = schema.dump(new_professor)
        return data, 201
    else:
        # Otherwise professor exists
        abort(409, f'Professor {fname} {lname} exists already')
