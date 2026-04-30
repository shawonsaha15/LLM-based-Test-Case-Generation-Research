import unittest

class TestWordBreak(unittest.TestCase):
    def test_basic_true(self):
        s = "leetcode"
        word_dict = ["leet", "code"]
        result = word_break(s, word_dict)
        self.assertTrue(result)

    def test_basic_false(self):
        s = "catsandog"
        word_dict = ["cats", "dog", "sand", "and", "cat"]
        result = word_break(s, word_dict)
        self.assertFalse(result)

    def test_entire_string_in_dict(self):
        s = "hello"
        word_dict = ["hello"]
        result = word_break(s, word_dict)
        self.assertTrue(result)

    def test_multiple_words(self):
        s = "applepenapple"
        word_dict = ["apple", "pen"]
        result = word_break(s, word_dict)
        self.assertTrue(result)

    def test_overlapping_words(self):
        s = "aaaa"
        word_dict = ["a", "aa", "aaa"]
        result = word_break(s, word_dict)
        self.assertTrue(result)

    def test_empty_string_and_dict(self):
        s = ""
        word_dict = []
        result = word_break(s, word_dict)
        self.assertFalse(result)

    def test_empty_string_nonempty_dict(self):
        s = ""
        word_dict = ["a"]
        result = word_break(s, word_dict)
        self.assertFalse(result)

    def test_no_possible_break(self):
        s = "abcd"
        word_dict = ["a", "abc", "b", "cd"]
        result = word_break(s, word_dict)
        self.assertFalse(result)

    def test_duplicate_words_in_dict(self):
        s = "catsdog"
        word_dict = ["cat", "cats", "dog", "dog"]
        result = word_break(s, word_dict)
        self.assertTrue(result)