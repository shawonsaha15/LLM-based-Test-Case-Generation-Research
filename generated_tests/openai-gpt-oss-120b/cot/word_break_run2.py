import unittest

class TestWordBreak(unittest.TestCase):
    def test_basic_true(self):
        self.assertTrue(word_break("leetcode", ["leet", "code"]))

    def test_basic_false(self):
        self.assertFalse(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))

    def test_exact_match(self):
        # Checks that the base‑case `sub in word_set` is effective
        self.assertTrue(word_break("apple", ["apple", "pear"]))

    def test_multiple_segments(self):
        self.assertTrue(word_break("applepenapple", ["apple", "pen"]))

    def test_empty_string(self):
        # According to the implementation, empty string returns False
        self.assertFalse(word_break("", ["a", "b"]))

    def test_empty_dict(self):
        self.assertFalse(word_break("a", []))

    def test_none_input_string(self):
        with self.assertRaises(TypeError):
            word_break(None, ["a"])

    def test_none_input_dict(self):
        with self.assertRaises(TypeError):
            word_break("a", None)

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            word_break(123, ["1", "2", "3"])

    def test_non_list_dict_iterable(self):
        # The function uses `set(word_dict)`, so any iterable works
        self.assertTrue(word_break("abc", "abc"))  # dict as a string (iterable of chars)

    def test_large_input(self):
        s = "a" * 1000
        dict_words = ["a", "aa", "aaa"]
        self.assertTrue(word_break(s, dict_words))

    def test_split_at_first_character(self):
        self.assertTrue(word_break("ab", ["a", "b"]))

    def test_no_possible_split(self):
        self.assertFalse(word_break("abcd", ["ab", "abc"]))

    def test_repeated_word(self):
        self.assertTrue(word_break("aaaaaa", ["aa", "aaa"]))

    def test_word_dict_with_duplicates(self):
        self.assertTrue(word_break("catdog", ["cat", "dog", "cat", "dog"]))

    def test_word_dict_contains_empty_string(self):
        # Empty string in dict should not affect the result
        self.assertFalse(word_break("a", ["", "b"]))

    def test_word_dict_contains_substrings(self):
        self.assertTrue(word_break("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))

    def test_word_dict_all_characters(self):
        self.assertTrue(word_break("abcd", ["a", "b", "c", "d"]))

    def test_word_dict_long_word(self):
        self.assertTrue(word_break("longword", ["longword"]))
        self.assertFalse(word_break("longword", ["long", "word"]))  # cannot split without overlap

    def test_recursive_caching_effectiveness(self):
        # This case would cause exponential recursion without caching
        s = "a" * 20
        dict_words = ["a", "aa", "aaa", "aaaa"]
        self.assertTrue(word_break(s, dict_words))