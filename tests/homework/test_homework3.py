import unittest

from src.homework.homework3 import sum_odd_numbers
from src.homework.homework3 import list_of_even_numbers

class TestHomework3(unittest.TestCase):

    def test_sum_odd_numbers_w_value_11(self):
        self.assertEquals(36, sum_odd_numbers(11))

    def test_sum_odd_numbers_w_value_20(self):
        self.assertEquals(100, sum_odd_numbers(20))

    def test_sum_odd_numbers_w_value_100(self):
        self.assertEquals(2500, sum_odd_numbers(100))

    def test_list_even_numbers_w_value_10(self):
        self.assertEqual('2,4,6,8,10,', list_of_even_numbers(10))

    def test_list_even_numbers_w_value_20(self):
        self.assertEqual('2,4,6,8,10,12,14,16,18,20,', list_of_even_numbers(20))



