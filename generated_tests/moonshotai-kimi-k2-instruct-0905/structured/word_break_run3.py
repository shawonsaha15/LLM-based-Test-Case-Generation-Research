import unittest

class TestWordBreak(unittest.TestCase):

    def test_single_word_in_dict(self):
        # Arrange
        s = "apple"
        word_dict = ["apple", "banana"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertTrue(result)

    def test_concatenated_words(self):
        # Arrange
        s = "applepen"
        word_dict = ["apple", "pen"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertTrue(result)

    def test_no_break_possible(self):
        # Arrange
        s = "catsandog"
        word_dict = ["cats", "dog", "sand", "and", "cat"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertFalse(result)

    def test_empty_string(self):
        # Arrange
        s = ""
        word_dict = ["a", "b"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertFalse(result)

    def test_empty_dict(self):
        # Arrange
        s = "anything"
        word_dict = []
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertFalse(result)

    def test_overlapping_segments(self):
        # Arrange
        s = "cars"
        word_dict = ["car", "ca", "rs"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertTrue(result)

    def test_repeated_words(self):
        # Arrange
        s = "aaaaaaa"
        word_dict = ["aaaa", "aaa"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertTrue(result)

    def test_long_word_not_in_dict(self):
        # Arrange
        s = "abcdefghijklmnopqrstuvwxyz"
        word_dict = ["a", "b", "c", "d"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertFalse(result)

    def test_single_char_dict(self):
        # Arrange
        s = "abc"
        word_dict = ["a", "b", "c"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertTrue(result)

    def test_prefix_not_in_dict(self):
        # Arrange
        s = "leetcode"
        word_dict = ["leet", "code"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertTrue(result)

    def test_boundary_max_len_word(self):
        # Arrange
        s = "a" * 20
        word_dict = ["a" * 20]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertTrue(result)

    def test_invalid_input_non_string_s(self):
        # Arrange
        s = None
        word_dict = ["a", "b"]
        # Act & Assert
        with self.assertRaises(AttributeError):
            word_break(s, word_dict)

    def test_invalid_input_non_list_dict(self):
        # Arrange
        s = "abc"
        word_dict = "abc"
        # Act & Assert
        with self.assertRaises(TypeError):
            word_break(s, word_dict)

    def test_invalid_input_dict_with_non_strings(self):
        # Arrange
        s = "abc"
        word_dict = ["a", 1, "c"]
        # Act & Assert
        with self.assertRaises(TypeError):
            word_break(s, word_dict)