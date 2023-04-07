from flask import Flask
from tutor_service import routes
from flask_sqlalchemy import SQLAlchemy


def create_app(config_file=None):
    # create and configure the app
    app = Flask(__name__)

    app.add_url_rule("/home", view_func=routes.home_page)
    app.add_url_rule("/", view_func=routes.calendar_page)
    app.add_url_rule("/calendar", view_func=routes.calendar_page)
    app.add_url_rule("/test", view_func=routes.home_page)
    app.add_url_rule("/tutorPage", view_func=routes.tutor_page, methods=["POST", "GET"])
    app.add_url_rule('/add_to_dictionary/<string:entire>', view_func=routes.add_to_dictionary, methods=["POST"])
    app.add_url_rule('/remove_from_dictionary/<string:entire>', view_func=routes.remove_from_dictionary, methods=["POST"])
    app.add_url_rule("/get_dictionary", view_func=routes.tutor_page, methods=["POST"])

    app.config['SECRET_KEY'] = "secret"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

    


    return app

#This is where we will declare the db, login manager, 
