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

    def test_normal_inputs(self):
        self.assertEqual(generate_pascals_triangle(1), [[1]])
        self.assertEqual(generate_pascals_triangle(2), [[1], [1, 1]])
        self.assertEqual(generate_pascals_triangle(3), [[1], [1, 1], [1, 2, 1]])
        self.assertEqual(generate_pascals_triangle(4), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]])
        self.assertEqual(generate_pascals_triangle(5), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])

    def test_edge_cases(self):
        self.assertEqual(generate_pascals_triangle(0), [])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            generate_pascals_triangle('a')
        with self.assertRaises(TypeError):
            generate_pascals_triangle(1.5)
        with self.assertRaises(ValueError):
            generate_pascals_triangle(-1)

if __name__ == '__main__':
    unittest.main()