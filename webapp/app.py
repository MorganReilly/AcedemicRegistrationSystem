from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

PROFESSORS = {
    '1': {'name': 'Alice'},
    '2': {'name': 'Bob'}
}

STUDENTS = {
    '1': {'name': 'Greg'},
    '2': {'name': 'Tina'}
}

COURSES = {
    '101': {'name': 'Maths', 'p_id': '1'},
    '102': {'name': 'English', 'p_id': '2'},
    '103': {'name': 'Latin'}
}


def abort_if_prof_not_exist(p_id):
    """Handles non existing professor"""
    if p_id not in PROFESSORS:
        abort(404, message="Professor {} does not exist".format(p_id))


def abort_if_student_not_exist(s_id):
    """Handles non existing student"""
    if s_id not in STUDENTS:
        abort(404, message="Student {} does not exist".format(s_id))


def abort_if_course_not_exist(c_id):
    """Handles non existing student"""
    if c_id not in COURSES:
        abort(404, message="Course {} does not exist".format(c_id))


parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('p_id')


class Professor(Resource):
    """Handles single entries; GET, DELETE, PUT"""

    def get(self, p_id):
        abort_if_prof_not_exist(p_id)
        return PROFESSORS[p_id]

    def delete(self, p_id):
        abort_if_prof_not_exist(p_id)
        del PROFESSORS[p_id]
        return '', 204

    def put(self, p_id):
        args = parser.parse_args()
        professor = {'name': args['name']}
        PROFESSORS[p_id] = professor
        return professor, 201


class ProfessorList(Resource):
    """Handles multiple entries: GET, POST"""

    def get(self):
        return PROFESSORS

    def post(self):
        args = parser.parse_args()
        p_id = int(max(PROFESSORS.keys()).lstrip('professor')) + 1
        p_id = '%i' % p_id
        PROFESSORS[p_id] = {'name': args['name']}
        return PROFESSORS[p_id], 201


class Student(Resource):
    """Handles single entries; GET, DELETE, PUT"""

    def get(self, s_id):
        abort_if_student_not_exist(s_id)
        return STUDENTS[s_id]

    def delete(self, s_id):
        abort_if_student_not_exist(s_id)
        del STUDENTS[s_id]
        return '', 204

    def put(self, s_id):
        args = parser.parse_args()
        student = {'name': args['name']}
        STUDENTS[s_id] = student
        return student, 201


class StudentList(Resource):
    """Handles multiple entries: GET, POST"""

    def get(self):
        return STUDENTS

    def post(self):
        args = parser.parse_args()
        s_id = int(max(STUDENTS.keys()).lstrip('student')) + 1
        s_id = '%i' % s_id
        STUDENTS[s_id] = {'name': args['name']}
        return STUDENTS[s_id], 201


class Course(Resource):
    """Handles single entries; GET, DELETE, PUT"""

    def get(self, c_id):
        abort_if_course_not_exist(c_id)
        return COURSES[c_id]

    def delete(self, c_id):
        abort_if_course_not_exist(c_id)
        del COURSES[c_id]
        return '', 204

    def put(self, c_id):
        args = parser.parse_args()
        course = {'name': args['name'], 'p_id': args['p_id']}
        COURSES[c_id] = course
        return course, 201


class CourseList(Resource):
    """Handles multiple entries: GET, POST"""

    def get(self):
        return COURSES

    def post(self):
        args = parser.parse_args()
        c_id = int(max(COURSES.keys()).lstrip('course')) + 1
        c_id = '%i' % c_id
        COURSES[c_id] = {'name': args['name'], 'p_id': args['p_id']}
        return COURSES[c_id], 201


# API Resource Routing
api.add_resource(ProfessorList, '/professors')
api.add_resource(Professor, '/professors/<p_id>')
api.add_resource(StudentList, '/students')
api.add_resource(Student, '/students/<s_id>')
api.add_resource(CourseList, '/courses')
api.add_resource(Course, '/courses/<c_id>')

if __name__ == '__main__':
    app.run(debug=True)
