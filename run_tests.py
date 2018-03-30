import unittest

from tests.assignments import test_assign9

suite = unittest.TestLoader().loadTestsFromModule(test_assign9)
unittest.TextTestRunner(verbosity=2).run(suite)
