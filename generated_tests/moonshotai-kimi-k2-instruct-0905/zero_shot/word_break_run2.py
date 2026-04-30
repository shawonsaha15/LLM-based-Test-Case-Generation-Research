import unittest


class TestWordBreak(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(word_break("", []))

    def test_single_word_in_dict(self):
        self.assertTrue(word_break("apple", ["apple"]))

    def test_single_word_not_in_dict(self):
        self.assertFalse(word_break("apple", ["banana"]))

    def test_multiple_words_valid(self):
        self.assertTrue(word_break("leetcode", ["leet", "code"]))

    def test_multiple_words_invalid(self):
        self.assertFalse(word_break("leetcode", ["leet", "cod"]))

    def test_overlapping_words(self):
        self.assertTrue(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))

    def test_repeated_words(self):
        self.assertTrue(word_break("aaaaaaa", ["aaaa", "aaa"]))

    def test_long_word_not_segmentable(self):
        self.assertFalse(word_break("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
                                    ["a", "aa", "aaa", "aaaa", "aaaaa"]))

    def test_prefix_not_in_dict(self):
        self.assertFalse(word_break("applepenapple", ["apple", "pen"]))

    def test_suffix_not_in_dict(self):
        self.assertFalse(word_break("applepenapple", ["apple", "pen", "applepen"]))

    def test_empty_dict(self):
        self.assertFalse(word_break("anything", []))

    def test_dict_with_empty_string(self):
        self.assertTrue(word_break("", [""]))

    def test_single_char_words(self):
        self.assertTrue(word_break("abc", ["a", "b", "c"]))

    def test_case_sensitivity(self):
        self.assertFalse(word_break("Apple", ["apple"]))

    def test_duplicate_words_in_dict(self):
        self.assertTrue(word_break("appleapple", ["apple", "apple"]))