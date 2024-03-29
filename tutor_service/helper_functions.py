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
            if x < 12:
                val = x
                if count == 0:
                    start_time = f"{val}:00AM"
                    end_time = f"{val}:25AM"

                else:
                    start_time = f"{val}:30AM"
                    end_time = f"{val}:55AM"

            else:
                if x != 12:
                    val = x - 12
                else: 
                    val = 12
                        
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
    d = date.today()
    dates_list = []

    for x in range(7):
        day_and_date = []
        d = date.today() + timedelta(days=x)
        d_format = d.strftime("%m/%d/%y")
        day_name = calendar.day_name[d.weekday()]
        #day_string = f"{day_name}, {d_format}"
        day_and_date.append(day_name)
        day_and_date.append(d_format)
        dates_list.append(day_and_date)

    return dates_list

def get_weekday():
    day_and_date_list = []
    day_and_date = []
    d = date.today()
    d_format = d.strftime("%m/%d/%y")
    day_name = calendar.day_name[d.weekday()]
    day_and_date.append(day_name)
    day_and_date.append(d_format)
    day_and_date_list.append(day_and_date)
    return day_and_date_list

def get_columns(*args):
    col_list = []
    for x in args:
        col_list.append(x)
    
    return col_list    

def create_column_list(col_list, num_days):
    all_cols_list = []
    for x in range(num_days):
        for y in col_list:
            all_cols_list.append(y)

    return all_cols_list        
