import os
import json
from flask_sqlalchemy import SQLAlchemy

db

def connect_db(app):
    app.config['SECRET_KEY'] = "secret"
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
    # username : password @ origin / db name
    # postgresql://csschool_db_user:yjDUamhvkOQqnai5zIZ8ySMCGkbMUOkh@dpg-cg53dbo2qv287cseev80-a.ohio-postgres.render.com/csschool_db

    db = SQLAlchemy(app)
    db.init_app(app)
    return db

def create_db(app):
    global db
    #if db is None:
    #    db = connect_db(app)
    db = connect_db(app)
    return db



class Student(db.Model):
    __tablename__='students'
    id=db.Column(db.Integer,primary_key=True)
    fname=db.Column(db.String(40))
    lname=db.Column(db.String(40))
    pet=db.Column(db.String(40))

def add_item(self,fname,lname,pet):
    self.fname=fname
    self.lname=lname
    self.pet=pet