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

    def test_multiple_words_combined(self):
        result = word_break("applepen", ["apple", "pen"])
        self.assertTrue(result)

    def test_multiple_words_not_combined(self):
        result = word_break("applepen", ["apple", "banana"])
        self.assertFalse(result)

    def test_overlapping_words(self):
        result = word_break("catsandog", ["cats", "cat", "sand", "and", "dog"])
        self.assertFalse(result)

    def test_repeated_words(self):
        result = word_break("aaaaaaa", ["a", "aa", "aaa"])
        self.assertTrue(result)

    def test_long_string_with_small_words(self):
        result = word_break("leetcode", ["leet", "code"])
        self.assertTrue(result)

    def test_no_possible_break(self):
        result = word_break("abcdef", ["ab", "cd", "efg"])
        self.assertFalse(result)

    def test_empty_dict(self):
        result = word_break("anything", [])
        self.assertFalse(result)