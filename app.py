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

# login page
@app.route('/login')
def login():

    print("------ in login")
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) #bound to the db
   
    # get user input
    if 'email' in request.form and 'password' in request.form and  request.method == 'POST':
        inputEmail = request.form['email']
        inputPass = request.form['password']
 
        # get rows from db to match with user input
        cursor.execute('SELECT * FROM users WHERE email = %s', (inputEmail,)) # keep comma behind email as its a tuple
        dbAcc = cursor.fetchone()
 
        if dbAcc:
            print(inputEmail)

            # hashed and input pass match:
            if check_password_hash(dbAcc['password'], inputPass):
                # get session data for later use
                session['loggedin'] = True
                session['id'] = ['id']
                session['email'] = dbAcc['email']

                # load main page for user with vallid credentials
                return redirect('/index.html')
            
            # if hashed match but email does not ( do not let user know whether pass or email does not match, for security reason)
            else:
                flash('Incorrect username/password')  #send message with flash, combine with get_flash_message in html
        else:
            # inputs do not match any attribute in the db
            flash('Incorrect username/password')
   
    return render_template('login.html') #return the login template with appropreate message

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
            cursor.execute("INSERT INTO users (email,username, pass) VALUES (%s,%s,%s)", ( email,username,hashedpass))
            conn.commit()
            flash('You have successfully registered!')
            print ("added")


    print ("Done!!!")

    return render_template('register.html') #return the template with appropreate alert


if __name__ == "__main__":
    app.run(debug=True)

