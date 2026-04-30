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
    def test_valid_word_break(self):
        self.assertTrue(word_break("leetcode", ["leet", "code"]))

    def test_invalid_word_break(self):
        self.assertFalse(word_break("leetcode", ["leet", "go"]))

    def test_empty_string(self):
        self.assertTrue(word_break("", ["a", "b"]))

    def test_single_word(self):
        self.assertTrue(word_break("a", ["a"]))

    def test_multiple_words(self):
        self.assertTrue(word_break("applepenapple", ["apple", "pen"]))

    def test_no_words(self):
        self.assertFalse(word_break("applepenapple", []))

if __name__ == "__main__":
    unittest.main()