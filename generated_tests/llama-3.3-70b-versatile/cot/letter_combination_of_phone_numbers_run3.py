class TestLetterCombinations:
    def test_empty_string(self):
        assert letter_combinations("") == []

    def test_single_digit(self):
        assert letter_combinations("2") == ["a", "b", "c"]

    def test_multiple_digits(self):
        assert letter_combinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

    def test_large_input(self):
        result = letter_combinations("234")
        assert len(result) == 27
        assert all(len(combination) == 3 for combination in result)

    def test_invalid_input_none(self):
        assert letter_combinations(None) == []

    def test_invalid_input_non_string(self):
        try:
            letter_combinations(123)
            assert False, "Expected TypeError"
        except TypeError:
            pass

    def test_invalid_input_non_digit_string(self):
        try:
            letter_combinations("abc")
            assert False, "Expected ValueError or incorrect result"
        except ValueError:
            pass
        else:
            assert letter_combinations("abc") == [], "Expected empty list or ValueError"

    def test_edge_case_zero(self):
        try:
            letter_combinations("0")
            assert False, "Expected KeyError or incorrect result"
        except KeyError:
            pass
        else:
            assert letter_combinations("0") == [], "Expected empty list or KeyError"

    def test_edge_case_large_digits(self):
        try:
            letter_combinations("1234567890")
            assert False, "Expected KeyError or incorrect result"
        except KeyError:
            pass
        else:
            assert letter_combinations("1234567890") == [], "Expected empty list or KeyError"