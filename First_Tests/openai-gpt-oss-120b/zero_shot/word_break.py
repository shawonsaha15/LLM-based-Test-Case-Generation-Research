from typing import List
import functools


def word_break(s: str, word_dict: List[str]) -> bool:
    word_set = set(word_dict)

    @functools.lru_cache(None)
    def dfs(sub: str) -> bool:
        if sub in word_set:
            return True

        for i in range(1, len(sub)):
            if sub[:i] in word_set and dfs(sub[i:]):
                return True

        return False

    return dfs(s)

import unittest

class TestWordBreak(unittest.TestCase):
    def test_basic_true(self):
        self.assertTrue(word_break("leetcode", ["leet", "code"]))

    def test_basic_false(self):
        self.assertFalse(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))

    def test_multiple_segments(self):
        self.assertTrue(word_break("applepenapple", ["apple", "pen"]))

    def test_empty_string(self):
        self.assertFalse(word_break("", ["a", "b"]))

    def test_empty_dict(self):
        self.assertFalse(word_break("test", []))

    def test_single_char_true(self):
        self.assertTrue(word_break("a", ["a"]))

    def test_single_char_false(self):
        self.assertFalse(word_break("b", ["a"]))

    def test_repeated_words(self):
        self.assertTrue(word_break("aaaa", ["a", "aa"]))

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            word_break(None, ["a"])

    def test_non_list_dict(self):
        with self.assertRaises(TypeError):
            word_break("a", None)

if __name__ == "__main__":
    unittest.main()