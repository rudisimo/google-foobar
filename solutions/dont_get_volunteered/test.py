import unittest
from . import solution

class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            solution.answer(19, 36),
            1
        )

    def test_case_2(self):
        self.assertEqual(
            solution.answer(0, 1),
            3
        )

    def test_case_3(self):
        self.assertEqual(
            solution.answer(0, 0),
            0
        )
