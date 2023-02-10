import calendar, tutorPage
from datetime import datetime, timedelta, date

def get_time_list(start, end):
    list_times = []
    #start time is 8:00am
    #end time is 21:00pm -> 8:00pm
    for x in range(start, end, 1):
        start_time = ""
        end_time = ""
        start_end_time = []

        for count in range(2):
            if x <= 12:
                # for count in range(1,2):
                val = x
                start_time = f"{val}:00AM"
                end_time = f"{val}:25AM"

                if count == 1:
                    start_time = f"{val}:30AM"
                    end_time = f"{val}:55AM"

                # :00-:25
                # :30-:55
            else:
                val = x - 12
                start_time = f"{val}:00PM - {val}:25PM"
                end_time = f"{val}:30PM - {val}:55PM"

            start_end_time.append(start_time)
            start_end_time.append(end_time)
            list_times.append(start_end_time)

    print(list_times, "\n")
    return list_times


def get_weekdays():
    d = date.today()
    dates_list = []

    for x in range(7):
        d = date.today() + timedelta(days=x)
        d_format = d.strftime("%m/%d/%y")
        day_name = calendar.day_name[d.weekday()]
        day_string = f"{day_name}, {d_format}"
        dates_list.append(day_string)

    return dates_list    

