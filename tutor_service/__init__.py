from flask import Flask
from .extensions import mail
from flask_sqlalchemy import SQLAlchemy


def create_app(config_file=None):
    # create and configure the app
    app = Flask(__name__)

    app.add_url_rule("/home", view_func=routes.home_page)
    app.add_url_rule("/", view_func=routes.calendar_page)
    app.add_url_rule("/calendar", view_func=routes.calendar_page)
    app.add_url_rule("/test", view_func=routes.home_page)

    app.config['SECRET_KEY'] = "secret"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

    # mail routes
    app.add_url_rule("/foo", view_func=routes.foo)
    app.add_url_rule("/email", view_func=routes.email, methods = methods)

    # set up mail server - if you want your own account, change username / password
    app.config['MAIL_SERVER']='sandbox.smtp.mailtrap.io'
    app.config['MAIL_PORT'] = 2525
    app.config['MAIL_USERNAME'] = '15948b25a40464'
    app.config['MAIL_PASSWORD'] = '3791137de16d49'
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    
    mail.init_app(app)
    


    return app

#This is where we will declare the db, login manager, 
from tutor_service import routes
