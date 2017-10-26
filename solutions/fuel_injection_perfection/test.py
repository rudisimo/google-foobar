import unittest
from . import solution

class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            solution.answer("4"),
            2L
        )

    def test_case_2(self):
        self.assertEqual(
            solution.answer("15"),
            5L
        )

    def test_case_3(self):
        self.assertEqual(
            solution.answer("-1"),
            0L
        )

    def test_case_4(self):
        self.assertEqual(
            solution.answer("1024"),
            10L
        )