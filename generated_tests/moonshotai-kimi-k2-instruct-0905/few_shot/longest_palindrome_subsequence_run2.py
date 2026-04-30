class TestLongestPalindromeSubseq(unittest.TestCase):
    def test_empty_string(self):
        result = longest_palindrome_subseq("")
        self.assertEqual(result, 0)

    def test_single_character(self):
        result = longest_palindrome_subseq("a")
        self.assertEqual(result, 1)

    def test_all_same_characters(self):
        result = longest_palindrome_subseq("aaaa")
        self.assertEqual(result, 4)

    def test_no_palindrome_subsequence(self):
        result = longest_palindrome_subseq("abcd")
        self.assertEqual(result, 1)

    def test_mixed_palindrome_subsequence(self):
        result = longest_palindrome_subseq("bbbab")
        self.assertEqual(result, 4)

    def test_palindrome_subsequence_scattered(self):
        result = longest_palindrome_subseq("cbbd")
        self.assertEqual(result, 2)

    def test_longer_string(self):
        result = longest_palindrome_subseq("agbdba")
        self.assertEqual(result, 5)