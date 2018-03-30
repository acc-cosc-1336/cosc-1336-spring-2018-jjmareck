import unittest
from src.assignments.assignment9.invoice import Invoice
from src.assignments.assignment9.invoice_item import InvoiceItem

class Test_Assign8(unittest.TestCase):

    invoice_items = [] #list of Invoice Item instance objects

    def test_invoice_item_extended_cost_w_qty_10_cost_5(self):
        '''
        Create an Invoice item instance with argument values: 'Widget1', 10, and 5
        The extended cost result should be 50;

        '''
        invoice_item = InvoiceItem('Widget1', 10, 5)

        #create the assert code
        self.assertEqual(invoice_item.get_extended_cost(),50)

    def test_invoice__w_3_invoice_items(self):
        '''
        Create an Invoice instance with argument values: 'ABC company', '03282018'
        Three invoice items as follows argument values:
        'Widget1', 10, and  5
        'Widget2',  7, and  8
        'Widget3', 20, and 10
        Get Extended result  should be 50 + 56 + 200 = 306
        '''
        invoice = Invoice('ABC Company', '03282018')

        invoice.add_invoice_item(InvoiceItem('Widget1', 10, 5))
        invoice.add_invoice_item(InvoiceItem('Widget2', 7, 8))
        invoice.add_invoice_item(InvoiceItem('Widget3', 20, 10))

        #create the assert equal code
        self.assertEqual(306,invoice.get_invoice_total())

