# This file is for the actual test definitions

from flask import url_for
import pytest

# 0. Test that Pytest is set up correctly
def test_null():
    '''
    GIVEN a running environment
    WHEN tests are run
    THEN check that no errors occur
    '''
    pass

# 1. Test that Playwright is set up correctly
def test_end_setup(page):
    '''
    GIVEN a running environment
    WHEN tests are run
    THEN check that end-to-end test framework is setup correctly
    '''
    page.goto("https://wonderproxy.com")
    assert page.title() == 'Localization testing with confidence - WonderProxy'

# 2. Test that Flask is set up correctly
def test_setup(client):
    '''
    GIVEN a null state
    WHEN a new connection is created
    THEN check that flask is set up correctly
    '''
    response = client.get("/home")
    assert response.status_code == 200

# 3. Test student login
def test_valid_login(client_db, app):
    '''
    GIVEN test database is created and populated
    WHEN given valid login credentials
    THEN the user can access app
    '''

    client.post("/login", data = {"username": "John", "password": "password"})
    response = client.get("/calendar")
    assert response.status_code = 200

def test_invalid_login_username(client_db, app):
    '''
    GIVEN test database is created and populated
    WHEN given invalid login credentials
    THEN the user cannot access the app
    '''

    client.post("/login", data = {"username": "Jhon", "password": "password"})
    response = client.get("/calendar")
    assert response.status_code = 401

def test_invalid_login_password(client_db):
    '''
    GIVEN test database is created and populated
    WHEN given invalid login credentials
    THEN the user cannot access the app
    '''
    
    client.post("/login", data = {"username": "John", "password": "notmypassword"})
    response = client.get("/calendar")
    assert response.status_code = 401
   
def	test_invalid_login_credentials(client_db):
    '''
    GIVEN test database is created and populated
    WHEN given invalid login credentials
    THEN the user cannot access the app
    ''' 

    client.post("/login", data = {"username": "Jorge", "password": "notmyschool"})
    response = client.get("/calendar")
    assert response.status_code = 401

# 4. Test tutor login
def	test_valid_login_tutor(client_db):
    '''
    GIVEN test database is created and populated
    WHEN given valid login credentials
    THEN the tutor can access app
    '''

    client.post("/tutor_login", data = {"username": "Tammy", "password": "letmein1234"})
    response = client.get("/calendar")
    assert response.status_code = 200

def	test_invalid_login_tutor_username(client_db):
    '''
    GIVEN test database is created and populated
    WHEN given invalid username
    THEN the tutor cannot access the app
    '''

    client.post("/tutor_login", data = {"username": "Tmamy", "password": "letmein1234"})
    response = client.get("/calendar")
    assert response.status_code = 401

def	test_invalid_login_tutor_password(client_db):
    '''
    GIVEN test database is created and populated
    WHEN given invalid password
    THEN the tutor cannot access the app
    '''
    
    client.post("/tutor_login", data = {"username": "Tammy", "password": "letmein134"})
    response = client.get("/calendar")
    assert response.status_code = 401

# 5. Test sign up
def test_valid_signup(client_db, app):
    '''
    GIVEN that database is empty and a table named User
    WHEN a user signs up
    THEN the database should be updated
    '''

    client.post("/register", data = {"username": "GarySpivey", "password": "psycicGuru247"})

    with app.app_context():
        assert User.query.count() == 1
        assert User.query.first().username == "GarySpivey"

def test_login_new_user(client_db, app):
    '''
    GIVEN that database is empty
    WHEN that user logs in
    THEN the dashboard is displayed
    '''

    client.post("/register", data = {"username": "GarySpivey", "password": "psycicGuru247"})
    client.post("/login", data = {"username": "GarySpivey", "password": "psycicGuru247"})
    response = client.get("/calendar")
    assert response.status_code = 200

# 6. Test calendar
def	test_view_calendar(student_login):
    '''
    GIVEN that a user is logged in
    WHEN they view the calendar page
    THEN the calendar is displayed
    '''

    response = student_login.get("/calendar")
    assert response.status == 200

# 7. Test join a session
def	test_book_success(student_login, app):
    '''
    GIVEN that a no sessions are scheduled
    WHEN the user books a session
    THEN the database is updated
    '''
    '''
    also assuming meeting id = 1234 and a table named Sessions
    '''
    response = student_login.post("/schedule/confirm", data = {"id": 1234})
    
    with app.app_context():
        assert Sessions.query.count() == 1
        assert Sessions.query.first().id == 1234

def	test_join_success(student_login, app):
    '''
    GIVEN a session is scheduled but not full
    WHEN a user joins that session
    THEN the database is updated
    '''

    '''
    This test should join a session 1235 where the session is scheduled but not full
    The previous test creates a new session
    '''
    
    response = student_login.post("/schedule/confirm", data = {"id": 1235})
    
    with app.app_context():
        assert Sessions.query.first().num_students == 2

def	test_join_success_message(student_login):
    '''
    GIVEN a student is logged in
    WHEN a user schedules a new session
    THEN a confirmation message is displayed
    '''

    response = student_login.post("/schedule", data = {"id": 1234})
    assert b"Session Scheduled" in response.data

def	test_join_success_email(student_login):
    '''
    GIVEN a student is logged in
    WHEN a user schedules a new session
    THEN a confirmation message is displayed
    '''
    student_login.post("/schedule", data = {"id": 1234})
    response = student_login.post("/schedule/email", data = {"id": 1234})
    assert response.status_code == 200


