import unittest

class TestLetterCombinations(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(letter_combinations(""), [])

    def test_single_digit(self):
        expected = ["a", "b", "c"]
        self.assertEqual(letter_combinations("2"), expected)

    def test_two_digits(self):
        expected = [
            "ad", "ae", "af",
            "bd", "be", "bf",
            "cd", "ce", "cf"
        ]
        self.assertEqual(letter_combinations("23"), expected)

    def test_invalid_digits(self):
        # Digits 0 and 1 have no mapping; the function should return an empty list
        self.assertEqual(letter_combinations("1"), [])
        self.assertEqual(letter_combinations("0"), [])
        self.assertEqual(letter_combinations("10"), [])

    def test_three_digits_length(self):
        # Verify that the number of combinations matches 3 * 3 * 3 = 27 for "222"
        result = letter_combinations("222")
        self.assertEqual(len(result), 27)
        # Spot‑check a few expected combinations
        self.assertIn("aaa", result)
        self.assertIn("aab", result)
        self.assertIn("ccc", result)

    def test_seven_digit_combinations_count(self):
        # '7' maps to 4 letters; 4^3 = 64 combinations for "777"
        result = letter_combinations("777")
        self.assertEqual(len(result), 64)
        # Ensure first and last combinations follow the expected order
        self.assertEqual(result[0], "ppp")
        self.assertEqual(result[-1], "sss")