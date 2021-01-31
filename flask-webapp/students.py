"""
TITLE: students.py
ABOUT: Handler for Student endpoint
AUTHOR: Morgan Reilly
"""
from flask import make_response, abort

# Data to serve with API
STUDENTS = {
    'S001': {
        's_id': 'S001',
        'fname': 'Roger',
        'lname': 'Cullina'
    },
    'S002': {
        's_id': 'S002',
        'fname': 'Megan',
        'lname': 'Greenwood'
    },
}


# Create handler for GET request on Students
def read_all():
    """
        This function responds to a request for /api/students
        with the complete lists of students

        :return:        sorted list of students
        """
    # Create the list of students from our data
    return [STUDENTS[key] for key in sorted(STUDENTS.keys())]


def create(student):
    """
    This function creates a new student in the student structure
    based on the passed in student data
    :param student:  student to create in student structure
    :return:        201 on success, 406 on student exists
    """
    s_id = student.get("s_id", None)
    fname = student.get("fname", None)
    lname = student.get("lname", None)

    # Does the student exist already?
    if s_id not in STUDENTS and s_id is not None:
        STUDENTS[s_id] = {
            "s_id": s_id,
            "fname": fname,
            "lname": lname
        }
        return make_response(
            "Student {s_id} successfully created".format(s_id=s_id), 201
        )

    # Otherwise, they exist, that's an error
    else:
        abort(
            406,
            "Student with {s_id} already exists".format(s_id=s_id),
        )