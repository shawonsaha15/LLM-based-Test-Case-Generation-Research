import functools


def longest_palindrome_subseq(s: str) -> int:
    @functools.lru_cache(None)
    def dp(i: int, j: int) -> int:
        if i > j:
            return 0
        if i == j:
            return 1
        if s[i] == s[j]:
            return 2 + dp(i + 1, j - 1)
        return max(dp(i + 1, j), dp(i, j - 1))

    return dp(0, len(s) - 1)

import unittest

class TestLongestPalindromeSubseq(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(longest_palindrome_subseq("bbbab"), 4)
        self.assertEqual(longest_palindrome_subseq("cbbd"), 2)

    def test_edge(self):
        self.assertEqual(longest_palindrome_subseq(""), 0)
        self.assertEqual(longest_palindrome_subseq("a"), 1)
        self.assertEqual(longest_palindrome_subseq("ab"), 1)

    def test_symmetric(self):
        self.assertEqual(longest_palindrome_subseq("abba"), 4)
        self.assertEqual(longest_palindrome_subseq("abcba"), 5)

if __name__ == "__main__":
    unittest.main()