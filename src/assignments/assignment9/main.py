#Write import statements for classes invoice and invoice_item
from src.assignments.assignment9.invoice import Invoice
from src.assignments.assignment9.invoice_item import InvoiceItem

'''
LOOK AT THE TEST CASES FOR HINTS
Create an invoice object
In the loop:
Create a new InvoiceItem
Create a user controlled loop to continue until y is not typed, in loop...
    Prompt user for description, quantity, and cost.
    Add values to the InvoiceItem.
    Add the InvoiceItem to the invoice object.
    Once user types a letter other than y display the Invoice to screen
'''

invoice=Invoice('ACME Bricks','04202018')
keep = 'y'
while keep == 'y':
    description = input('Description: ')
    quantity = int(input('Quantity: '))
    cost = int(input('Cost: '))

    invoice.add_invoice_item(InvoiceItem(description,quantity,cost))
    keep = input('Keep going? y or n: ')

invoice.print_invoice()
