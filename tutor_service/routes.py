from flask import render_template, redirect, url_for, flash
from tutor_service.helper_functions import get_time_list, get_weekdays


def home_page():
    return render_template('home.html')

def calendar_page():
    total_cols = 28
    times = get_time_list(8, 21)
    weekdays = get_weekdays()
    return render_template('calendar.html', times=times, weekdays=weekdays, total_cols=total_cols)    

def test_page():
    return render_template('home.html')    

