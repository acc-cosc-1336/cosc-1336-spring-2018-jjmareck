'''
Create a product class.
Add a constructor with parameters product_id, name, and cost
Create public attributes for product_id, name, and cost

STUDENT MUST ALSO MODIFY INVOICE item CLASS TO USE THIS CLASS
SEE INVOICE item file FOR INSTRUCTIONS
'''

class Product:

    def __init__(self, product_id, name, cost):

        self.product_id = product_id
        self.cost = cost
        self.name  = name
