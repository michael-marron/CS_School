import os

from flask import Flask
 
#from tutor_service import routes
from tutor_service.extensions import mail

from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_login import UserMixin
import psycopg2

def create_app(config_file=None):
    # create and configure the app
    app = Flask(__name__)

    return app
