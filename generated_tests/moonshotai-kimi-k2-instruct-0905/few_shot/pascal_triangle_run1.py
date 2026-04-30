class TestGeneratePascalsTriangle(unittest.TestCase):
    def test_zero_rows(self):
        result = generate_pascals_triangle(0)
        self.assertEqual(result, [])

    def test_one_row(self):
        result = generate_pascals_triangle(1)
        self.assertEqual(result, [[1]])

    def test_two_rows(self):
        result = generate_pascals_triangle(2)
        self.assertEqual(result, [[1], [1, 1]])

    def test_three_rows(self):
        result = generate_pascals_triangle(3)
        self.assertEqual(result, [[1], [1, 1], [1, 2, 1]])

    def test_four_rows(self):
        result = generate_pascals_triangle(4)
        self.assertEqual(result, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]])

    def test_five_rows(self):
        result = generate_pascals_triangle(5)
        self.assertEqual(result, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])