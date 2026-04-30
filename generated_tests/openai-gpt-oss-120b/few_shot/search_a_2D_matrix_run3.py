import unittest

class TestSearchMatrix(unittest.TestCase):
    def test_empty_matrix(self):
        self.assertFalse(search_matrix([], 5))

    def test_matrix_with_empty_row(self):
        self.assertFalse(search_matrix([[]], 5))

    def test_single_element_found(self):
        matrix = [[7]]
        self.assertTrue(search_matrix(matrix, 7))

    def test_single_element_not_found(self):
        matrix = [[7]]
        self.assertFalse(search_matrix(matrix, 3))

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

    def test_negative_numbers(self):
        matrix = [
            [-10, -5, -1],
            [0, 4, 9],
            [12, 15, 20]
        ]
        self.assertTrue(search_matrix(matrix, -5))
        self.assertFalse(search_matrix(matrix, -2))

    def test_large_matrix(self):
        # 5x5 matrix with consecutive integers from 0 to 24
        matrix = [list(range(i, i + 5)) for i in range(0, 25, 5)]
        for target in [0, 12, 24]:
            self.assertTrue(search_matrix(matrix, target))
        self.assertFalse(search_matrix(matrix, 25))