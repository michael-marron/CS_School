from flask import render_template, redirect, url_for, flash, request
from tutor_service.helper_functions import get_time_list, get_weekdays, get_columns, create_column_list, get_weekday
from tutor_service.forms import ConfirmSessionForm

tutor_selected_from_dropdown = "all"

times_dictionary = {
    "8:00AM": 0,
    "8:30AM": 0,
    "9:00AM": 0,
    "9:30AM": 0,
    "10:00AM": 0,
    "10:30AM": 0,
    "11:00AM": 0,
    "11:30AM": 0,
    "12:00PM": 0,
    "12:30PM": 0,
    "1:00PM": 0,
    "1:30PM": 0,
    "2:00PM": 0,
    "2:30PM": 0,
    "3:00PM": 0,
    "3:30PM": 0,
    "4:00PM": 0,
    "4:30PM": 0,
    "5:00PM": 0,
    "5:30PM": 0,
    "6:00PM": 0,
    "6:30PM": 0,
    "7:00PM": 0,
    "7:30PM": 0,
    "8:00PM": 0,
    "8:30PM": 0
}

sessions = [
    {
        "id": "0", 
        "times_available": "10:00AM",
        "tutor": "Sarah",
        "tutor_service": "Machine Learning",
        "zoom_link": "sarah@zoom.com",
        "spaces_available": 3
    },
    {
        "id": "1", 
        "times_available": "3:00PM",
        "tutor": "John",
        "tutor_service": "Data Science",
        "zoom_link": "john@zoom.com",
        "spaces_available": 2
    },
    {
        "id": "2", 
        "times_available": "3:30PM",
        "tutor": "John",
        "tutor_service": "Data Science",
        "zoom_link": "john@zoom.com",
        "spaces_available": 2
    },
    {
        "id": "3", 
        "times_available": "9:00AM",
        "tutor": "Paul",
        "tutor_service": "Web Development",
        "zoom_link": "paul@zoom.com",
        "spaces_available": 1
    },
    {
        "id": "4", 
        "times_available": "12:00PM",
        "tutor": "Paul",
        "tutor_service": "Web Development",
        "zoom_link": "paul@zoom.com",
        "spaces_available": 1
    }
]

extra =  {
        "id": "5", 
        "times_available": "12:00PM",
        "tutor": "Sarah",
        "tutor_service": "Blockchain",
        "zoom_link": "sarah@zoom.com",
        "spaces_available": 1
    }

def home_page():
    return render_template('home.html')

def calendar_page():
    mock_data = []

    john_data = {
        "Times Available": {
            "Monday": ["10:00AM", "12:00PM"],
            "Tuesday": ["3:30PM"],
            "Friday": ["8:00PM"]
            }, 
        "Tutor" : "John",
        "Tutor Service": "Data Structures",
        "Zoom Link": "john@zoom.com",
        "Spaces Available": 1
    }

    jane_data = {
        "Times Available": {
            "Monday": ["3:00PM", "5:00PM"],
            "Wednesday": ["2:30PM"],
            "Saturday": ["6:00PM", "7:00PM"]
            }, 
        "Tutor" : "Jane",
        "Tutor Service": "Machine Learning",
        "Zoom Link": "jane@zoom.com",
        "Spaces Available": 3
    }

    simon_data = {
        "Times Available": {
            "Wednesday": ["3:00PM", "5:00PM"],
            "Thursday": ["10:00AM", ],
            "Sunday": ["8:00AM", "6:00PM", "7:00PM"]
            }, 
        "Tutor" : "Simon",
        "Tutor Service": "Front End Development",
        "Zoom Link": "Simon@zoom.com",
        "Spaces Available": 1
    }

    mock_data.append(john_data)
    mock_data.append(jane_data)
    mock_data.append(simon_data)

    times = get_time_list(start=8, end=21)
    weekdays_and_dates = get_weekdays()
    calendar_attributes = ["Tutor", "Tutor Service", "Zoom Link", "Spaces Available", "Confirm"]
    num_attributes = len(calendar_attributes)
    weekday = get_weekday()
    confirm_form = ConfirmSessionForm()
    tutor_set = set()
    
    global tutor_selected_from_dropdown
    global times_dictionary

    for session in sessions: 
        time_aval = session["times_available"]
        times_dictionary[time_aval]+=1

    for session in sessions:
        tutor_set.add(session["tutor"])

    if request.method == "POST":
        session_id_from_form = request.form.get('session_confirmed')
        for data in sessions:
            if data["id"] == session_id_from_form:
                if data["spaces_available"] > 0:
                    data["spaces_available"] = data["spaces_available"] - 1
                    flash("Congratulations! You have confirmed your tutoring session", category="success")

        if 'tutors_dropdown' in request.form:
            tutor_selected_from_dropdown = request.form.get('tutors_dropdown')            
    
    #These three html pages represent different calendar page iterations
    #The html pages have a more in depth description of which each calendar page is attempting to accomplish in a comment on the html page itself 
    #calendar_seven_days.html
    #calendar_one_day_no_multiple_sessions.html
    #calendar_one_day_multiple_sessions_attempt.html
    return render_template('calendar_one_day_no_multiple_sessions.html', 
    times=times, 
    weekdays_and_dates=weekdays_and_dates, 
    calendar_attributes=calendar_attributes, 
    num_attributes=num_attributes, 
    mock_data=mock_data, 
    weekday=weekday, 
    confirm_form=confirm_form, 
    sessions=sessions,
    tutor_set=tutor_set,
    tutor_selected_from_dropdown=tutor_selected_from_dropdown,
    times_dictionary=times_dictionary)

def test_page():
    return render_template('home.html')    

