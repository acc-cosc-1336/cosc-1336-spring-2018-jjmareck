import unittest

from src.homework.homework2 import get_time
from src.homework.homework2 import time_from_utc

class TestHomework2(unittest.TestCase):

    def test_get_time_when_time_type_when_value_0(self):
        self.assertEqual('Invalid time_type(12 or 24 only)', get_time(9,30,45,-5))

    def test_get_time_when_time_type_when_value_25(self):
        self.assertEqual('Invalid time_type(12 or 24 only)', get_time(9,30,45, 25))

    def test_get_time_when_time_type_24_hours_gt_23(self):
        self.assertEqual('Invalid hours(range 0-23)', get_time(24,11,45, 24))

    def test_get_time_when_time_type_12_hours_gt_12(self):
        self.assertEqual('Invalid hours(range 1-12)', get_time(13,11,45, 12))

    def test_get_time_when_time_type_12_hours_lt_0(self):
        self.assertEqual('Invalid hours(range 1-12)', get_time(-5,11,45, 12))

    def test_get_time_when_minutes_lt_0(self):
        self.assertEqual('Invalid minutes(range 0-59)', get_time(9,-1,45, 12))

    def test_get_time_when_minutes_gt_59(self):
        self.assertEqual('Invalid minutes(range 0-59)', get_time(9,60,45, 12))

    def test_get_time_when_seconds_lt_0(self):
        self.assertEqual('Invalid seconds(range 0-59)', get_time(9,10,-1, 12))

    def test_get_time_when_seconds_gt_59(self):
        self.assertEqual('Invalid seconds(range 0-59)', get_time(9,50,60, 12))

    def test_get_time_when_time_type_24_w_valid_time_21_9_9_24(self):
        self.assertEqual('21:09:09', get_time(21, 9, 9, 24))

    def test_get_time_when_time_type_12_w_valid_time_9_9_9_12_PM(self):
        self.assertEqual('09:09:09 PM', get_time(9, 9, 9, 12, 'PM'))

    def test_get_time_when_time_type_24_w_valid_time_21_29_19_24(self):
        self.assertEqual('21:29:19', get_time(21, 29, 19, 24))

    def test_get_time_when_time_type_12_w_valid_time_9_29_19_12_PM(self):
        self.assertEqual('09:29:19 PM', get_time(9, 29, 19, 12, 'PM'))

    def test_get_time_when_time_type_12_w_valid_time_9_29_19_12_AM(self):
        self.assertEqual('09:29:19 AM', get_time(9, 29, 19, 12, 'AM'))

    def test_get_time_when_time_type_12_w_valid_time_9_9_9_12_AM_no_argument(self):
        self.assertEqual('09:29:19 AM', get_time(9, 29, 19, 12))

    def test_utc_time_to_eastern_standard_time(self):
        self.assertEqual(15, time_from_utc(-5, 20))

    def test_utc_time_to_central_standard_time(self):
        self.assertEqual(14, time_from_utc(-6, 20))

    def test_utc_time_to_mountain_standard_time(self):
        self.assertEqual(13, time_from_utc(-7, 20))

    def test_utc_time_to_pacific_standard_time(self):
        self.assertEqual(12, time_from_utc(-8, 20))

