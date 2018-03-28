import unittest
#write the import for function for assignment8 add_inventory
from src.homework.homework8 import add_inventory, remove_inventory_widget


class Test_Assign8(unittest.TestCase):


    widgets = {'Widget0': 20 }

    def test_sample(self):
        self.assertEqual(1,1)

    #sample test using a class member variable
    def test_add_widget1_inventory_of_10(self):
        add_inventory(self.widgets, 'Widget1', 10) #use self.widgets in your other test cases to as shown here
        self.assertEqual(10, self.widgets['Widget1'])#use self.widgets in your other test cases to as shown here

    #create another test to add Widget1 and a value of 25 result should be 35
    def test_add_widget1_inventory_of_25(self):
        add_inventory(self.widgets, 'Widget1', 25)
        self.assertEqual(35, self.widgets['Widget1'])

    #create a test to add Widget2 with a value of 15
    def test_add_widget2_inventory_of_15(self):
        add_inventory(self.widgets, 'Widget2', 15)
        self.assertEqual(15, self.widgets['Widget2'])

    #create a test to reduce Widget2 inventory by 5 result should be 10
    def test_add_widget2_inventory_reduce_5(self):
        add_inventory(self.widgets, 'Widget2', -5)
        self.assertEqual(10, self.widgets['Widget2'])

    #create a test to remove Widget0, get the length of self.widgets, the length should be 2
    #in same test, check that return value is 'Record deleted'
    def test_add_wwidget0_remove_record(self):
        self.assertEqual(remove_inventory_widget(self.widgets,'Widget0'),'Record deleted')
        lenwidgets=len(self.widgets)
        self.assertEqual(lenwidgets,2)


