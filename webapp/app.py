from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

PROFESSORS = {
    '1': {'name': 'Alice'},
    '2': {'name': 'Bob'}
}


def abort_if_prof_not_exist(prof_id):
    """Handles non existing professor"""
    if prof_id not in PROFESSORS:
        abort(404, message="Professor {} does not exist".format(prof_id))


parser = reqparse.RequestParser()
parser.add_argument('name')


class Professor(Resource):
    """Handles single entries; GET, DELETE, PUT"""

    def get(self, prof_id):
        abort_if_prof_not_exist(prof_id)
        return PROFESSORS[prof_id]

    def delete(self, prof_id):
        abort_if_prof_not_exist(prof_id)
        del PROFESSORS[prof_id]
        return '', 204

    def put(self, prof_id):
        args = parser.parse_args()
        professor = {'name': args['name']}
        PROFESSORS[prof_id] = professor
        return professor, 201


class ProfessorList(Resource):
    """Handles multiple entries: GET, POST"""

    def get(self):
        return PROFESSORS

    def post(self):
        args = parser.parse_args()
        prof_id = int(max(PROFESSORS.keys()).lstrip('professor')) + 1
        prof_id = '%i' % prof_id
        PROFESSORS[prof_id] = {'name': args['name']}
        return PROFESSORS[prof_id], 201


# API Resource Routing
api.add_resource(ProfessorList, '/professors')
api.add_resource(Professor, '/professors/<prof_id>')

if __name__ == '__main__':
    app.run(debug=True)
