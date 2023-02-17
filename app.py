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

# test page
@app.route('/test')
def test():
    return render_template('test.html')
# login page
@app.route('/login')
def login():
    return render_template('login.html')

# register
@app.route('/reg', methods=['GET', 'POST'])
def reg(request):
    # bound to the db during the registration
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) 
    
    print ("in register")

    # Check if input POST requests
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        print (username, email, password ) #check for input in dev stage

        hashedpass = generate_password_hash(password) #hask password before storing

        #Check if account exists 
        cursor.execute('SELECT * FROM userlist WHERE username = %s', (username,))
        account = cursor.fetchone()
        print(account) #show account in terminal

        # message prompt after input

        # existing acc:
        if account:
            flash('Account already exists! Please log in.')
        # invalid email (using regular expression)
        elif not re.match(r'[^@]+@ufl.edu', email):
            flash('Invalid email address!')
        # invalid username (only accept numbers and chars)
        elif not re.match(r'[A-Za-z0-9]+', username):
            flash('Invalid!\nUsername must contain only characters and numbers')
        # not enough input
        elif not username or not password or not email:
            flash('Please fill out the information to register!')
        # create new acc if pass all checks
        else:
            cursor.execute("INSERT INTO userlist (username,email, pass) VALUES (%s,%s,%s)", (username, email, hashedpass))
            conn.commit()
            flash('You have successfully registered!')
            print ("added")

    elif request.method == 'POST': #require user input
        flash('Please fill out the form!')

    return render_template('reg.html') #return the template with appropreate alert

if __name__ == "__main__":
    app.run(debug=True)

