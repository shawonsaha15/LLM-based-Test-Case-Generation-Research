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
    def test_target_found(self):
        matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]
        self.assertTrue(search_matrix(matrix, 3))
        self.assertTrue(search_matrix(matrix, 16))
        self.assertTrue(search_matrix(matrix, 50))

    def test_target_not_found(self):
        matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]
        self.assertFalse(search_matrix(matrix, 0))
        self.assertFalse(search_matrix(matrix, 13))
        self.assertFalse(search_matrix(matrix, 51))

    def test_empty_matrix(self):
        self.assertFalse(search_matrix([], 1))

    def test_empty_row(self):
        self.assertFalse(search_matrix([[]], 1))

    def test_single_element_found(self):
        self.assertTrue(search_matrix([[42]], 42))

    def test_single_element_not_found(self):
        self.assertFalse(search_matrix([[42]], 7))

    def test_none_matrix(self):
        self.assertFalse(search_matrix(None, 5))

    def test_negative_numbers(self):
        matrix = [
            [-10, -5, -2],
            [0, 3, 8],
            [12, 15, 20]
        ]
        self.assertTrue(search_matrix(matrix, -5))
        self.assertTrue(search_matrix(matrix, 0))
        self.assertFalse(search_matrix(matrix, -1))

    def test_single_row(self):
        matrix = [[1, 2, 3, 4, 5]]
        self.assertTrue(search_matrix(matrix, 3))
        self.assertFalse(search_matrix(matrix, 6))

    def test_single_column(self):
        matrix = [[1], [3], [5], [7]]
        self.assertTrue(search_matrix(matrix, 5))
        self.assertFalse(search_matrix(matrix, 2))

    def test_large_matrix(self):
        matrix = [list(range(i, i + 100)) for i in range(0, 1000, 100)]
        self.assertTrue(search_matrix(matrix, 0))
        self.assertTrue(search_matrix(matrix, 999))
        self.assertFalse(search_matrix(matrix, 1000))

if __name__ == "__main__":
    unittest.main()