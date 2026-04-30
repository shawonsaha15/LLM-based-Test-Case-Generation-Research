import unittest

class TestWordBreak(unittest.TestCase):
    def test_basic_true(self):
        self.assertTrue(word_break("leetcode", ["leet", "code"]))

    def test_basic_false(self):
        self.assertFalse(word_break("applepenapple", ["apple", "pen"]))

    def test_empty_string(self):
        # Empty string should be considered breakable (trivially)
        self.assertTrue(word_break("", []))
        self.assertTrue(word_break("", ["a"]))

    def test_empty_dict(self):
        self.assertFalse(word_break("any", []))

    def test_single_character(self):
        self.assertTrue(word_break("a", ["a"]))
        self.assertFalse(word_break("b", ["a"]))

    def test_multiple_options(self):
        self.assertTrue(word_break("catsanddog", ["cat", "cats", "and", "sand", "dog"]))

    def test_overlapping_words(self):
        self.assertTrue(word_break("aaaaaaa", ["a", "aa", "aaa"]))

    def test_no_possible_break(self):
        self.assertFalse(word_break("abcd", ["a", "abc", "b"]))

    def test_long_input_performance(self):
        # A long string that cannot be broken should return False without recursion overflow
        s = "a" * 20 + "b"
        dict_words = ["a" * i for i in range(1, 11)]
        self.assertFalse(word_break(s, dict_words))

    def test_full_string_in_dict(self):
        self.assertTrue(word_break("test", ["test", "testing"]))