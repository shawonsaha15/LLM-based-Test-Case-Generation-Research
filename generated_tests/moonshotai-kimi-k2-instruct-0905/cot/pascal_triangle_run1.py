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

    def test_negative_rows(self):
        with self.assertRaises(ValueError):
            generate_pascals_triangle(-1)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            generate_pascals_triangle("five")

    def test_none_input(self):
        with self.assertRaises(TypeError):
            generate_pascals_triangle(None)

    def test_large_rows(self):
        result = generate_pascals_triangle(20)
        self.assertEqual(len(result), 20)
        self.assertEqual(result[0], [1])
        self.assertEqual(result[19][0], 1)
        self.assertEqual(result[19][-1], 1)

    def test_each_row_sum_is_power_of_two(self):
        for num_rows in range(1, 8):
            triangle = generate_pascals_triangle(num_rows)
            for i, row in enumerate(triangle):
                self.assertEqual(sum(row), 2 ** i)

    def test_symmetry_of_rows(self):
        triangle = generate_pascals_triangle(6)
        for row in triangle:
            self.assertEqual(row, row[::-1])

    def test_edge_values_always_one(self):
        triangle = generate_pascals_triangle(7)
        for row in triangle:
            self.assertEqual(row[0], 1)
            self.assertEqual(row[-1], 1)