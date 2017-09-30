import unittest
from . import solution

class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            solution.answer('2', '1'),
            '1'
        )

    def test_case_2(self):
        self.assertEqual(
            solution.answer('4', '7'),
            '4'
        )

    def test_case_3(self):
        self.assertEqual(
            solution.answer('2', '4'),
            'impossible'
        )

    def test_case_4(self):
        self.assertEqual(
            solution.answer('4', '31'),
            '10'
        )

    def test_case_5(self):
        self.assertEqual(
            solution.answer('9', '68'),
            '12'
        )

    def test_case_6(self):
        self.assertEqual(
            solution.answer('95', '302'),
            '14'
        )
