class TestLetterCombinations:
    def test_normal_case(self):
        # Arrange
        digits = "23"
        expected_result = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

        # Act
        result = letter_combinations(digits)

        # Assert
        assert result == expected_result

    def test_single_digit(self):
        # Arrange
        digits = "2"
        expected_result = ["a", "b", "c"]

        # Act
        result = letter_combinations(digits)

        # Assert
        assert result == expected_result

    def test_multiple_digits(self):
        # Arrange
        digits = "234"
        expected_result = [
            "adg", "adh", "adi", "aeg", "aeh", "aei", "afg", "afh", "afi",
            "bdg", "bdh", "bdi", "beg", "beh", "bei", "bfg", "bfh", "bfi",
            "cdg", "cdh", "cdi", "ceg", "ceh", "cei", "cfg", "cfh", "cfi"
        ]

        # Act
        result = letter_combinations(digits)

        # Assert
        assert result == expected_result

    def test_empty_input(self):
        # Arrange
        digits = ""
        expected_result = []

        # Act
        result = letter_combinations(digits)

        # Assert
        assert result == expected_result

    def test_invalid_input(self):
        # Arrange
        digits = "10"
        expected_result = []

        # Act
        result = letter_combinations(digits)

        # Assert
        assert result == expected_result

    def test_zero_input(self):
        # Arrange
        digits = "0"
        expected_result = []

        # Act
        result = letter_combinations(digits)

        # Assert
        assert result == expected_result

    def test_non_numeric_input(self):
        # Arrange
        digits = "a"
        expected_result = []

        # Act
        result = letter_combinations(digits)

        # Assert
        assert result == expected_result