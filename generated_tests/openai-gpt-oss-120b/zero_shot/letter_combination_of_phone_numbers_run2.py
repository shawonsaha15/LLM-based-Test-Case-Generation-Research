import unittest

class TestLetterCombinations(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(letter_combinations(""), [])

    def test_single_digit(self):
        expected = ["a", "b", "c"]
        result = letter_combinations("2")
        self.assertEqual(result, expected)

    def test_two_digits(self):
        expected = [
            "ad", "ae", "af",
            "bd", "be", "bf",
            "cd", "ce", "cf"
        ]
        result = letter_combinations("23")
        self.assertEqual(result, expected)

    def test_three_digits(self):
        # 2 -> abc, 7 -> pqrs, 9 -> wxyz
        expected = [
            a + b + c
            for a in "abc"
            for b in "pqrs"
            for c in "wxyz"
        ]
        result = letter_combinations("279")
        self.assertEqual(result, expected)

    def test_invalid_digit_ignored(self):
        # '*' is not in the mapping, so no combinations should be produced
        self.assertEqual(letter_combinations("2*3"), [])

    def test_mixed_valid_and_invalid_digits(self):
        # Only the leading valid digit should be processed, but since the next digit is invalid,
        # the recursion will not reach the end, resulting in no complete combinations.
        self.assertEqual(letter_combinations("2#"), [])

    def test_all_digits(self):
        # Verify that the total number of combinations equals the product of the
        # number of letters for each digit.
        digits = "2345"
        mapping_lengths = [3, 3, 3, 3]  # each of these digits maps to 3 letters
        expected_count = 1
        for l in mapping_lengths:
            expected_count *= l
        result = letter_combinations(digits)
        self.assertEqual(len(result), expected_count)
        # Ensure all results are strings of correct length
        for combo in result:
            self.assertIsInstance(combo, str)
            self.assertEqual(len(combo), len(digits))