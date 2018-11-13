from sqlalchemy import Column, Integer, String, DateTime, Boolean
from app import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    full_name = db.Column(db.String(120), index=True)
    smu_id = db.Column(db.String(12), index=True, unique=True)
    location = db.Column(db.String(120))
    admin_status = db.Column(db.Boolean, default=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __init__(self, email, smu_id, full_name):
        self.email = email
        self.smu_id = smu_id
        self.full_name = full_name

    def __repr__(self):
        return '<User {}>'.format(self.email)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
 