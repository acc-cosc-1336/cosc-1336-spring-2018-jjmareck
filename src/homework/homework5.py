#Create a function named write_sales_data with file_object, item and price as parameters.
#The function should write item and price to a file.
def write_sales_data(file, item, price):
    file.write(item + '   ' + price +'\n')

#Create another function named read_sales_data with file_object as a parameter.
#The function will read the file line by line and display to screen to produce the table described in homework 5.

def read_sales_data(file_object):

    for line in file_object:
        print(line.rstrip('\n'))
