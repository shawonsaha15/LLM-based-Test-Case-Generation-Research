import unittest

class TestSearchMatrix(unittest.TestCase):
    def test_empty_matrix(self):
        self.assertFalse(search_matrix([], 1))

    def test_empty_row_matrix(self):
        self.assertFalse(search_matrix([[]], 1))

    def test_single_element_found(self):
        self.assertTrue(search_matrix([[5]], 5))

    def test_single_element_not_found(self):
        self.assertFalse(search_matrix([[5]], 3))

    def test_target_in_first_row(self):
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
        self.assertTrue(search_matrix(matrix, 3))

    def test_target_in_last_row(self):
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
        self.assertTrue(search_matrix(matrix, 8))

    def test_target_not_present(self):
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
        self.assertFalse(search_matrix(matrix, 10))

    def test_target_smallest_element(self):
        matrix = [[1, 3, 5],
                  [7, 9, 11]]
        self.assertTrue(search_matrix(matrix, 1))

    def test_target_largest_element(self):
        matrix = [[1, 3, 5],
                  [7, 9, 11]]
        self.assertTrue(search_matrix(matrix, 11))

    def test_single_row_found(self):
        self.assertTrue(search_matrix([[1, 4, 7, 11]], 7))

    def test_single_row_not_found(self):
        self.assertFalse(search_matrix([[1, 4, 7, 11]], 5))

    def test_single_column_found(self):
        self.assertTrue(search_matrix([[1], [4], [7], [11]], 7))

    def test_single_column_not_found(self):
        self.assertFalse(search_matrix([[1], [4], [7], [11]], 5))

    def test_duplicate_elements_found(self):
        matrix = [[1, 1, 2],
                  [3, 3, 4]]
        self.assertTrue(search_matrix(matrix, 3))

    def test_negative_numbers(self):
        matrix = [[-5, -2, 0],
                  [1, 3, 7]]
        self.assertTrue(search_matrix(matrix, -2))
        self.assertFalse(search_matrix(matrix, -1))