def sum_odd_numbers(num):
    '''
    WITH A FOR LOOP
    Given a number calculate and return the sum of odd numbers from 1 to num.
    Example: if num is 11 the sum total is 1+3+5+7+9+11 = 36
    :param num: Number greater than 0
    :return: the sum of all the odd numbers from 1 to num
    '''
    total = 0
    #write your code starting here; use total as the sum total
    for i in range(1,num+1,2):
        total += i

    return total

def list_of_even_numbers(num):
    '''
    WITH  WHILE LOOP
    Given a number return a list of all the even numbers from 1 to num
    Example: if num is 12 return the list 2,4,6,8,10,12,
    :param num:
    :return: A list of all even numbers up to a num
    '''
    even_numbers = ''
    #write your code starting here; you'll need to concatenate evens to even_numbers
    i = 2
    while i <= num:
        even_numbers += str(i) + ','
        i += 2
        

    return even_numbers

def main1():
    '''
    You will make calls to sum_odd_numbers and list_of_even_numbers functions above.
    Example:
    Call list sum_odd_numbers and save its return value to a result variable
    result = sum_odd_numbers(10)
    print(result)

    For your assignment:

    Prompt user for a number from keyboard
    This is the number of times the program will loop and ...
    In the loop call the sum_odd_numbers(index) with the current value of the loop index and save return value
    print the value
    In the loop call the list_even_numbers(index) with the current value of the loop index and save return value
    print the value

    WHAT IS LOOP INDEX?
    for i in range(1,5): #i is loop index
       #other code

    while i < 10: #i is loop index
       #other code

    TO RUN YOUR PROGRAM IN IDLE SELECT RUN->RUN MODULE OR THE F5 KEY
    IN THE PYTHON SHELL TYPE main1() to run the code in this function

    DON'T ADD A RETURN STATEMENT TO THIS FUNCTION
    '''
    #write your code here
    loops = int(input("This is the number of times the program will loop... "))
    for i in range(loops):
        odds = sum_odd_numbers(i)
        print(odds)
        evens = list_of_even_numbers(i)
        print(evens)
