'''
This file is for tests written using Selenium

class SetUpTest(BaseCase):
    def test_google(self):
        # open a page to confirm that selenium works
        self.open("https://google.com")
        self.assert_title("Google")


'''

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