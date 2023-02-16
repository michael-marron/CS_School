#from:https://www.digitalocean.com/community/tutorials/how-to-use-a-postgresql-database-in-a-flask-application
#from: codemy.com https://www.youtube.com/watch?v=bxyaJ8w_wak
#from: frecodecamp.org https://www.youtube.com/watch?v=Qr4QMBUPxWo https://github.com/jimdevops19/FlaskSeries
#From: https://tutorial101.blogspot.com/2021/04/python-flask-postgresql-login-register.html


from flask import Flask, request, session, redirect, url_for, render_template, flash
import psycopg2,psycopg2.extras
import re, os # use regular expression to check for valid email and username
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

#connect to DB

DB_HOST = "localhost"
DB_NAME = "login"
DB_USER = "postgres"
DB_PASS = "000000"
 
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

@app.route('/')
def index():
    return render_template('index.html')

# login page
@app.route('/login')
def login():
    return render_template('login.html')

# register
@app.route('/reg', methods=['GET', 'POST'])
def reg():
    # bound to the db
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) 
 
    # Check if input POST requests exist
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
   
        print (username, email, password ) #check for input in dev stage

        hashedpass = generate_password_hash(password) #hask password before storing

        #Check if account exists 
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        account = cursor.fetchone()
        print(account) #show account in terminal 

        # message prompt after input

        # existing acc:
        if account:
            flash('Account already exists! Please log in.')
        # invalid email (using regular expression)
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            flash('Invalid email address!')
        # invalid username (only accept numbers and chars)
        elif not re.match(r'[A-Za-z0-9]+', username):
            flash('Invalid!\nUsername must contain only characters and numbers')
        # not enough input
        elif not username or not password or not email:
            flash('Please fill out the information to register!')
        # create new acc if pass all checks
        else:
            cursor.execute("INSERT INTO users (username, password, email) VALUES (%s,%s,%s)", (username, hashedpass, email))
            conn.commit()
            flash('You have successfully registered!')

   
    return render_template('reg.html')

if __name__ == "__main__":
    app.run(debug=True)
