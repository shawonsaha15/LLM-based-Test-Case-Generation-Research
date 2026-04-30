import unittest

class TestLetterCombinations(unittest.TestCase):
    def test_normal_single_digit(self):
        # Arrange
        digits = "2"
        expected = ["a", "b", "c"]
        # Act
        result = letter_combinations(digits)
        # Assert
        self.assertEqual(result, expected)

    def test_normal_multiple_digits(self):
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
        self.assertEqual(result, expected)

    def test_boundary_empty_string(self):
        # Arrange
        digits = ""
        expected = []
        # Act
        result = letter_combinations(digits)
        # Assert
        self.assertEqual(result, expected)

    def test_boundary_long_input(self):
        # Arrange
        digits = "2345"  # 3 * 3 * 3 * 3 = 81 combinations
        expected_length = 81
        # Act
        result = letter_combinations(digits)
        # Assert
        self.assertEqual(len(result), expected_length)
        # Spot‑check a few expected combinations
        self.assertIn("adgj", result)
        self.assertIn("cfil", result)
        self.assertIn("behk", result)

    def test_invalid_contains_zero_one(self):
        # Arrange
        digits = "210"
        expected = []  # '0' and '1' have no mapping, leading to no combinations
        # Act
        result = letter_combinations(digits)
        # Assert
        self.assertEqual(result, expected)

    def test_invalid_non_digit_characters(self):
        # Arrange
        digits = "2a3"
        expected = []  # 'a' is not a valid digit key, treated as empty mapping
        # Act
        result = letter_combinations(digits)
        # Assert
        self.assertEqual(result, expected)

    def test_invalid_none_input(self):
        # Arrange
        digits = None
        # Act & Assert
        with self.assertRaises(TypeError):
            letter_combinations(digits)