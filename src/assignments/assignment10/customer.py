'''
Create a customer class
Add a constructor with parameters first, last, and phone_number
Create public attributes for first, last, and phone_number

STUDENT MUST ALSO MODIFY INVOICE CLASS TO USE THIS CLASS
SEE INVOICE file FOR INSTRUCTIONS
'''
class Customer:
    def __init__(self,first,last,phone_number):
        self.first = first
        self.last = last
        self.phone_number = phone_number
