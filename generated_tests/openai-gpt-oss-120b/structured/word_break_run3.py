import unittest

class TestWordBreak(unittest.TestCase):
    # Normal cases
    def test_normal_true_simple(self):
        # Arrange
        s = "leetcode"
        word_dict = ["leet", "code"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertTrue(result)

    def test_normal_true_multiple_words(self):
        # Arrange
        s = "applepenapple"
        word_dict = ["apple", "pen"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertTrue(result)

    def test_normal_false_no_segmentation(self):
        # Arrange
        s = "catsandog"
        word_dict = ["cats", "dog", "sand", "and", "cat"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertFalse(result)

    # Boundary cases
    def test_boundary_empty_string(self):
        # Arrange
        s = ""
        word_dict = ["a", "b"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertFalse(result)  # implementation returns False for empty input

    def test_boundary_empty_dict(self):
        # Arrange
        s = "any"
        word_dict = []
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertFalse(result)

    def test_boundary_single_character_match(self):
        # Arrange
        s = "a"
        word_dict = ["a"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertTrue(result)

    def test_boundary_single_character_no_match(self):
        # Arrange
        s = "b"
        word_dict = ["a"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertFalse(result)

    def test_boundary_dict_contains_empty_string(self):
        # Arrange
        s = ""
        word_dict = [""]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertTrue(result)  # empty string is considered a word in the set

    # Invalid input cases
    def test_invalid_input_none_string(self):
        # Arrange
        s = None
        word_dict = ["a"]
        # Act & Assert
        with self.assertRaises(TypeError):
            word_break(s, word_dict)

    def test_invalid_input_none_dict(self):
        # Arrange
        s = "a"
        word_dict = None
        # Act & Assert
        with self.assertRaises(TypeError):
            word_break(s, word_dict)

    def test_invalid_input_non_string_elements(self):
        # Arrange
        s = "123"
        word_dict = [123, 456]  # integers instead of strings
        # Act & Assert
        with self.assertRaises(TypeError):
            word_break(s, word_dict)