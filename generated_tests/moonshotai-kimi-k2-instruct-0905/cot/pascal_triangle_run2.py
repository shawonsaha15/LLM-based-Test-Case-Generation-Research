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
            generate_pascals_triangle("5")

    def test_none_input(self):
        with self.assertRaises(TypeError):
            generate_pascals_triangle(None)

    def test_large_rows(self):
        result = generate_pascals_triangle(20)
        self.assertEqual(len(result), 20)
        self.assertEqual(result[0], [1])
        self.assertEqual(result[-1][0], 1)
        self.assertEqual(result[-1][-1], 1)

    def test_triangle_properties(self):
        triangle = generate_pascals_triangle(6)
        for row in triangle:
            self.assertEqual(row[0], 1)
            self.assertEqual(row[-1], 1)
        for i in range(2, len(triangle)):
            for j in range(1, len(triangle[i]) - 1):
                self.assertEqual(triangle[i][j], triangle[i - 1][j - 1] + triangle[i - 1][j])