from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
import os

# Create the db object
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    # Load configurations
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'you-will-never-guess')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///jamdate.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        # Import parts of the app
        from app import views
        db.create_all()

    return app
