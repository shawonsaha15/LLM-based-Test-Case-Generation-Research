import unittest

class TestWordBreak(unittest.TestCase):
    def test_basic_true(self):
        self.assertTrue(word_break("leetcode", ["leet", "code"]))

    def test_basic_false(self):
        self.assertFalse(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))

    def test_multiple_segmentations(self):
        self.assertTrue(word_break("applepenapple", ["apple", "pen"]))

    def test_overlapping_words(self):
        self.assertTrue(word_break("aaaa", ["a", "aa", "aaa"]))

    def test_full_match(self):
        self.assertTrue(word_break("test", ["test"]))

    def test_empty_string_no_dict(self):
        self.assertFalse(word_break("", []))

    def test_empty_string_with_empty_string_in_dict(self):
        self.assertTrue(word_break("", [""]))

    def test_nonempty_string_empty_dict(self):
        self.assertFalse(word_break("nonempty", []))

    def test_reuse_words(self):
        self.assertTrue(word_break("aaaaa", ["aa", "aaa"]))

    def test_no_possible_segmentation(self):
        self.assertFalse(word_break("abcd", ["a", "abc", "b", "cdx"]))