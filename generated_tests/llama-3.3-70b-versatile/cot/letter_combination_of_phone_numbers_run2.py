class TestLetterCombinations:
    def test_empty_input(self):
        assert letter_combinations("") == []

    def test_single_digit(self):
        assert letter_combinations("2") == ["a", "b", "c"]

    def test_multiple_digits(self):
        assert letter_combinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

    def test_invalid_input(self):
        with pytest.raises(KeyError):
            letter_combinations("01")

    def test_large_input(self):
        result = letter_combinations("234")
        assert len(result) == 3 * 3 * 3
        for combination in result:
            assert len(combination) == 3

    def test_zero_input(self):
        with pytest.raises(KeyError):
            letter_combinations("0")

    def test_none_input(self):
        with pytest.raises(AttributeError):
            letter_combinations(None)

    def test_non_string_input(self):
        with pytest.raises(AttributeError):
            letter_combinations(123)

    def test_non_digit_string_input(self):
        with pytest.raises(KeyError):
            letter_combinations("abc")