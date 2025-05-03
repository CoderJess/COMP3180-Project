from . import db
from werkzeug.security import generate_password_hash
from datetime import datetime  # Import datetime directly

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    name = db.Column(db.String(80))
    password = db.Column(db.String(200))
    email = db.Column(db.String(120))
    photo = db.Column(db.String(120))
    date_joined = db.Column(db.DateTime, default=datetime.now)
    profiles = db.relationship('Profile', backref='user')

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id_fk = db.Column(db.Integer, db.ForeignKey('user.id')) 
    name = db.Column(db.String(80))
    description = db.Column(db.String(255))
    parish = db.Column(db.String(80))
    biography = db.Column(db.String(255))
    sex = db.Column(db.String(20))
    race = db.Column(db.String(50))
    birth_year = db.Column(db.Integer)
    height = db.Column(db.Float)
    fav_cuisine = db.Column(db.String(80))
    fav_colour = db.Column(db.String(80))
    fav_school_subject = db.Column(db.String(80))
    political = db.Column(db.Boolean)
    religious = db.Column(db.Boolean)
    family_oriented = db.Column(db.Boolean)


class Favourite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id_fk = db.Column(db.Integer)
    fav_user_id_fk = db.Column(db.Integer)

def is_authenticated(self):
    return True

def is_active(self):
    return True

def is_anonymous(self):
    return False

def get_id(self):
    try:
        return unicode(self.id)  # python 2 support
    except NameError:
        return str(self.id)  # python 3 support

def __repr__(self):
    return '<User %r>' % (self.username)