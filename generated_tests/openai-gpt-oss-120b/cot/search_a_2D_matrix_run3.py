import unittest

class TestSearchMatrix(unittest.TestCase):
    def test_target_present(self):
        matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]
        self.assertTrue(search_matrix(matrix, 3))
        self.assertTrue(search_matrix(matrix, 16))
        self.assertTrue(search_matrix(matrix, 50))

    def test_target_absent(self):
        matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]
        self.assertFalse(search_matrix(matrix, 0))
        self.assertFalse(search_matrix(matrix, 13))
        self.assertFalse(search_matrix(matrix, 60))

    def test_empty_matrix(self):
        self.assertFalse(search_matrix([], 1))
        self.assertFalse(search_matrix([[]], 1))

    def test_single_element_matrix(self):
        matrix = [[42]]
        self.assertTrue(search_matrix(matrix, 42))
        self.assertFalse(search_matrix(matrix, -1))

    def test_first_and_last_element(self):
        matrix = [
            [2, 4, 6],
            [8, 10, 12],
            [14, 16, 18]
        ]
        self.assertTrue(search_matrix(matrix, 2))   # first
        self.assertTrue(search_matrix(matrix, 18))  # last

    def test_negative_numbers(self):
        matrix = [
            [-10, -5, -2],
            [0, 3, 7],
            [12, 15, 20]
        ]
        self.assertTrue(search_matrix(matrix, -5))
        self.assertTrue(search_matrix(matrix, 0))
        self.assertFalse(search_matrix(matrix, -1))
        self.assertFalse(search_matrix(matrix, 21))

    def test_target_out_of_bounds(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6]
        ]
        self.assertFalse(search_matrix(matrix, -100))
        self.assertFalse(search_matrix(matrix, 100))

    def test_large_matrix(self):
        size = 100
        matrix = [list(range(i * size, (i + 1) * size)) for i in range(size)]
        # test a few random positions
        self.assertTrue(search_matrix(matrix, 0))               # first element
        self.assertTrue(search_matrix(matrix, size * size - 1)) # last element
        self.assertTrue(search_matrix(matrix, 1234))
        self.assertFalse(search_matrix(matrix, size * size))   # just beyond last

    def test_none_matrix_raises(self):
        with self.assertRaises(TypeError):
            search_matrix(None, 1)

    def test_non_int_elements(self):
        matrix = [
            ["a", "b"],
            ["c", "d"]
        ]
        # comparison of strings with int target raises TypeError
        with self.assertRaises(TypeError):
            search_matrix(matrix, 1)