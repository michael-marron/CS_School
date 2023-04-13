from tutor_service import routes
from flask import Flask

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

    # Log in- sign in, reset, admin
    app.add_url_rule("/log", view_func=routes.login, methods=['GET', 'POST'])
    app.add_url_rule("/reg", view_func=routes.register,
                     methods=['GET', 'POST'])
    app.add_url_rule("/reset", view_func=routes.reset, methods=['GET', 'POST'])
    app.add_url_rule("/admin", view_func=routes.ad_page,
                     methods=['GET', 'POST'])
    app.add_url_rule("/logout", view_func=routes.logout)

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

    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(200), nullable=False)
        email = db.Column(db.String(200), nullable=False, unique=True)
        password = db.Column(db.String(255), nullable=False)

    #class Post(db.Model)

    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='Tutor Service', template_mode='bootstrap3')
    admin.add_view(ModelView(User, db.session))
    #admin.add_view(ModelView(Post, db.session))


    return app