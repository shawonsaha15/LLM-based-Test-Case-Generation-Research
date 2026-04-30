import unittest

class TestSearchMatrix(unittest.TestCase):
    def test_empty_matrix(self):
        self.assertFalse(search_matrix([], 5))

    def test_matrix_with_empty_row(self):
        self.assertFalse(search_matrix([[]], 1))

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
            [2, 4, 6],
            [8, 10, 12],
            [14, 16, 18]
        ]
        self.assertTrue(search_matrix(matrix, 18))

    def test_target_middle_element(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ]
        self.assertTrue(search_matrix(matrix, 7))

    def test_target_not_present(self):
        matrix = [
            [1, 3, 5],
            [7, 9, 11],
            [13, 15, 17]
        ]
        self.assertFalse(search_matrix(matrix, 8))

    def test_multiple_rows_and_columns(self):
        matrix = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20]
        ]
        # Test a few present values
        for target in (1, 5, 10, 14, 20):
            with self.subTest(target=target):
                self.assertTrue(search_matrix(matrix, target))
        # Test a few absent values
        for target in (0, 21, 8.5, -3):
            with self.subTest(target=target):
                self.assertFalse(search_matrix(matrix, target))