import unittest

class TestSearchMatrix(unittest.TestCase):

    def test_target_present(self):
        matrix = [
            [1, 3, 5],
            [7, 9, 11],
            [13, 15, 17]
        ]
        self.assertTrue(search_matrix(matrix, 9))

    def test_target_not_present(self):
        matrix = [
            [1, 3, 5],
            [7, 9, 11],
            [13, 15, 17]
        ]
        self.assertFalse(search_matrix(matrix, 10))

    def test_empty_matrix(self):
        matrix = []
        self.assertFalse(search_matrix(matrix, 5))

    def test_empty_row(self):
        matrix = [[]]
        self.assertFalse(search_matrix(matrix, 5))

    def test_single_element_found(self):
        matrix = [[5]]
        self.assertTrue(search_matrix(matrix, 5))

    def test_single_element_not_found(self):
        matrix = [[5]]
        self.assertFalse(search_matrix(matrix, 3))

    def test_first_element(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.assertTrue(search_matrix(matrix, 1))

    def test_last_element(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.assertTrue(search_matrix(matrix, 9))

    def test_target_smaller_than_all(self):
        matrix = [
            [2, 4, 6],
            [8, 10, 12]
        ]
        self.assertFalse(search_matrix(matrix, 1))

    def test_target_larger_than_all(self):
        matrix = [
            [2, 4, 6],
            [8, 10, 12]
        ]
        self.assertFalse(search_matrix(matrix, 13))