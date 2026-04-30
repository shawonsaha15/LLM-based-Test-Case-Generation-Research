class TestLongestPalindromeSubseq(unittest.TestCase):
    def test_single_character(self):
        self.assertEqual(longest_palindrome_subseq('a'), 1)

    def test_two_characters_same(self):
        self.assertEqual(longest_palindrome_subseq('aa'), 2)

    def test_two_characters_different(self):
        self.assertEqual(longest_palindrome_subseq('ab'), 1)

    def test_palindrome(self):
        self.assertEqual(longest_palindrome_subseq('aba'), 3)

    def test_not_palindrome(self):
        self.assertEqual(longest_palindrome_subseq('abc'), 1)

    def test_longer_string(self):
        self.assertEqual(longest_palindrome_subseq('banana'), 3)

    def test_empty_string(self):
        self.assertEqual(longest_palindrome_subseq(''), 0)