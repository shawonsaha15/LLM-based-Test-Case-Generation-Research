import unittest

class TestLongestPalindromeSubseq(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(longest_palindrome_subseq(""), 0)

    def test_single_character(self):
        self.assertEqual(longest_palindrome_subseq("a"), 1)

    def test_all_same_characters(self):
        self.assertEqual(longest_palindrome_subseq("aaaaaa"), 6)

    def test_no_repeating_characters(self):
        self.assertEqual(longest_palindrome_subseq("abcde"), 1)

    def test_palindrome_string(self):
        self.assertEqual(longest_palindrome_subseq("racecar"), 7)

    def test_mixed_examples(self):
        # Example from classic DP problems
        self.assertEqual(longest_palindrome_subseq("bbbab"), 4)   # "bbbb"
        self.assertEqual(longest_palindrome_subseq("character"), 5)  # "carac"
        self.assertEqual(longest_palindrome_subseq("agbdba"), 5)  # "abdba"

    def test_long_string(self):
        s = "a" * 1000 + "b" * 1000
        # The longest palindrome subsequence will be the longer block of identical characters
        self.assertEqual(longest_palindrome_subseq(s), 1000)

    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            longest_palindrome_subseq(None)

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            longest_palindrome_subseq(12345)
        with self.assertRaises(TypeError):
            longest_palindrome_subseq(['a', 'b', 'c'])