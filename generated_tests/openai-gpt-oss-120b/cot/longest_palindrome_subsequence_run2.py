import unittest

class TestLongestPalindromeSubseq(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(longest_palindrome_subseq(""), 0)

    def test_single_character(self):
        self.assertEqual(longest_palindrome_subseq("a"), 1)

    def test_all_same_characters(self):
        s = "aaaaaa"
        self.assertEqual(longest_palindrome_subseq(s), len(s))

    def test_no_repeating_characters(self):
        self.assertEqual(longest_palindrome_subseq("abcde"), 1)

    def test_even_length_palindrome(self):
        s = "abccba"
        self.assertEqual(longest_palindrome_subseq(s), len(s))

    def test_odd_length_palindrome(self):
        s = "racecar"
        self.assertEqual(longest_palindrome_subseq(s), len(s))

    def test_mixed_example_1(self):
        # Classic example: longest palindrome subsequence length is 4 ("bbbb")
        self.assertEqual(longest_palindrome_subseq("bbbab"), 4)

    def test_mixed_example_2(self):
        # Example: "agbdba" -> "abdba" length 5
        self.assertEqual(longest_palindrome_subseq("agbdba"), 5)

    def test_unicode_characters(self):
        s = "あいあ"
        # The longest palindrome subsequence is "あいあ" (length 3)
        self.assertEqual(longest_palindrome_subseq(s), 3)

    def test_longer_string(self):
        s = "character"
        # Known longest palindrome subsequence length is 5 ("carac")
        self.assertEqual(longest_palindrome_subseq(s), 5)

    def test_none_input_raises_type_error(self):
        with self.assertRaises(TypeError):
            longest_palindrome_subseq(None)

    def test_non_string_input_raises_type_error(self):
        with self.assertRaises(TypeError):
            longest_palindrome_subseq(12345)