from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


from settings import Settings


app = Flask(__name__, static_folder='static')
app.config.from_object(Settings)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from ya_cut import views

