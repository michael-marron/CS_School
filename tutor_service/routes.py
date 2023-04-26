from tutor_service.helper_functions import get_time_list, get_weekdays, get_columns, create_column_list, get_weekday
from tutor_service.forms import ConfirmSessionForm
import json
import flask
from flask import Flask, request, render_template, redirect, url_for, flash
from tutor_service.helper_functions import get_time_list, get_weekdays, get_columns, create_column_list
# from tutor_service.tutorFuctions import get_dictionary
from flask import render_template, redirect, url_for, flash, session, current_app, request
from flask import request, session, redirect, url_for, render_template, flash
import psycopg2
import psycopg2.extras
import re
from flask_admin import Admin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message
from .extensions import mail
from datetime import timedelta, datetime
from flask_sqlalchemy import SQLAlchemy

tutor_selected_from_dropdown = "all"

times_dictionary = {
    "8:00AM": 0,
    "8:30AM": 0,
    "9:00AM": 0,
    "9:30AM": 0,
    "10:00AM": 0,
    "10:30AM": 0,
    "11:00AM": 0,
    "11:30AM": 0,
    "12:00PM": 0,
    "12:30PM": 0,
    "1:00PM": 0,
    "1:30PM": 0,
    "2:00PM": 0,
    "2:30PM": 0,
    "3:00PM": 0,
    "3:30PM": 0,
    "4:00PM": 0,
    "4:30PM": 0,
    "5:00PM": 0,
    "5:30PM": 0,
    "6:00PM": 0,
    "6:30PM": 0,
    "7:00PM": 0,
    "7:30PM": 0,
    "8:00PM": 0,
    "8:30PM": 0
}

sessions = [
    {
        "id": "0", 
        "times_available": "10:00AM",
        "tutor": "Sarah",
        "tutor_service": "Machine Learning",
        "zoom_link": "sarah@zoom.com",
        "spaces_available": 3
    },
    {
        "id": "1", 
        "times_available": "3:00PM",
        "tutor": "John",
        "tutor_service": "Data Science",
        "zoom_link": "john@zoom.com",
        "spaces_available": 2
    },
    {
        "id": "2", 
        "times_available": "3:30PM",
        "tutor": "John",
        "tutor_service": "Data Science",
        "zoom_link": "john@zoom.com",
        "spaces_available": 2
    },
    {
        "id": "3", 
        "times_available": "9:00AM",
        "tutor": "Paul",
        "tutor_service": "Web Development",
        "zoom_link": "paul@zoom.com",
        "spaces_available": 1
    },
    {
        "id": "4", 
        "times_available": "12:00PM",
        "tutor": "Paul",
        "tutor_service": "Web Development",
        "zoom_link": "paul@zoom.com",
        "spaces_available": 1
    }
]

extra =  {
        "id": "5", 
        "times_available": "12:00PM",
        "tutor": "Sarah",
        "tutor_service": "Blockchain",
        "zoom_link": "sarah@zoom.com",
        "spaces_available": 1
    }

def home_page():
    return render_template('home.html')

def calendar_page():
    mock_data = []

    john_data = {
        "Times Available": {
            "Monday": ["10:00AM", "12:00PM"],
            "Tuesday": ["3:30PM"],
            "Friday": ["8:00PM"]
            }, 
        "Tutor" : "John",
        "Tutor Service": "Data Structures",
        "Zoom Link": "john@zoom.com",
        "Spaces Available": 1
    }

    jane_data = {
        "Times Available": {
            "Monday": ["3:00PM", "5:00PM"],
            "Wednesday": ["2:30PM"],
            "Saturday": ["6:00PM", "7:00PM"]
            }, 
        "Tutor" : "Jane",
        "Tutor Service": "Machine Learning",
        "Zoom Link": "jane@zoom.com",
        "Spaces Available": 3
    }

    simon_data = {
        "Times Available": {
            "Wednesday": ["3:00PM", "5:00PM"],
            "Thursday": ["10:00AM", ],
            "Sunday": ["8:00AM", "6:00PM", "7:00PM"]
            }, 
        "Tutor" : "Simon",
        "Tutor Service": "Front End Development",
        "Zoom Link": "Simon@zoom.com",
        "Spaces Available": 1
    }

    mock_data.append(john_data)
    mock_data.append(jane_data)
    mock_data.append(simon_data)

    times = get_time_list(start=8, end=21)
    weekdays_and_dates = get_weekdays()
    calendar_attributes = ["Tutor", "Tutor Service", "Zoom Link", "Spaces Available", "Confirm"]
    num_attributes = len(calendar_attributes)
    weekday = get_weekday()
    confirm_form = ConfirmSessionForm()
    tutor_set = set()
    
    global tutor_selected_from_dropdown
    global times_dictionary

    for session in sessions: 
        time_aval = session["times_available"]
        times_dictionary[time_aval]+=1

    for session in sessions:
        tutor_set.add(session["tutor"])

    if request.method == "POST":
        session_id_from_form = request.form.get('session_confirmed')
        for data in sessions:
            if data["id"] == session_id_from_form:
                if data["spaces_available"] > 0:
                    data["spaces_available"] = data["spaces_available"] - 1
                    flash("Congratulations! You have confirmed your tutoring session", category="success")

        if 'tutors_dropdown' in request.form:
            tutor_selected_from_dropdown = request.form.get('tutors_dropdown')            
    

    # log user out after a certain amount of time
    logout_after = 60

    #These three html pages represent different calendar page iterations
    #The html pages have a more in depth description of which each calendar page is attempting to accomplish in a comment on the html page itself 
    #calendar_seven_days.html
    #calendar_one_day_no_multiple_sessions.html
    #calendar_one_day_multiple_sessions_attempt.html
    return render_template('calendar_one_day_no_multiple_sessions.html', 
    times=times, 
    weekdays_and_dates=weekdays_and_dates, 
    calendar_attributes=calendar_attributes, 
    num_attributes=num_attributes, 
    mock_data=mock_data, 
    weekday=weekday, 
    confirm_form=confirm_form, 
    sessions=sessions,
    tutor_set=tutor_set,
    tutor_selected_from_dropdown=tutor_selected_from_dropdown,
    times_dictionary=times_dictionary,
    logout_after=logout_after)

