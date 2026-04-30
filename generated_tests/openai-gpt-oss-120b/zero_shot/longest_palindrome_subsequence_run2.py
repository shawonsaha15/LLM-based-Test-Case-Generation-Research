import unittest

class TestLongestPalindromeSubseq(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(longest_palindrome_subseq(""), 0)

    def test_single_character(self):
        self.assertEqual(longest_palindrome_subseq("a"), 1)

    def test_two_characters_equal(self):
        self.assertEqual(longest_palindrome_subseq("aa"), 2)

    def test_two_characters_unequal(self):
        self.assertEqual(longest_palindrome_subseq("ab"), 1)

    def test_palindrome_string(self):
        self.assertEqual(longest_palindrome_subseq("racecar"), 7)
        self.assertEqual(longest_palindrome_subseq("madamimadam"), 11)

    def test_non_palindrome_string(self):
        self.assertEqual(longest_palindrome_subseq("character"), 5)  # "carac" or similar
        self.assertEqual(longest_palindrome_subseq("abcde"), 1)

    def test_mixed_string(self):
        self.assertEqual(longest_palindrome_subseq("bbbab"), 4)  # "bbbb"
        self.assertEqual(longest_palindrome_subseq("agbdba"), 5)  # "abdba"

    def test_long_string(self):
        s = "a" * 1000
        self.assertEqual(longest_palindrome_subseq(s), 1000)

    def test_complex_case(self):
        s = "forgeeksskeegfor"
        # The longest palindrome subsequence is "geeksskeeg" (length 10)
        self.assertEqual(longest_palindrome_subseq(s), 10)