import unittest


class TestLongestPalindromeSubseq(unittest.TestCase):

    # Normal cases
    def test_normal_palindrome(self):
        # Arrange
        s = "bbbab"
        expected = 4
        # Act
        result = longest_palindrome_subseq(s)
        # Assert
        self.assertEqual(result, expected)

    def test_normal_non_palindrome(self):
        # Arrange
        s = "cbbd"
        expected = 2
        # Act
        result = longest_palindrome_subseq(s)
        # Assert
        self.assertEqual(result, expected)

    def test_normal_all_same(self):
        # Arrange
        s = "aaaa"
        expected = 4
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

    def test_single_character(self):
        # Arrange
        s = "a"
        expected = 1
        # Act
        result = longest_palindrome_subseq(s)
        # Assert
        self.assertEqual(result, expected)

    def test_two_different_chars(self):
        # Arrange
        s = "ab"
        expected = 1
        # Act
        result = longest_palindrome_subseq(s)
        # Assert
        self.assertEqual(result, expected)

    def test_two_same_chars(self):
        # Arrange
        s = "aa"
        expected = 2
        # Act
        result = longest_palindrome_subseq(s)
        # Assert
        self.assertEqual(result, expected)

    # Invalid inputs (not applicable for str type, but testing edge types)
    def test_none_input(self):
        # Arrange
        s = None
        # Act & Assert
        with self.assertRaises(TypeError):
            longest_palindrome_subseq(s)

    def test_non_string_input(self):
        # Arrange
        s = 12345
        # Act & Assert
        with self.assertRaises(TypeError):
            longest_palindrome_subseq(s)