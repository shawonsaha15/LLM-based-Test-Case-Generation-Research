import unittest


class TestLongestPalindromeSubseq(unittest.TestCase):

    # Normal cases
    def test_single_character(self):
        # Arrange
        s = "a"
        expected = 1
        # Act
        result = longest_palindrome_subseq(s)
        # Assert
        self.assertEqual(result, expected)

    def test_all_same_characters(self):
        # Arrange
        s = "aaaa"
        expected = 4
        # Act
        result = longest_palindrome_subseq(s)
        # Assert
        self.assertEqual(result, expected)

    def test_no_repeated_characters(self):
        # Arrange
        s = "abcdef"
        expected = 1
        # Act
        result = longest_palindrome_subseq(s)
        # Assert
        self.assertEqual(result, expected)

    def test_typical_palindrome_subsequence(self):
        # Arrange
        s = "bbbab"
        expected = 4  # "bbbb"
        # Act
        result = longest_palindrome_subseq(s)
        # Assert
        self.assertEqual(result, expected)

    def test_mixed_characters_with_palindrome(self):
        # Arrange
        s = "cbbd"
        expected = 2  # "bb"
        # Act
        result = longest_palindrome_subseq(s)
        # Assert
        self.assertEqual(result, expected)

    # Boundary cases
    def test_empty_string(self):
        # Arrange
        s = ""
        expected = 0
        # Act
        result = longest_palindrome_subseq(s)
        # Assert
        self.assertEqual(result, expected)

    def test_two_same_characters(self):
        # Arrange
        s = "aa"
        expected = 2
        # Act
        result = longest_palindrome_subseq(s)
        # Assert
        self.assertEqual(result, expected)

    def test_two_different_characters(self):
        # Arrange
        s = "ab"
        expected = 1
        # Act
        result = longest_palindrome_subseq(s)
        # Assert
        self.assertEqual(result, expected)

    def test_entire_string_is_palindrome(self):
        # Arrange
        s = "racecar"
        expected = 7
        # Act
        result = longest_palindrome_subseq(s)
        # Assert
        self.assertEqual(result, expected)

    # Invalid inputs (though per type hints, function expects str)
    # Testing with non-string inputs is not applicable here due to type hints.
    # If runtime type checking is added, these would be relevant.