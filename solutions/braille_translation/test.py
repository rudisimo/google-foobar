import unittest
from . import solution

class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            solution.answer('code'),
            '100100101010100110100010'
        )

    def test_case_2(self):
        self.assertEqual(
            solution.answer('Braille'),
            '000001110000111010100000010100111000111000100010'
        )

    def test_case_3(self):
        self.assertEqual(
            solution.answer('The quick brown fox jumped over the lazy dog'),
            '000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100100010100110000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110'
        )
