"""
TITLE: students.py
ABOUT: Handler for Student endpoint
AUTHOR: Morgan Reilly
"""
from flask import make_response, abort
from config import db
# from models import Student, StudentSchema


# Create handler for GET request on Students
def read_all():
    """
        This function responds to a request for /api/students

        :return:        json string of list of students
        """
    # Create the list of students from our data
    students = Student.query.order_by(Student.lname).all()

    # Serialise data for response
    student_schema = StudentSchema(many=True)
    data = student_schema.dump(students)
    return data


def create(student):
    """
    This function creates a new student in the student structure
    based on the passed in student data
    :param student:  student to create in student structure
    :return:        201 on success, 406 on student exists
    """
    fname = student.get("fname")
    lname = student.get("lname")

    existing_student = (
        Student.query.filter(Student.fname == fname)
            .filter(Student.lname == lname)
            .one_or_none()
    )

    # Insertion possible?
    if existing_student is None:
        # Create student instance using schema and passed-in student
        schema = StudentSchema()
        new_student = schema.load(student, session=db.session)

        # Add student to database
        db.session.add(new_student)
        db.session.commit()

        # Serialise and return newly created student in response
        data = schema.dump(new_student)
        return data, 201
    else:
        # Otherwise professor exists
        abort(409, f'Student {fname} {lname} exists already')
