import unittest

class TestLetterCombinations(unittest.TestCase):
    def test_empty_input(self):
        # Arrange
        digits = ""
        # Act
        result = letter_combinations(digits)
        # Assert
        self.assertEqual(result, [])

    def test_single_digit(self):
        # Arrange
        digits = "2"
        expected = ["a", "b", "c"]
        # Act
        result = letter_combinations(digits)
        # Assert
        self.assertCountEqual(result, expected)

    def test_two_digits_normal(self):
        # Arrange
        digits = "23"
        expected = [
            "ad", "ae", "af",
            "bd", "be", "bf",
            "cd", "ce", "cf"
        ]
        # Act
        result = letter_combinations(digits)
        # Assert
        self.assertEqual(result, expected)  # order is deterministic

    def test_three_digits_boundary(self):
        # Arrange
        digits = "234"
        # Act
        result = letter_combinations(digits)
        # Assert
        self.assertEqual(len(result), 27)               # 3 * 3 * 3 combinations
        self.assertIn("adg", result)                    # first possible combo
        self.assertIn("cfi", result)                    # last possible combo

    def test_invalid_digit_zero(self):
        # Arrange
        digits = "20"
        # Act
        result = letter_combinations(digits)
        # Assert
        self.assertEqual(result, [])                     # '0' yields no letters

    def test_invalid_non_digit_character(self):
        # Arrange
        digits = "2a3"
        # Act
        result = letter_combinations(digits)
        # Assert
        self.assertEqual(result, [])                     # 'a' yields no letters

    def test_long_input(self):
        # Arrange
        digits = "79"                                   # 4 letters * 4 letters = 16 combos
        expected_len = 16
        # Act
        result = letter_combinations(digits)
        # Assert
        self.assertEqual(len(result), expected_len)
        self.assertIn("pw", result)                     # one valid combo
        self.assertIn("sz", result)                     # another valid combo