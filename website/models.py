from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
class Personalinfo(db.Model):
    workid=db.Column(db.String(100),db.ForeignKey('workspace.workid'))
    ids=db.Column(db.String(100), primary_key=True)
    name=  db.Column(db.String(100),nullable=False)
    
    phone=db.Column(db.Integer(),nullable=False)
    email = db.Column(db.String(150),nullable=False )
    freelance = db.Column(db.String(150),nullable=True )
    degree=db.Column(db.String(150),nullable=False )
    age=db.Column(db.Integer(),nullable=False)
    designation=db.Column(db.String(150),nullable=False )
    yoex=db.Column(db.Integer(),nullable=True)
    project=db.Column(db.Integer(),nullable=True)
    hpclients=db.Column(db.Integer(),nullable=True)
    awards=db.Column(db.Integer(),nullable=True)
    about=db.Column(db.String(100000),nullable=False)

class Skill(db.Model):
    workid=db.Column(db.String(100),db.ForeignKey('workspace.workid'))
    ids=db.Column(db.String(100), primary_key=True)
    skill=db.Column(db.String(100),nullable=False)
    perc=db.Column(db.Integer(),nullable=False)
    

class Education(db.Model):
    workid=db.Column(db.String(100),db.ForeignKey('workspace.workid'))
    ids=db.Column(db.String(100), primary_key=True)
    course=db.Column(db.String(1000),nullable=True)
    year=db.Column(db.String(1000),nullable=True)
    descr=db.Column(db.String(10000000),nullable=True)
    clg=db.Column(db.String(1000),nullable=True)
    

class Experience(db.Model):
    workid=db.Column(db.String(100),db.ForeignKey('workspace.workid'))
    ids=db.Column(db.String(100), primary_key=True)
    title=db.Column(db.String(1000),nullable=True)
    year=db.Column(db.String(1000),nullable=True)
    descr=db.Column(db.String(10000000),nullable=True)
    company=db.Column(db.String(1000),nullable=True)
    
    
class Note(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    data = db.Column(db.String(1000000))
    title = db.Column(db.String(10000))
    privacy = db.Column(db.String(100))
    date = db.Column(db.DateTime(timezone=True),default=func.now())
    userid = db.Column(db.String(100),db.ForeignKey('user.id'))

class Workspace(db.Model):
    workid = db.Column(db.String(100), primary_key=True)
    name=db.Column(db.String(150),nullable=False)

class User(db.Model, UserMixin):
    id = db.Column(db.String(100), primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(500))
    name = db.Column(db.String(150))
    workid=db.Column(db.String(100),db.ForeignKey('workspace.workid'))
    notes=db.relationship('Note')
    workspace=db.relationship('Workspace')

