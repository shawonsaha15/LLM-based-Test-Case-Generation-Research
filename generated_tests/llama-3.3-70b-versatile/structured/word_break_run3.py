class TestWordBreak(unittest.TestCase):

    def test_normal_case(self):
        # Arrange
        s = "leetcode"
        word_dict = ["leet", "code"]
        
        # Act
        result = word_break(s, word_dict)
        
        # Assert
        self.assertTrue(result)

    def test_normal_case_multiple_words(self):
        # Arrange
        s = "applepenapple"
        word_dict = ["apple", "pen"]
        
        # Act
        result = word_break(s, word_dict)
        
        # Assert
        self.assertTrue(result)

    def test_boundary_case_empty_string(self):
        # Arrange
        s = ""
        word_dict = ["a"]
        
        # Act
        result = word_break(s, word_dict)
        
        # Assert
        self.assertFalse(result)

    def test_boundary_case_single_word(self):
        # Arrange
        s = "a"
        word_dict = ["a"]
        
        # Act
        result = word_break(s, word_dict)
        
        # Assert
        self.assertTrue(result)

    def test_invalid_input_empty_word_dict(self):
        # Arrange
        s = "a"
        word_dict = []
        
        # Act
        result = word_break(s, word_dict)
        
        # Assert
        self.assertFalse(result)

    def test_invalid_input_none_string(self):
        # Arrange
        s = None
        word_dict = ["a"]
        
        # Act and Assert
        with self.assertRaises(TypeError):
            word_break(s, word_dict)

    def test_invalid_input_none_word_dict(self):
        # Arrange
        s = "a"
        word_dict = None
        
        # Act and Assert
        with self.assertRaises(TypeError):
            word_break(s, word_dict)

    def test_invalid_input_empty_string_and_word_dict(self):
        # Arrange
        s = ""
        word_dict = []
        
        # Act
        result = word_break(s, word_dict)
        
        # Assert
        self.assertFalse(result)

    def test_invalid_input_string_with_spaces(self):
        # Arrange
        s = "a b"
        word_dict = ["a", "b"]
        
        # Act
        result = word_break(s, word_dict)
        
        # Assert
        self.assertFalse(result)