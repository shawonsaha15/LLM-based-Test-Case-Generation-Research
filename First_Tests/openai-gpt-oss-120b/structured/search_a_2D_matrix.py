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
        self.assertTrue(search_matrix(matrix, 16))
        self.assertTrue(search_matrix(matrix, 50))
        self.assertFalse(search_matrix(matrix, 13))
        self.assertFalse(search_matrix(matrix, 0))

    def test_edge_cases(self):
        self.assertFalse(search_matrix([], 1))
        self.assertFalse(search_matrix([[]], 1))
        self.assertTrue(search_matrix([[5]], 5))
        self.assertFalse(search_matrix([[5]], 4))
        self.assertTrue(search_matrix([[1, 2, 3]], 2))
        self.assertFalse(search_matrix([[1, 2, 3]], 4))
        self.assertTrue(search_matrix([[1], [3], [5]], 3))
        self.assertFalse(search_matrix([[1], [3], [5]], 2))

    def test_invalid_inputs(self):
        self.assertFalse(search_matrix(None, 1))
        self.assertFalse(search_matrix([None], 1))
        self.assertFalse(search_matrix([[1, 2], None], 2))
        self.assertFalse(search_matrix([[1, 'a'], [3, 4]], 3))

if __name__ == "__main__":
    unittest.main()