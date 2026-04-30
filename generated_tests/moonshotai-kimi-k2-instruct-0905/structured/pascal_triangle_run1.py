import unittest


class TestGeneratePascalsTriangle(unittest.TestCase):
    """Test suite for generate_pascals_triangle function."""

    # Normal cases
    def test_zero_rows(self):
        """Test generating triangle with 0 rows."""
        # Arrange
        num_rows = 0
        expected = []

        # Act
        result = generate_pascals_triangle(num_rows)

        # Assert
        self.assertEqual(result, expected)

    def test_one_row(self):
        """Test generating triangle with 1 row."""
        # Arrange
        num_rows = 1
        expected = [[1]]

        # Act
        result = generate_pascals_triangle(num_rows)

        # Assert
        self.assertEqual(result, expected)

    def test_five_rows(self):
        """Test generating triangle with 5 rows."""
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

    # Boundary cases
    def test_two_rows(self):
        """Test generating triangle with 2 rows."""
        # Arrange
        num_rows = 2
        expected = [[1], [1, 1]]

        # Act
        result = generate_pascals_triangle(num_rows)

        # Assert
        self.assertEqual(result, expected)

    def test_three_rows(self):
        """Test generating triangle with 3 rows."""
        # Arrange
        num_rows = 3
        expected = [[1], [1, 1], [1, 2, 1]]

        # Act
        result = generate_pascals_triangle(num_rows)

        # Assert
        self.assertEqual(result, expected)

    def test_large_number_of_rows(self):
        """Test generating triangle with 10 rows."""
        # Arrange
        num_rows = 10
        expected_last_row = [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]

        # Act
        result = generate_pascals_triangle(num_rows)

        # Assert
        self.assertEqual(len(result), 10)
        self.assertEqual(result[-1], expected_last_row)

    # Invalid inputs
    def test_negative_rows(self):
        """Test generating triangle with negative number of rows."""
        # Arrange
        num_rows = -1
        expected = []

        # Act
        result = generate_pascals_triangle(num_rows)

        # Assert
        self.assertEqual(result, expected)