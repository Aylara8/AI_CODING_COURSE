from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    profile = db.relationship('Profile', backref='user', uselist=False)
    resources = db.relationship('Resource', backref='uploader', lazy=True)

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hobby = db.Column(db.String(100))
    job_title = db.Column(db.String(100))
    contacts = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    filename = db.Column(db.String(100))
    # --- ADD THIS LINE BELOW ---
    cover_image = db.Column(db.String(500)) 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)