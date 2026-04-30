import unittest

class TestSearchMatrix(unittest.TestCase):
    def test_target_present(self):
        matrix = [
            [1, 3, 5],
            [7, 9, 11],
            [13, 15, 17]
        ]
        self.assertTrue(search_matrix(matrix, 9))
        self.assertTrue(search_matrix(matrix, 1))
        self.assertTrue(search_matrix(matrix, 17))

    def test_target_absent(self):
        matrix = [
            [1, 3, 5],
            [7, 9, 11],
            [13, 15, 17]
        ]
        self.assertFalse(search_matrix(matrix, 2))
        self.assertFalse(search_matrix(matrix, 18))
        self.assertFalse(search_matrix(matrix, 0))

    def test_single_element_matrix_target_present(self):
        matrix = [[5]]
        self.assertTrue(search_matrix(matrix, 5))

    def test_single_element_matrix_target_absent(self):
        matrix = [[5]]
        self.assertFalse(search_matrix(matrix, 3))

    def test_empty_matrix(self):
        matrix = []
        self.assertFalse(search_matrix(matrix, 5))

    def test_empty_row_matrix(self):
        matrix = [[]]
        self.assertFalse(search_matrix(matrix, 5))

    def test_single_row_matrix(self):
        matrix = [[1, 2, 3, 4, 5]]
        self.assertTrue(search_matrix(matrix, 3))
        self.assertFalse(search_matrix(matrix, 6))

    def test_single_column_matrix(self):
        matrix = [[1], [2], [3], [4], [5]]
        self.assertTrue(search_matrix(matrix, 3))
        self.assertFalse(search_matrix(matrix, 6))

    def test_large_matrix(self):
        matrix = [[i * 10 + j for j in range(10)] for i in range(10)]
        self.assertTrue(search_matrix(matrix, 55))
        self.assertFalse(search_matrix(matrix, 111))