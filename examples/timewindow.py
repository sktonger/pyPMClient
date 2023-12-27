import datetime

def getTimeWindow (time):
    dt = datetime.datetime.fromtimestamp(time)
    print(dt)
    hour = dt.hour;
    min = dt.minute
    # 9 hour 15 min is starting of 1 minute
    result = hour*60+min - 554
    return result


