class TestLongestPalindromeSubseq(unittest.TestCase):

    def test_normal_case_single_character(self):
        # Arrange
        s = "a"
        expected_output = 1

        # Act
        actual_output = longest_palindrome_subseq(s)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_normal_case_multiple_characters(self):
        # Arrange
        s = "bbbab"
        expected_output = 4

        # Act
        actual_output = longest_palindrome_subseq(s)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_boundary_case_empty_string(self):
        # Arrange
        s = ""
        expected_output = 0

        # Act
        actual_output = longest_palindrome_subseq(s)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_boundary_case_long_string(self):
        # Arrange
        s = "a" * 1000
        expected_output = 1000

        # Act
        actual_output = longest_palindrome_subseq(s)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_invalid_input_none(self):
        # Arrange
        s = None
        expected_output = None

        # Act and Assert
        with self.assertRaises(TypeError):
            longest_palindrome_subseq(s)

    def test_invalid_input_non_string(self):
        # Arrange
        s = 123
        expected_output = None

        # Act and Assert
        with self.assertRaises(TypeError):
            longest_palindrome_subseq(s)

    def test_invalid_input_mixed_characters_and_numbers(self):
        # Arrange
        s = "abc123"
        expected_output = 1

        # Act
        actual_output = longest_palindrome_subseq(s)

        # Assert
        self.assertLessEqual(actual_output, len(s))