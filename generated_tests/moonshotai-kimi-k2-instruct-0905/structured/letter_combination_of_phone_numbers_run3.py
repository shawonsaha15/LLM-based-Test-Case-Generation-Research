import unittest

class TestLetterCombinations(unittest.TestCase):

    # Normal cases
    def test_single_digit(self):
        # Arrange
        digits = "2"
        expected = ["a", "b", "c"]
        # Act
        result = letter_combinations(digits)
        # Assert
        self.assertEqual(sorted(result), sorted(expected))

    def test_two_digits(self):
        # Arrange
        digits = "23"
        expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        # Act
        result = letter_combinations(digits)
        # Assert
        self.assertEqual(sorted(result), sorted(expected))

    def test_three_digits(self):
        # Arrange
        digits = "234"
        expected_length = 27  # 3*3*3
        # Act
        result = letter_combinations(digits)
        # Assert
        self.assertEqual(len(result), expected_length)

    # Boundary cases
    def test_empty_string(self):
        # Arrange
        digits = ""
        expected = []
        # Act
        result = letter_combinations(digits)
        # Assert
        self.assertEqual(result, expected)

    def test_digit_with_four_letters(self):
        # Arrange
        digits = "7"
        expected = ["p", "q", "r", "s"]
        # Act
        result = letter_combinations(digits)
        # Assert
        self.assertEqual(sorted(result), sorted(expected))

    def test_digit_with_three_letters(self):
        # Arrange
        digits = "8"
        expected = ["t", "u", "v"]
        # Act
        result = letter_combinations(digits)
        # Assert
        self.assertEqual(sorted(result), sorted(expected))

    # Invalid inputs
    def test_invalid_digit(self):
        # Arrange
        digits = "1"
        expected = []
        # Act
        result = letter_combinations(digits)
        # Assert
        self.assertEqual(result, expected)

    def test_mixed_invalid_digits(self):
        # Arrange
        digits = "29"
        expected = ["w", "x", "y", "z"]  # '2' maps to abc, '9' maps to nothing
        # Act
        result = letter_combinations(digits)
        # Assert
        self.assertEqual(sorted(result), sorted(expected))

    def test_only_invalid_digits(self):
        # Arrange
        digits = "019"
        expected = []
        # Act
        result = letter_combinations(digits)
        # Assert
        self.assertEqual(result, expected)