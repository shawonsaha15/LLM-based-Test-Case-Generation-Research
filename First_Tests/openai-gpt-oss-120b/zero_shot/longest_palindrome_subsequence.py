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

class TestLongest_palindrome_subseq(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(longest_palindrome_subseq(""), 0)

    def test_single_character(self):
        self.assertEqual(longest_palindrome_subseq("a"), 1)

    def test_typical_cases(self):
        self.assertEqual(longest_palindrome_subseq("bbbab"), 4)
        self.assertEqual(longest_palindrome_subseq("cbbd"), 2)

    def test_palindrome_string(self):
        self.assertEqual(longest_palindrome_subseq("racecar"), 7)

    def test_all_same_characters(self):
        self.assertEqual(longest_palindrome_subseq("aaaaa"), 5)

    def test_unicode_characters(self):
        self.assertEqual(longest_palindrome_subseq("あいあ"), 3)
        self.assertEqual(longest_palindrome_subseq("😀ab😀"), 3)

    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            longest_palindrome_subseq(None)

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            longest_palindrome_subseq(12345)

if __name__ == "__main__":
    unittest.main()