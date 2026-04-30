class TestWordBreakFunction(unittest.TestCase):
    def test_word_break_with_valid_input(self):
        s = "leetcode"
        word_dict = ["leet", "code"]
        self.assertTrue(word_break(s, word_dict))

    def test_word_break_with_invalid_input(self):
        s = "applepenapple"
        word_dict = ["apple", "pen"]
        self.assertTrue(word_break(s, word_dict))

    def test_word_break_with_empty_string(self):
        s = ""
        word_dict = ["a", "b"]
        self.assertFalse(word_break(s, word_dict))

    def test_word_break_with_empty_word_dict(self):
        s = "apple"
        word_dict = []
        self.assertFalse(word_break(s, word_dict))

    def test_word_break_with_single_word_in_dict(self):
        s = "apple"
        word_dict = ["apple"]
        self.assertTrue(word_break(s, word_dict))

    def test_word_break_with_multiple_words_in_dict(self):
        s = "catsanddog"
        word_dict = ["cat", "cats", "and", "sand", "dog"]
        self.assertFalse(word_break(s, word_dict))