class TestWordBreak(unittest.TestCase):
    def test_simple_word_break(self):
        s = "leetcode"
        word_dict = ["leet", "code"]
        result = word_break(s, word_dict)
        self.assertTrue(result)

    def test_no_word_break(self):
        s = "applepenapple"
        word_dict = ["apple"]
        result = word_break(s, word_dict)
        self.assertFalse(result)

    def test_empty_string(self):
        s = ""
        word_dict = ["a", "b"]
        result = word_break(s, word_dict)
        self.assertTrue(result)

    def test_single_word(self):
        s = "a"
        word_dict = ["a"]
        result = word_break(s, word_dict)
        self.assertTrue(result)

    def test_word_not_in_dict(self):
        s = "a"
        word_dict = ["b", "c"]
        result = word_break(s, word_dict)
        self.assertFalse(result)

    def test_long_string(self):
        s = "catsanddog"
        word_dict = ["cat", "cats", "and", "sand", "dog"]
        result = word_break(s, word_dict)
        self.assertTrue(result)