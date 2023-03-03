from flask import render_template, redirect, url_for, flash
from tutor_service.helper_functions import get_time_list, get_weekdays, get_columns, create_column_list


def home_page():
    return render_template('home.html')

def calendar_page():
    times = get_time_list(start=8, end=21)
    weekdays = get_weekdays()
    #num_cols_per_day = 5
    cols_list = ["Tutor", "Tutor Service", "Zoom Link", "Spaces Available", "Confirm"]
    total_cols = create_column_list(cols_list, 7)
    #total_cols = len(weekdays) * num_cols_per_day
    return render_template('calendar.html', times=times, weekdays=weekdays, total_cols=total_cols, cols_list=cols_list)    

def test_page():
    return render_template('home.html')    

