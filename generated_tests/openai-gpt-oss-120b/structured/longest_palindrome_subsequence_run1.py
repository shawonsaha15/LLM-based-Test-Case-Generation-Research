import unittest

class TestLongestPalindromeSubseq(unittest.TestCase):
    def test_normal_case_bbbab(self):
        # Arrange
        s = "bbbab"
        expected = 4
        # Act
        result = longest_palindrome_subseq(s)
        # Assert
        self.assertEqual(result, expected)

    def test_normal_case_cbbd(self):
        # Arrange
        s = "cbbd"
        expected = 2
        # Act
        result = longest_palindrome_subseq(s)
        # Assert
        self.assertEqual(result, expected)

    def test_normal_case_character(self):
        # Arrange
        s = "character"
        expected = 5
        # Act
        result = longest_palindrome_subseq(s)
        # Assert
        self.assertEqual(result, expected)

    def test_boundary_empty_string(self):
        # Arrange
        s = ""
        expected = 0
        # Act
        result = longest_palindrome_subseq(s)
        # Assert
        self.assertEqual(result, expected)

    def test_boundary_single_character(self):
        # Arrange
        s = "a"
        expected = 1
        # Act
        result = longest_palindrome_subseq(s)
        # Assert
        self.assertEqual(result, expected)

    def test_boundary_two_same_characters(self):
        # Arrange
        s = "aa"
        expected = 2
        # Act
        result = longest_palindrome_subseq(s)
        # Assert
        self.assertEqual(result, expected)

    def test_boundary_two_different_characters(self):
        # Arrange
        s = "ab"
        expected = 1
        # Act
        result = longest_palindrome_subseq(s)
        # Assert
        self.assertEqual(result, expected)

    def test_invalid_input_none(self):
        # Arrange
        s = None
        # Act & Assert
        with self.assertRaises(TypeError):
            longest_palindrome_subseq(s)

    def test_invalid_input_integer(self):
        # Arrange
        s = 12345
        # Act & Assert
        with self.assertRaises(TypeError):
            longest_palindrome_subseq(s)

    def test_invalid_input_list(self):
        # Arrange
        s = ['a', 'b', 'c']
        # Act & Assert
        with self.assertRaises(TypeError):
            longest_palindrome_subseq(s)