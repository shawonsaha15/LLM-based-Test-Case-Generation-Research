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
from typing import List

# Assume word_break is defined in the same module
# from your_module import word_break

class TestWordBreak(unittest.TestCase):
    def test_simple_positive(self):
        self.assertTrue(word_break("leetcode", ["leet", "code"]))

    def test_simple_negative(self):
        self.assertFalse(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))

    def test_multiple_segments(self):
        self.assertTrue(word_break("applepenapple", ["apple", "pen"]))

    def test_empty_string_empty_dict(self):
        self.assertFalse(word_break("", []))

    def test_empty_string_with_empty_word(self):
        self.assertTrue(word_break("", [""]))

    def test_exact_match(self):
        self.assertTrue(word_break("hello", ["hello"]))

    def test_overlapping_prefixes(self):
        self.assertTrue(word_break("aaaaaaa", ["a", "aa", "aaa"]))

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            word_break(123, ["1", "2", "3"])

    def test_none_word_dict(self):
        with self.assertRaises(TypeError):
            word_break("test", None)

if __name__ == "__main__":
    unittest.main()