import unittest


class TestGeneratePascalsTriangle(unittest.TestCase):

    # Normal cases
    def test_zero_rows(self):
        # Arrange
        num_rows = 0
        expected = []
        # Act
        actual = generate_pascals_triangle(num_rows)
        # Assert
        self.assertEqual(actual, expected)

    def test_one_row(self):
        # Arrange
        num_rows = 1
        expected = [[1]]
        # Act
        actual = generate_pascals_triangle(num_rows)
        # Assert
        self.assertEqual(actual, expected)

    def test_five_rows(self):
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
        actual = generate_pascals_triangle(num_rows)
        # Assert
        self.assertEqual(actual, expected)

    # Boundary cases
    def test_two_rows(self):
        # Arrange
        num_rows = 2
        expected = [[1], [1, 1]]
        # Act
        actual = generate_pascals_triangle(num_rows)
        # Assert
        self.assertEqual(actual, expected)

    def test_large_row_count(self):
        # Arrange
        num_rows = 10
        # Act
        actual = generate_pascals_triangle(num_rows)
        # Assert
        self.assertEqual(len(actual), 10)
        self.assertEqual(actual[9], [1, 9, 36, 84, 126, 126, 84, 36, 9, 1])

    # Invalid inputs
    def test_negative_rows(self):
        # Arrange
        num_rows = -1
        # Act
        actual = generate_pascals_triangle(num_rows)
        # Assert
        self.assertEqual(actual, [])

    def test_non_integer_input(self):
        # Arrange
        num_rows = 3.5
        # Act & Assert
        with self.assertRaises(TypeError):
            generate_pascals_triangle(num_rows)