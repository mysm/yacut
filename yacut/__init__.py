import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from settings import Config

template_dir = Config.TEMPLATE_FOLDER
if not template_dir:
    template_dir = "."
app = Flask(__name__, template_folder=template_dir)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import views