def test_page():
    return render_template('home.html')    


# connect to local db
DB_HOST = "localhost"
DB_NAME = "login"
DB_USER = "postgres"
DB_PASS = "000000"

""" DB_HOST = "dpg-cg53dbo2qv287cseev80-a"
DB_NAME = "csschool_db"
DB_USER = "csschool_db_user"
DB_PASS = "yjDUamhvkOQqnai5zIZ8ySMCGkbMUOkh" """
SECRET_KEY = "secret"

#DATABASE_URL = 'postgresql://csschool_db_user:yjDUamhvkOQqnai5zIZ8ySMCGkbMUOkh@dpg-cg53dbo2qv287cseev80-a.ohio-postgres.render.com/csschool_db'

#conn = psycopg2.connect(DATABASE_URL, sslmode='disable', keepalives=1, keepalives_idle=30, keepalives_interval=10, keepalives_count=5)
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)


def register():
    # bound to the db during the registration
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    print("in register")

    # Check if input POST requests
    if 'firstname' in request.form and 'lastname' in request.form and 'password' in request.form and 'email' in request.form and request.method == 'POST' and 'confirmpass' in request.form:

        fname = request.form['firstname']
        lname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']
        confirmpass = request.form['confirmpass']

        print("user: ", fname, email)  # check for input in dev stage

        hashedpass = generate_password_hash(
            password, "pbkdf2:sha256", 64)  # hash password , salt 64 bits

        # Check if account exists, use cursor.fetchon to get each row in the table
        cursor.execute('SELECT * FROM userinfo WHERE email = %s',
                       (email,))  # keep this comma
        account = cursor.fetchone()

        # existing acc
        if account:
            flash('Account already exists! Please log in.')
        # invalid email (.re is regular expression)
        elif not re.match(r'[^@]+@+[A-Za-z0-9]+.edu', email):
            flash('Invalid email address! Only use .edu email to register!')
            print("---invalid email")
        # invalid firstrname (only accept numbers and chars)
        elif not re.match(r'[A-Za-z0-9]+', fname):
            flash('Invalid!\nUsername must contain only characters and numbers')
            print("---invalid name")
        # invalid lastname (only accept numbers and chars)
        elif not re.match(r'[A-Za-z0-9]+', lname):
            flash('Invalid!\nUsername must contain only characters and numbers')
            print("---invalid last name")
        # check password strength
        elif not re.match(r'^.{8,}$', password):
            flash("At least 8 characters for password!")
        # confirm password before signing up
        elif password != confirmpass:
            flash('Passwords do not match!')

        else:
            cursor.execute(
                "INSERT INTO userinfo (email, firstname, lastname, userpassword) VALUES (%s,%s,%s, %s)", (email, fname, lname, hashedpass))
            conn.commit()
            flash('You have successfully registered!')
            print("added")

    print("Done!!!")

    # return the template with appropreate alert
    return render_template('register.html')

# need to be emplemented, does not work yet


def configure_session_expiration():
    session.permanent = True
    current_app.permanent_session_lifetime = timedelta(seconds=5)
    session['expires_at'] = (
        datetime.now() + timedelta(seconds=5)).strftime('%Y-%m-%d %H:%M:%S.%f')

