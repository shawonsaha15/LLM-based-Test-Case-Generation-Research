import unittest

class TestGeneratePascalsTriangle(unittest.TestCase):
    def test_zero_rows(self):
        self.assertEqual(generate_pascals_triangle(0), [])

    def test_one_row(self):
        self.assertEqual(generate_pascals_triangle(1), [[1]])

    def test_two_rows(self):
        self.assertEqual(generate_pascals_triangle(2), [[1], [1, 1]])

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
        num_rows = 7
        triangle = generate_pascals_triangle(num_rows)
        for i, row in enumerate(triangle):
            self.assertEqual(len(row), i + 1, f"Row {i} length mismatch")

    def test_negative_input(self):
        # Negative numbers should behave like zero rows (empty list)
        self.assertEqual(generate_pascals_triangle(-3), [])