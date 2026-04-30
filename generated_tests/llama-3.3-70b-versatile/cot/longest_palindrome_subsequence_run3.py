class TestLongestPalindromeSubseq:
    def test_normal_cases(self):
        assert longest_palindrome_subseq("bbbab") == 4
        assert longest_palindrome_subseq("cbbd") == 2

    def test_empty_string(self):
        assert longest_palindrome_subseq("") == 0

    def test_single_character(self):
        assert longest_palindrome_subseq("a") == 1

    def test_two_characters(self):
        assert longest_palindrome_subseq("aa") == 2
        assert longest_palindrome_subseq("ab") == 1

    def test_large_string(self):
        assert longest_palindrome_subseq("a" * 100) == 100

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

    def test_non_string_input(self):
        try:
            longest_palindrome_subseq([1, 2, 3])
            assert False, "Expected TypeError"
        except TypeError:
            pass