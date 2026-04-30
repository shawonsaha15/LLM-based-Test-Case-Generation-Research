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

    def test_normal_input_found(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
        target = 3
        self.assertTrue(search_matrix(matrix, target))

    def test_normal_input_not_found(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
        target = 13
        self.assertFalse(search_matrix(matrix, target))

    def test_edge_case_empty_matrix(self):
        matrix = []
        target = 1
        self.assertFalse(search_matrix(matrix, target))

    def test_edge_case_single_element_matrix_found(self):
        matrix = [[1]]
        target = 1
        self.assertTrue(search_matrix(matrix, target))

    def test_edge_case_single_element_matrix_not_found(self):
        matrix = [[1]]
        target = 2
        self.assertFalse(search_matrix(matrix, target))

    def test_edge_case_single_row_matrix_found(self):
        matrix = [[1, 3, 5, 7]]
        target = 3
        self.assertTrue(search_matrix(matrix, target))

    def test_edge_case_single_row_matrix_not_found(self):
        matrix = [[1, 3, 5, 7]]
        target = 2
        self.assertFalse(search_matrix(matrix, target))

    def test_edge_case_single_column_matrix_found(self):
        matrix = [[1], [3], [5], [7]]
        target = 3
        self.assertTrue(search_matrix(matrix, target))

    def test_edge_case_single_column_matrix_not_found(self):
        matrix = [[1], [3], [5], [7]]
        target = 2
        self.assertFalse(search_matrix(matrix, target))

    def test_invalid_input_none(self):
        matrix = None
        target = 1
        self.assertFalse(search_matrix(matrix, target))

if __name__ == '__main__':
    unittest.main()