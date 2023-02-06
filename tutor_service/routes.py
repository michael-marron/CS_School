from tutor_service import app
from flask import render_template, redirect, url_for, flash 

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/test')
def test_page():
    return render_template('home.html')    