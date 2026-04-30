import unittest

class TestWordBreak(unittest.TestCase):
    # Normal cases
    def test_example_true(self):
        # Arrange
        s = "leetcode"
        word_dict = ["leet", "code"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertTrue(result)

    def test_example_true_multiple_words(self):
        # Arrange
        s = "applepenapple"
        word_dict = ["apple", "pen"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertTrue(result)

    def test_example_false(self):
        # Arrange
        s = "catsandog"
        word_dict = ["cats", "dog", "sand", "and", "cat"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertFalse(result)

    # Boundary cases
    def test_empty_string_empty_dict(self):
        # Arrange
        s = ""
        word_dict = []
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertFalse(result)  # According to current implementation

    def test_single_character_match(self):
        # Arrange
        s = "a"
        word_dict = ["a"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertTrue(result)

    def test_single_character_no_match(self):
        # Arrange
        s = "b"
        word_dict = ["a"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertFalse(result)

    def test_string_equals_word_in_dict(self):
        # Arrange
        s = "hello"
        word_dict = ["hello", "world"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertTrue(result)

    # Invalid input cases
    def test_non_string_input_raises_type_error(self):
        # Arrange
        s = 12345  # not a string
        word_dict = ["1", "2", "3", "4", "5"]
        # Act & Assert
        with self.assertRaises(TypeError):
            word_break(s, word_dict)

    def test_none_string_input_raises_type_error(self):
        # Arrange
        s = None
        word_dict = ["none"]
        # Act & Assert
        with self.assertRaises(TypeError):
            word_break(s, word_dict)

    def test_none_word_dict_raises_type_error(self):
        # Arrange
        s = "test"
        word_dict = None  # not iterable
        # Act & Assert
        with self.assertRaises(TypeError):
            word_break(s, word_dict)

    def test_word_dict_with_non_string_elements(self):
        # Arrange
        s = "123"
        word_dict = [1, 2, 3]  # integers instead of strings
        # Act
        result = word_break(s, word_dict)
        # Assert
        # Integers are hashable and will be stored in the set; the algorithm will never match substrings,
        # so the result should be False.
        self.assertFalse(result)