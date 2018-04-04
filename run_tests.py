import unittest

from tests.homework import test_homework9

suite = unittest.TestLoader().loadTestsFromModule(test_homework9)
unittest.TextTestRunner(verbosity=2).run(suite)
