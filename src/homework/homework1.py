def get_hours_since_midnight(seconds):
    '''
    Type the code to calculate total hours given n(number) of seconds
    For example, given 3800 seconds the total hours is 1
    '''
    hours = seconds // 3600
    return hours

'''
IF YOU ARE OK WITH A GRADE OF 70 FOR THIS ASSIGNMENT STOP HERE.
'''

def get_minutes(seconds):
    '''
    Type the code to calculate total minutes less whole hour given n(number) of seconds
    For example, given 3800 seconds the total minutes is 3
    '''
    minutes = (seconds % 3600) // 60
    return minutes

def get_seconds(seconds):
    '''
    Type the code to calculate total minutes less whole hour given n(number) of seconds
    For example, given 3800 seconds the total minutes is 20
    '''
    seconds = (seconds % 3600) % 60
    return seconds
