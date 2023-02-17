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

# register
@app.route('/register', methods=['GET', 'POST'])
def register():
    # bound to the db during the registration
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) 
    
    print ("in register")

    # Check if input POST requests
    if 'username' in request.form and 'password' in request.form and 'email' in request.form and  request.method == 'POST':
        
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        print ("user: ", username, email ) #check for input in dev stage

        hashedpass = generate_password_hash(password) #hask password before storing

        #Check if account exists 
        cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
        account = cursor.fetchone()
    

        # message prompt after input

        # existing acc:
        if account:
            flash('Account already exists! Please log in.')
        # invalid email (using regular expression)
        elif not re.match(r'[^@]+@ufl.edu', email):
            flash('Invalid email address!')
            print ("---invalid email")
        # invalid username (only accept numbers and chars)
        elif not re.match(r'[A-Za-z0-9]+', username):
            flash('Invalid!\nUsername must contain only characters and numbers')
            print ("invalid pass")
        # not enough input
        elif not username or not password or not email:
            flash('Please fill out the information to register!')
        # create new acc if pass all checks
        else:
            cursor.execute("INSERT INTO users (email,username, password) VALUES (%s,%s,%s)", ( email,username,hashedpass))
            conn.commit()
            flash('You have successfully registered!')
            print ("added")


    print ("Done!!!")

    return render_template('register.html') #return the template with appropreate alert

@app.route('/login/', methods=['GET', 'POST'])
def login():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    # Check if "username" and "password" POST requests exist (user submitted form)
    if 'email' in request.form and 'password' in request.form and request.method == 'POST':
        email= request.form['email']
        password = request.form['password']
        print("in log in function")
 
        # fetch row in db
        cursor.execute('SELECT * FROM users WHERE email = %s', (email,)) # comma for tuples
        account = cursor.fetchone()
        print ("fetch db row")
 
        if account:
            password_rs = account['password']
         
            # If account exists in users table in out database
            if check_password_hash(password_rs, password):
                # Create session data, we can access this data in other routes
                session['loggedin'] = True
                session['id'] = account['id']
                session['email'] = account['email']
                # Redirect to home page
                return redirect(url_for('index'))
            else:
                # Account doesnt exist or username/password incorrect
                flash('Incorrect email/password')
        else:
            # Account doesnt exist or username/password incorrect
            flash('Incorrect email/password')
 
    else: 
        print ("input???")

    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)

