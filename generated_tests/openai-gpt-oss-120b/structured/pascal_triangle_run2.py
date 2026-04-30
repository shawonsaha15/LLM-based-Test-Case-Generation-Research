import unittest

class TestGeneratePascalsTriangle(unittest.TestCase):
    def test_normal_case_five_rows(self):
        # Arrange
        num_rows = 5
        expected = [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1],
        ]

        # Act
        result = generate_pascals_triangle(num_rows)

        # Assert
        self.assertEqual(result, expected)

    def test_normal_case_one_row(self):
        # Arrange
        num_rows = 1
        expected = [[1]]

        # Act
        result = generate_pascals_triangle(num_rows)

        # Assert
        self.assertEqual(result, expected)

    def test_boundary_zero_rows(self):
        # Arrange
        num_rows = 0
        expected = []

        # Act
        result = generate_pascals_triangle(num_rows)

        # Assert
        self.assertEqual(result, expected)

    def test_boundary_two_rows(self):
        # Arrange
        num_rows = 2
        expected = [
            [1],
            [1, 1],
        ]

        # Act
        result = generate_pascals_triangle(num_rows)

        # Assert
        self.assertEqual(result, expected)

    def test_negative_rows_returns_empty(self):
        # Arrange
        num_rows = -3
        expected = []

        # Act
        result = generate_pascals_triangle(num_rows)

        # Assert
        self.assertEqual(result, expected)

    def test_invalid_type_raises_type_error(self):
        # Arrange
        num_rows = "three"

        # Act & Assert
        with self.assertRaises(TypeError):
            generate_pascals_triangle(num_rows)