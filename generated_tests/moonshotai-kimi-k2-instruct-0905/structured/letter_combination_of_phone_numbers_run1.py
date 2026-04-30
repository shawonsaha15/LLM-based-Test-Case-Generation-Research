import unittest


class TestLetterCombinations(unittest.TestCase):

    def test_single_digit_normal_case(self):
        # Arrange
        digits = "2"
        expected = ["a", "b", "c"]
        # Act
        result = letter_combinations(digits)
        # Assert
        self.assertEqual(sorted(result), sorted(expected))

    def test_two_digits_normal_case(self):
        # Arrange
        digits = "23"
        expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        # Act
        result = letter_combinations(digits)
        # Assert
        self.assertEqual(sorted(result), sorted(expected))

    def test_three_digits_normal_case(self):
        # Arrange
        digits = "234"
        expected_length = 27  # 3*3*3
        # Act
        result = letter_combinations(digits)
        # Assert
        self.assertEqual(len(result), expected_length)

    def test_empty_string_boundary_case(self):
        # Arrange
        digits = ""
        expected = []
        # Act
        result = letter_combinations(digits)
        # Assert
        self.assertEqual(result, expected)

    def test_digit_with_four_letters_boundary_case(self):
        # Arrange
        digits = "7"
        expected = ["p", "q", "r", "s"]
        # Act
        result = letter_combinations(digits)
        # Assert
        self.assertEqual(sorted(result), sorted(expected))

    def test_digit_with_three_letters_boundary_case(self):
        # Arrange
        digits = "8"
        expected = ["t", "u", "v"]
        # Act
        result = letter_combinations(digits)
        # Assert
        self.assertEqual(sorted(result), sorted(expected))

    def test_invalid_digit_with_no_mapping_invalid_case(self):
        # Arrange
        digits = "1"
        expected = []
        # Act
        result = letter_combinations(digits)
        # Assert
        self.assertEqual(result, expected)

    def test_mixed_valid_and_invalid_digits_invalid_case(self):
        # Arrange
        digits = "29"
        expected = ["a", "b", "c"]  # '9' maps to empty string
        # Act
        result = letter_combinations(digits)
        # Assert
        self.assertEqual(sorted(result), sorted(expected))

    def test_long_valid_sequence_boundary_case(self):
        # Arrange
        digits = "222"
        expected_length = 27  # 3^3
        # Act
        result = letter_combinations(digits)
        # Assert
        self.assertEqual(len(result), expected_length)

    def test_all_digits_with_four_letters_boundary_case(self):
        # Arrange
        digits = "79"
        expected = ["p", "q", "r", "s"]  # '9' maps to empty
        # Act
        result = letter_combinations(digits)
        # Assert
        self.assertEqual(sorted(result), sorted(expected))