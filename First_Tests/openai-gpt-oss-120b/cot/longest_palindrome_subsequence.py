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
    def test_empty_string(self):
        self.assertEqual(longest_palindrome_subseq(""), 0)

    def test_single_character(self):
        self.assertEqual(longest_palindrome_subseq("a"), 1)

    def test_all_same_characters(self):
        s = "aaaaaa"
        self.assertEqual(longest_palindrome_subseq(s), len(s))

    def test_palindrome_string(self):
        s = "racecar"
        self.assertEqual(longest_palindrome_subseq(s), len(s))

    def test_example_bbbab(self):
        self.assertEqual(longest_palindrome_subseq("bbbab"), 4)

    def test_example_cbbd(self):
        self.assertEqual(longest_palindrome_subseq("cbbd"), 2)

    def test_character(self):
        self.assertEqual(longest_palindrome_subseq("character"), 5)

    def test_case_sensitivity(self):
        self.assertEqual(longest_palindrome_subseq("Aa"), 1)

    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            longest_palindrome_subseq(None)

    def test_invalid_input_int(self):
        with self.assertRaises(TypeError):
            longest_palindrome_subseq(12345)

if __name__ == "__main__":
    unittest.main()