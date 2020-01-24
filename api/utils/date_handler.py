import datetime

def get_interval(day):
    distance_to_friday = day.isoweekday() - 5
    if distance_to_friday > 0:
        start = day - datetime.timedelta(days=(distance_to_friday + 7)) # start of interval
        end = day - datetime.timedelta(days=distance_to_friday) # end of interval
    else:
        start = day - datetime.timedelta(days=(distance_to_friday + 7 + 7)) # start of interval
        end = day - datetime.timedelta(days=(distance_to_friday + 7)) # end of interval
    start = date_to_str(start)
    end = date_to_str(end)
    return f'{start}--{end}'

def date_to_str(date):
    return f'{date.year}-{date.month:02d}-{date.day:02d}'

def get_3weeks():
    last_3weeks = []
    day = datetime.date.today()
    for _ in range(3):
        last_3weeks.append(get_interval(day))
        day = day - datetime.timedelta(days=7)
    return last_3weeks