# This file is for the actual test definitions
'''
These are the tests I have written and ran so far on a toy app that I made. Trying to run these on the code
in github will probably result in an import error being thrown because there is no "app.py" in our project.
It will take some time to sync these with the actual code, but the testing framework is set up.
'''

# 1. Test that Flask is set up correctly

def test_setup(client):
    '''
    GIVEN a null state
    WHEN a new connection is created
    THEN check that flask is set up correctly
    '''
    response = client.get("/welcome")
    assert response.status_code == 200

# 2. Test login and logout

def test_login_prompt(client):
    '''
    GIVEN that the app is set up correctly
    WHEN the user tries to access the app
    THEN check that the user is prompted to login
    '''
    response = client.get("/login")
    assert b"Please login" in response.data

def test_valid_login(client):
    '''
    GIVEN a session
    WHEN the user enters valid valid credentials
    THEN check that the user is logged in
    '''
    client.post('/login', data={"username":"admin", "password": "password"})
    response = client.post(
            '/login',
            data = dict(username="admin", password="admin"),
            follow_redirects=True
    )
    assert (response.status_code == 200) and (b"Hello World!" in response.data)


def test_invalid_password(client):
    '''
    GIVEN a session
    WHEN the user enters invalid password
    THEN check that the user is denied access
    '''

    #TODO this will have to be updated once the DB is working

    client.post('/login', data={"username":"admin", "password": "password"})
    response = client.get("/")
    assert response.status_code == 401

def test_invalid_username(client):
    '''
    GIVEN a session
    WHEN the user enters invalid username
    THEN check that the user is denied access
    '''

    # TODO this will have to be updated once the DB is working

    client.post('/login', data={"username":"Uncle Bob", "password": "admin"})
    response = client.get("/")
    assert response.status_code == 401

def test_logout(self):
    '''
    GIVEN a session
    WHEN the user logs out
    THEN a message will be displayed
    '''
    tester = app.test_client(self)
    response = tester.post('/login',data = dict(username="admin", password="admin"), follow_redirects=True)
    response = tester.get('/logout', follow_redirects = True)
    assert b"You were just logged out" in response.data

def test_logout_redirect(self):
    '''
    GIVEN a session
    WHEN the user logs out
    THEN they are redirected to welcome page
    '''
    tester = app.test_client(self)
    response = tester.post('/login',data = dict(username="admin", password="admin"), follow_redirects=True)
    response = tester.get('/logout', follow_redirects = True)
    response = client.get("/welcome")
    assert response.status_code == 200

def test_logout_requires_login(client):
    '''
    GIVEN a session
    WHEN the user is not logged in
    THEN the logout page is inaccessible
    '''
    response = client.get("/logout")
    assert response.status_code == 401

# 3. Test DB connection

# TODO valid write to DB

# valid read from DB
def test_DB_read(self):
    '''
    GIVEN a database containing the message "Hello from DB"
    WHEN the home page is displayed
    THEN the message from DB is displayed
    '''

    '''
    Here I am assuning that the database has been created and initialized with a 
    message "Hello from DB. This test was written for sqlite in another toy app I wrote.
    The toy app printed database entries onto the home page. I haven't tested it with
    postgres, and it wouldn't work on our app anyway. 
    '''

    tester = app.test_client()
    response = client.get('/login', data = dict(username="admin", password="admin"), follow_redirects=True)
    assert b"Hello from DB" in response.data


# 4. Test sign up
# valid sign up adds to DB
# valid sign up redirects to login page
# invalid email / non edu fails
# invalid password fails - too short
# invalid password fails - missing capital
# invalid password fails - missing number
# invalid password fails - missing symbol

# 5. Test calendar
# This will probably have to use selenium / playwright because of UI? I'm not sure how that is being implemented.
# In any case, it has to wait until the code is completed
