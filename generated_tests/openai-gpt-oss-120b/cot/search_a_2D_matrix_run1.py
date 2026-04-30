import unittest

class TestSearchMatrix(unittest.TestCase):
    def test_target_found_various_positions(self):
        matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]
        # first element
        self.assertTrue(search_matrix(matrix, 1))
        # last element
        self.assertTrue(search_matrix(matrix, 50))
        # middle element
        self.assertTrue(search_matrix(matrix, 16))
        # element in second row, first column
        self.assertTrue(search_matrix(matrix, 10))
        # element in third row, second column
        self.assertTrue(search_matrix(matrix, 30))

    def test_target_not_found(self):
        matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]
        # less than minimum
        self.assertFalse(search_matrix(matrix, -5))
        # greater than maximum
        self.assertFalse(search_matrix(matrix, 100))
        # between existing values
        self.assertFalse(search_matrix(matrix, 8))
        self.assertFalse(search_matrix(matrix, 22))
        self.assertFalse(search_matrix(matrix, 51))

    def test_empty_matrix(self):
        self.assertFalse(search_matrix([], 1))
        self.assertFalse(search_matrix([[]], 1))

    def test_single_element_matrix(self):
        matrix = [[42]]
        self.assertTrue(search_matrix(matrix, 42))
        self.assertFalse(search_matrix(matrix, 0))
        self.assertFalse(search_matrix(matrix, 43))

    def test_single_row_matrix(self):
        matrix = [[2, 4, 6, 8, 10]]
        self.assertTrue(search_matrix(matrix, 6))
        self.assertFalse(search_matrix(matrix, 5))
        self.assertTrue(search_matrix(matrix, 2))
        self.assertTrue(search_matrix(matrix, 10))
        self.assertFalse(search_matrix(matrix, 11))

    def test_single_column_matrix(self):
        matrix = [
            [1],
            [3],
            [5],
            [7],
            [9]
        ]
        self.assertTrue(search_matrix(matrix, 5))
        self.assertFalse(search_matrix(matrix, 4))
        self.assertTrue(search_matrix(matrix, 1))
        self.assertTrue(search_matrix(matrix, 9))
        self.assertFalse(search_matrix(matrix, 10))

    def test_large_matrix(self):
        size = 100
        matrix = [list(range(i * size, (i + 1) * size)) for i in range(size)]
        # test a few random positions
        self.assertTrue(search_matrix(matrix, 0))
        self.assertTrue(search_matrix(matrix, 9999))
        self.assertTrue(search_matrix(matrix, 5000))
        # values not present
        self.assertFalse(search_matrix(matrix, -1))
        self.assertFalse(search_matrix(matrix, 10000))

    def test_none_matrix(self):
        # None should be treated as falsy and return False without error
        self.assertFalse(search_matrix(None, 1))

    def test_invalid_target_type(self):
        matrix = [[1, 2], [3, 4]]
        with self.assertRaises(TypeError):
            search_matrix(matrix, "2")
        with self.assertRaises(TypeError):
            search_matrix(matrix, None)

    def test_non_integer_matrix_elements(self):
        matrix = [["a", "b"], ["c", "d"]]
        with self.assertRaises(TypeError):
            search_matrix(matrix, 1)