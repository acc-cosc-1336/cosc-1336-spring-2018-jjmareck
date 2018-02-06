def get_time(hour, minutes, seconds, time_type, meridiem='AM'):
    '''
    Returns a time in 12 or 24 hour format

    :param hour: The hour of day-
                 when time_type 12 hr hour valid range 1 to 12 otherwise return 'Invalid hours(1-12)'
                 when time_type 24 hr hour valid range 0 to 23 otherwise return 'Invalid hours(range 0-23)'

    :param minutes: Minutes of an hour--minutes valid range 0 to 59 otherwise return 'Invalid minutes(range 0-59)'
    :param seconds:  seconds of an hour--seconds valid range 0 to 59 otherwise 'Invalid seconds(range 0-59)'
    :param time_type: Indicates the format of time to derive 12hr or 24hr
                      Valid time_type values 12 or 24 otherwise return 'Invalid time_type(12 or 24 only)'
                      If time_type is 24 ignore meridiem value;

                      If time_type is 12hr time use meridiem parameter value(AM or PM)

    :param meridiem:  AM, PM

    :return: time in 12 or 24 hour format
      Example for 12 hour format 09:09:09 PM
      Example for 24 hour format 21:09:09
    ADD YOUR CODE AFTER THE THREE QUOTES BELOW (dont forget to include a return statement at the end
    '''
    time = ''
    hour = int(hour)
    minutes = int(minutes)
    seconds = int(seconds)
    if minutes < 0 or minutes > 59:
        return "Invalid minutes(range 0-59)" #check minutes
    elif minutes >= 0 and minutes <= 9:
        minutes = '0' + str(minutes) #add a 0 to min

        
    if seconds < 0 or seconds > 59:
        return "Invalid seconds(range 0-59)" #check seconds
    elif seconds >= 0 and seconds <= 9:
        seconds = '0' + str(seconds) #add a 0 to sec

        
    if time_type==12:
        if hour < 1 or hour > 12:
            return "Invalid hours(range 1-12)" #check hour
        elif hour >= 0 and hour <= 9:
            hour = '0' + str(hour) #add a 0 to hour
            
        time = str(hour) + ':' + str(minutes) + ':' + str(seconds) + ' ' + meridiem
        
    elif time_type==24:
        if hour < 0 or hour > 23:
            return "Invalid hours(range 0-23)" #check hour
        elif hour >= 0 and hour <= 9:
            hour = '0' + str(hour) #add a 0 to hour
        
        time = str(hour) + ':' + str(minutes) + ':' + str(seconds)
        
    else:
        return "Invalid time_type(12 or 24 only)"
    return  time

def time_from_utc(utc_offset, utc_zero_time):
    '''
    Write code to calculate a time zone's time after applying utc_offset
    :param utc_offset:
    :param utc_zero_time:
    :return:
    DON NOT CHANGE ANYTHING IN THIS FUNCTION
    '''

    return (utc_zero_time + utc_offset) % 24
