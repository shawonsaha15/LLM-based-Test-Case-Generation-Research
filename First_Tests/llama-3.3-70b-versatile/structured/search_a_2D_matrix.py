def search_matrix(matrix: list[list[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False

    m = len(matrix)
    n = len(matrix[0])
    left = 0
    right = m * n

    while left < right:
        mid = (left + right) // 2
        row = mid // n
        col = mid % n

        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            left = mid + 1
        else:
            right = mid

    return False

import unittest

class TestSearchMatrix(unittest.TestCase):
    def test_normal_cases(self):
        matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]
        self.assertTrue(search_matrix(matrix, 3))
        self.assertTrue(search_matrix(matrix, 13))
        self.assertFalse(search_matrix(matrix, 13))

        matrix = [
            [1, 3],
            [5, 7]
        ]
        self.assertTrue(search_matrix(matrix, 1))
        self.assertTrue(search_matrix(matrix, 7))
        self.assertFalse(search_matrix(matrix, 0))

    def test_edge_cases(self):
        matrix = [
            [1]
        ]
        self.assertTrue(search_matrix(matrix, 1))
        self.assertFalse(search_matrix(matrix, 0))

        matrix = [
            [1, 2, 3]
        ]
        self.assertTrue(search_matrix(matrix, 1))
        self.assertTrue(search_matrix(matrix, 2))
        self.assertTrue(search_matrix(matrix, 3))
        self.assertFalse(search_matrix(matrix, 0))

        matrix = [
            [1],
            [2],
            [3]
        ]
        self.assertTrue(search_matrix(matrix, 1))
        self.assertTrue(search_matrix(matrix, 2))
        self.assertTrue(search_matrix(matrix, 3))
        self.assertFalse(search_matrix(matrix, 0))

    def test_invalid_inputs(self):
        matrix = []
        self.assertFalse(search_matrix(matrix, 1))

        matrix = [[]]
        self.assertFalse(search_matrix(matrix, 1))

        matrix = [
            [1, 2, 3],
            [],
            [4, 5, 6]
        ]
        with self.assertRaises(IndexError):
            search_matrix(matrix, 1)

if __name__ == "__main__":
    unittest.main()