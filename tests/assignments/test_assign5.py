import unittest
from src.assignments.assignment5 import recursive_decimal_binary

#write import for decimal to binary function


class Test_Assign5(unittest.TestCase):

    def test_rdb_w_basecase(self):
        self.assertEqual('00000000',recursive_decimal_binary(0))

    def test_rdb_w_65(self):
        self.assertEqual('01000001',recursive_decimal_binary(65))

    def test_rdb_w_128(self):
        self.assertEqual('10000000',recursive_decimal_binary(128))

    def test_rdb_w_255(self):
        self.assertEqual('11111111',recursive_decimal_binary(255))
    #write test cases with arguments 85 and 63 for recursive_decimal_binary function


#unittest.main(verbosity=2)
