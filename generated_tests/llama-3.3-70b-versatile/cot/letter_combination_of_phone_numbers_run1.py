class TestLetterCombinations:
    def test_empty_input(self):
        assert letter_combinations("") == []

    def test_single_digit(self):
        assert letter_combinations("2") == ["a", "b", "c"]

    def test_multiple_digits(self):
        assert letter_combinations("23") == [
            "ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"
        ]

    def test_large_input(self):
        assert len(letter_combinations("234")) == 27

    def test_invalid_input(self):
        assert letter_combinations("01") == []

    def test_zero_input(self):
        assert letter_combinations("0") == []

    def test_none_input(self):
        assert letter_combinations(None) == []

    def test_non_digit_input(self):
        assert letter_combinations("abc") == []

    def test_large_non_digit_input(self):
        assert letter_combinations("abcdefghijklmnopqrstuvwxyz") == []