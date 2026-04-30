import unittest

class TestLongestPalindromeSubseq(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(longest_palindrome_subseq(""), 0)

    def test_single_character(self):
        self.assertEqual(longest_palindrome_subseq("a"), 1)

    def test_all_same_characters(self):
        s = "aaaaaa"
        self.assertEqual(longest_palindrome_subseq(s), len(s))

    def test_palindrome_string(self):
        s = "racecar"
        self.assertEqual(longest_palindrome_subseq(s), len(s))

    def test_two_different_characters(self):
        self.assertEqual(longest_palindrome_subseq("ab"), 1)

    def test_mixed_string_example(self):
        # Known example: "bbbab" -> LPS length 4 ("bbbb")
        self.assertEqual(longest_palindrome_subseq("bbbab"), 4)

    def test_another_known_example(self):
        # Known example: "agbdba" -> LPS length 5 ("abdba")
        self.assertEqual(longest_palindrome_subseq("agbdba"), 5)

    def test_longer_string(self):
        # Known example: "forgeeksskeegfor" -> LPS length 10 ("geeksskeeg")
        self.assertEqual(longest_palindrome_subseq("forgeeksskeegfor"), 10)

    def test_unicode_characters(self):
        # Emoji and non‑ASCII characters should be handled correctly
        s = "😀abcb😀"
        # The longest palindrome subsequence is "😀bcb😀" (length 5)
        self.assertEqual(longest_palindrome_subseq(s), 5)