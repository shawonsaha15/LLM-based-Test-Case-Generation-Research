import unittest

class TestWordBreak(unittest.TestCase):
    def test_simple_true(self):
        s = "leetcode"
        word_dict = ["leet", "code"]
        self.assertTrue(word_break(s, word_dict))

    def test_multiple_words_true(self):
        s = "applepenapple"
        word_dict = ["apple", "pen"]
        self.assertTrue(word_break(s, word_dict))

    def test_no_possible_break_false(self):
        s = "catsandog"
        word_dict = ["cats", "dog", "sand", "and", "cat"]
        self.assertFalse(word_break(s, word_dict))

    def test_empty_string_and_empty_dict(self):
        s = ""
        word_dict = []
        self.assertFalse(word_break(s, word_dict))

    def test_empty_string_with_nonempty_dict(self):
        s = ""
        word_dict = ["a"]
        self.assertFalse(word_break(s, word_dict))

    def test_dict_contains_empty_string(self):
        s = "any"
        word_dict = [""]
        self.assertFalse(word_break(s, word_dict))

    def test_overlapping_words(self):
        s = "aaaaaaa"
        word_dict = ["a", "aa", "aaa"]
        self.assertTrue(word_break(s, word_dict))

    def test_long_string_false(self):
        s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        word_dict = ["b", "ab", "ba"]
        self.assertFalse(word_break(s, word_dict))