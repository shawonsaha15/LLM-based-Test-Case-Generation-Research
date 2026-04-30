import unittest

class TestLetterCombinations(unittest.TestCase):
    def test_normal_two_digits(self):
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

    def test_normal_single_digit(self):
        # Arrange
        digits = "2"
        expected = ["a", "b", "c"]

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

    def test_boundary_maximum_letters_per_digit(self):
        # Arrange
        digits = "79"  # 7 -> 4 letters, 9 -> 4 letters => 16 combinations
        expected = [
            "pw", "px", "py", "pz",
            "qw", "qx", "qy", "qz",
            "rw", "rx", "ry", "rz",
            "sw", "sx", "sy", "sz"
        ]

        # Act
        result = letter_combinations(digits)

        # Assert
        self.assertEqual(result, expected)

    def test_invalid_contains_zero(self):
        # Arrange
        digits = "20"
        expected = []  # '0' maps to no letters, so no combinations are possible

        # Act
        result = letter_combinations(digits)

        # Assert
        self.assertEqual(result, expected)

    def test_invalid_contains_one(self):
        # Arrange
        digits = "31"
        expected = []  # '1' maps to no letters

        # Act
        result = letter_combinations(digits)

        # Assert
        self.assertEqual(result, expected)

    def test_invalid_non_digit_characters(self):
        # Arrange
        digits = "2a3"
        expected = []  # 'a' maps to no letters, breaking the combination chain

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