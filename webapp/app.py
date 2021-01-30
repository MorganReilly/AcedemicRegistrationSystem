"""
app.py
TITLE: Academic Registration System
ABOUT: Main entry point to application
AUTHOR: Morgan Reilly
LINKS:
    * https://flask-restful.readthedocs.io/
    * https://flask.palletsprojects.com/en/1.1.x/tutorial/
"""
import os
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource


def create_app(test_config=None):
    # App creation and configuration
    app = app = Flask(__name__)
    app.config['BUNDLE_ERRORS'] = True  # Global Error Settings for Parser
    app.config.from_mapping(SECRET_KEY='dev',
                            DATABASE=os.path.join(app.instance_path, 'webapp.sqlite'))
    api = Api(app)  # Api definition

    if test_config is None:
        # Load instance config, if exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load test config if passed in
        app.config.from_mapping(test_config)
    # Ensure instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    """
    Mock Data for:
    Professors, Students, Courses, Course Registries

    Still need to hook up the database and use that instead
    """
    PROFESSORS = {
        '1': {'name': 'Alice'},
        '2': {'name': 'Bob'}
    }
    STUDENTS = {
        '1': {'name': 'Greg'},
        '2': {'name': 'Tina'}
    }
    COURSES = {
        '101': {'name': 'Maths', 'p_id': '1'},  # Example of single professor
        '102': {'name': 'English', 'p_id': '2'},
        '103': {'name': 'Latin', 'p_id': [1, 2]}  # Example of multiple professors
    }
    COURSE_REGISTRIES = {
        '1': {'c_id': '100', 's_id': '1'},
        '2': {'c_id': '100', 's_id': '2'},
        '3': {'c_id': '101', 's_id': '1'},
        '4': {'c_id': '101', 's_id': '2'}
    }

    def abort_if_elem_not_exist(elem_id, elements, message):
        """Handles non existing element"""
        if elem_id not in elements:
            abort(404, message="{} {} does not exist".format(message, elem_id))

    """
    Parsers
    Used to handle various requests.
    I have split these up due to each request taking somewhat different values.
    """
    # Parser for Professor Requests
    p_parser = reqparse.RequestParser()  # Create a new parser
    p_parser.add_argument('name', type=str, required=True, help="Name cannot be blank")
    # Inherit parser arguments from professor requests,
    # but also include p_id since it's unique to course requests
    c_parser = p_parser.copy()
    c_parser.add_argument('p_id', type=int, required=False, action='append')  # Append
    # Student parser will only inherit name
    s_parser = p_parser.copy()
    # Course Registry is unique to requests in that it doesn't need a name, but instead has 2 id's passed
    r_parser = reqparse.RequestParser()
    r_parser.add_argument('c_id', type=int, required=True, help="Course ID cannot be blank")
    r_parser.add_argument('s_id', type=int, required=True, help="Student ID cannot be blank")

    class Professor(Resource):
        """Handles single entries; GET, DELETE, PUT"""

        def get(self, p_id):
            abort_if_elem_not_exist(p_id, PROFESSORS, "Professor")
            return PROFESSORS[p_id]

        def delete(self, p_id):
            abort_if_elem_not_exist(p_id, PROFESSORS, "Professor")
            del PROFESSORS[p_id]
            return '', 204

        def put(self, p_id):
            args = p_parser.parse_args()
            professor = {'name': args['name']}
            PROFESSORS[p_id] = professor
            return professor, 201

    class ProfessorList(Resource):
        """Handles multiple entries: GET, POST"""

        def get(self):
            return PROFESSORS

        def post(self):
            args = p_parser.parse_args()
            p_id = int(max(PROFESSORS.keys()).lstrip('professor')) + 1
            p_id = '%i' % p_id
            PROFESSORS[p_id] = {'name': args['name']}
            return PROFESSORS[p_id], 201

    class Student(Resource):
        """Handles single entries; GET, DELETE, PUT"""

        def get(self, s_id):
            abort_if_elem_not_exist(s_id, STUDENTS, "Student")
            return STUDENTS[s_id]

        def delete(self, s_id):
            abort_if_elem_not_exist(s_id, STUDENTS, "Student")
            del STUDENTS[s_id]
            return '', 204

        def put(self, s_id):
            args = s_parser.parse_args()
            student = {'name': args['name']}
            STUDENTS[s_id] = student
            return student, 201

    class StudentList(Resource):
        """Handles multiple entries: GET, POST"""

        def get(self):
            return STUDENTS

        def post(self):
            args = s_parser.parse_args()
            s_id = int(max(STUDENTS.keys()).lstrip('student')) + 1
            s_id = '%i' % s_id
            STUDENTS[s_id] = {'name': args['name']}
            return STUDENTS[s_id], 201

    class Course(Resource):
        """Handles single entries; GET, DELETE, PUT"""

        def get(self, c_id):
            abort_if_elem_not_exist(c_id, COURSES, "Course")
            return COURSES[c_id]

        def delete(self, c_id):
            abort_if_elem_not_exist(c_id, COURSES, "Course")
            del COURSES[c_id]
            return '', 204

        def put(self, c_id):
            args = c_parser.parse_args()
            course = {'name': args['name'], 'p_id': args['p_id']}
            COURSES[c_id] = course
            return course, 201

    class CourseList(Resource):
        """Handles multiple entries: GET, POST"""

        def get(self):
            return COURSES

        def post(self):
            args = c_parser.parse_args()
            c_id = int(max(COURSES.keys()).lstrip('course')) + 1
            c_id = '%i' % c_id
            COURSES[c_id] = {'name': args['name'], 'p_id': args['p_id']}
            return COURSES[c_id], 201

    class CourseRegistry(Resource):
        """Handles single entries; GET, DELETE, PUT"""

        def get(self, r_id):
            abort_if_elem_not_exist(r_id, COURSE_REGISTRIES, "Course Registry")
            return COURSE_REGISTRIES[r_id]

        def delete(self, r_id):
            abort_if_elem_not_exist(r_id, COURSE_REGISTRIES, "Course Registry")
            del COURSE_REGISTRIES[r_id]
            return '', 204

        def put(self, r_id):
            args = r_parser.parse_args()
            course_registry = {'c_id': args['c_id'], 's_id': args['s_id']}
            COURSE_REGISTRIES[r_id] = course_registry
            return course_registry, 201

    class CourseRegistryList(Resource):
        """Handles multiple entries: GET, POST"""

        def get(self):
            return COURSE_REGISTRIES

        def post(self):
            args = r_parser.parse_args()
            r_id = int(max(COURSE_REGISTRIES.keys()).lstrip('course_registry')) + 1
            r_id = '%i' % r_id
            COURSE_REGISTRIES[r_id] = {'c_id': args['c_id'], 's_id': args['s_id']}
            return COURSE_REGISTRIES[r_id], 201

    """API Resource Routing"""
    # Professors
    api.add_resource(ProfessorList, '/professors')
    api.add_resource(Professor, '/professors/<p_id>')
    # Students
    api.add_resource(StudentList, '/students')
    api.add_resource(Student, '/students/<s_id>')
    # Courses
    api.add_resource(CourseList, '/courses')
    api.add_resource(Course, '/courses/<c_id>')
    # Course Registries
    api.add_resource(CourseRegistryList, '/courses/registries')
    api.add_resource(CourseRegistry, '/courses/registries/<r_id>')

    return app


# if __name__ == '__main__':
#     app.run(debug=True)
