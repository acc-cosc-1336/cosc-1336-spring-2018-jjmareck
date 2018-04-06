#ASSIGNMENT10 write import statement for customer class
from src.assignments.assignment10.customer import Customer

class Invoice:

    def __init__(self, customer, date):
        #ASSIGNMENT10: 
        #change bill_to parameter name to customer and modify code below to use customer class
        self.customer = customer
        self.date = date
        self.invoice_items = []
        self.invoice_total = 0



    def add_invoice_item(self, invoice_item):
        '''
        Write the code to append an invoice_item to the self.invoice_items list
        :param invoice_item:
        :return: doesn't return a value
        '''

        self.invoice_items.append(invoice_item)


    def get_invoice_total(self):
        '''
        Write code to iterate the self.invoice_items list and get the invoice self.invoice_total
        :return: the self.invoice_total
        '''
        self.invoice_total = 0
        #ASSIGNMENT10: modify invoice_item.cost to get cost from product attribute
        for invoice_item in self.invoice_items:
            self.invoice_total += invoice_item.quantity * invoice_item.product.cost

        return self.invoice_total

    def print_invoice(self):
        '''
        :return:
        '''

        #ASSIGNMENT10 WRITE CODE TO DISPLAY THE CUSTOMER NAME HERE
        print('')
        print('Hello ' + self.customer.first, self.customer.last)
        print('')

        total_cost = 0
        print('Description', 'Quantity', '     Cost', 'Extended Cost')

        for invoice_item in self.invoice_items:
            total_cost += invoice_item.get_extended_cost()
            #ASSIGNMENT10 MODIFY invoice_item.cost TO get the cost from the invoice item product attribute
            print(invoice_item.get_description(), format(invoice_item.quantity, '12d'), \
                  format(invoice_item.product.cost, '9,.2f'), format(invoice_item.get_extended_cost(), '13,.2f'))

        print('Total: ', ' ' *29,format(total_cost, '.2f'))
