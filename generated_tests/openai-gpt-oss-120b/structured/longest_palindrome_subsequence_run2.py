class TestLongestPalindromeSubseq(unittest.TestCase):
    def test_empty_string(self):
        # Arrange
        s = ""
        # Act
        result = longest_palindrome_subseq(s)
        # Assert
        self.assertEqual(result, 0)

    def test_single_character(self):
        # Arrange
        s = "a"
        # Act
        result = longest_palindrome_subseq(s)
        # Assert
        self.assertEqual(result, 1)

    def test_two_same_characters(self):
        # Arrange
        s = "aa"
        # Act
        result = longest_palindrome_subseq(s)
        # Assert
        self.assertEqual(result, 2)

    def test_two_different_characters(self):
        # Arrange
        s = "ab"
        # Act
        result = longest_palindrome_subseq(s)
        # Assert
        self.assertEqual(result, 1)

    def test_all_same_characters(self):
        # Arrange
        s = "aaaa"
        # Act
        result = longest_palindrome_subseq(s)
        # Assert
        self.assertEqual(result, 4)

    def test_regular_example_1(self):
        # Arrange
        s = "bbbab"
        # Act
        result = longest_palindrome_subseq(s)
        # Assert
        self.assertEqual(result, 4)  # "bbbb"

    def test_regular_example_2(self):
        # Arrange
        s = "cbbd"
        # Act
        result = longest_palindrome_subseq(s)
        # Assert
        self.assertEqual(result, 2)  # "bb"

    def test_mixed_string(self):
        # Arrange
        s = "character"
        # Act
        result = longest_palindrome_subseq(s)
        # Assert
        self.assertEqual(result, 5)  # e.g., "carac"

    def test_long_palindrome(self):
        # Arrange
        s = "agbdba"
        # Act
        result = longest_palindrome_subseq(s)
        # Assert
        self.assertEqual(result, 5)  # "abdba"

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
        s = ["a", "b", "c"]
        # Act & Assert
        with self.assertRaises(TypeError):
            longest_palindrome_subseq(s)