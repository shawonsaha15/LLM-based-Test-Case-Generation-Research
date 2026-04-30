import unittest

class TestLongestPalindromeSubseq(unittest.TestCase):
    def test_normal_cases(self):
        # Arrange
        cases = [
            ("bbbab", 4),          # "bbbb"
            ("cbbd", 2),           # "bb"
            ("agbdba", 5),         # "abdba"
            ("character", 5),      # "carac"
        ]
        for s, expected in cases:
            with self.subTest(s=s):
                # Act
                result = longest_palindrome_subseq(s)
                # Assert
                self.assertEqual(result, expected)

    def test_boundary_cases(self):
        # Arrange & Act & Assert for empty string
        self.assertEqual(longest_palindrome_subseq(""), 0)

        # Arrange & Act & Assert for single character
        self.assertEqual(longest_palindrome_subseq("a"), 1)

        # Arrange & Act & Assert for all identical characters
        s = "aaaaaa"
        self.assertEqual(longest_palindrome_subseq(s), len(s))

        # Arrange & Act & Assert for a full palindrome (even length)
        self.assertEqual(longest_palindrome_subseq("abccba"), 6)

        # Arrange & Act & Assert for a full palindrome (odd length)
        self.assertEqual(longest_palindrome_subseq("racecar"), 7)

    def test_invalid_inputs(self):
        # Arrange
        invalid_inputs = [None, 123, 45.6, ["a", "b"], {"s": "abc"}]
        for inval in invalid_inputs:
            with self.subTest(inval=inval):
                # Act & Assert
                with self.assertRaises(Exception):
                    longest_palindrome_subseq(inval)