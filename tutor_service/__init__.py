from flask import Flask

from .extensions import mail

from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_login import UserMixin
import psycopg2

def create_app(config_file=None):
    # create and configure the app
    app = Flask(__name__)
    
    methods = ['GET', 'POST']



    app.add_url_rule("/", view_func=routes.calendar_page)
    app.add_url_rule("/calendar", view_func=routes.calendar_page)
    app.add_url_rule("/test", view_func=routes.home_page)
    app.add_url_rule("/log", view_func=routes.login, methods=['GET','POST'])
    app.add_url_rule("/reg", view_func=routes.register, methods=['GET','POST'])
    app.add_url_rule("/reset", view_func=routes.reset, methods=['GET','POST'])
    app.add_url_rule("/admin", view_func=routes.ad_page, methods=['GET','POST'])

    app.config['SECRET_KEY'] = "secret"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://csschool_db_user:yjDUamhvkOQqnai5zIZ8ySMCGkbMUOkh@dpg-cg53dbo2qv287cseev80-a.ohio-postgres.render.com/csschool_db'

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
