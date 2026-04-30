import unittest

class TestGeneratePascalsTriangle(unittest.TestCase):
    def test_zero_rows(self):
        result = generate_pascals_triangle(0)
        self.assertEqual(result, [])

    def test_negative_rows(self):
        result = generate_pascals_triangle(-3)
        self.assertEqual(result, [])

    def test_one_row(self):
        result = generate_pascals_triangle(1)
        self.assertEqual(result, [[1]])

    def test_two_rows(self):
        result = generate_pascals_triangle(2)
        self.assertEqual(result, [[1], [1, 1]])

    def test_five_rows(self):
        expected = [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1]
        ]
        result = generate_pascals_triangle(5)
        self.assertEqual(result, expected)

    def test_row_lengths(self):
        num_rows = 7
        result = generate_pascals_triangle(num_rows)
        for i, row in enumerate(result):
            self.assertEqual(len(row), i + 1, f"Row {i} length should be {i + 1}")

    def test_symmetry(self):
        """Each row in Pascal's triangle should be symmetric."""
        result = generate_pascals_triangle(6)
        for i, row in enumerate(result):
            self.assertEqual(row, row[::-1], f"Row {i} is not symmetric")