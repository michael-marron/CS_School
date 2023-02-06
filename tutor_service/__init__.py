from flask import Flask


app = Flask(__name__)

#This is where we will declare the db, login manager, 

from tutor_service import routes