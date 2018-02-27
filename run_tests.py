import unittest

from tests.homework import test_homework4

suite = unittest.TestLoader().loadTestsFromModule(test_homework4)
unittest.TextTestRunner(verbosity=2).run(suite)
