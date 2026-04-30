class TestWordBreak(unittest.TestCase):
    def test_exact_match(self):
        result = word_break("apple", ["apple", "banana"])
        self.assertTrue(result)

    def test_two_words(self):
        result = word_break("applebanana", ["apple", "banana"])
        self.assertTrue(result)

    def test_three_words(self):
        result = word_break("catsandog", ["cats", "and", "dog"])
        self.assertTrue(result)

    def test_no_break_possible(self):
        result = word_break("catsandog", ["cats", "sand", "dog"])
        self.assertFalse(result)

    def test_empty_string(self):
        result = word_break("", ["a", "b"])
        self.assertTrue(result)

    def test_single_char_true(self):
        result = word_break("a", ["a"])
        self.assertTrue(result)

    def test_single_char_false(self):
        result = word_break("a", ["b"])
        self.assertFalse(result)

    def test_reuse_words(self):
        result = word_break("aaaaaa", ["a", "aa"])
        self.assertTrue(result)

    def test_long_word_not_in_dict(self):
        result = word_break("abcd", ["a", "bc", "d"])
        self.assertTrue(result)

    def test_overlapping_prefixes(self):
        result = word_break("leetcode", ["leet", "code", "le", "et"])
        self.assertTrue(result)