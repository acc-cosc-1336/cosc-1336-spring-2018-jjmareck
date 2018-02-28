import unittest

from tests.homework import test_homework6

suite = unittest.TestLoader().loadTestsFromModule(test_homework6)
unittest.TextTestRunner(verbosity=2).run(suite)
