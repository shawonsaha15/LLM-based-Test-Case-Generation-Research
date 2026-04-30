import unittest

class TestLongestPalindromeSubseq(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(longest_palindrome_subseq(""), 0)

    def test_single_character(self):
        self.assertEqual(longest_palindrome_subseq("a"), 1)

    def test_all_same_characters(self):
        self.assertEqual(longest_palindrome_subseq("aaaaa"), 5)

    def test_no_repeating_characters(self):
        self.assertEqual(longest_palindrome_subseq("abcde"), 1)

    def test_simple_palindrome(self):
        self.assertEqual(longest_palindrome_subseq("racecar"), 7)

    def test_known_examples(self):
        # Example from LeetCode
        self.assertEqual(longest_palindrome_subseq("bbbab"), 4)
        self.assertEqual(longest_palindrome_subseq("cbbd"), 2)
        self.assertEqual(longest_palindrome_subseq("character"), 5)

    def test_mixed_case(self):
        self.assertEqual(longest_palindrome_subseq("AaBbAa"), 4)  # "AaAa" or "BbBb"

    def test_with_spaces_and_punctuation(self):
        self.assertEqual(longest_palindrome_subseq("A man, a plan, a canal: Panama"), 7)  # "anana" or similar

    def test_long_string(self):
        s = "agbdba" * 10  # repeats of a known pattern
        # For "agbdba", LPS length is 5 ("abdba")
        self.assertEqual(longest_palindrome_subseq(s), 5 * 10)