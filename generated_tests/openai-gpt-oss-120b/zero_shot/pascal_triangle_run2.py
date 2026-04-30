import unittest

class TestGeneratePascalsTriangle(unittest.TestCase):
    def test_zero_rows(self):
        self.assertEqual(generate_pascals_triangle(0), [])

    def test_negative_rows(self):
        # Negative input should behave like zero rows (empty list)
        self.assertEqual(generate_pascals_triangle(-5), [])

    def test_one_row(self):
        expected = [[1]]
        self.assertEqual(generate_pascals_triangle(1), expected)

    def test_two_rows(self):
        expected = [
            [1],
            [1, 1]
        ]
        self.assertEqual(generate_pascals_triangle(2), expected)

    def test_five_rows(self):
        expected = [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1]
        ]
        self.assertEqual(generate_pascals_triangle(5), expected)

    def test_row_lengths(self):
        """Each row i should have length i+1."""
        for n in range(1, 10):
            triangle = generate_pascals_triangle(n)
            for i, row in enumerate(triangle):
                self.assertEqual(len(row), i + 1,
                                 f"Row {i} length mismatch for n={n}")

    def test_row_sums(self):
        """Sum of elements in row i should be 2**i."""
        for n in range(1, 12):
            triangle = generate_pascals_triangle(n)
            for i, row in enumerate(triangle):
                self.assertEqual(sum(row), 2 ** i,
                                 f"Row {i} sum mismatch for n={n}")

    def test_symmetry(self):
        """Each row should be symmetric."""
        for n in range(1, 15):
            triangle = generate_pascals_triangle(n)
            for i, row in enumerate(triangle):
                self.assertEqual(row, row[::-1],
                                 f"Row {i} is not symmetric for n={n}")