#write the import for function for assignment7 sum_list_values
from src.assignments.assignment7 import sum_list_values

'''
Create a function named process_list that calls the sum_list_values function.
Prints the list values and the sum of the element in the list as follows:
joe 10 15 20 30 40 sum: 115

Create a main function.
In the function loop as long as user wants to add another list.
Prompt the user for name and append to the list.
Prompt the user for number of numeric values in the list.
Iterate the number of times the user enters and prompt end-user for n numeric values.
Process the list youve created


Call the main function
--------------------
joe 10 15 20 30 40
bill 23 16 19 22
sue 8 22 17 14 32 17 24 21 2 9 11 17
grace 12 28 21 45 26 10
john 14 32 25 16 89

'''
def process_list(stuff):
    for item in stuff:
        print(item, end=' ')

    sum_of_vals = sum_list_values(stuff)
    print('sum:', sum_of_vals)

def main():
    keep_going = 'y'
    user_list = []
    while keep_going == 'y' or keep_going == 'Y':
        name = input('Type a name: ')
        user_list.append(name)
        num_of_vals = int(input('Enter number of values you wish to enter: '))
        for i in range(num_of_vals):
            value = int(input('Enter value #' + str(i+1) + ': '))
            user_list.append(value)
        process_list(user_list)
        keep_going = input('Type y to continue... ')
main()
