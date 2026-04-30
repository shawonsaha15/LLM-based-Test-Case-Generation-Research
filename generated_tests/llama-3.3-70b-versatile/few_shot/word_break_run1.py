class TestWordBreak(unittest.TestCase):
    def test_breakable_string(self):
        result = word_break("leetcode", ["leet", "code"])
        self.assertTrue(result)

    def test_unbreakable_string(self):
        result = word_break("applepenapple", ["apple", "pen"])
        self.assertTrue(result)

    def test_empty_string(self):
        result = word_break("", ["apple", "pen"])
        self.assertTrue(result)

    def test_string_with_single_word(self):
        result = word_break("apple", ["apple"])
        self.assertTrue(result)

    def test_string_with_no_matching_words(self):
        result = word_break("apple", ["banana", "orange"])
        self.assertFalse(result)

    def test_string_with_repeated_words(self):
        result = word_break("appleapple", ["apple"])
        self.assertTrue(result)

    def test_string_with_long_word(self):
        result = word_break("abcdefghijklmnopqrstuvwxyz", ["abcdefghijklmnopqrstuvwxyz"])
        self.assertTrue(result)