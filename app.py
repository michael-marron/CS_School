#from:https://www.digitalocean.com/community/tutorials/how-to-use-a-postgresql-database-in-a-flask-application
#from: codemy.com https://www.youtube.com/watch?v=bxyaJ8w_wak
#from: frecodecamp.org https://www.youtube.com/watch?v=Qr4QMBUPxWo https://github.com/jimdevops19/FlaskSeries
#From: https://tutorial101.blogspot.com/2021/04/python-flask-postgresql-login-register.html


from flask import Flask, request, session, redirect, url_for, render_template, flash
import psycopg2,psycopg2.extras
import re, os # use regular expression to check for valid email and username
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'sosecret'

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

# create account
@app.route('/create/', methods=[ 'POST','GET'])
def create():
    # bound to the db during the registration
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) 
    
    print ("in create")

    # Check if input POST requests
    if 'username' in request.form and 'password' in request.form and 'email' in request.form and  request.method == 'POST':
        
        username = request.form['username']
        email = request.form['email']
        pwd = request.form['password']
        
        print ("user: ", username, email ) #check for input in dev stage

        

        #Check if account exists 
        cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
        account = cursor.fetchone()
    

        # message prompt after input

        # existing acc:
        if account:
            flash('Your account already exists! Please log in.')
        # invalid email (using regular expression)
        elif not re.match(r'[^@]+@+[^@]+.edu', email):
            flash('Please sign up with a .edu email address!')
            print ("---invalid email")
        # invalid username (only accept numbers and chars)
        elif not re.match(r'[A-Za-z0-9]+', username):
            flash('Only accpet characters and numbers for username!')
            print ("invalid name")
        # password requirement
        elif not re.match(r'[A-Za-z0-9]+', pwd):
            flash('Only accpet characters and numbers for username!')
            print ("invalid name")

        # create new acc in db if pass all checks, hask the pass before passing in
        else:
            cursor.execute("INSERT INTO users (email,username, password) VALUES (%s,%s,%s)", ( email,username,generate_password_hash(pwd)))
            conn.commit()
            flash('Account is successfully created!')
            print ("added")

    return render_template('create.html') #return the template with appropreate alert

# log in
@app.route('/signin/', methods=['GET', 'POST'])
def signin():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    # Check if "username" and "password" POST requests exist (user submitted form)
    if 'email' in request.form and 'password' in request.form and request.method == 'POST':
        email= request.form['email']
        pwd = request.form['password']
        print("in log in function")
 
        # fetch row in db
        cursor.execute('SELECT * FROM users WHERE email = %s', (email,)) # comma for tuples
        acc = cursor.fetchone()
        print ("fetch db row")
 
        if acc:         
            # If account exists in users table in out database
            if check_password_hash(acc['password'], pwd):
                # Create session data, we can access this data in other routes
                session['loggedin'] = True
                session['id'] = acc['id']
                session['email'] = acc['email']
                # Redirect to home page
                return redirect(url_for('index'))
            else:
                # username/password wrong
                flash('Incorrect email/password')
                print ("----wrong pass")
        else:
            # no acc found
            flash('No account found! Please create a new account.')

    return render_template('signin.html')

if __name__ == "__main__":
    app.run(debug=True)

