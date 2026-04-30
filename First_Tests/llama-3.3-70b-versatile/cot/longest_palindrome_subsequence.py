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

    def test_normal_inputs(self):
        self.assertEqual(longest_palindrome_subseq("bbbab"), 4)
        self.assertEqual(longest_palindrome_subseq("cbbd"), 2)
        self.assertEqual(longest_palindrome_subseq("a"), 1)
        self.assertEqual(longest_palindrome_subseq("ab"), 1)
        self.assertEqual(longest_palindrome_subseq("aba"), 3)

    def test_edge_cases(self):
        self.assertEqual(longest_palindrome_subseq(""), 0)
        self.assertEqual(longest_palindrome_subseq("a" * 100), 100)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            longest_palindrome_subseq(123)
        with self.assertRaises(TypeError):
            longest_palindrome_subseq(None)

if __name__ == '__main__':
    unittest.main()