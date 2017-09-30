import unittest
from . import solution

class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(solution.answer("2", "1"), "1")

    def test_case_2(self):
        self.assertEqual(solution.answer("4", "7"), "4")

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
