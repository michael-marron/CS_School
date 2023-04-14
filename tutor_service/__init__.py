
from flask import Flask
from tutor_service import routes
from tutor_service import routes
from flask import Flask, session
from datetime import timedelta
from .extensions import mail
from flask_sqlalchemy import SQLAlchemy

from flask_admin import Admin
from flask_security import RoleMixin, UserMixin
from flask_admin.contrib.sqla import ModelView
import psycopg2

def create_app(config_file=None):
    # create and configure the app
    app = Flask(__name__)

    methods = ['GET', 'POST']

    app.add_url_rule("/", view_func=routes.calendar_page)
    app.add_url_rule("/calendar", view_func=routes.calendar_page)
    app.add_url_rule("/test", view_func=routes.home_page)
    app.add_url_rule("/tutorPage", view_func=routes.tutor_page, methods=["POST", "GET"])
    app.add_url_rule('/add_to_dictionary/<string:entire>', view_func=routes.add_to_dictionary, methods=["POST"])
    app.add_url_rule('/remove_from_dictionary/<string:entire>', view_func=routes.remove_from_dictionary, methods=["POST"])
    app.add_url_rule("/get_dictionary", view_func=routes.tutor_page, methods=["POST"])

    # Log in- sign in, log out button,reset, admin, 
    app.add_url_rule("/log", view_func=routes.login, methods=['GET', 'POST'])
    app.add_url_rule("/reg", view_func=routes.register,
                     methods=['GET', 'POST'])
    app.add_url_rule("/reset", view_func=routes.reset, methods=['GET', 'POST'])
    app.add_url_rule("/admin", view_func=routes.ad_page,
                     methods=['GET', 'POST'])
    app.add_url_rule("/logout", view_func=routes.logout)

    app.config['SESSION_PERMANENT'] = True
    app.config['SESSION_TYPE'] = 'filesystem'

    #app.config['PERMANENT_SESSION_LIFETIME'] = 20



    # mail routes
    app.add_url_rule("/foo", view_func=routes.foo)
    app.add_url_rule("/email", view_func=routes.email, methods=methods)

    # set up mail server - if you want your own account, change username / password
    app.config['MAIL_SERVER'] = 'sandbox.smtp.mailtrap.io'
    app.config['MAIL_PORT'] = 2525
    app.config['MAIL_USERNAME'] = '15948b25a40464'
    app.config['MAIL_PASSWORD'] = '3791137de16d49'
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False

    mail.init_app(app)

    # db for app admin 
    DB_HOST = "dpg-cg53dbo2qv287cseev80-a"
    DB_NAME = "csschool_db"
    DB_USER = "csschool_db_user"
    DB_PASS = "yjDUamhvkOQqnai5zIZ8ySMCGkbMUOkh"
    app.config['SECRET_KEY'] = "secret"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://csschool_db_user:yjDUamhvkOQqnai5zIZ8ySMCGkbMUOkh@dpg-cg53dbo2qv287cseev80-a.ohio-postgres.render.com/csschool_db'
    db = SQLAlchemy(app)

    #class Post(db.Model)

    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='Tutor Service', template_mode='bootstrap3')
    #admin.add_view(ModelView(User, db.session))
    #admin.add_view(ModelView(Post, db.session))

#This is where we will declare the db, login manager, 

    return app

