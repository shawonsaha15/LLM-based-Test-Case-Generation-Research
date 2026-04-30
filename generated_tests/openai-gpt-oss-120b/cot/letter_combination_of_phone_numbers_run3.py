import unittest

class TestLetterCombinations(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(letter_combinations(""), [])

    def test_none_input(self):
        self.assertEqual(letter_combinations(None), [])

    def test_single_digit(self):
        expected = ["a", "b", "c"]
        self.assertListEqual(letter_combinations("2"), expected)

    def test_two_digits(self):
        expected = [
            "ad", "ae", "af",
            "bd", "be", "bf",
            "cd", "ce", "cf"
        ]
        self.assertListEqual(letter_combinations("23"), expected)

    def test_invalid_digit_only(self):
        # Digits 0 and 1 have no mapping, should yield empty list
        self.assertEqual(letter_combinations("1"), [])
        self.assertEqual(letter_combinations("0"), [])

    def test_mixed_valid_invalid(self):
        # Presence of an unmapped character should result in no combinations
        self.assertEqual(letter_combinations("2a3"), [])
        self.assertEqual(letter_combinations("2#3"), [])

    def test_large_input_length(self):
        digits = "2345"
        result = letter_combinations(digits)
        # 3 letters per digit -> 3^4 = 81 combinations
        self.assertEqual(len(result), 81)
        # All strings should have length equal to number of digits
        for combo in result:
            self.assertIsInstance(combo, str)
            self.assertEqual(len(combo), len(digits))

    def test_output_order_consistency(self):
        # Verify that the order matches the expected lexical order for a known case
        digits = "79"
        expected = [
            "pw", "px", "py", "pz",
            "qw", "qx", "qy", "qz",
            "rw", "rx", "ry", "rz",
            "sw", "sx", "sy", "sz"
        ]
        self.assertListEqual(letter_combinations(digits), expected)

    def test_non_string_input_raises(self):
        with self.assertRaises(TypeError):
            letter_combinations(23)  # integer input should raise TypeError due to len()
        with self.assertRaises(TypeError):
            letter_combinations([2, 3])  # list input should raise TypeError

    def test_all_combinations_unique(self):
        digits = "23"
        result = letter_combinations(digits)
        self.assertEqual(len(result), len(set(result)))  # no duplicates

    def test_combination_characters(self):
        # Ensure each character in each combination is from the correct mapping
        mapping = {
            '2': "abc", '3': "def", '4': "ghi",
            '5': "jkl", '6': "mno", '7': "pqrs",
            '8': "tuv", '9': "wxyz"
        }
        digits = "279"
        result = letter_combinations(digits)
        for combo in result:
            for idx, ch in enumerate(combo):
                self.assertIn(ch, mapping[digits[idx]])