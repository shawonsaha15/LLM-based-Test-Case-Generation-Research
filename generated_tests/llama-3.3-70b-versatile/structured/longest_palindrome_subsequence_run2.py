class TestLongestPalindromeSubseq(unittest.TestCase):

    def test_normal_case_single_character(self):
        # Arrange
        s = "a"
        expected_result = 1

        # Act
        result = longest_palindrome_subseq(s)

        # Assert
        self.assertEqual(result, expected_result)

    def test_normal_case_multiple_characters(self):
        # Arrange
        s = "banana"
        expected_result = 3

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

    def test_boundary_case_two_characters(self):
        # Arrange
        s = "ab"
        expected_result = 1

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

    def test_invalid_input_non_string(self):
        # Arrange
        s = 123
        expected_result = None

        # Act and Assert
        with self.assertRaises(TypeError):
            longest_palindrome_subseq(s)

    def test_normal_case_palindrome(self):
        # Arrange
        s = "madam"
        expected_result = 5

        # Act
        result = longest_palindrome_subseq(s)

        # Assert
        self.assertEqual(result, expected_result)

    def test_normal_case_long_string(self):
        # Arrange
        s = "abcdefghba"
        expected_result = 3

        # Act
        result = longest_palindrome_subseq(s)

        # Assert
        self.assertEqual(result, expected_result)