from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
db = SQLAlchemy()
db.init_app(app)
app.config.from_object(Config)
migrate = Migrate(app, db)

from app import views


