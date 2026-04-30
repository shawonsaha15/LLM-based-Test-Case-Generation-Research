import unittest

class TestLetterCombinations(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(letter_combinations(""), [])

    def test_single_digit(self):
        expected = ["a", "b", "c"]
        result = letter_combinations("2")
        self.assertCountEqual(result, expected)
        self.assertEqual(len(result), 3)

    def test_two_digits(self):
        expected = [
            "ad", "ae", "af",
            "bd", "be", "bf",
            "cd", "ce", "cf"
        ]
        result = letter_combinations("23")
        self.assertEqual(result, expected)

    def test_invalid_digit(self):
        # Digits like '1' and '0' have no mapping, should yield no combinations
        self.assertEqual(letter_combinations("1"), [])
        self.assertEqual(letter_combinations("0"), [])
        # Mixed valid and invalid digits result in no combinations because the
        # branch for the invalid digit produces no letters.
        self.assertEqual(letter_combinations("2 3".replace(" ", "")), [])

    def test_multiple_digits(self):
        # Verify length and a few sample combinations for a longer input
        digits = "234"
        result = letter_combinations(digits)
        # Expected number of combinations: 3 * 3 * 3 = 27
        self.assertEqual(len(result), 27)
        # Check that the first and last combinations follow the expected order
        self.assertEqual(result[0], "adg")
        self.assertEqual(result[-1], "cfi")
        # Ensure all results are strings of length equal to input length
        for combo in result:
            self.assertIsInstance(combo, str)
            self.assertEqual(len(combo), len(digits))