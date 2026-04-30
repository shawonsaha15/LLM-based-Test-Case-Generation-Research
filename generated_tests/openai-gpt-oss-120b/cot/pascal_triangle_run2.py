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
        self.assertEqual(generate_pascals_triangle(-3), [])

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            generate_pascals_triangle("5")
        with self.assertRaises(TypeError):
            generate_pascals_triangle(3.5)
        with self.assertRaises(TypeError):
            generate_pascals_triangle(None)

    def test_large_input(self):
        n = 20
        triangle = generate_pascals_triangle(n)
        self.assertEqual(len(triangle), n)
        for row in triangle:
            self.assertEqual(row[0], 1)
            self.assertEqual(row[-1], 1)
        self.assertIn(252, triangle[10])  # C(10,5) = 252

    def test_mutation_detection(self):
        triangle = generate_pascals_triangle(7)
        self.assertEqual(triangle[4], [1, 4, 6, 4, 1])
        self.assertEqual(triangle[6], [1, 6, 15, 20, 15, 6, 1])