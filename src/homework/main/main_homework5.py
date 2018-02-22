#write the import statements for homework5 functions
from src.homework.homework5 import write_sales_data
from src.homework.homework5 import read_sales_data


#With the functions created in homework5...
#Prompt user for number of sales records to input.
num_records = int(input('How many sales records will you enter?: '))

#Open a file for text writing. (make file object)
records = open('records.txt', 'w')

#start loop
#--->Iterate and prompt user for item name and price.
#function write sales data takes file object, name, price
#--->Save item name and price to file in one line
total_price = 0
for index in range(num_records):
    name = input('Item name: ')
    price = float(input('Item price: '))
    total_price += price
    write_sales_data(records, name, price)

#Calculate sum of price and write to file
#Calculate average price and write to file
average_price = format(total_price/num_records, '.2f')
records.write('Total   ' + total_price)
records.write('Total   ' + average_price)

records.close()


#Open a file for text reading.

records = open('records.txt', 'r')
read_sales_data(records)
#Read the saved file and output table

