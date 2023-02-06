from tutor_service import app
from flask import render_template, redirect, url_for, flash 
from tutor_service.helper_functions import get_time_list, get_weekdays

@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/')
@app.route('/calendar')
def calendar_page():
    total_cols = 28
    times = get_time_list(8, 21)
    weekdays = get_weekdays()
    return render_template('calendar.html', times=times, weekdays=weekdays, total_cols=total_cols)    

@app.route('/test')
def test_page():
    return render_template('home.html')    