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
        expected = [
            "adg", "adh", "adi", "aeg", "aeh", "aei", "afg", "afh", "afi",
            "bdg", "bdh", "bdi", "beg", "beh", "bei", "bfg", "bfh", "bfi",
            "cdg", "cdh", "cdi", "ceg", "ceh", "cei", "cfg", "cfh", "cfi"
        ]
        
        # Act
        result = letter_combinations(digits)
        
        # Assert
        self.assertEqual(sorted(result), sorted(expected))

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
    def test_invalid_digit_with_zero(self):
        # Arrange
        digits = "20"
        expected = ["a", "b", "c"]  # '0' maps to empty string, so only letters from '2'
        
        # Act
        result = letter_combinations(digits)
        
        # Assert
        self.assertEqual(sorted(result), sorted(expected))

    def test_invalid_digit_with_one(self):
        # Arrange
        digits = "21"
        expected = ["a", "b", "c"]  # '1' maps to empty string, so only letters from '2'
        
        # Act
        result = letter_combinations(digits)
        
        # Assert
        self.assertEqual(sorted(result), sorted(expected))

    def test_mixed_invalid_and_valid_digits(self):
        # Arrange
        digits = "790"
        expected = ["p", "q", "r", "s"]  # only '7' contributes letters
        
        # Act
        result = letter_combinations(digits)
        
        # Assert
        self.assertEqual(sorted(result), sorted(expected))