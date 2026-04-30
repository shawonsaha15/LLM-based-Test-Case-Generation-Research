import unittest

class TestLetterCombinations(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(letter_combinations(""), [])

    def test_single_digit(self):
        self.assertCountEqual(letter_combinations("2"), ["a", "b", "c"])
        self.assertCountEqual(letter_combinations("7"), ["p", "q", "r", "s"])

    def test_two_digits(self):
        expected = [
            "ad", "ae", "af",
            "bd", "be", "bf",
            "cd", "ce", "cf"
        ]
        self.assertEqual(letter_combinations("23"), expected)

    def test_three_digits(self):
        result = letter_combinations("279")
        # 3 * 3 * 4 = 36 combinations
        self.assertEqual(len(result), 36)
        # each combination should have length 3
        for combo in result:
            self.assertIsInstance(combo, str)
            self.assertEqual(len(combo), 3)

    def test_invalid_digit_only(self):
        # Digits '0' and '1' have no mapping, should yield no combinations
        self.assertEqual(letter_combinations("1"), [])
        self.assertEqual(letter_combinations("0"), [])
        self.assertEqual(letter_combinations("10"), [])

    def test_mixed_valid_and_invalid_digits(self):
        # Presence of an unmapped digit should result in no output
        self.assertEqual(letter_combinations("21"), [])
        self.assertEqual(letter_combinations("2*3"), [])  # '*' is not in the map

    def test_order_preservation(self):
        # Verify that the order of results matches the backtracking order
        result = letter_combinations("23")
        expected_order = [
            "ad", "ae", "af",
            "bd", "be", "bf",
            "cd", "ce", "cf"
        ]
        self.assertEqual(result, expected_order)