from flask import render_template, redirect, url_for, flash
from tutor_service.helper_functions import get_time_list, get_weekdays, get_columns, create_column_list
from flask import request, session, redirect, url_for, render_template, flash
import psycopg2, psycopg2.extras, re
from flask_admin import Admin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message
from .extensions import mail


# connect to local db
DB_HOST = "localhost"
DB_NAME = "login"
DB_USER = "postgres"
DB_PASS = "000000"


conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASS, host=DB_HOST)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
            password, "pbkdf2:sha256", 64)  # hask password , salt 64 bits

        # Check if account exists, use cursor.fetchon to get each row in the table
        cursor.execute('SELECT * FROM userinfo WHERE email = %s', (email,))  # keep this comma
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
                "INSERT INTO userinfo (email, firstname, lastname, userpassword) VALUES (%s,%s,%s, %s)", (email, fname,lname, hashedpass))
            conn.commit()
            flash('You have successfully registered!')
            print("added")

    print("Done!!!")

    # return the template with appropreate alert
    return render_template('register.html')

# log in-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def login():
   cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

   # Check if "username" and "password" POST requests exist (user submitted form)
   if 'email' in request.form and 'password' in request.form and request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        print("in log in function")

        # fetch row in db
        cursor.execute('SELECT * FROM userinfo WHERE email = %s',
                       (email,))  # comma for tuples
        account = cursor.fetchone()
        print("fetch db row")

        if account:
            password_rs = account['userpassword']

            # If account exists in users table in out database
            if check_password_hash(password_rs, password):
                # Create session data, we can access this data in other routes
                session['loggedin'] = True
                session['id'] = account['userid']
                session['email'] = account['email']
                # Redirect to home page
                return redirect(url_for('calendar_page'))
            else:
                # Account doesnt exist or username/password incorrect
                flash('Incorrect email/password')
        else:
            # Account doesnt exist or username/password incorrect
            flash('Incorrect email/password')

   else:
        print("input???")
   return render_template('login.html')


def reset():
    return render_template('reset.html')

def ad_page():
    return render_template('admin.html')


def home_page():
    return render_template('home.html')


def calendar_page():
    times = get_time_list(start=8, end=21)
    weekdays = get_weekdays()
    # num_cols_per_day = 5
    cols_list = ["Tutor", "Tutor Service",
        "Zoom Link", "Spaces Available", "Confirm"]
    total_cols = create_column_list(cols_list, 7)
    # total_cols = len(weekdays) * num_cols_per_day
    return render_template('calendar.html', times=times, weekdays=weekdays, total_cols=total_cols, cols_list=cols_list)


def foo():
  return render_template('mail.html')

def email():
  msg = Message('Session Scheduled', sender =   'noreply@csschool.io', recipients = ['paul@mailtrap.io'])
  msg.body = "Hey Paul, your session has been scheduled!"
  mail.send(msg)
  return "Message sent!"

def test_page():
    return render_template('home.html')    


def test_page():
    return render_template('home.html')
