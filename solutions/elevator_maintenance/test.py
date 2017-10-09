import unittest
from . import solution

class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            solution.answer(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]),
            ["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"]
        )

    def test_case_2(self):
        self.assertEqual(
            solution.answer(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]),
            ["0.1", "1.1.1", "1.2", "1.2.1", "1.11", "2", "2.0", "2.0.0"]
        )
