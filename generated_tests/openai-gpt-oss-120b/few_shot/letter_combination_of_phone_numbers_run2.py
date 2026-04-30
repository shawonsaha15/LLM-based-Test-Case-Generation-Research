import unittest

class TestLetterCombinations(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(letter_combinations(""), [])

    def test_single_digit(self):
        self.assertListEqual(
            sorted(letter_combinations("2")),
            sorted(["a", "b", "c"])
        )

    def test_two_digits(self):
        expected = [
            "ad", "ae", "af",
            "bd", "be", "bf",
            "cd", "ce", "cf"
        ]
        self.assertListEqual(letter_combinations("23"), expected)

    def test_digit_with_no_mapping(self):
        # Digits '0' and '1' are not in the mapping; the function should return an empty list
        self.assertEqual(letter_combinations("10"), [])
        self.assertEqual(letter_combinations("203"), [])

    def test_multiple_digits_combination_count(self):
        # '7' maps to 4 letters, '9' maps to 4 letters => 4 * 4 = 16 combinations
        combos = letter_combinations("79")
        self.assertEqual(len(combos), 16)
        # Verify that all expected combinations are present
        expected_set = {
            a + b
            for a in "pqrs"
            for b in "wxyz"
        }
        self.assertSetEqual(set(combos), expected_set)

    def test_longer_input_order(self):
        # Verify that the order of generation follows the backtracking sequence
        expected = [
            "adg", "adh", "adi",
            "aeg", "aeh", "aei",
            "afg", "afh", "afi",
            "bdg", "bdh", "bdi",
            "beg", "beh", "bei",
            "bfg", "bfh", "bfi",
            "cdg", "cdh", "cdi",
            "ceg", "ceh", "cei",
            "cfg", "cfh", "cfi"
        ]
        self.assertListEqual(letter_combinations("234"), expected)