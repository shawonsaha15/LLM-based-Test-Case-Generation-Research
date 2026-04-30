class TestWordBreak(unittest.TestCase):
    def test_word_break_true(self):
        self.assertTrue(word_break("leetcode", ["leet", "code"]))

    def test_word_break_false(self):
        self.assertFalse(word_break("applepenapple", ["apple", "pen"]))

    def test_word_break_empty_string(self):
        self.assertTrue(word_break("", ["a", "b"]))

    def test_word_break_single_word(self):
        self.assertTrue(word_break("a", ["a"]))

    def test_word_break_long_string(self):
        self.assertTrue(word_break("catsanddog", ["cat", "cats", "and", "sand", "dog"]))

    def test_word_break_empty_word_dict(self):
        self.assertFalse(word_break("a", []))

    def test_word_break_no_break(self):
        self.assertFalse(word_break("abcd", ["a", "b", "c"]))