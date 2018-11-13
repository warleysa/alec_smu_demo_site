from sqlalchemy import Column, Integer, String, DateTime, Boolean
from app import db
from datetime import datetime

class Class(db.Model):
    __tablename__ = 'classes'
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(50))
    dept = db.Column(db.String(10))
    number = db.Column(db.String(5))
    desc = db.Column(db.String(120))

    def __init__(self, class_name=None, dept=None, number=None,desc=None):
        self.class_name = class_name
        self.dept = dept
        self.number = number
        self.desc = desc

    def __repr__(self):
        return '<Class %r>' % (self.class_name)