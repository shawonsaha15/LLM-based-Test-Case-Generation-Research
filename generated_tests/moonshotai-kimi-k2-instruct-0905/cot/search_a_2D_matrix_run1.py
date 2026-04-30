import unittest

class TestSearchMatrix(unittest.TestCase):
    def test_target_present_in_middle(self):
        matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
        self.assertTrue(search_matrix(matrix, 9))

    def test_target_present_in_first_row(self):
        matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
        self.assertTrue(search_matrix(matrix, 3))

    def test_target_present_in_last_row(self):
        matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
        self.assertTrue(search_matrix(matrix, 15))

    def test_target_present_first_element(self):
        matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
        self.assertTrue(search_matrix(matrix, 1))

    def test_target_present_last_element(self):
        matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
        self.assertTrue(search_matrix(matrix, 17))

    def test_target_not_present_less_than_min(self):
        matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
        self.assertFalse(search_matrix(matrix, 0))

    def test_target_not_present_greater_than_max(self):
        matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
        self.assertFalse(search_matrix(matrix, 18))

    def test_target_not_present_middle_gap(self):
        matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
        self.assertFalse(search_matrix(matrix, 6))

    def test_empty_matrix(self):
        matrix = []
        self.assertFalse(search_matrix(matrix, 5))

    def test_empty_rows(self):
        matrix = [[]]
        self.assertFalse(search_matrix(matrix, 5))

    def test_single_element_found(self):
        matrix = [[5]]
        self.assertTrue(search_matrix(matrix, 5))

    def test_single_element_not_found(self):
        matrix = [[5]]
        self.assertFalse(search_matrix(matrix, 3))

    def test_single_row_found(self):
        matrix = [[1, 3, 5, 7, 9]]
        self.assertTrue(search_matrix(matrix, 7))

    def test_single_row_not_found(self):
        matrix = [[1, 3, 5, 7, 9]]
        self.assertFalse(search_matrix(matrix, 4))

    def test_single_column_found(self):
        matrix = [[1], [3], [5], [7], [9]]
        self.assertTrue(search_matrix(matrix, 5))

    def test_single_column_not_found(self):
        matrix = [[1], [3], [5], [7], [9]]
        self.assertFalse(search_matrix(matrix, 4))

    def test_duplicate_values_found(self):
        matrix = [[1, 2, 2], [3, 3, 4], [4, 5, 5]]
        self.assertTrue(search_matrix(matrix, 3))

    def test_large_matrix_found(self):
        matrix = [[i * 10 + j for j in range(100)] for i in range(100)]
        self.assertTrue(search_matrix(matrix, 505))

    def test_large_matrix_not_found(self):
        matrix = [[i * 10 + j for j in range(100)] for i in range(100)]
        self.assertFalse(search_matrix(matrix, 10000))

    def test_negative_numbers_found(self):
        matrix = [[-10, -5, -1], [0, 5, 10], [15, 20, 25]]
        self.assertTrue(search_matrix(matrix, -5))

    def test_negative_numbers_not_found(self):
        matrix = [[-10, -5, -1], [0, 5, 10], [15, 20, 25]]
        self.assertFalse(search_matrix(matrix, -3))

    def test_zero_target_found(self):
        matrix = [[-10, -5, 0], [5, 10, 15]]
        self.assertTrue(search_matrix(matrix, 0))

    def test_zero_target_not_found(self):
        matrix = [[1, 2, 3], [4, 5, 6]]
        self.assertFalse(search_matrix(matrix, 0))

    def test_rectangular_matrix_found(self):
        matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
        self.assertTrue(search_matrix(matrix, 7))

    def test_rectangular_matrix_not_found(self):
        matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
        self.assertFalse(search_matrix(matrix, 11))

    def test_non_uniform_rows_not_allowed(self):
        matrix = [[1, 2], [3]]
        with self.assertRaises(IndexError):
            search_matrix(matrix, 2)

    def test_target_is_none(self):
        matrix = [[1, 2, 3], [4, 5, 6]]
        with self.assertRaises(TypeError):
            search_matrix(matrix, None)

    def test_matrix_contains_none(self):
        matrix = [[1, None, 3], [4, 5, 6]]
        with self.assertRaises(TypeError):
            search_matrix(matrix, 3)

    def test_matrix_is_none(self):
        with self.assertRaises(AttributeError):
            search_matrix(None, 5)