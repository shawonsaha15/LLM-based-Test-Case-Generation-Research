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
import functools

class TestLongestPalindromeSubseq(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(longest_palindrome_subseq("abba"), 4)
        self.assertEqual(longest_palindrome_subseq("racecar"), 7)
        self.assertEqual(longest_palindrome_subseq("abcba"), 6)

    def test_edge_case_empty_string(self):
        self.assertEqual(longest_palindrome_subseq(""), 0)

    def test_edge_case_single_character(self):
        self.assertEqual(longest_palindrome_subseq("a"), 1)

    def test_edge_case_two_characters(self):
        self.assertEqual(longest_palindrome_subseq("ab"), 2)

    def test_invalid_input_not_string(self):
        with self.assertRaises(TypeError):
            longest_palindrome_subseq(123)

    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            longest_palindrome_subseq(None)

    def test_invalid_input_non_string_sequence(self):
        with self.assertRaises(TypeError):
            longest_palindrome_subseq([1, 2, 3])

    def test_invalid_input_string_with_non_ascii_characters(self):
        self.assertEqual(longest_palindrome_subseq("ábcba"), 6)

    def test_invalid_input_string_with_whitespace(self):
        self.assertEqual(longest_palindrome_subseq("a b cba"), 6)

if __name__ == "__main__":
    unittest.main()