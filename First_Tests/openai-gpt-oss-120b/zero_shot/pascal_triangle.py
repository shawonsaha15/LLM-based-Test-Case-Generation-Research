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

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            generate_pascals_triangle("3")

    def test_large_rows(self):
        result = generate_pascals_triangle(10)
        self.assertEqual(len(result), 10)
        self.assertEqual(result[0], [1])
        self.assertEqual(result[9][0], 1)
        self.assertEqual(result[9][-1], 1)
        self.assertEqual(result[9][4], 126)

if __name__ == "__main__":
    unittest.main()