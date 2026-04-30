import unittest


class TestWordBreak(unittest.TestCase):
    def test_empty_string(self):
        self.assertTrue(word_break("", []))

    def test_single_word_in_dict(self):
        self.assertTrue(word_break("apple", ["apple"]))

    def test_single_word_not_in_dict(self):
        self.assertFalse(word_break("apple", ["banana"]))

    def test_multiple_words_possible(self):
        self.assertTrue(word_break("leetcode", ["leet", "code"]))

    def test_overlapping_segments(self):
        self.assertTrue(word_break("applepenapple", ["apple", "pen"]))

    def test_no_break_possible(self):
        self.assertFalse(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))

    def test_repeated_words(self):
        self.assertTrue(word_break("aaaaaaa", ["aaaa", "aaa"]))

    def test_prefix_not_in_dict(self):
        self.assertFalse(word_break("abcdef", ["bc", "def"]))

    def test_suffix_not_in_dict(self):
        self.assertFalse(word_break("abcdef", ["abc", "de"]))

    def test_empty_dict(self):
        self.assertFalse(word_break("anything", []))

    def test_word_longer_than_string(self):
        self.assertFalse(word_break("a", ["apple"]))