import unittest

class TestWordBreak(unittest.TestCase):
    def test_basic_true(self):
        s = "leetcode"
        word_dict = ["leet", "code"]
        result = word_break(s, word_dict)
        self.assertTrue(result)

    def test_multiple_segments_true(self):
        s = "applepenapple"
        word_dict = ["apple", "pen"]
        result = word_break(s, word_dict)
        self.assertTrue(result)

    def test_no_possible_segmentation(self):
        s = "catsandog"
        word_dict = ["cats", "dog", "sand", "and", "cat"]
        result = word_break(s, word_dict)
        self.assertFalse(result)

    def test_empty_dictionary(self):
        s = "anyword"
        word_dict = []
        result = word_break(s, word_dict)
        self.assertFalse(result)

    def test_empty_string_without_empty_word(self):
        s = ""
        word_dict = ["a"]
        result = word_break(s, word_dict)
        self.assertFalse(result)

    def test_empty_string_with_empty_word(self):
        s = ""
        word_dict = [""]
        result = word_break(s, word_dict)
        self.assertTrue(result)

    def test_overlapping_words(self):
        s = "aaaaaaa"
        word_dict = ["a", "aa", "aaa"]
        result = word_break(s, word_dict)
        self.assertTrue(result)

    def test_long_string_performance(self):
        # A long string that can be segmented using repeated short words
        s = "ab" * 50  # 100 characters
        word_dict = ["a", "b", "ab"]
        result = word_break(s, word_dict)
        self.assertTrue(result)