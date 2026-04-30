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

    def test_multiple_words_concatenated(self):
        # Arrange
        s = "applebanana"
        word_dict = ["apple", "banana"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertTrue(result)

    def test_empty_string(self):
        # Arrange
        s = ""
        word_dict = ["apple", "banana"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertFalse(result)

    def test_word_not_in_dict(self):
        # Arrange
        s = "orange"
        word_dict = ["apple", "banana"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertFalse(result)

    def test_partial_match_cannot_split(self):
        # Arrange
        s = "appleban"
        word_dict = ["apple", "banana"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertFalse(result)

    def test_overlapping_words(self):
        # Arrange
        s = "catsandog"
        word_dict = ["cats", "dog", "sand", "and", "cat"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertFalse(result)

    def test_repeated_words(self):
        # Arrange
        s = "go"
        word_dict = ["go", "g", "o"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertTrue(result)

    def test_single_char_words(self):
        # Arrange
        s = "abc"
        word_dict = ["a", "b", "c"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertTrue(result)

    def test_long_word_not_in_dict(self):
        # Arrange
        s = "abcdefghijklmnopqrstuvwxyz"
        word_dict = ["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwx", "yz"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertTrue(result)

    def test_empty_dict(self):
        # Arrange
        s = "apple"
        word_dict = []
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertFalse(result)

    def test_prefix_match_but_no_valid_split(self):
        # Arrange
        s = "abcd"
        word_dict = ["a", "abc", "d"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertTrue(result)

    def test_case_with_suffix_only(self):
        # Arrange
        s = "abcd"
        word_dict = ["bcd", "a"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertTrue(result)

    def test_boundary_max_length_word(self):
        # Arrange
        s = "a" * 20
        word_dict = ["a" * 20]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertTrue(result)

    def test_boundary_min_length_word(self):
        # Arrange
        s = "a"
        word_dict = ["a"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertTrue(result)

    def test_invalid_input_non_string_s(self):
        # Arrange
        s = None
        word_dict = ["apple", "banana"]
        # Act & Assert
        with self.assertRaises(AttributeError):
            word_break(s, word_dict)

    def test_invalid_input_non_list_dict(self):
        # Arrange
        s = "apple"
        word_dict = "banana"
        # Act & Assert
        with self.assertRaises(TypeError):
            word_break(s, word_dict)

    def test_invalid_input_dict_with_non_strings(self):
        # Arrange
        s = "apple"
        word_dict = ["apple", 123]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertTrue(result)

    def test_unicode_characters(self):
        # Arrange
        s = "你好世界"
        word_dict = ["你好", "世界"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertTrue(result)

    def test_repeated_substrings(self):
        # Arrange
        s = "aaaaaaa"
        word_dict = ["aaaa", "aaa"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertTrue(result)

    def test_no_valid_segmentation(self):
        # Arrange
        s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        word_dict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertTrue(result)