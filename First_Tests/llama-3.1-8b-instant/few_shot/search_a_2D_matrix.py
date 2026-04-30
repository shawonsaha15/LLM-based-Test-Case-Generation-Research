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
    def test_found(self):
        self.assertTrue(search_matrix([[1, 3, 5], [7, 9, 11]], 9))

    def test_not_found(self):
        self.assertFalse(search_matrix([[1, 3, 5], [7, 9, 11]], 13))

    def test_empty_matrix(self):
        self.assertFalse(search_matrix([], 5))

    def test_single_row_matrix(self):
        self.assertTrue(search_matrix([[1, 2, 3]], 2))

    def test_single_element_matrix(self):
        self.assertTrue(search_matrix([[5]], 5))

    def test_target_out_of_range(self):
        self.assertFalse(search_matrix([[1, 3, 5], [7, 9, 11]], 0))

if __name__ == "__main__":
    unittest.main()