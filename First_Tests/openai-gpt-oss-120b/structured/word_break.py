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
    def test_normal_cases(self):
        self.assertTrue(word_break("leetcode", ["leet", "code"]))
        self.assertTrue(word_break("applepenapple", ["apple", "pen"]))
        self.assertFalse(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))

    def test_edge_cases(self):
        self.assertFalse(word_break("", []))
        self.assertFalse(word_break("", ["a"]))
        self.assertFalse(word_break("a", []))
        self.assertTrue(word_break("a", ["a"]))
        self.assertFalse(word_break("ab", ["a"]))
        self.assertTrue(word_break("ab", ["a", "b"]))
        self.assertTrue(word_break("aaaa", ["a", "aa", "aaa"]))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            word_break(None, ["a"])
        with self.assertRaises(TypeError):
            word_break("a", None)
        with self.assertRaises(TypeError):
            word_break(123, ["1", "2", "3"])
        with self.assertRaises(TypeError):
            word_break("abc", 5)

if __name__ == "__main__":
    unittest.main()