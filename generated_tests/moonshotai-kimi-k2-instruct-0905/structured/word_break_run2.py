import unittest


class TestWordBreak(unittest.TestCase):

    def test_normal_case_exact_match(self):
        # Arrange
        s = "apple"
        word_dict = ["apple", "banana"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertTrue(result)

    def test_normal_case_composite_match(self):
        # Arrange
        s = "applebanana"
        word_dict = ["apple", "banana"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertTrue(result)

    def test_normal_case_no_match(self):
        # Arrange
        s = "applepie"
        word_dict = ["apple", "banana"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertFalse(result)

    def test_boundary_case_empty_string(self):
        # Arrange
        s = ""
        word_dict = ["apple", "banana"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertFalse(result)

    def test_boundary_case_empty_dict(self):
        # Arrange
        s = "apple"
        word_dict = []
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertFalse(result)

    def test_boundary_case_single_char_match(self):
        # Arrange
        s = "a"
        word_dict = ["a"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertTrue(result)

    def test_boundary_case_single_char_no_match(self):
        # Arrange
        s = "a"
        word_dict = ["b"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertFalse(result)

    def test_boundary_case_repeated_words(self):
        # Arrange
        s = "aaaa"
        word_dict = ["a", "aa"]
        # Act
        result = word_break(s, word_dict)
        # Assert
        self.assertTrue(result)

    def test_invalid_input_none_string(self):
        # Arrange
        s = None
        word_dict = ["apple"]
        # Act & Assert
        with self.assertRaises(AttributeError):
            word_break(s, word_dict)

    def test_invalid_input_none_dict(self):
        # Arrange
        s = "apple"
        word_dict = None
        # Act & Assert
        with self.assertRaises(TypeError):
            word_break(s, word_dict)

    def test_invalid_input_dict_contains_non_string(self):
        # Arrange
        s = "apple"
        word_dict = ["apple", 123]
        # Act & Assert
        with self.assertRaises(TypeError):
            word_break(s, word_dict)