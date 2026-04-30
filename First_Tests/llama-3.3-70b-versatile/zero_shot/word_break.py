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

    def test_normal_case(self):
        self.assertTrue(word_break("leetcode", ["leet", "code"]))

    def test_normal_case_2(self):
        self.assertTrue(word_break("applepenapple", ["apple", "pen"]))

    def test_edge_case_empty_string(self):
        self.assertTrue(word_break("", ["a"]))

    def test_edge_case_single_word(self):
        self.assertTrue(word_break("a", ["a"]))

    def test_edge_case_no_words(self):
        self.assertFalse(word_break("a", []))

    def test_invalid_case_no_break(self):
        self.assertFalse(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))

    def test_invalid_case_no_break_2(self):
        self.assertFalse(word_break("aaaaaaa", ["aaaa", "aa"]))

    def test_invalid_case_empty_word_dict(self):
        self.assertFalse(word_break("a", []))

    def test_invalid_case_empty_string_and_empty_word_dict(self):
        self.assertTrue(word_break("", []))

if __name__ == "__main__":
    unittest.main()