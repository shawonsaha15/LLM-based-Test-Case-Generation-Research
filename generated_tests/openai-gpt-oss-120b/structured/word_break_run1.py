import unittest

class TestWordBreak(unittest.TestCase):
    # Normal cases
    def test_segmentation_possible_simple(self):
        # Arrange
        s = "leetcode"
        word_dict = ["leet", "code"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertTrue(result)

    def test_segmentation_possible_multiple_words(self):
        # Arrange
        s = "applepenapple"
        word_dict = ["apple", "pen"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertTrue(result)

    def test_segmentation_impossible(self):
        # Arrange
        s = "catsandog"
        word_dict = ["cats", "dog", "sand", "and", "cat"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertFalse(result)

    # Boundary cases
    def test_empty_string_with_nonempty_dict(self):
        # Arrange
        s = ""
        word_dict = ["a", "b"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertTrue(result)  # empty string is trivially segmentable

    def test_empty_string_with_empty_dict(self):
        # Arrange
        s = ""
        word_dict = []
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertTrue(result)

    def test_nonempty_string_with_empty_dict(self):
        # Arrange
        s = "a"
        word_dict = []
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertFalse(result)

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

    def test_long_string_performance_boundary(self):
        # Arrange
        s = "a" * 20  # relatively long repetitive string
        word_dict = ["a", "aa", "aaa", "aaaa"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertTrue(result)

    # Invalid inputs
    def test_non_string_input_raises_type_error(self):
        # Arrange
        s = None
        word_dict = ["a"]
        # Act & Assert
        with self.assertRaises(TypeError):
            word_break(s, word_dict)

    def test_non_iterable_word_dict_raises_type_error(self):
        # Arrange
        s = "a"
        word_dict = None
        # Act & Assert
        with self.assertRaises(TypeError):
            word_break(s, word_dict)

    def test_word_dict_contains_non_hashable_raises_type_error(self):
        # Arrange
        s = "ab"
        word_dict = ["a", ["b"]]  # list inside dict is unhashable
        # Act & Assert
        with self.assertRaises(TypeError):
            word_break(s, word_dict)