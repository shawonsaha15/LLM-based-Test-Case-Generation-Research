import unittest

class TestWordBreak(unittest.TestCase):
    def test_simple_true(self):
        self.assertTrue(word_break("leetcode", ["leet", "code"]))

    def test_simple_false(self):
        self.assertFalse(word_break("applepenapple", ["apple", "pen"]))

    def test_overlapping_words(self):
        self.assertTrue(word_break("catsanddog", ["cat", "cats", "and", "sand", "dog"]))

    def test_no_possible_break(self):
        self.assertFalse(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))

    def test_empty_string(self):
        self.assertTrue(word_break("", []))
        self.assertTrue(word_break("", ["a", "b"]))

    def test_empty_dictionary(self):
        self.assertFalse(word_break("any", []))

    def test_single_character_words(self):
        self.assertTrue(word_break("aaaa", ["a"]))
        self.assertFalse(word_break("ab", ["c", "d"]))

    def test_long_input_performance(self):
        # Repeating pattern that can be segmented
        s = "ab" * 50
        self.assertTrue(word_break(s, ["a", "b", "ab"]))

    def test_substring_not_at_start(self):
        self.assertTrue(word_break("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))

    def test_dictionary_with_duplicates(self):
        self.assertTrue(word_break("cats", ["cat", "cats", "cat", "cats"]))
        self.assertFalse(word_break("catsdog", ["cat", "cats", "dog"]))