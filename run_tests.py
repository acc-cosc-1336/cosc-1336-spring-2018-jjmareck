import unittest

from tests.homework import test_homework2

suite = unittest.TestLoader().loadTestsFromModule(test_homework2)
unittest.TextTestRunner(verbosity=2).run(suite)
