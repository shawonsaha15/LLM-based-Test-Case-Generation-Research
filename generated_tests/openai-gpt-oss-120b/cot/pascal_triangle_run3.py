import unittest
import math

class TestGeneratePascalsTriangle(unittest.TestCase):
    def expected_triangle(self, n):
        """Generate Pascal's triangle using combinatorial formula."""
        triangle = []
        for i in range(n):
            row = [math.comb(i, k) for k in range(i + 1)]
            triangle.append(row)
        return triangle

    def test_zero_rows(self):
        self.assertEqual(generate_pascals_triangle(0), [])

    def test_one_row(self):
        self.assertEqual(generate_pascals_triangle(1), [[1]])

    def test_small_triangle(self):
        num_rows = 5
        expected = self.expected_triangle(num_rows)
        result = generate_pascals_triangle(num_rows)
        self.assertEqual(result, expected)

    def test_row_lengths(self):
        for n in range(1, 8):
            result = generate_pascals_triangle(n)
            for i, row in enumerate(result):
                self.assertEqual(len(row), i + 1,
                                 f"Row {i} length should be {i + 1}")

    def test_large_triangle_central_value(self):
        num_rows = 10
        result = generate_pascals_triangle(num_rows)
        # central value of row 9 (0‑based) is C(9,4)=126
        self.assertEqual(result[9][4], 126)

    def test_negative_rows_returns_empty(self):
        self.assertEqual(generate_pascals_triangle(-3), [])

    def test_invalid_type_float_raises(self):
        with self.assertRaises(TypeError):
            generate_pascals_triangle(3.5)

    def test_invalid_type_str_raises(self):
        with self.assertRaises(TypeError):
            generate_pascals_triangle("5")

    def test_invalid_type_none_raises(self):
        with self.assertRaises(TypeError):
            generate_pascals_triangle(None)

    def test_invalid_type_list_raises(self):
        with self.assertRaises(TypeError):
            generate_pascals_triangle([3])