import unittest

class TestSearchMatrix(unittest.TestCase):
    def test_target_found_first_middle_last(self):
        matrix = [
            [1, 3, 5],
            [7, 9, 11],
            [13, 15, 17]
        ]
        self.assertTrue(search_matrix(matrix, 1))   # first element
        self.assertTrue(search_matrix(matrix, 9))   # middle element
        self.assertTrue(search_matrix(matrix, 17))  # last element

    def test_target_not_found(self):
        matrix = [
            [2, 4, 6],
            [8, 10, 12],
            [14, 16, 18]
        ]
        self.assertFalse(search_matrix(matrix, 1))   # less than min
        self.assertFalse(search_matrix(matrix, 5))   # between values
        self.assertFalse(search_matrix(matrix, 20))  # greater than max

    def test_empty_matrix(self):
        self.assertFalse(search_matrix([], 5))

    def test_matrix_with_empty_row(self):
        self.assertFalse(search_matrix([[]], 5))

    def test_single_element_matrix_found(self):
        matrix = [[42]]
        self.assertTrue(search_matrix(matrix, 42))

    def test_single_element_matrix_not_found(self):
        matrix = [[42]]
        self.assertFalse(search_matrix(matrix, 7))

    def test_single_row_matrix(self):
        matrix = [[1, 2, 3, 4, 5]]
        self.assertTrue(search_matrix(matrix, 3))
        self.assertFalse(search_matrix(matrix, 6))

    def test_single_column_matrix(self):
        matrix = [
            [1],
            [3],
            [5],
            [7],
            [9]
        ]
        self.assertTrue(search_matrix(matrix, 5))
        self.assertFalse(search_matrix(matrix, 2))

    def test_large_matrix(self):
        size = 100
        matrix = [list(range(i * size, (i + 1) * size)) for i in range(size)]
        # first, middle, last
        self.assertTrue(search_matrix(matrix, 0))
        middle_value = (size * size) // 2
        self.assertTrue(search_matrix(matrix, middle_value))
        self.assertTrue(search_matrix(matrix, size * size - 1))
        # not present
        self.assertFalse(search_matrix(matrix, -1))
        self.assertFalse(search_matrix(matrix, size * size))

    def test_invalid_matrix_none(self):
        with self.assertRaises(TypeError):
            search_matrix(None, 1)

    def test_invalid_matrix_non_rectangular(self):
        matrix = [
            [1, 2, 3],
            [4, 5]          # shorter row
        ]
        with self.assertRaises(IndexError):
            search_matrix(matrix, 5)

    def test_invalid_target_type(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6]
        ]
        with self.assertRaises(TypeError):
            search_matrix(matrix, "5")