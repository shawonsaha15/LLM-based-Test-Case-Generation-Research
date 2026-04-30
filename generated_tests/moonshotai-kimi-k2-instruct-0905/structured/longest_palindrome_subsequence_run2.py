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
        s = "abcde"
        expected = 1
        # Act
        result = longest_palindrome_subseq(s)
        # Assert
        self.assertEqual(result, expected)

    def test_typical_palindrome_subsequence(self):
        # Arrange
        s = "bbbab"
        expected = 4
        # Act
        result = longest_palindrome_subseq(s)
        # Assert
        self.assertEqual(result, expected)

    def test_mixed_characters_with_palindrome_subsequence(self):
        # Arrange
        s = "cbbd"
        expected = 2
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

    # Invalid inputs (not applicable for this function as per type hints)
    # However, testing robustness with non-string inputs may raise TypeError
    # Since function signature expects str, invalid types are not part of the contract.