from src.assignments.assignment10.product import Product

class InvoiceItem:

    def __init__(self, product, quantity):
        '''
        ASSIGNMENT10: 
        Remove description and cost parameters. Replace with a product class
        '''

        #ASSIGNMENT10: update code to use product class
        self.quantity = quantity
        self.product = product


    def get_extended_cost(self):
        '''
        Write a statement to multiply quantity * cost and return the result
        :return:  extended cost
        '''
        #ASSIGNMENT10: MODIFY CODE TO GET THE COST FROM THE PRODUCT ATTRIBUTE
        return self.product.cost * self.quantity

    def get_description(self):
        #ASSIGNMENT10: MODIFY CODE TO GET THE NAME FROM THE PRODUCT ATTRIBUTE
        return self.product.name
