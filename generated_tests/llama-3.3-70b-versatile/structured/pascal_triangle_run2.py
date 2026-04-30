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
        num_rows = -5

        # Act and Assert
        try:
            generate_pascals_triangle(num_rows)
            assert False, "Expected ValueError for negative input"
        except ValueError:
            assert True

    def test_invalid_input_non_integer_rows(self):
        # Arrange
        num_rows = 5.5

        # Act and Assert
        try:
            generate_pascals_triangle(num_rows)
            assert False, "Expected TypeError for non-integer input"
        except TypeError:
            assert True