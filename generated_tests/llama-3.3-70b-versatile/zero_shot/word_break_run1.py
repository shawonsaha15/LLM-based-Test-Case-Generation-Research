class TestWordBreak(unittest.TestCase):
    def test_word_break_true(self):
        s = "leetcode"
        word_dict = ["leet", "code"]
        self.assertTrue(word_break(s, word_dict))

    def test_word_break_false(self):
        s = "applepenapple"
        word_dict = ["apple", "pen"]
        self.assertFalse(word_break(s, word_dict))

    def test_word_break_empty_string(self):
        s = ""
        word_dict = ["a", "b"]
        self.assertTrue(word_break(s, word_dict))

    def test_word_break_empty_word_dict(self):
        s = "apple"
        word_dict = []
        self.assertFalse(word_break(s, word_dict))

    def test_word_break_single_word(self):
        s = "apple"
        word_dict = ["apple"]
        self.assertTrue(word_break(s, word_dict))

    def test_word_break_long_string(self):
        s = "a" * 100
        word_dict = ["a"]
        self.assertTrue(word_break(s, word_dict))

    def test_word_break_long_word_dict(self):
        s = "apple"
        word_dict = ["apple"] * 100
        self.assertTrue(word_break(s, word_dict))