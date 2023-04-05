import json

from flask import Flask, request, render_template, redirect, url_for, flash
from tutor_service.helper_functions import get_time_list, get_weekdays, get_columns, create_column_list

# from tutor_service.tutorFuctions import get_dictionary


# from tutor_service.tutorFunctions import get_dictionary
myDictionary = {}


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
    times = get_time_list(8, 21)
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if request.method == 'POST':
        # print("trying to print table data ", request.form['dictionary'])
        print("post request")
    else:
        print("bye")
    return render_template('tutorPage.html', times=times, weekdays=weekdays, total_cols=total_cols)


# @app.route('/my_function')
def add_to_dictionary(entire):
    #get data that was sent in tutorHelp.js
    req = json.loads(request.get_data())
    temp = req
    #split the string into 2 parts: day and time
    split_string = temp.split(" ", 1)
    #key = day
    key = split_string[0]
    #value = time
    value = split_string[1]

    #check if the key is in the dictionary
    if key not in myDictionary.keys():
        myDictionary[key] = value
    elif type(myDictionary[key]) == list:
        myDictionary[key].append(value)
    else:
        myDictionary[key] = [myDictionary[key], value]

    #debug statement to see format of dictionary
    #print(myDictionary)
    return ('/')


def remove_from_dictionary(entire):
    req = json.loads(request.get_data())
    # temp = request.get_json(entire)
    split_string = req.split(" ", 1)
    key = split_string[0]
    value = split_string[1]

    k = myDictionary.get(key,None) # returns None if key not found
    if isinstance(k,list) and k: # this is a list, and not empty
        v = k.index(value)
        myDictionary[key].pop(v)
        # k.pop(v)
    else:
        # error message
        print("Warning: nothing done")

    #debug statements to see what is being deleted from dictionary
    #print("trying to delete ", req)
    #print(myDictionary)
    return ('/')
def get_dictionary():
    #debug statement to see format of dictionary

    print(myDictionary)
    return myDictionary

# Monday -> [8-8:30], [10-10:30]
# Wednesday -> [9-9:30], [10-10:30]
