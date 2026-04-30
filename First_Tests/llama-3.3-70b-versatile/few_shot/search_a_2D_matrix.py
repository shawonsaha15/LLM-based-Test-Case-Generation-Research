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
    def test_basic(self):
        self.assertTrue(search_matrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 3))
        self.assertTrue(search_matrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 11))

    def test_edge(self):
        self.assertFalse(search_matrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 0))
        self.assertFalse(search_matrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 51))

    def test_empty(self):
        self.assertFalse(search_matrix([], 1))
        self.assertFalse(search_matrix([[1, 2, 3]], 1))

    def test_single_element(self):
        self.assertTrue(search_matrix([[1]], 1))
        self.assertFalse(search_matrix([[1]], 2))

if __name__ == "__main__":
    unittest.main()