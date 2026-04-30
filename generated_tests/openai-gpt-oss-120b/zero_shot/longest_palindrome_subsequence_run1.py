import unittest

class LongestPalindromeSubseqTests(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(longest_palindrome_subseq(""), 0)

    def test_single_character(self):
        self.assertEqual(longest_palindrome_subseq("a"), 1)

    def test_two_same_characters(self):
        self.assertEqual(longest_palindrome_subseq("aa"), 2)

    def test_two_different_characters(self):
        self.assertEqual(longest_palindrome_subseq("ab"), 1)

    def test_already_palindrome(self):
        s = "racecar"
        self.assertEqual(longest_palindrome_subseq(s), len(s))

    def test_known_example(self):
        # Classic LeetCode example: "bbbab" -> 4 ("bbbb")
        self.assertEqual(longest_palindrome_subseq("bbbab"), 4)

    def test_complex_string(self):
        # "character" -> 5 ("carac")
        self.assertEqual(longest_palindrome_subseq("character"), 5)

    def test_all_same_characters_large(self):
        s = "a" * 1000
        self.assertEqual(longest_palindrome_subseq(s), 1000)

    def test_unicode_characters(self):
        s = "あいあ"
        # The longest palindrome subsequence is "ああ" (length 2)
        self.assertEqual(longest_palindrome_subseq(s), 2)

    def test_random_small_strings_bruteforce(self):
        # Verify against a brute‑force implementation for strings up to length 6
        from itertools import combinations

        def brute_force_lps(t: str) -> int:
            n = len(t)
            best = 0
            for r in range(1, n + 1):
                for idxs in combinations(range(n), r):
                    subseq = "".join(t[i] for i in idxs)
                    if subseq == subseq[::-1]:
                        best = max(best, r)
            return best

        test_cases = ["", "a", "ab", "aa", "abc", "aba", "abca", "abcdba", "abcbda"]
        for s in test_cases:
            with self.subTest(s=s):
                self.assertEqual(longest_palindrome_subseq(s), brute_force_lps(s))