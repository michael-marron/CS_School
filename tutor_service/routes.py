from flask import Flask, request, render_template, redirect, url_for, flash
from tutor_service.helper_functions import get_time_list, get_weekdays, get_columns, create_column_list
# from tutor_service.tutorFunctions import get_dictionary


def home_page():
    return render_template('home.html')

def calendar_page():
    total_cols = 28
    times = get_time_list(8, 21)
    weekdays = get_weekdays()
    return render_template('calendar.html', times=times, weekdays=weekdays, total_cols=total_cols)

def test_page():
    return render_template('home.html')

def tutor_page():
    print("Hello!!")
    total_cols = 7
    times = get_time_list(8,21)
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if request.method == 'POST':
        # print("trying to print table data ", request.form['dictionary'])
        print("bye")
    else:
        print("bye")
    return render_template('tutorPage.html', times = times, weekdays=weekdays, total_cols = total_cols)
