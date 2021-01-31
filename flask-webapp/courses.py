"""
TITLE: courses.py
ABOUT: Handler for Course endpoint
AUTHOR: Morgan Reilly
"""
from flask import make_response, abort

# Data to serve with API
COURSES = {
    'Maths':{
        'title': 'Maths',
        'p_id': 'P001'
    },  # Example of single professor
    'English': {
        'title': 'English',
        'p_id': 'P002'
    },
    'Latin': {
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
    title = course.get("title", None)
    p_id = course.get("p_id", None)

    # Does the professor exist already?
    if title not in COURSES and title is not None:
        COURSES[title] = {
            "title": title,
            "p_id": p_id
        }
        return make_response(
            "Course {title} successfully created".format(title=title), 201
        )

    # Otherwise, they exist, that's an error
    else:
        abort(
            406,
            "Course with {title} already exists".format(title=title),
        )