# log in-----------------------------------------------------------------------------------------------------------------------------------------------------------------------


def login():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    query = '''SELECT *
               FROM userinfo
               JOIN userrole
               ON userinfo.userid = userrole.userid
               WHERE userinfo.email = %s
            '''

    # Check if "username" and "password" POST requests exist (user submitted form)
    if 'email' in request.form and 'password' in request.form and request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        print("in log in function")

        if 'loggedin' in session and 'expires_at' in session:
            expires_at = datetime.strptime(
                session['expires_at'], '%Y-%m-%d %H:%M:%S.%f')
            if datetime.now() > expires_at:
                logout()
                flash('Your session has expired. Please log in again.')
            else:
                configure_session_expiration()

        cursor.execute(query, (email,))
        account = cursor.fetchone()

        print("fetch db row")

        if account:
            password_ = account['userpassword']

            # If account exists in users table in out database
            if check_password_hash(password_, password):
                # Create session data, we can access this data in other routes
                session['loggedin'] = True
                session['id'] = account['userid']
                session['email'] = account['email']
                session['role'] = account['userrole']

                if account['userrole'] == 'Admin':
                    print('expect Admin, get ',
                          account['userrole'], " email: ", account['email'])
                    configure_session_expiration()
                    return redirect(url_for('ad_page'))

                elif account['userrole'] == 'Tutor':
                    print('expect Tutor, get ',
                          account['userrole'], " email: ", account['email'])
                    configure_session_expiration()
                    # do not have tutor page in the code, need route to tutor page
                    return redirect(url_for('tutor_page'))

                else:
                    # Redirect to home page
                    print('expect student, get ', account['userrole'], ', name: ',
                          account['firstname'], ", email: ", account['email'])
                    configure_session_expiration()
                    return redirect(url_for('calendar_page'))
            else:

                print('in log in _ wrong pass')
                flash('Incorrect email/password')
        else:
            print('in log in page - wrong email')
            flash('Incorrect email/password')

    else:
        print("input???")
    return render_template('login.html')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def logout():

    # session.permanent = True
    # current_app.permanent_session_lifetime = timedelta(seconds=5)

    session.pop('expires_at', None)
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('email', None)
    session.pop('role', None)
    session.clear()

    session.modified = True

    return redirect(url_for('login'))

# not implemented


def reset():
    return render_template('reset.html')
# not implemented


def ad_page():
    return render_template('admin.html')


def home_page():
    return render_template('home.html')


def foo():
    return render_template('mail.html')


def email():
    msg = Message('Session Scheduled', sender='noreply@csschool.io',
                  recipients=['paul@mailtrap.io'])
    msg.body = "Hey Paul, your session has been scheduled!"
    mail.send(msg)
    return "Message sent!"


def home_page():
    return render_template('home.html')


# --------------------------------------------------------------------------------------------------------------------------------
myDictionary = {}


def tutor_page():

    logout_after = 60

    print("Hello!!")
    total_cols = 7
    times = get_time_list(8, 21)
    weekdays = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]
    if request.method == 'POST':
        finalResult = get_dictionary()
        # print("post request")
    else:
        print("bye")
    return render_template('tutorPage.html', times=times, weekdays=weekdays, total_cols=total_cols, logout_after=logout_after)


def add_to_dictionary(entire):
    # get data that was sent in tutorHelp.js
    req = json.loads(request.get_data())
    temp = req
    # split the string into 2 parts: day and time
    split_string = temp.split(" ", 1)
    # key = day
    key = split_string[0]
    # value = time
    value = split_string[1]

    # check if the key is in the dictionary
    if key not in myDictionary.keys():
        myDictionary[key] = value
    elif type(myDictionary[key]) == list:
        myDictionary[key].append(value)
    else:
        myDictionary[key] = [myDictionary[key], value]

    # print(myDictionary)
    return ('/')


def remove_from_dictionary(entire):
    req = json.loads(request.get_data())
    # temp = request.get_json(entire)
    split_string = req.split(" ", 1)
    key = split_string[0]
    value = split_string[1]

    k = myDictionary.get(key, None)  # returns None if key not found
    if isinstance(k, list) and k:  # this is a list, and not empty
        v = k.index(value)
        myDictionary[key].pop(v)
    else:
        # error message
        print("Warning: could not find ", key, " in dictionary")

    # debug statements to see what is being deleted from dictionary
    # print("trying to delete ", req)
    # print(myDictionary)
    return ('/')


def get_dictionary():
    # debug statement to see contents of dictionary
    # if request.method == 'POST':
    #     result = request.form
    # print("result: ", result)
    print(myDictionary)
    return myDictionary
