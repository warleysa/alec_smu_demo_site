from sqlalchemy import Column, Integer, String, DateTime, Boolean
from app import db
from datetime import datetime

class TutorClasses(db.Model):
    __tablename__ = 'tutor_classes'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, primary_key=True)

    def __init__(self, class_name=None, dept=None, number=None,desc=None):
        self.class_name = class_name
        self.dept = dept
        self.number = number
        self.desc = desc

    def __repr__(self):
        return '<Class %r>' % (self.class_name)