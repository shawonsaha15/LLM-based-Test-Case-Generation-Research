import unittest


class TestLongestPalindromeSubseq(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(longest_palindrome_subseq(""), 0)

    def test_single_character(self):
        self.assertEqual(longest_palindrome_subseq("a"), 1)

    def test_all_same_characters(self):
        self.assertEqual(longest_palindrome_subseq("aaaa"), 4)

    def test_no_repeating_characters(self):
        self.assertEqual(longest_palindrome_subseq("abcd"), 1)

    def test_palindromic_string(self):
        self.assertEqual(longest_palindrome_subseq("abba"), 4)

    def test_mixed_string(self):
        self.assertEqual(longest_palindrome_subseq("bbbab"), 4)

    def test_complex_case(self):
        self.assertEqual(longest_palindrome_subseq("cbbd"), 2)

    def test_longer_string(self):
        self.assertEqual(longest_palindrome_subseq("agbdba"), 5)

    def test_two_characters_different(self):
        self.assertEqual(longest_palindrome_subseq("ab"), 1)

    def test_two_characters_same(self):
        self.assertEqual(longest_palindrome_subseq("aa"), 2)