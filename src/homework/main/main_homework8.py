from src.homework.homework8 import add_inventory

'''
Write a main function to create an empty dictionary and
a user-controlled loop to prompt for a widget name and quantity.
Add the values to the dictionary as key(widget name) and value(quantity) pairs.

After user decides to exit write data to file .

'''



def main():
    keep = 'y'
    widgets = {}
    while keep == 'y' or keep == 'Y':
        
        widget_name = input('Enter widget name: ')

        
        valid = False
        while not valid:
            try:
                quantity = int(input('Enter widget quantity: '))
                valid = True
            except:
                print('Enter an integer')
                valid = False

        add_inventory(widgets,widget_name,quantity)

        keep = input('Enter another widget? type y or Y to continue: ')

    #print(widgets)
main()
