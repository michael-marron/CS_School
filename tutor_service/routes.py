from flask import render_template, redirect, url_for, flash, session, current_app
import flask
from tutor_service.helper_functions import get_time_list, get_weekdays, get_columns, create_column_list
from flask import request, session, redirect, url_for, render_template, flash
import psycopg2, psycopg2.extras, re
from flask_admin import Admin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message
from .extensions import mail
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta,datetime
#from . import app

# connect to local db
DB_HOST = "localhost"
DB_NAME = "login"
DB_USER = "postgres"
DB_PASS = "000000"


conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

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
            password, "pbkdf2:sha256", 64)  # hash password , salt 64 bits

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

def configure_session_expiration():
    session.permanent = True
    current_app.permanent_session_lifetime = timedelta(seconds=5)
    session['expires_at'] = (datetime.now() + timedelta(seconds=5)).strftime('%Y-%m-%d %H:%M:%S.%f')
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
           expires_at = datetime.strptime(session['expires_at'], '%Y-%m-%d %H:%M:%S.%f')
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

                if account['userrole']== 'Admin': 
                    print ('expect Admin, get ', account['userrole'], " email: ", account['email'] )
                    configure_session_expiration()
                    return redirect(url_for('ad_page'))

                elif account['userrole']== 'Tutor': 
                    print ('expect Tutor, get ', account['userrole']," email: ", account['email'])
                    configure_session_expiration()
                    return redirect(url_for('calendar_page')) # do not have tutor page in the code, need route to tutor page
                
                else:
                # Redirect to home page
                    print ('expect student, get ', account['userrole'], ', name: ', account['firstname'], ", email: ", account['email'])
                    configure_session_expiration()
                    return redirect(url_for('calendar_page'))
            else:
                
                print('in log in _ wrong pass')
                flash('Incorrect email/password')
        else:
            print ('in log in page - wrong email')
            flash('Incorrect email/password')

   else:
        print("input???")
   return render_template('login.html')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def logout():

    #session.permanent = True
    #current_app.permanent_session_lifetime = timedelta(seconds=5)
    
    session.pop('expires_at', None)
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('email', None)
    session.pop('role', None)

    session.clear()
    
    session.modified = True

    return redirect(url_for('login'))

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

    # log user out after a certain amount of time 
    logout_after = 60

    return render_template('calendar.html', times=times, weekdays=weekdays, total_cols=total_cols, cols_list=cols_list, logout_after=logout_after)


def foo():
  return render_template('mail.html')

def email():
  msg = Message('Session Scheduled', sender =   'noreply@csschool.io', recipients = ['paul@mailtrap.io'])
  msg.body = "Hey Paul, your session has been scheduled!"
  mail.send(msg)
  return "Message sent!"

def test_page():
    return render_template('home.html')    

