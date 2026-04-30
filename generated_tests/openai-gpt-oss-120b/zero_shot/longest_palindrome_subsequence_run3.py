import unittest

class TestLongestPalindromeSubseq(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(longest_palindrome_subseq(""), 0)

    def test_single_character(self):
        self.assertEqual(longest_palindrome_subseq("a"), 1)

    def test_all_same_characters(self):
        self.assertEqual(longest_palindrome_subseq("aaaaa"), 5)

    def test_simple_palindrome(self):
        self.assertEqual(longest_palindrome_subseq("racecar"), 7)

    def test_non_palindrome(self):
        self.assertEqual(longest_palindrome_subseq("abcde"), 1)

    def test_mixed_string(self):
        # "bbbab" -> longest palindrome subsequence is "bbbb" of length 4
        self.assertEqual(longest_palindrome_subseq("bbbab"), 4)

    def test_another_mixed_string(self):
        # "agbdba" -> longest palindrome subsequence is "abdba" of length 5
        self.assertEqual(longest_palindrome_subseq("agbdba"), 5)

    def test_long_string(self):
        s = "characteristic"
        # Known LPS length for this string is 7 ("caracra" or similar)
        self.assertEqual(longest_palindrome_subseq(s), 7)