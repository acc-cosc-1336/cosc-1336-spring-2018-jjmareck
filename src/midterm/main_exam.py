#write import statement for reverse string function
from src.midterm.exam import reverse_string
'''
10 points
Write a main function to ....
Loop as long as user types y.
Prompt user for a string (assume user will always give you good data).
Pass the string to the reverse string function and display the reversed string

'''
def main():
    keep_going = 'y'

    while keep_going == 'y' or keep_going == 'Y':
        user_string = input('Please type a string... ')
        reverse = reverse_string(user_string)
        print(reverse)
        keep_going = input('Type y to go again: ')


main()
