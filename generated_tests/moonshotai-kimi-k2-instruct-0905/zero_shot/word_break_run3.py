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

    def test_partial_match_at_end(self):
        self.assertTrue(word_break("goalspecial", ["go", "goal", "goals", "special"]))

    def test_long_unbreakable_prefix(self):
        self.assertFalse(word_break("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa"]))

    def test_empty_dict(self):
        self.assertFalse(word_break("anything", []))