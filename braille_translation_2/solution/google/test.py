import unittest
from . import answer

class TestGoogleSolution(unittest.TestCase):
    def test_translate_simple(self):
        self.assertEqual(
            answer('code'),
            '100100101010100110100010'
        )

    def test_translate_uppercase(self):
        self.assertEqual(
            answer('Braille'),
            '000001110000111010100000010100111000111000100010'
        )

    def test_translate_lazy_dog(self):
        self.assertEqual(
            answer('The quick brown fox jumped over the lazy dog'),
            '000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100100010100110000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110'
        )

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGoogleSolution)
    unittest.TextTestRunner(verbosity=2).run(suite)
