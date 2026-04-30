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

    def test_target_not_present(self):
        matrix = [
            [1, 3, 5],
            [7, 9, 11],
            [13, 15, 17]
        ]
        self.assertFalse(search_matrix(matrix, 8))
        self.assertFalse(search_matrix(matrix, 0))
        self.assertFalse(search_matrix(matrix, 18))

    def test_negative_numbers(self):
        matrix = [
            [-10, -5, -1],
            [0, 3, 8],
            [12, 15, 20]
        ]
        self.assertTrue(search_matrix(matrix, -5))
        self.assertTrue(search_matrix(matrix, 0))
        self.assertFalse(search_matrix(matrix, -2))
        self.assertFalse(search_matrix(matrix, 21))

    def test_large_matrix(self):
        # Create a 100x100 matrix with values 0..9999 in row-major order
        size = 100
        matrix = [list(range(i * size, (i + 1) * size)) for i in range(size)]
        # Test a few random positions
        self.assertTrue(search_matrix(matrix, 0))          # first element
        self.assertTrue(search_matrix(matrix, 9999))       # last element
        self.assertTrue(search_matrix(matrix, 5678))       # somewhere in the middle
        self.assertFalse(search_matrix(matrix, -1))        # below range
        self.assertFalse(search_matrix(matrix, 10000))     # above range