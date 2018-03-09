import unittest
from src.midterm.exam import get_miles_per_hour
from src.midterm.exam import get_bonus_pay_amount
from src.midterm.exam import reverse_string
from src.midterm.exam import get_list_min_max
from src.midterm.exam import get_list_min_max_file
#write import statements for exam functions

class Test_Midterm(unittest.TestCase):

    def test_get_miles_per_hour(self):
        self.assertEquals(19.883872,get_miles_per_hour(32,60))
        '''
        5 points
        Test with arguments kilometers 32 and minutes 60 return value should be 19.883872
        '''



    def test_get_bonus_pay_amount_w_good_value (self):
        self.assertEquals(70.0,get_bonus_pay_amount(1000))
        '''
        5 points
        Test with value 1000 return value should be 70
        '''



    def test_get_bonus_pay_amount_w_bad_value(self):
        self.assertEquals('Invalid arguments',get_bonus_pay_amount(-5))
        '''
        5 points
        Test with -5 return value should be 'Invalid arguments'
        '''



    def test_reverse_string(self):
        self.assertEquals('ataD gnirtS yM',reverse_string('My String Data'))
        '''
        5 points
        Test with value My String Data return value should be ataD gnirtS yM
        '''



    def test_get_list_min_max(self):
        self.assertEquals([10, 40],get_list_min_max(['joe', 10, 15, 20, 30, 40]))
        '''
        5 points
        Test with ['joe', 10, 15, 20, 30, 40]    Returns:    [10, 40]
        '''



    def test_get_list_min_max_file(self):
        self.assertEquals([2,89],get_list_min_max_file())
        '''
        5 points
        Test with quiz.data file the return value should be [2,89]
        '''

    
