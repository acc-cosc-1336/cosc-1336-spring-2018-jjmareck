import unittest

from tests.homework import test_homework8

suite = unittest.TestLoader().loadTestsFromModule(test_homework8)
unittest.TextTestRunner(verbosity=2).run(suite)
