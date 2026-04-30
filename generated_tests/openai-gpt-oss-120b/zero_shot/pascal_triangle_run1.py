import unittest

class TestGeneratePascalsTriangle(unittest.TestCase):
    def test_zero_rows(self):
        self.assertEqual(generate_pascals_triangle(0), [])

    def test_one_row(self):
        self.assertEqual(generate_pascals_triangle(1), [[1]])

    def test_multiple_rows(self):
        expected = [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1],
            [1, 5, 10, 10, 5, 1],
        ]
        self.assertEqual(generate_pascals_triangle(6), expected)

    def test_negative_rows(self):
        # Negative input should behave like zero rows (empty list)
        self.assertEqual(generate_pascals_triangle(-5), [])

    def test_immutable_result(self):
        # Ensure that modifying the returned triangle does not affect a new call
        triangle1 = generate_pascals_triangle(4)
        triangle1[2][1] = 999  # mutate
        triangle2 = generate_pascals_triangle(4)
        # triangle2 should be the correct unmodified triangle
        self.assertEqual(triangle2, [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
        ])