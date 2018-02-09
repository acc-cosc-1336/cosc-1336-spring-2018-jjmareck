def sample_function(value):
    '''
    This is just a sample function, you'll find a sample test_sample_function test case in test_assign4.py
    DO NOT CHANGE THE CODE
    :param value:
    :return: return the given value
    '''
    return value

def factorial(number):#value return function
    '''
    Given a number return its factorial using a for loop.
    A factorial of 5 is 1 * 2 * 3 * 4 * 5 = 120.
    :param number: A number greater than 0
    :return: the factorial of a number
    Using a for loop implement the following, the factorial function should
    work for any number.
    1 * 2 = 2
    2 * 3 = 6
    6 * 4 = 24
    24 * 5 = 120

    WRITE CODE AFTER THREE QUOTES BELOW
    '''
    total = 1
    for i in range(number): #loops calculates factorial
        total *= i+1

    return total #returns running total    
        
