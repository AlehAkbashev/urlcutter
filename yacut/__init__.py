from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from settings import Settings
from .converters import RegexConverter


app = Flask(__name__, static_folder='static')
app.config.from_object(Settings)
app.url_map.converters['regex'] = RegexConverter


db = SQLAlchemy(app)
migrate = Migrate(app, db)

from yacut import views, error_handlers, api_views

