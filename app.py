import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
######################################
#### SET UP OUR SQLite DATABASE #####
####################################

# This grabs our directory
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# Connects our Flask App to our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


class Student(db.Model):
    __tablename__ = "student"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    # one to many  student has many teachers
    teacher = db.relationship('Teacher', backref='Student', lazy='dynamic')
# one to on one student has one Hod
    hod = db.relationship('Hod', backref='Student', uselist=False)

    def __init__(self, name):
        # Note how a puppy only needs to be initalized with a name!
        self.name = name

    def __repr__(self):
        if self.hod:
            return f"student name is {self.name} and hod is {self.hod.name}"
        else:
            return f"student name is {self.name} and has no hod assigned yet."

    def report_Teachers(self):
        print("Here are my TEachers!")
        for tech in self.teacher:
            print(tech.tech_name)


class Teacher(db.Model):
    __tabelname__ = "teacher"
    id = db.Column(db.Integer, primary_key=True)
    tech_name = db.Column(db.Text)
    # Connect the toy to the puppy that owns it.
    # We use puppies.id because __tablename__='puppies'
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))

    def __init__(self, tech_name, student_id):
        self.tech_name = tech_name
        self.student_id = student_id


class Hod(db.Model):
    __tabelname__ = "hod"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    # Connect the toy to the puppy that owns it.
    # We use puppies.id because __tablename__='puppies'
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
