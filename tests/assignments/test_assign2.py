import unittest
from src.assignments.assignment2 import faculty_evaluation_result

class Test_Assignment2(unittest.TestCase):

    def test_excellent_rating(self):
        self.assertEqual("Excellent", faculty_evaluation_result(0, 0, 1, 2, 4, 190))

    def test_very_good_rating(self):
        self.assertEqual("Very Good", faculty_evaluation_result(0, 0, 7, 10, 37, 65))

    def test_good_rating(self):
        self.assertEqual("Good", faculty_evaluation_result(4, 18, 52, 95, 81, 97))

    def test_needs_improvement_rating(self):
        self.assertEqual("Needs Improvement", faculty_evaluation_result(0, 50, 7, 10, 17, 35))

    def test_unacceptable_rating(self):
        self.assertEqual("Unacceptable", faculty_evaluation_result(176, 148, 0, 5, 11, 7))

if __name__ == '__main__':
    unittest.main(verbosity=2)
