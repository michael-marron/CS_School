# from https://exploreflask.com/en/latest/blueprints.html
from flask import request, session, render_template
from flask import Blueprint
import psycopg2,psycopg2.extras

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app_roles = Blueprint('app-roles', __name__, static_folder= "static", template_folder='template' )

app_roles.secret_key = 'sosecret'

#connect to DB
DB_HOST = "localhost"
DB_NAME = "login"
DB_USER = "postgres"
DB_PASS = "000000"
 
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

admin = Admin(app_roles)



app_roles.route('/index')
def index(): 
    return render_template ("index.html")

@app_roles.route('/roles')
def roles():
    return render_template('roles.html')
