import unittest

class TestGeneratePascalsTriangle(unittest.TestCase):
    def test_zero_rows(self):
        self.assertEqual(generate_pascals_triangle(0), [])

    def test_one_row(self):
        self.assertEqual(generate_pascals_triangle(1), [[1]])

    def test_two_rows(self):
        self.assertEqual(generate_pascals_triangle(2), [[1], [1, 1]])

    def test_three_rows(self):
        self.assertEqual(generate_pascals_triangle(3), [[1], [1, 1], [1, 2, 1]])

    def test_four_rows(self):
        self.assertEqual(generate_pascals_triangle(4), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]])

    def test_five_rows(self):
        self.assertEqual(generate_pascals_triangle(5), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])