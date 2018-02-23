import unittest

from tests.assignments import test_assign6

suite = unittest.TestLoader().loadTestsFromModule(test_assign6)
unittest.TextTestRunner(verbosity=2).run(suite)
