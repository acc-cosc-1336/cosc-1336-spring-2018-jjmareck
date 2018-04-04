import unittest
from src.homework.homework9.die import Die

#Write the import statement for the Die class

class TestHomework9(unittest.TestCase):

    def test_rolls_values_1_to_6(self):
        '''
        Write a test case to ensure that the Die class only rolls values from 1 to 6

        '''
        die = Die()
        roll = die.roll()
        self.assertTrue(roll == 1 or roll == 2 or roll ==3 or roll == 4 or roll == 5 or roll ==6)
        
