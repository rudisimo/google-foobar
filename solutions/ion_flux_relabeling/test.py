import unittest
from . import solution

class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            solution.answer(3, [7, 3, 5, 1]),
            [-1, 7, 6, 3]
        )

    def test_case_2(self):
        self.assertEqual(
            solution.answer(5, [19, 14, 28]),
            [21, 15, 29]
        )
