import unittest

from tests.homework import test_homework3

suite = unittest.TestLoader().loadTestsFromModule(test_homework3)
unittest.TextTestRunner(verbosity=2).run(suite)
