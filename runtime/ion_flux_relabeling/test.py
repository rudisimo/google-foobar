import unittest
from . import solution

class TestChallengeSolution(unittest.TestCase):
    def test_missing(self):
        self.assertTrue(False)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestChallengeSolution)
    unittest.TextTestRunner(verbosity=2).run(suite)
