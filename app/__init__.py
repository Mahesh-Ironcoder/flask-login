import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, login_manager


APP = Flask(__name__)
APP.config['SECRET_KEY'] = 'MAHESH'
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

login_manager = LoginManager(APP)
login_manager.login_view = 'login'

db = SQLAlchemy(APP)
migrate = Migrate(APP, db)

from app import routes,models