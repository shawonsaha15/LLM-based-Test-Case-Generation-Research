import unittest

class TestLongestPalindromeSubseq(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(longest_palindrome_subseq(""), 0)

    def test_single_character(self):
        self.assertEqual(longest_palindrome_subseq("a"), 1)

    def test_all_same_characters(self):
        self.assertEqual(longest_palindrome_subseq("aaaaaa"), 6)

    def test_simple_palindrome(self):
        self.assertEqual(longest_palindrome_subseq("racecar"), 7)

    def test_non_palindrome_short(self):
        self.assertEqual(longest_palindrome_subseq("ab"), 1)

    def test_mixed_string_example1(self):
        # Example from LeetCode: "bbbab" -> "bbbb" length 4
        self.assertEqual(longest_palindrome_subseq("bbbab"), 4)

    def test_mixed_string_example2(self):
        # Example from LeetCode: "cbbd" -> "bb" length 2
        self.assertEqual(longest_palindrome_subseq("cbbd"), 2)

    def test_longer_mixed_string(self):
        # "agbdba" -> "abdba" length 5
        self.assertEqual(longest_palindrome_subseq("agbdba"), 5)

    def test_string_with_spaces_and_punctuation(self):
        # Spaces and punctuation are treated as normal characters
        self.assertEqual(longest_palindrome_subseq("A man, a plan, a canal: Panama"), 7)

    def test_unicode_characters(self):
        # Unicode characters should be handled correctly
        self.assertEqual(longest_palindrome_subseq("😀abcb😀"), 5)  # "😀bcb😀"