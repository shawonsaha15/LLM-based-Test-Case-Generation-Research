import unittest

class TestWordBreak(unittest.TestCase):
    # 1. Normal expected behavior
    def test_basic_true(self):
        self.assertTrue(word_break("leetcode", ["leet", "code"]))
        self.assertTrue(word_break("applepenapple", ["apple", "pen"]))

    def test_basic_false(self):
        self.assertFalse(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))

    # 2. Edge cases
    def test_empty_string(self):
        # According to the implementation, empty string returns False
        self.assertFalse(word_break("", ["a", "b"]))

    def test_empty_dictionary(self):
        self.assertFalse(word_break("nonempty", []))

    def test_dictionary_contains_empty_string(self):
        # Empty string in dictionary does not help segment a non‑empty string
        self.assertFalse(word_break("abc", [""]))
        # Empty string can segment an empty input (still False per implementation)
        self.assertFalse(word_break("", [""]))

    def test_large_input(self):
        s = "a" * 1000
        word_dict = ["a", "aa", "aaa", "aaaa", "aaaaa"]
        self.assertTrue(word_break(s, word_dict))

    # 3. Invalid inputs
    def test_invalid_string_input(self):
        with self.assertRaises(TypeError):
            word_break(None, ["a"])

        with self.assertRaises(TypeError):
            word_break(123, ["a"])

    def test_invalid_dictionary_input(self):
        with self.assertRaises(TypeError):
            word_break("test", None)

        with self.assertRaises(TypeError):
            word_break("test", "notalist")

        # Non‑string elements inside the list should raise when set() tries to hash them
        with self.assertRaises(TypeError):
            word_break("test", [1, 2, 3])

    # 4. Re‑entrancy / caching sanity check
    def test_multiple_calls(self):
        # First call
        self.assertTrue(word_break("leetcode", ["leet", "code"]))
        # Second call with different data to ensure cache does not leak state
        self.assertFalse(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))