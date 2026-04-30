class TestWordBreak(unittest.TestCase):
    def test_empty_string(self):
        result = word_break("", ["a", "b"])
        self.assertTrue(result)

    def test_single_word_in_dict(self):
        result = word_break("apple", ["apple", "banana"])
        self.assertTrue(result)

    def test_single_word_not_in_dict(self):
        result = word_break("apple", ["banana", "orange"])
        self.assertFalse(result)

    def test_multiple_words_can_be_segmented(self):
        result = word_break("applepen", ["apple", "pen"])
        self.assertTrue(result)

    def test_multiple_words_cannot_be_segmented(self):
        result = word_break("applepenapple", ["apple", "pen"])
        self.assertFalse(result)

    def test_overlapping_words(self):
        result = word_break("catsandog", ["cats", "dog", "sand", "and", "cat"])
        self.assertFalse(result)

    def test_repeated_words(self):
        result = word_break("aaaaaaa", ["aaaa", "aaa"])
        self.assertTrue(result)

    def test_long_string_with_small_words(self):
        result = word_break("leetcode", ["leet", "code"])
        self.assertTrue(result)

    def test_prefix_not_in_dict(self):
        result = word_break("abcd", ["bc", "d"])
        self.assertFalse(result)

    def test_suffix_not_in_dict(self):
        result = word_break("abcd", ["a", "bc"])
        self.assertFalse(result)