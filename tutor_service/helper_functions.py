import calendar
from datetime import datetime, timedelta, date

def get_time_list(start, end):
    list_times = []
    #start time is 8:00am
    #end time is 21:00pm -> 9:00pm
    #step of 1
    for x in range(start, end, 1):
        start_time = ""
        end_time = ""
        start_end_time = []

        for count in range(2):
            if x <= 12:
                val = x
                if count == 0:
                    start_time = f"{val}:00AM"
                    end_time = f"{val}:25AM"

                else:
                    start_time = f"{val}:30AM"
                    end_time = f"{val}:55AM"

            else:
                val = x - 12
                if count == 0:
                    start_time = f"{val}:00PM"
                    end_time = f"{val}:25PM"

                else:
                    start_time = f"{val}:30PM"
                    end_time = f"{val}:55PM"

            start_end_time.clear()
            start_end_time.append(start_time)
            start_end_time.append(end_time)
            list_times.append(start_end_time[:])


    return list_times


def get_weekdays():
    # d = datetime.date.today()
    dates_list = []

    for x in range(7):
        d = date.today() + timedelta(days=x)
        d_format = d.strftime("%m/%d/%y")
        day_name = calendar.day_name[d.weekday()]
        day_string = f"{day_name}, {d_format}"
        dates_list.append(day_string)

    return dates_list    

