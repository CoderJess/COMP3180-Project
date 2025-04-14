from datetime import datetime
from . import db

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    photo = db.Column(db.String(200))
    date_joined = db.Column(db.DateTime, default=datetime.utcnow)
    profiles = db.relationship('Profile', backref='user', lazy=True)

class Profile(db.Model):
    __tablename__ = 'profiles'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    parish = db.Column(db.String(50), nullable=False)
    biography = db.Column(db.Text, nullable=False)
    sex = db.Column(db.String(20), nullable=False)
    race = db.Column(db.String(50), nullable=False)
    birth_year = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Float, nullable=False)
    fav_cuisine = db.Column(db.String(50), nullable=False)
    fav_colour = db.Column(db.String(30), nullable=False)
    fav_school_subject = db.Column(db.String(50), nullable=False)
    political = db.Column(db.Boolean, nullable=False)
    religious = db.Column(db.Boolean, nullable=False)
    family_oriented = db.Column(db.Boolean, nullable=False)

class Favourite(db.Model):
    __tablename__ = 'favourites'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    fav_user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Define unique constraint to prevent duplicate favorites
    __table_args__ = (db.UniqueConstraint('user_id', 'fav_user_id', name='unique_favourite'),)