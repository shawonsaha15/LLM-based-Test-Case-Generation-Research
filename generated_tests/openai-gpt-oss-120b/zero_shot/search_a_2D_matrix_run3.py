import unittest

class TestSearchMatrix(unittest.TestCase):
    def test_empty_matrix(self):
        self.assertFalse(search_matrix([], 5))

    def test_empty_row(self):
        self.assertFalse(search_matrix([[]], 5))

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

    def test_target_middle(self):
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

    def test_target_smaller_than_all(self):
        matrix = [
            [10, 20, 30],
            [40, 50, 60]
        ]
        self.assertFalse(search_matrix(matrix, 5))

    def test_target_larger_than_all(self):
        matrix = [
            [10, 20, 30],
            [40, 50, 60]
        ]
        self.assertFalse(search_matrix(matrix, 100))

    def test_multiple_rows_target_present(self):
        matrix = [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ]
        self.assertTrue(search_matrix(matrix, 14))
        self.assertTrue(search_matrix(matrix, 30))
        self.assertTrue(search_matrix(matrix, 1))

    def test_multiple_rows_target_absent(self):
        matrix = [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ]
        self.assertFalse(search_matrix(matrix, 0))
        self.assertFalse(search_matrix(matrix, 13.5))
        self.assertFalse(search_matrix(matrix, 31))

    def test_large_matrix_performance(self):
        # Create a 100x100 matrix with consecutive numbers
        size = 100
        matrix = [list(range(i * size, (i + 1) * size)) for i in range(size)]
        self.assertTrue(search_matrix(matrix, 0))
        self.assertTrue(search_matrix(matrix, 9999))
        self.assertFalse(search_matrix(matrix, 10000))
        self.assertFalse(search_matrix(matrix, -1))