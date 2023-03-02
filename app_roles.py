# from https://exploreflask.com/en/latest/blueprints.html
from flask import request, session, render_template
from flask import Blueprint
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


app_roles = Blueprint('app-roles', __name__, static_folder= "static", template_folder='template' )

app_roles.route('/index')
def index(): 
    return render_template ("index.html")

@app_roles.route('/roles')
def roles():
    return render_template('roles.html')
