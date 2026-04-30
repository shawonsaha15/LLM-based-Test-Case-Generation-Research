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

    def test_negative_rows(self):
        # Negative input results in an empty list due to range behavior
        self.assertEqual(generate_pascals_triangle(-3), [])

    def test_invalid_type_float(self):
        with self.assertRaises(TypeError):
            generate_pascals_triangle(3.5)

    def test_invalid_type_str(self):
        with self.assertRaises(TypeError):
            generate_pascals_triangle("4")

    def test_invalid_type_none(self):
        with self.assertRaises(TypeError):
            generate_pascals_triangle(None)

    def test_large_input_structure(self):
        n = 20
        triangle = generate_pascals_triangle(n)
        # Verify number of rows
        self.assertEqual(len(triangle), n)
        # Verify each row length
        for i, row in enumerate(triangle):
            self.assertEqual(len(row), i + 1)
            # First and last elements must be 1
            self.assertEqual(row[0], 1)
            self.assertEqual(row[-1], 1)
        # Spot‑check a middle value using binomial coefficient
        # Row 10, element 5 should be C(10,5) = 252
        self.assertEqual(triangle[10][5], 252)

    def test_row_symmetry(self):
        """Each row should be symmetric."""
        for rows in range(2, 12):
            triangle = generate_pascals_triangle(rows)
            for row in triangle:
                self.assertEqual(row, row[::-1])