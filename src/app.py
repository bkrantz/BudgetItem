from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

import src.config

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from src.models import *
from src.views import *