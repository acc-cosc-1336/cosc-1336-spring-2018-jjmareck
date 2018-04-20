from src.assignments.assignment11.product import Product

class InvoiceItem:

    def __init__(self, product, quantity):
        '''
        Remove description and cost parameters. Replace with a product class
        '''

        self.product = product
        self.quantity = quantity

    def get_extended_cost(self):
        '''
        Write a statement to multiply quantity * cost and return the result
        :return:  extended cost
        '''

        return self.product.cost * self.quantity

    def get_description(self):
        return self.product.name
