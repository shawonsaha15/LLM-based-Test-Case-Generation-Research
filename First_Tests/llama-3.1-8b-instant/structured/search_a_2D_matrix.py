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
        matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
        self.assertTrue(search_matrix(matrix, 9))
        self.assertTrue(search_matrix(matrix, 15))
        self.assertTrue(search_matrix(matrix, 11))

    def test_edge_cases(self):
        matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
        self.assertFalse(search_matrix(matrix, 0))
        self.assertFalse(search_matrix(matrix, 18))
        self.assertFalse(search_matrix([], 5))
        self.assertFalse(search_matrix([[1, 2, 3]], 4))

    def test_invalid_inputs(self):
        matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
        with self.assertRaises(TypeError):
            search_matrix(matrix, 'a')
        with self.assertRaises(TypeError):
            search_matrix('matrix', 5)
        with self.assertRaises(TypeError):
            search_matrix(matrix, 5.5)

if __name__ == "__main__":
    unittest.main()