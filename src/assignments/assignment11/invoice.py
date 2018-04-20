from src.assignments.assignment11.customer import Customer

class Invoice:

    def __init__(self, customer, date):
        #change bill_to parameter name to customer and modify code below to use customer class that
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

        for invoice_item in self.invoice_items:
            self.invoice_total += invoice_item.quantity * invoice_item.product.cost

        #ASSIGNMENT 11: add a statement that sets attribute invoice_total the invoice total less customer discount,
        #(multiply invoice total * customer discount)
        self.invoice_total -= self.invoice_total * self.customer.discount

        return self.invoice_total

    def print_invoice(self):
        '''
        :return:
        '''

        print("Name: ", self.customer.last_name, self.customer.first_name)

        total_cost = 0
        total_discount = 0
        print('Description', 'Quantity', '     Cost', 'Extended Cost')

        for invoice_item in self.invoice_items:
            total_cost += invoice_item.get_extended_cost()
            print(invoice_item.get_description(), format(invoice_item.quantity, '12d'), \
                  format(invoice_item.product.cost, '9,.2f'), format(invoice_item.get_extended_cost(), '13,.2f'))

        #ASSIGNMENT 11: add a statement that displays Discount and the product of total cost times customer discount

        #ASSIGNMENT 11: modify the statement below to display total cost less total cost times customer discount

        total_discount = total_cost * self.customer.discount
        print("Discount:" + " "*29 +"%" + format(self.customer.discount * 100,'.2f'))
        print('Total: ', ' ' *29,format(total_cost-total_discount, '.2f'))
        print()
