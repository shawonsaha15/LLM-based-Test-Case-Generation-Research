class TestGeneratePascalsTriangle:
    def test_normal_case(self):
        # Arrange
        num_rows = 5

        # Act
        result = generate_pascals_triangle(num_rows)

        # Assert
        expected_result = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        assert result == expected_result

    def test_single_row(self):
        # Arrange
        num_rows = 1

        # Act
        result = generate_pascals_triangle(num_rows)

        # Assert
        expected_result = [[1]]
        assert result == expected_result

    def test_zero_rows(self):
        # Arrange
        num_rows = 0

        # Act
        result = generate_pascals_triangle(num_rows)

        # Assert
        expected_result = []
        assert result == expected_result

    def test_negative_rows(self):
        # Arrange
        num_rows = -1

        # Act and Assert
        try:
            generate_pascals_triangle(num_rows)
            assert False, "Expected an exception for negative input"
        except Exception:
            assert True

    def test_non_integer_rows(self):
        # Arrange
        num_rows = 2.5

        # Act and Assert
        try:
            generate_pascals_triangle(num_rows)
            assert False, "Expected an exception for non-integer input"
        except Exception:
            assert True

    def test_large_number_of_rows(self):
        # Arrange
        num_rows = 10

        # Act
        result = generate_pascals_triangle(num_rows)

        # Assert
        expected_result = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1], [1, 8, 28, 56, 70, 56, 28, 8, 1], [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]]
        assert result == expected_result