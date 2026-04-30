class TestGeneratePascalsTriangle(unittest.TestCase):
    def test_single_row(self):
        result = generate_pascals_triangle(1)
        self.assertEqual(result, [[1]])

    def test_multiple_rows(self):
        result = generate_pascals_triangle(5)
        self.assertEqual(result, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])

    def test_zero_rows(self):
        result = generate_pascals_triangle(0)
        self.assertEqual(result, [])

    def test_negative_rows(self):
        with self.assertRaises(ValueError):
            generate_pascals_triangle(-1)

    def test_non_integer_rows(self):
        with self.assertRaises(TypeError):
            generate_pascals_triangle(1.5)