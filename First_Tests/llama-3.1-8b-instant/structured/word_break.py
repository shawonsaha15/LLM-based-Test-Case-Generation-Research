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
from your_module import word_break  # Replace 'your_module' with the actual module name

class TestWordBreak(unittest.TestCase):

    def test_normal_cases(self):
        self.assertTrue(word_break("leetcode", ["leet", "code"]))
        self.assertTrue(word_break("applepenapple", ["apple", "pen"]))
        self.assertTrue(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))

    def test_edge_cases(self):
        self.assertFalse(word_break("leetcode", ["leet", "le"]))
        self.assertFalse(word_break("", ["leet", "code"]))
        self.assertFalse(word_break("a", ["leet", "code"]))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            word_break(123, ["leet", "code"])
        with self.assertRaises(TypeError):
            word_break("leetcode", 123)
        with self.assertRaises(TypeError):
            word_break("leetcode", ["leet", 123])

if __name__ == "__main__":
    unittest.main()