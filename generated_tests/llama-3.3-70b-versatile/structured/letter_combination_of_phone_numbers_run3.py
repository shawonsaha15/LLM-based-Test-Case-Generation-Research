class TestLetterCombinations:
    def test_normal_case_single_digit(self):
        # Arrange
        digits = '2'
        expected_result = ['a', 'b', 'c']

        # Act
        result = letter_combinations(digits)

        # Assert
        assert result == expected_result

    def test_normal_case_multiple_digits(self):
        # Arrange
        digits = '23'
        expected_result = ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

        # Act
        result = letter_combinations(digits)

        # Assert
        assert result == expected_result

    def test_boundary_case_empty_string(self):
        # Arrange
        digits = ''
        expected_result = []

        # Act
        result = letter_combinations(digits)

        # Assert
        assert result == expected_result

    def test_boundary_case_single_letter(self):
        # Arrange
        digits = '2'
        expected_result = ['a', 'b', 'c']

        # Act
        result = letter_combinations(digits)

        # Assert
        assert result == expected_result

    def test_invalid_input_non_digit_string(self):
        # Arrange
        digits = 'abc'
        expected_result = []

        # Act
        result = letter_combinations(digits)

        # Assert
        assert result == expected_result

    def test_invalid_input_special_characters(self):
        # Arrange
        digits = '!@#'
        expected_result = []

        # Act
        result = letter_combinations(digits)

        # Assert
        assert result == expected_result

    def test_invalid_input_numbers_out_of_range(self):
        # Arrange
        digits = '01'
        expected_result = []

        # Act
        result = letter_combinations(digits)

        # Assert
        assert result == expected_result