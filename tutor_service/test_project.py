# This file is for the actual test definitions

from flask import url_for

# 0. Test that Pytest is set up correctly
def test_null():
    '''
    GIVEN a running environment
    WHEN tests are run
    THEN check that no errors occur
    '''
    pass

# 1. Test that Flask is set up correctly
def test_setup(client):
    '''
    GIVEN a null state
    WHEN a new connection is created
    THEN check that flask is set up correctly
    '''
    response = client.get("/home")
    assert response.status_code == 200

# 2. Test Calendar loads

def test_calendar_loads(client):
    '''
    GIVEN that the app is set up correctly
    WHEN the user goes to the calendar page
    THEN check that the calendar is displayed
    '''
    response = client.get("/calendar")
    assert b"Tutor Calendar" in response.data

def test_calendar_loads_2(client):
    '''
    GIVEN that the app is set up correctly
    WHEN the user goes to the calendar page
    THEN check that the calendar is displayed
    '''
    response = client.get("/calendar")
    assert b"Tuesday" in response.data


#-------------------------------------------------------
#@pytest.fixture(scope='function')
def test_take_screenshot():
    pass