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

class TestWordBreak(unittest.TestCase):

    def test_normal_input(self):
        self.assertTrue(word_break("leetcode", ["leet", "code"]))
        self.assertTrue(word_break("applepenapple", ["apple", "pen"]))
        self.assertFalse(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))

    def test_empty_string(self):
        self.assertTrue(word_break("", ["a", "b", "c"]))

    def test_empty_word_dict(self):
        self.assertFalse(word_break("a", []))

    def test_single_word(self):
        self.assertTrue(word_break("a", ["a"]))
        self.assertFalse(word_break("a", ["b"]))

    def test_long_string(self):
        self.assertTrue(word_break("a" * 100, ["a"]))

    def test_long_word_dict(self):
        self.assertTrue(word_break("a", ["a"] * 100))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            word_break(123, ["a", "b", "c"])
        with self.assertRaises(TypeError):
            word_break("a", 123)

if __name__ == '__main__':
    unittest.main()