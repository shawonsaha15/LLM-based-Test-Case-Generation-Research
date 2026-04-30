class TestGeneratePascalsTriangle:
    def test_normal_case(self):
        # Arrange
        num_rows = 5
        expected_result = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

        # Act
        result = generate_pascals_triangle(num_rows)

        # Assert
        assert result == expected_result

    def test_boundary_case_zero_rows(self):
        # Arrange
        num_rows = 0
        expected_result = []

        # Act
        result = generate_pascals_triangle(num_rows)

        # Assert
        assert result == expected_result

    def test_boundary_case_one_row(self):
        # Arrange
        num_rows = 1
        expected_result = [[1]]

        # Act
        result = generate_pascals_triangle(num_rows)

        # Assert
        assert result == expected_result

    def test_invalid_input_negative_rows(self):
        # Arrange
        num_rows = -1
        expected_result = []

        # Act and Assert
        try:
            result = generate_pascals_triangle(num_rows)
            assert False, "Expected ValueError to be raised"
        except ValueError:
            assert True

    def test_invalid_input_non_integer_rows(self):
        # Arrange
        num_rows = 5.5

        # Act and Assert
        try:
            result = generate_pascals_triangle(num_rows)
            assert False, "Expected TypeError to be raised"
        except TypeError:
            assert True

    def test_large_input(self):
        # Arrange
        num_rows = 10
        expected_result = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], 
                            [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], 
                            [1, 7, 21, 35, 35, 21, 7, 1], [1, 8, 28, 56, 70, 56, 28, 8, 1], 
                            [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]]

        # Act
        result = generate_pascals_triangle(num_rows)

        # Assert
        assert result == expected_result