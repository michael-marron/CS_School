from flask import Flask

from flask_sqlalchemy import SQLAlchemy


def create_app(config_file=None):
    # create and configure the app
    app = Flask(__name__)

    app.add_url_rule("/home", view_func=routes.home_page)
    app.add_url_rule("/", view_func=routes.calendar_page)
    app.add_url_rule("/calendar", view_func=routes.calendar_page)
    app.add_url_rule("/test", view_func=routes.home_page)
    app.add_url_rule("/tutorPage", view_func=routes.tutor_page, methods=["POST", "GET"])
    app.add_url_rule('/get_dictionary/<string:weekday>', view_func=routes.get_dictionary, methods=["POST"])


    app.config['SECRET_KEY'] = "secret"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

    


    return app

#This is where we will declare the db, login manager, 
from tutor_service import routes