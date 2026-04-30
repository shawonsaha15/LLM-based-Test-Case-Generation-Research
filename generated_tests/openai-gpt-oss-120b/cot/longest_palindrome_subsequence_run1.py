import unittest

class TestLongestPalindromeSubseq(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(longest_palindrome_subseq(""), 0)

    def test_single_character(self):
        self.assertEqual(longest_palindrome_subseq("a"), 1)

    def test_all_same_characters(self):
        self.assertEqual(longest_palindrome_subseq("aaaaaa"), 6)

    def test_no_palindromic_subseq_longer_than_one(self):
        self.assertEqual(longest_palindrome_subseq("abcde"), 1)

    def test_palindrome_string(self):
        self.assertEqual(longest_palindrome_subseq("racecar"), 7)

    def test_mixed_example(self):
        # Example from classic LPS problems
        self.assertEqual(longest_palindrome_subseq("bbbab"), 4)

    def test_another_mixed_example(self):
        self.assertEqual(longest_palindrome_subseq("character"), 5)

    def test_unicode_characters(self):
        self.assertEqual(longest_palindrome_subseq("åßçßå"), 5)  # whole string is a palindrome

    def test_large_input_all_same(self):
        large_str = "a" * 1000
        self.assertEqual(longest_palindrome_subseq(large_str), 1000)

    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            longest_palindrome_subseq(None)

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            longest_palindrome_subseq(12345)
        with self.assertRaises(TypeError):
            longest_palindrome_subseq(['a', 'b', 'c'])