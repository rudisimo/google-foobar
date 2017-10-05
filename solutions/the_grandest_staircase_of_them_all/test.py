import unittest
from . import solution

class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            solution.answer(1),
            0
        )

    def test_case_2(self):
        self.assertEqual(
            solution.answer(3),
            1
        )

    def test_case_3(self):
        self.assertEqual(
            solution.answer(4),
            1
        )

    def test_case_4(self):
        self.assertEqual(
            solution.answer(5),
            2
        )

    def test_case_5(self):
        self.assertEqual(
            solution.answer(200),
            487067745
        )
