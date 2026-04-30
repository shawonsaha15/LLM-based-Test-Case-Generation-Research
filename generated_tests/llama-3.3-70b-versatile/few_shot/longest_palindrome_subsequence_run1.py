class TestLongestPalindromeSubseq(unittest.TestCase):
    def test_single_character(self):
        result = longest_palindrome_subseq("a")
        self.assertEqual(result, 1)

    def test_two_characters_same(self):
        result = longest_palindrome_subseq("aa")
        self.assertEqual(result, 2)

    def test_two_characters_different(self):
        result = longest_palindrome_subseq("ab")
        self.assertEqual(result, 1)

    def test_longer_palindrome(self):
        result = longest_palindrome_subseq("abcba")
        self.assertEqual(result, 5)

    def test_longer_not_palindrome(self):
        result = longest_palindrome_subseq("abcdefgh")
        self.assertEqual(result, 1)

    def test_empty_string(self):
        result = longest_palindrome_subseq("")
        self.assertEqual(result, 0)

    def test_long_palindrome(self):
        result = longest_palindrome_subseq("madam")
        self.assertEqual(result, 5)