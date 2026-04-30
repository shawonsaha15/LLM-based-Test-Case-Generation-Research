import unittest


class TestGeneratePascalsTriangle(unittest.TestCase):

    def test_zero_rows(self):
        # Arrange
        num_rows = 0
        # Act
        triangle = generate_pascals_triangle(num_rows)
        # Assert
        self.assertEqual(triangle, [])

    def test_one_row(self):
        # Arrange
        num_rows = 1
        # Act
        triangle = generate_pascals_triangle(num_rows)
        # Assert
        self.assertEqual(triangle, [[1]])

    def test_two_rows(self):
        # Arrange
        num_rows = 2
        # Act
        triangle = generate_pascals_triangle(num_rows)
        # Assert
        self.assertEqual(triangle, [[1], [1, 1]])

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
        triangle = generate_pascals_triangle(num_rows)
        # Assert
        self.assertEqual(triangle, expected)

    def test_negative_rows(self):
        # Arrange
        num_rows = -1
        # Act
        triangle = generate_pascals_triangle(num_rows)
        # Assert
        self.assertEqual(triangle, [])

    def test_large_rows(self):
        # Arrange
        num_rows = 10
        # Act
        triangle = generate_pascals_triangle(num_rows)
        # Assert
        self.assertEqual(len(triangle), 10)
        self.assertEqual(triangle[0], [1])
        self.assertEqual(triangle[9][0], 1)
        self.assertEqual(triangle[9][-1], 1)
        self.assertEqual(triangle[9][4], 126)