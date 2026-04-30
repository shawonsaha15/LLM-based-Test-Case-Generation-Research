class TestLongestPalindromeSubseq:
    def test_normal_inputs(self):
        assert longest_palindrome_subseq("bbbab") == 4
        assert longest_palindrome_subseq("cbbd") == 2

    def test_empty_input(self):
        assert longest_palindrome_subseq("") == 0

    def test_single_character(self):
        assert longest_palindrome_subseq("a") == 1

    def test_two_characters(self):
        assert longest_palindrome_subseq("aa") == 2
        assert longest_palindrome_subseq("ab") == 1

    def test_large_input(self):
        assert longest_palindrome_subseq("a" * 1000) == 1000

    def test_invalid_input(self):
        try:
            longest_palindrome_subseq(123)
            assert False, "Expected TypeError"
        except TypeError:
            pass

    def test_none_input(self):
        try:
            longest_palindrome_subseq(None)
            assert False, "Expected TypeError"
        except TypeError:
            pass

    def test_mutation_test_cases(self):
        assert longest_palindrome_subseq("abba") == 4
        assert longest_palindrome_subseq("abcba") == 5
        assert longest_palindrome_subseq("abccba") == 6