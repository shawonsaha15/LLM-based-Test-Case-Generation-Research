import unittest

class TestWordBreak(unittest.TestCase):
    def test_basic_true(self):
        s = "leetcode"
        word_dict = ["leet", "code"]
        self.assertTrue(word_break(s, word_dict))

    def test_basic_false(self):
        s = "applepenapple"
        word_dict = ["apple", "pen"]
        self.assertFalse(word_break(s, word_dict))

    def test_multiple_segmentations(self):
        s = "catsanddog"
        word_dict = ["cat", "cats", "and", "sand", "dog"]
        self.assertTrue(word_break(s, word_dict))

    def test_no_possible_segmentation(self):
        s = "catsandog"
        word_dict = ["cats", "dog", "sand", "and", "cat"]
        self.assertFalse(word_break(s, word_dict))

    def test_empty_string(self):
        # According to the implementation, empty string returns False
        self.assertFalse(word_break("", ["a", "b"]))

    def test_empty_dictionary(self):
        s = "anystring"
        word_dict = []
        self.assertFalse(word_break(s, word_dict))

    def test_string_equals_dictionary_word(self):
        s = "single"
        word_dict = ["single"]
        self.assertTrue(word_break(s, word_dict))

    def test_none_input_string(self):
        with self.assertRaises(TypeError):
            word_break(None, ["a"])

    def test_none_input_dictionary(self):
        with self.assertRaises(TypeError):
            word_break("test", None)

    def test_non_string_elements_in_dictionary(self):
        s = "123"
        word_dict = ["1", 2, "3"]
        # The function expects strings; non‑string elements should raise an exception
        with self.assertRaises(TypeError):
            word_break(s, word_dict)

    def test_large_input_performance(self):
        # Construct a long string that is a repetition of a known word
        base = "ab"
        s = base * 1000  # 2000 characters
        word_dict = ["a", "b", "ab"]
        # Should return True quickly; if recursion is not cached this could be slow
        self.assertTrue(word_break(s, word_dict))