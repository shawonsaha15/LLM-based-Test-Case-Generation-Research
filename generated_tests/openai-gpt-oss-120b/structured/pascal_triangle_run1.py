import unittest

class TestGeneratePascalsTriangle(unittest.TestCase):
    def test_normal_three_rows(self):
        # Arrange
        num_rows = 3
        expected = [
            [1],
            [1, 1],
            [1, 2, 1]
        ]

        # Act
        result = generate_pascals_triangle(num_rows)

        # Assert
        self.assertEqual(result, expected)

    def test_normal_five_rows(self):
        # Arrange
        num_rows = 5
        expected = [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1]
        ]

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

    def test_boundary_one_row(self):
        # Arrange
        num_rows = 1
        expected = [[1]]

        # Act
        result = generate_pascals_triangle(num_rows)

        # Assert
        self.assertEqual(result, expected)

    def test_boundary_two_rows(self):
        # Arrange
        num_rows = 2
        expected = [
            [1],
            [1, 1]
        ]

        # Act
        result = generate_pascals_triangle(num_rows)

        # Assert
        self.assertEqual(result, expected)

    def test_invalid_negative_rows(self):
        # Arrange
        num_rows = -5
        expected = []  # function treats negative range as empty

        # Act
        result = generate_pascals_triangle(num_rows)

        # Assert
        self.assertEqual(result, expected)

    def test_invalid_non_integer_string(self):
        # Arrange
        num_rows = "three"

        # Act & Assert
        with self.assertRaises(TypeError):
            generate_pascals_triangle(num_rows)

    def test_invalid_non_integer_float(self):
        # Arrange
        num_rows = 3.5

        # Act & Assert
        with self.assertRaises(TypeError):
            generate_pascals_triangle(num_rows)