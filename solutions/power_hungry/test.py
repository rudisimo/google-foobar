import unittest
from . import solution

class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            solution.answer(
                [2, 0, 2, 2, 0]
            ), "8"
        )

    def test_case_2(self):
        self.assertEqual(
            solution.answer(
                [-2, -3, 4, -5],
            ), "60"
        )

    def test_case_3(self):
        self.assertEqual(
            solution.answer(
                [0],
            ), "0"
        )

    def test_case_4(self):
        self.assertEqual(
            solution.answer(
                [1],
            ), "1"
        )

    def test_case_5(self):
        self.assertEqual(
            solution.answer(
                [0, 2, 2, -4, -2, -2],
            ), "32"
        )

    def test_case_6(self):
        self.assertEqual(
            solution.answer(
                [1, 1, 1, 1, 1, 1],
            ), "1"
        )

    def test_case_7(self):
        self.assertEqual(
            solution.answer(
                [-1, -1, -1, -1, -1, -1, -1],
            ), "1"
        )

    def test_case_8(self):
        self.assertEqual(
            solution.answer(
                [0, -1],
            ), "0"
        )
