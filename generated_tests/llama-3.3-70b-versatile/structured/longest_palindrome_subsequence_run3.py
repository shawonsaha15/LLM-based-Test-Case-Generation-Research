class TestLongestPalindromeSubseq(unittest.TestCase):
    def test_normal_case_single_character(self):
        # Arrange
        s = "a"
        expected_result = 1

        # Act
        result = longest_palindrome_subseq(s)

        # Assert
        self.assertEqual(result, expected_result)

    def test_normal_case_multiple_characters_palindrome(self):
        # Arrange
        s = "aba"
        expected_result = 3

        # Act
        result = longest_palindrome_subseq(s)

        # Assert
        self.assertEqual(result, expected_result)

    def test_normal_case_multiple_characters_not_palindrome(self):
        # Arrange
        s = "abc"
        expected_result = 1

        # Act
        result = longest_palindrome_subseq(s)

        # Assert
        self.assertEqual(result, expected_result)

    def test_boundary_case_empty_string(self):
        # Arrange
        s = ""
        expected_result = 0

        # Act
        result = longest_palindrome_subseq(s)

        # Assert
        self.assertEqual(result, expected_result)

    def test_boundary_case_long_string(self):
        # Arrange
        s = "a" * 100
        expected_result = 100

        # Act
        result = longest_palindrome_subseq(s)

        # Assert
        self.assertEqual(result, expected_result)

    def test_invalid_input_none(self):
        # Arrange
        s = None
        expected_result = None

        # Act and Assert
        with self.assertRaises(TypeError):
            longest_palindrome_subseq(s)

    def test_invalid_input_integer(self):
        # Arrange
        s = 123
        expected_result = None

        # Act and Assert
        with self.assertRaises(TypeError):
            longest_palindrome_subseq(s)

    def test_invalid_input_list(self):
        # Arrange
        s = ["a", "b", "c"]
        expected_result = None

        # Act and Assert
        with self.assertRaises(TypeError):
            longest_palindrome_subseq(s)