def	test_book_fail(student_login, app):
    '''
    GIVEN that a student has scheduled the maximum number of sessions
    WHEN that student tries to schedule a new session
    THEN the student cannot schedule a new session and an error message is returned
    '''

    student_login.post("/schedule/confirm", data = {"id": 1234})
    student_login.post("/schedule/confirm", data = {"id": 1235})
    response = student_login.post("/schedule/confirm", data = {"id": 1236})
    assert b"Oops! Too many sessions scheduled!" in response.data

def	test_join_fail(student_login):
    '''
    GIVEN thas a session is scheduled and full
    WHEN a student tries to join session
    THEN then error message is displayed
    '''

    '''
    Here we are assuming that session 1237 has been scheduled and is full
    '''
    
    student_login.post("/schedule/confirm", data = {"id": 1237})
    assert b"Oops! That session is full!" in response.data


# 8. Test cancel a session
def	test_cancel_success(student_login, app):
    '''
    GIVEN a session is scheduled
    WHEN a user cancels that session
    THEN the database is updated
    '''
    
    response = student_login.post("/cancel/confirm", data = {"id": 1234})
    
    with app.app_context():
        assert Sessions.query.count() == 0

def test_cancel_success_message(student_login):
    '''
    GIVEN a student is logged in
    WHEN a user cancels a session
    THEN a confirmation message is displayed
    '''

    response = student_login.post("/cancel/confirm", data = {"id": 1234})
    assert b"Session Canceled" in response.data

def	test_cancel_success_tutor(tutor_login, app):
    '''
    GIVEN a session is scheduled
    WHEN a tutor cancels that session
    THEN the database is updated
    '''
    
    response = tutor_login.post("/cancel/confirm", data = {"id": 1234})
    
    with app.app_context():
        assert Sessions.query.count() == 0

def	test_cancel_success_tutor_message(tutor_login):
    '''
    GIVEN a session is scheduled
    WHEN a tutor cancels that session
    THEN a confirmation message is displayed
    '''
    
    response = tutor_login.post("/cancel/confirm", data = {"id": 1234})
    assert b"Session Canceled" in response.data

# 9. Test tutor change settings
def	test_change_settings_success(tutor_login):
    '''
    GIVEN that a tutor has existing settings
    WHEN settings are changed
    THEN the database is updated
    '''
    '''
    On the settings page,
    change settings
    and confirm.
    Query the DB to ensure it returns correct result.
    '''
    pass

def	test_change_settings_fail(tutor_login):
    '''
    GIVEN that a tutor has existing settings
    WHEN settings change is not confirmed
    THEN the database is not updated
    '''
    '''
    On the settings page,
    change settings
    exit page without confirming
    Query the DB to ensure it returns correct result.
    '''
    pass

# 10. Test tutor schedule
def	test_create_schedule(tutor_login_no_db):
    '''
    GIVEN that a tutor has no existing schedule
    WHEN a schedule is created
    THEN the database is updated
    '''
    '''
    On the schedule page,
    create a schedule
    and confirm.
    Query the DB to ensure it returns correct result.
    '''
    pass

def	test_change_schedule_success(tutor_login):
    '''
    GIVEN that a tutor has an existing schedule
    WHEN a schedule is changed
    THEN the database is updated
    '''
    '''
    On the schedule page,
    change schedule
    and confirm.
    Query the DB to ensure it returns correct result.
    '''
    pass

def	test_change_schedule_fail(tutor_login):
    '''
    GIVEN that a tutor has an existing schedule
    WHEN a schedule change is not confirmed
    THEN the database is not updated
    '''
    '''
    On the schedule page,
    change schedule
    exit page without confirming
    Query the DB to ensure it returns correct result.
    '''
    pass

# 11. Test change shifts
def	test_change_shifts(tutor_login):
    '''
    GIVEN that a tutor has a set shift
    WHEN a shift is changed
    THEN the calendar is updated
    '''
    '''
    On the shift page page,
    change shift
    and confirm.
    Query the celendar to ensure it returns correct result.
    '''
    pass



# 12. Test session info
def	test_view_session_info_tutor(tutor_login):
    '''
    GIVEN that a student has scheduled a session
    WHEN the tutor clicks on that session from dashboard
    THEN session info is displayed
    '''
    response = tutor_login.get("/session/info", data = {"id": 1234})
    assert b"Time:" in response.data

def	test_view_session_info_student(student_login):
    '''
    GIVEN that a student has scheduled a session
    WHEN the student clicks on that session from dashboard
    THEN session info is displayed
    '''
    response = student_login.get("/session/info", data = {"id": 1234})
    assert b"Time:" in response.data

# 13. Test logout
def	test_login_required(client):
    '''
    GIVEN that a user is not logged in
    WHEN they navigate to the dashboard
    THEN they are denied access (HTTP 403)
    '''
    response = client.get("/dashboard")
    assert response.status_code == 401
    
def	test_student_logout(student_login):
    '''
    GIVEN that a student is logged in
    WHEN the student logs out
    THEN they are logged out successfully
    '''
    student_login.post("/logout")
    response = student_login.get("/calendar")
    assert response.status_code == 401

def	test_tutor_logout(tutor_login):
    '''
    GIVEN that a tutor is logged in
    WHEN the tutor logs out
    THEN they are logged out successfully
    '''
    tutor_login.post("/logout")
    response = tutor_login.get("/calendar")
    assert response.status_code == 401