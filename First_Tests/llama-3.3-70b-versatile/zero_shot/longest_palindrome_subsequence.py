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

    def test_normal_case(self):
        self.assertEqual(longest_palindrome_subseq("bbbab"), 4)

    def test_single_character(self):
        self.assertEqual(longest_palindrome_subseq("a"), 1)

    def test_empty_string(self):
        self.assertEqual(longest_palindrome_subseq(""), 0)

    def test_two_characters(self):
        self.assertEqual(longest_palindrome_subseq("ab"), 1)

    def test_two_characters_palindrome(self):
        self.assertEqual(longest_palindrome_subseq("aa"), 2)

    def test_long_string(self):
        self.assertEqual(longest_palindrome_subseq("abcdefghhgfedcba"), 20)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            longest_palindrome_subseq(123)

    def test_invalid_input_type_list(self):
        with self.assertRaises(TypeError):
            longest_palindrome_subseq([1, 2, 3])

if __name__ == "__main__":
    unittest.main()