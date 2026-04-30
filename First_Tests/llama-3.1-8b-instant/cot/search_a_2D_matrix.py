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

    def test_normal_input(self):
        matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
        self.assertTrue(search_matrix(matrix, 9))

    def test_edge_case_target_not_found(self):
        matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
        self.assertFalse(search_matrix(matrix, 10))

    def test_edge_case_empty_matrix(self):
        matrix = []
        self.assertFalse(search_matrix(matrix, 5))

    def test_edge_case_single_row_matrix(self):
        matrix = [[1, 2, 3]]
        self.assertTrue(search_matrix(matrix, 2))

    def test_edge_case_single_element_matrix(self):
        matrix = [[5]]
        self.assertTrue(search_matrix(matrix, 5))

    def test_invalid_input_non_list_matrix(self):
        matrix = 'not a list'
        with self.assertRaises(TypeError):
            search_matrix(matrix, 5)

    def test_invalid_input_non_list_target(self):
        matrix = [[1, 2, 3]]
        with self.assertRaises(TypeError):
            search_matrix(matrix, 'not an int')

    def test_invalid_input_non_int_target(self):
        matrix = [[1, 2, 3]]
        with self.assertRaises(TypeError):
            search_matrix(matrix, 3.5)

if __name__ == '__main__':
    unittest.main()