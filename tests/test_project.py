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

def test_valid_signup(client_db):
    '''
    GIVEN that app is running with context
    WHEN a user signs up
    THEN a confirmation email should be sent
    '''
    '''
    Navigate to sign up page
    create a new account.
    Check that the confirmation email is sent (POST 200)
    '''
    pass

def test_login_new_user():
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

def	test_join_success(student_login):
    '''
    GIVEN a session is scheduled but not full
    WHEN a user joins that session
    THEN the database is updated
    '''
    '''
    Select the existing session on the user dashboard
    navigate to join session page
    join session
    Database should be updated.
    '''
    pass

def	test_join_success_message(student_login):
    '''
    GIVEN a student is logged in
    WHEN a user schedules a new session
    THEN a confirmation message is displayed
    '''
    '''
    Navigate to user dashboard
    schedule a new session. 
    test that a confirmation message should be displayed (response data)
    '''
    pass

def	test_join_success_email(student_login):
    '''
    GIVEN a student is logged in
    WHEN a user schedules a new session
    THEN a confirmation message is displayed
    '''
    '''
    Navigate to user dashboard
    schedule a new session. 
    test that a confirmation email should be sent (POST 200)
    '''
    pass

def	test_book_fail(student_login, app):
    '''
    GIVEN that a student has scheduled the maximum number of sessions
    WHEN that student tries to schedule a new session
    THEN the student cannot schedule a new session and an error message is returned
    '''
    
    '''
    App must be created with context.
    Add two sessions to DB
    Schedule one more session. 
    Third session should fail and error message should be displayed.
    '''
    pass

def	test_join_fail(student_login):
    '''
    GIVEN thas a session is scheduled and full
    WHEN a student tries to join session
    THEN then error message is displayed
    '''
    '''
    Navigate to join session page for full session
    attempt to join. 
    Should fail with error message
    '''
    pass

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

def	test_refresh_selection(tutor_login):
    '''
    GIVEN
    WHEN
    THEN
    '''
    '''
    On the schedule page, create a schedule.
    Hit the reresh button.
    Scheduel should be cleared.
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
    '''
    Navigate to session info page.
    Response data should show expected results
    '''
    pass

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

# 14. Test UI
def	test_UI_unavailable_is_gray(student_login):
    '''
    GIVEN that a session is not available
    WHEN a student views the dashboard
    THEN that session is colored gray
    '''
    '''
    App must be created with context including tutor schedules
    Check that unavailable time slots are gray.
    '''
    pass

def	test_UI_available_is_white(student_login):
    '''
    GIVEN that a session is not scheduled but is available
    WHEN a student views the dashboard
    THEN that session is colored white
    '''
    '''
    App must be created with context including tutor schedules
    Check that available time slots are white.
    '''
    pass

def	test_UI_scheduled_is_orange_student(tutor_login):
    '''
    GIVEN that s session is scheduled
    WHEN a tutor views the dashboard
    THEN that session is colored orange
    '''
    '''
    App must be created with context including tutor schedules and a booked session
    Check that booked time slots are orange.
    '''
    pass

def	test_UI_available_is_orange(student_login):
    '''
    GIVEN that a session is scheduled, but is not full
    WHEN a student views the dashboard
    THEN that session is colored orange
    '''
    '''
    App must be created with context including tutor schedules and a booked session that allows multiple students
    Check that time slots already booked (but not full) are orange.
    '''
    pass

def	test_view_available_tutors(student_login):
    '''
    GIVEN that the app is running with context
    WHEN a student views the calendar page
    THEN a list of tutors is displayed
    '''
    '''
    Navigate to dashboard
    and query response data for expected drop down list.
    '''
    pass

def	test_calendar_dynamic(student_login):
    '''
    GIVEN that a tutor is selected on the calendar page
    WHEN a student selects a different tutor
    THEN the calendar changes accordingly
    '''
    '''
    Calendar changes in response to tutor being selected.
    Navigate to dashboard
    query response data for expected drop down list.
    Select a different tutor
    see if the calendar changed.
    '''
    pass