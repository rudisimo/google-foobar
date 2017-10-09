import unittest
from . import solution

class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            solution.answer(
                [13, 5, 6, 2, 5],
                [5, 2, 5, 13],
            ), 6
        )

    def test_case_2(self):
        self.assertEqual(
            solution.answer(
                [14, 27, 1, 4, 2, 50, 3, 1],
                [2, 4, -4, 3, 1, 1, 14, 27, 50],
            ), -4
        )
