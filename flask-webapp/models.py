"""
TITLE: models.py
ABOUT: Provide Model and Schema classes for serializing data
AUTHOR: Morgan Reilly
LINKS:
    * https://stackoverflow.com/questions/61810855/sqlalchemy-orm-exc-unmappedinstanceerror-class-builtins-dict-is-not-mapped
"""
from config import db, ma
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field


class Professor(db.Model):
    __tablename__ = 'professor'
    p_id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(32))
    fname = db.Column(db.String(32))


class ProfessorSchema(SQLAlchemyAutoSchema):
    # Used to find SQLAlchemy model and db session
    class Meta:
        model = Professor
        include_relationships = True
        load_instance = True


class Course(db.Model):
    __tablename__ = 'course'
    c_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32))
    p_id = db.Column(db.Integer)


class CourseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Course
        include_relationships = True
        load_instance = True


class Student(db.Model):
    __tablename__ = 'student'
    s_id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(32))
    fname = db.Column(db.String(32))


class StudentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Student
        include_relationships = True
        load_instance = True
