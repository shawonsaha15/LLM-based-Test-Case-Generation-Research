def generate_pascals_triangle(num_rows: int) -> list[list[int]]:
    result = []

    for i in range(num_rows):
        result.append([1] * (i + 1))

    for i in range(2, num_rows):
        for j in range(1, len(result[i]) - 1):
            result[i][j] = result[i - 1][j - 1] + result[i - 1][j]

    return result

import unittest

class TestGeneratePascalsTriangle(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(generate_pascals_triangle(5), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])

    def test_edge_case_zero_rows(self):
        self.assertEqual(generate_pascals_triangle(0), [])

    def test_edge_case_one_row(self):
        self.assertEqual(generate_pascals_triangle(1), [[1]])

    def test_edge_case_negative_rows(self):
        with self.assertRaises(ValueError):
            generate_pascals_triangle(-1)

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            generate_pascals_triangle(3.5)

    def test_invalid_input_non_integer_zero(self):
        with self.assertRaises(TypeError):
            generate_pascals_triangle(0.0)

    def test_invalid_input_string(self):
        with self.assertRaises(TypeError):
            generate_pascals_triangle('hello')

    def test_invalid_input_list(self):
        with self.assertRaises(TypeError):
            generate_pascals_triangle([1, 2, 3])

if __name__ == "__main__":
    unittest.main()