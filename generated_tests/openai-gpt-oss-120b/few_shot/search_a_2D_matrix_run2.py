import unittest

class TestSearchMatrix(unittest.TestCase):
    def test_empty_matrix(self):
        self.assertFalse(search_matrix([], 5))

    def test_matrix_with_empty_row(self):
        self.assertFalse(search_matrix([[]], 0))

    def test_single_element_found(self):
        self.assertTrue(search_matrix([[7]], 7))

    def test_single_element_not_found(self):
        self.assertFalse(search_matrix([[7]], 3))

    def test_target_first_element(self):
        matrix = [
            [1, 3, 5],
            [7, 9, 11],
            [13, 15, 17]
        ]
        self.assertTrue(search_matrix(matrix, 1))

    def test_target_last_element(self):
        matrix = [
            [1, 3, 5],
            [7, 9, 11],
            [13, 15, 17]
        ]
        self.assertTrue(search_matrix(matrix, 17))

    def test_target_middle_element(self):
        matrix = [
            [1, 3, 5],
            [7, 9, 11],
            [13, 15, 17]
        ]
        self.assertTrue(search_matrix(matrix, 9))

    def test_target_not_present_between_values(self):
        matrix = [
            [1, 3, 5],
            [7, 9, 11],
            [13, 15, 17]
        ]
        self.assertFalse(search_matrix(matrix, 8))

    def test_one_row_multiple_columns_found(self):
        matrix = [[2, 4, 6, 8, 10]]
        self.assertTrue(search_matrix(matrix, 6))

    def test_one_row_multiple_columns_not_found(self):
        matrix = [[2, 4, 6, 8, 10]]
        self.assertFalse(search_matrix(matrix, 5))

    def test_one_column_multiple_rows_found(self):
        matrix = [
            [1],
            [3],
            [5],
            [7],
            [9]
        ]
        self.assertTrue(search_matrix(matrix, 7))

    def test_one_column_multiple_rows_not_found(self):
        matrix = [
            [1],
            [3],
            [5],
            [7],
            [9]
        ]
        self.assertFalse(search_matrix(matrix, 2))

    def test_negative_numbers_found(self):
        matrix = [
            [-10, -5, -1],
            [0, 3, 8],
            [12, 15, 20]
        ]
        self.assertTrue(search_matrix(matrix, -5))

    def test_negative_numbers_not_found(self):
        matrix = [
            [-10, -5, -1],
            [0, 3, 8],
            [12, 15, 20]
        ]
        self.assertFalse(search_matrix(matrix, -6))

    def test_large_matrix_found(self):
        # Create a 100x100 matrix with values 0..9999 in row-major order
        size = 100
        matrix = [list(range(i * size, (i + 1) * size)) for i in range(size)]
        self.assertTrue(search_matrix(matrix, 5555))

    def test_large_matrix_not_found(self):
        size = 100
        matrix = [list(range(i * size, (i + 1) * size)) for i in range(size)]
        self.assertFalse(search_matrix(matrix, 10000))