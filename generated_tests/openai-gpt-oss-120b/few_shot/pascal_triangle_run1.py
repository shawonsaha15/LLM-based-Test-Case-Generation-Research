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
            [1, 4, 6, 4, 1],
        ]
        self.assertEqual(generate_pascals_triangle(5), expected)

    def test_ten_rows_structure(self):
        """Check that each row has the correct length and ends with 1."""
        triangle = generate_pascals_triangle(10)
        self.assertEqual(len(triangle), 10)
        for i, row in enumerate(triangle):
            # Row length should be i+1
            self.assertEqual(len(row), i + 1)
            # First and last elements should be 1
            self.assertEqual(row[0], 1)
            self.assertEqual(row[-1], 1)

    def test_negative_input(self):
        """Negative row count should behave like zero rows (empty list)."""
        self.assertEqual(generate_pascals_triangle(-3), [])