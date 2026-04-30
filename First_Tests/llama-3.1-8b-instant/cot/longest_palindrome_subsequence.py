import functools


def longest_palindrome_subseq(s: str) -> int:
    @functools.lru_cache(None)
    def dp(i: int, j: int) -> int:
        if i > j:
            return 0
        if i == j:
            return 1
        if s[i] == s[j]:
            return 2 + dp(i + 1, j - 1)
        return max(dp(i + 1, j), dp(i, j - 1))

    return dp(0, len(s) - 1)

def longest_palindrome_subseq(s: str) -> int:
    @functools.lru_cache(None)
    def dp(i: int, j: int) -> int:
        if i > j:
            return 0
        if i == j:
            return 1
        if s[i] == s[j]:
            return 2 + dp(i + 1, j - 1)
        return max(dp(i + 1, j), dp(i, j - 1))

    return dp(0, len(s) - 1)

class TestLongestPalindromeSubseq(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(longest_palindrome_subseq("abba"), 4)

    def test_single_char(self):
        self.assertEqual(longest_palindrome_subseq("a"), 1)

    def test_empty_string(self):
        self.assertEqual(longest_palindrome_subseq(""), 0)

    def test_no_palindrome(self):
        self.assertEqual(longest_palindrome_subseq("abc"), 2)

    def test_palindrome_with_spaces(self):
        self.assertEqual(longest_palindrome_subseq("a b b a"), 4)

    def test_palindrome_with_numbers(self):
        self.assertEqual(longest_palindrome_subseq("a1b2b2a"), 4)

    def test_long_palindrome(self):
        self.assertEqual(longest_palindrome_subseq("abccba"), 6)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            longest_palindrome_subseq(123)

if __name__ == '__main__':
    unittest.main()