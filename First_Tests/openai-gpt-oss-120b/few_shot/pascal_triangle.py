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

    def test_three_rows(self):
        self.assertEqual(generate_pascals_triangle(3), [[1], [1, 1], [1, 2, 1]])

    def test_five_rows(self):
        self.assertEqual(
            generate_pascals_triangle(5),
            [
                [1],
                [1, 1],
                [1, 2, 1],
                [1, 3, 3, 1],
                [1, 4, 6, 4, 1]
            ]
        )

    def test_ten_rows(self):
        expected = [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1],
            [1, 5, 10, 10, 5, 1],
            [1, 6, 15, 20, 15, 6, 1],
            [1, 7, 21, 35, 35, 21, 7, 1],
            [1, 8, 28, 56, 70, 56, 28, 8, 1],
            [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
        ]
        self.assertEqual(generate_pascals_triangle(10), expected)

if __name__ == "__main__":
    unittest.main()