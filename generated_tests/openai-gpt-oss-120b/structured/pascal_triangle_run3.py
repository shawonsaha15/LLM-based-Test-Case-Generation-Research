import unittest

class TestGeneratePascalsTriangle(unittest.TestCase):
    def test_normal_cases(self):
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

        # Arrange (second normal case)
        num_rows = 1
        expected = [[1]]

        # Act
        result = generate_pascals_triangle(num_rows)

        # Assert
        self.assertEqual(result, expected)

    def test_boundary_cases(self):
        # Arrange: zero rows
        num_rows = 0
        expected = []

        # Act
        result = generate_pascals_triangle(num_rows)

        # Assert
        self.assertEqual(result, expected)

        # Arrange: large number of rows (performance not tested, just correctness of first and last rows)
        num_rows = 10
        expected_first_row = [1]
        expected_last_row = [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]

        # Act
        result = generate_pascals_triangle(num_rows)

        # Assert
        self.assertEqual(result[0], expected_first_row)
        self.assertEqual(result[-1], expected_last_row)

    def test_invalid_inputs(self):
        # Arrange: negative number of rows
        num_rows = -3
        expected = []  # function returns empty list for negative input due to range behavior

        # Act
        result = generate_pascals_triangle(num_rows)

        # Assert
        self.assertEqual(result, expected)

        # Arrange: non-integer input (string)
        num_rows = "5"

        # Act & Assert
        with self.assertRaises(TypeError):
            generate_pascals_triangle(num_rows)

        # Arrange: None as input
        num_rows = None

        # Act & Assert
        with self.assertRaises(TypeError):
            generate_pascals_triangle(num_rows)