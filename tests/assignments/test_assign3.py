import unittest

from src.assignments.assignment3 import decimal_to_binary
from src.assignments.assignment3 import sum_square_of_number
from src.assignments.assignment3 import is_prime
from src.assignments.assignment3 import list_of_primes

class Test_Assign3(unittest.TestCase):

    def test_decimal_to_binary_w_value_0(self):
        self.assertEqual("00000000", decimal_to_binary(0))

    def test_decimal_to_binary_w_value_65(self):
        self.assertEqual("01000001", decimal_to_binary(65))

    def test_decimal_to_binary_w_value_157(self):
        self.assertEqual("10011101", decimal_to_binary(157))

    def test_decimal_to_binary_w_value_255(self):
        self.assertEqual("11111111", decimal_to_binary(255))

    def test_sum_of_square_w_value_3(self):
        self.assertEqual(14, sum_square_of_number(3))

    def test_sum_of_square_w_value_5(self):
        self.assertEqual(55, sum_square_of_number(5))

    def test_sum_of_square_w_value_10(self):
        self.assertEqual(385, sum_square_of_number(10))

    def test_is_prime_w_1(self):
        self.assertEqual(False, is_prime(1))

    def test_is_prime_w_2(self):
        self.assertEqual(True, is_prime(2))

    def test_is_prime_w_43(self):
        self.assertEqual(True, is_prime(43))

    def test_is_prime_w_91(self):
        self.assertEqual(False, is_prime(91))

    def test_is_prime_w_197(self):
        self.assertEqual(True, is_prime(197))

    def test_list_of_primes_w_10(self):
        self.assertEqual('2,3,5,7,', list_of_primes(10))

    def test_list_of_primes_w_20(self):
        self.assertEqual('2,3,5,7,11,13,17,19,', list_of_primes(20))

    def test_list_of_primes_w_50(self):
        self.assertEqual('2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,', list_of_primes(50))
