class TestWordBreak(unittest.TestCase):
    def test_simple_break(self):
        s = "leetcode"
        word_dict = ["leet", "code"]
        result = word_break(s, word_dict)
        self.assertTrue(result)

    def test_no_break(self):
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

    def test_long_string(self):
        s = "catsandog"
        word_dict = ["cats", "dog", "sand", "and", "cat"]
        result = word_break(s, word_dict)
        self.assertFalse(result)

    def test_repeated_words(self):
        s = "aaba"
        word_dict = ["aa", "ba"]
        result = word_break(s, word_dict)
        self.assertFalse(result)

    def test_no_words(self):
        s = "a"
        word_dict = []
        result = word_break(s, word_dict)
        self.assertFalse(result)