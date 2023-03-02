from flask import Flask, Blueprint
from .app_roles import app_roles
def create_app():
    create_app = Flask(__name__)

    
    create_app.register_blueprint(app_roles)

    return create_app
