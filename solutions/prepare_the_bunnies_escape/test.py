import unittest
from . import solution

class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            solution.answer([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]),
            7
        )

    def test_case_2(self):
        self.assertEqual(
            solution.answer([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]),
            11
        )
