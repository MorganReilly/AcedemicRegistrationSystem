"""
TITLE: courses.py
ABOUT: Handler for Course endpoint
AUTHOR: Morgan Reilly
"""
from flask import make_response, abort

# Data to serve with API
COURSES = {
    101: {
        'c_id': 101,
        'title': 'Maths',
        'p_id': 'P001'
    },  # Example of single professor
    102: {
        'c_id': 102,
        'title': 'English',
        'p_id': 'P002'
    },
    103: {
        'c_id': 103,
        'title': 'Latin',
        'p_id': [
            'P001',
            'P002'
        ]
    }  # Example of multiple professors
}


# Create handler for GET request on Courses
def read_all():
    """
        This function responds to a request for /api/courses
        with the complete lists of courses

        :return:        sorted list of courses
        """
    # Create the list of courses from our data
    return [COURSES[key] for key in sorted(COURSES.keys())]


def create(course):
    """
    This function creates a new course in the course structure
    based on the passed in course data
    :param course:  course to create in course structure
    :return:        201 on success, 406 on course exists
    """
    c_id = course.get("c_id", None)
    title = course.get("title", None)
    p_id = course.get("p_id", None)

    # Does the professor exist already?
    if c_id not in COURSES and c_id is not None:
        COURSES[c_id] = {
            "c_id": c_id,
            "title": title,
            "p_id": p_id
        }
        return make_response(
            "Course {c_id} successfully created".format(c_id=c_id), 201
        )

    # Otherwise, they exist, that's an error
    else:
        abort(
            406,
            "Course with {c_id} already exists".format(c_id=c_id),
        )
