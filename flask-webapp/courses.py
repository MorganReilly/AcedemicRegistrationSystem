"""
TITLE: courses.py
ABOUT: Handler for Course endpoint
AUTHOR: Morgan Reilly
"""
from flask import make_response, abort
from config import db
# from models import Course, CourseSchema


# Create handler for GET request on Courses
def read_all():
    """
        This function responds to a request for /api/courses

        :return:        json string of list of courses
        """
    courses = Course.query.order_by(Course.title).all()

    # Serialise data for response
    course_schema = CourseSchema(many=True)
    data = course_schema.dump(courses)
    return data


def create(course):
    """
    This function creates a new course in the course structure
    based on the passed in course data
    :param course:  course to create in course structure
    :return:        201 on success, 406 on course exists
    """
    title = course.get("title")
    p_id = course.get("p_id")

    existing_course = (
        Course.query.filter(Course.title == title)
            .filter(Course.p_id == p_id)
            .one_or_none()
    )

    # Inserting possible
    if existing_course is None:
        # Create course instance using schema and passed-in course
        schema = CourseSchema()
        new_course = schema.load(course, session=db.session)

        # Add course to db
        db.session.add(new_course)
        db.session.commit()

        # Serialise and return newly created course in response
        data = schema.dump(new_course)
        return data, 201
    else:
        # otherwise course exists
        abort(409, f'Course {title} taught by {p_id} exists already')
