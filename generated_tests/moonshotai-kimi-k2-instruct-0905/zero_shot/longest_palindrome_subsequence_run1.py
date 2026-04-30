import unittest

class TestLongestPalindromeSubseq(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(longest_palindrome_subseq(""), 0)

    def test_single_character(self):
        self.assertEqual(longest_palindrome_subseq("a"), 1)

    def test_all_same_characters(self):
        self.assertEqual(longest_palindrome_subseq("aaaa"), 4)

    def test_no_palindrome_subsequence(self):
        self.assertEqual(longest_palindrome_subseq("abcd"), 1)

    def test_palindrome_string(self):
        self.assertEqual(longest_palindrome_subseq("abba"), 4)

    def test_mixed_string(self):
        self.assertEqual(longest_palindrome_subseq("bbbab"), 4)

    def test_another_mixed_string(self):
        self.assertEqual(longest_palindrome_subseq("cbbd"), 2)

    def test_long_string(self):
        self.assertEqual(longest_palindrome_subseq("character"), 5)

    def test_two_characters_not_equal(self):
        self.assertEqual(longest_palindrome_subseq("ab"), 1)

    def test_two_characters_equal(self):
        self.assertEqual(longest_palindrome_subseq("aa"), 2)