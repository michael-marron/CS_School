<<<<<<< Updated upstream
from tutor_service import create_app
=======
from app_manager import create_app
from db_manager import create_db

from tutor_service.helper_functions import get_time_list, get_weekdays, get_columns, create_column_list
from flask import Flask, request, session, redirect, url_for, render_template, flash
import psycopg2,psycopg2.extras
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message
from tutor_service.extensions import mail
>>>>>>> Stashed changes

app = create_app()
db = create_db(app)

@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/calendar', methods=['GET','POST'])
def calendar_page():
    times = get_time_list(start=8, end=21)
    weekdays = get_weekdays()
    # num_cols_per_day = 5
    cols_list = ["Tutor", "Tutor Service",
        "Zoom Link", "Spaces Available", "Confirm"]
    total_cols = create_column_list(cols_list, 7)
    # total_cols = len(weekdays) * num_cols_per_day
    return render_template('calendar.html', times=times, weekdays=weekdays, total_cols=total_cols, cols_list=cols_list)  


@app.route('/test')
def test_page():
    return render_template('home.html')    


@app.route('/reset', methods=['GET','POST'])
def reset():
    return render_template('reset.html')


@app.route('/foo')
def foo():
    return render_template('mail.html')


@app.route('/email', methods=['GET','POST'])
def email():
    msg = Message('Session Scheduled', sender =   'noreply@csschool.io', recipients = ['paul@mailtrap.io'])
    msg.body = "Hey Paul, your session has been scheduled!"
    mail.send(msg)
    return "Message sent!"


@app.route('/db', methods=['GET','POST'])
def see_db():
    fname= request.form['fname']
    lname=request.form['lname']
    pet=request.form['pets']

    student= db_manager.Student(fname,lname,pet)
    db.session.add(student)
    db.session.commit()

  #fetch a certain student2
    studentResult=db.session.query(db_manager.Student).filter(db_manager.Student.id==1)
    for result in studentResult:
        print(result.fname)
    return render_template('db.html')


if __name__ == '__main__':
    app.run(debug=True)

