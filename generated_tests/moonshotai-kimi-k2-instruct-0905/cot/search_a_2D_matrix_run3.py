import unittest

class TestSearchMatrix(unittest.TestCase):

    def test_target_present_in_middle(self):
        matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
        target = 9
        self.assertTrue(search_matrix(matrix, target))

    def test_target_present_first_element(self):
        matrix = [[1, 3, 5], [7, 9, 11]]
        target = 1
        self.assertTrue(search_matrix(matrix, target))

    def test_target_present_last_element(self):
        matrix = [[1, 3, 5], [7, 9, 11]]
        target = 11
        self.assertTrue(search_matrix(matrix, target))

    def test_target_not_present(self):
        matrix = [[1, 3, 5], [7, 9, 11]]
        target = 6
        self.assertFalse(search_matrix(matrix, target))

    def test_empty_matrix(self):
        matrix = []
        target = 5
        self.assertFalse(search_matrix(matrix, target))

    def test_empty_sub_matrix(self):
        matrix = [[]]
        target = 5
        self.assertFalse(search_matrix(matrix, target))

    def test_single_element_found(self):
        matrix = [[5]]
        target = 5
        self.assertTrue(search_matrix(matrix, target))

    def test_single_element_not_found(self):
        matrix = [[5]]
        target = 3
        self.assertFalse(search_matrix(matrix, target))

    def test_large_matrix_target_present(self):
        matrix = [[i * 10 + j for j in range(100)] for i in range(100)]
        target = 5055
        self.assertTrue(search_matrix(matrix, target))

    def test_large_matrix_target_absent(self):
        matrix = [[i * 10 + j for j in range(100)] for i in range(100)]
        target = 9999
        self.assertFalse(search_matrix(matrix, target))

    def test_negative_numbers_found(self):
        matrix = [[-10, -5, -1], [0, 5, 10]]
        target = -5
        self.assertTrue(search_matrix(matrix, target))

    def test_negative_numbers_not_found(self):
        matrix = [[-10, -5, -1], [0, 5, 10]]
        target = -3
        self.assertFalse(search_matrix(matrix, target))

    def test_duplicate_values_found(self):
        matrix = [[2, 2, 2], [2, 2, 2]]
        target = 2
        self.assertTrue(search_matrix(matrix, target))

    def test_wide_matrix(self):
        matrix = [[i] for i in range(100)]
        target = 50
        self.assertTrue(search_matrix(matrix, target))

    def test_wide_matrix_not_found(self):
        matrix = [[i] for i in range(100)]
        target = 150
        self.assertFalse(search_matrix(matrix, target))

    def test_target_smaller_than_all(self):
        matrix = [[5, 10, 15], [20, 25, 30]]
        target = 1
        self.assertFalse(search_matrix(matrix, target))

    def test_target_larger_than_all(self):
        matrix = [[5, 10, 15], [20, 25, 30]]
        target = 35
        self.assertFalse(search_matrix(matrix, target))

    def test_matrix_with_none_elements_raises(self):
        matrix = [[1, None, 3], [4, 5, 6]]
        target = 3
        with self.assertRaises(TypeError):
            search_matrix(matrix, target)

    def test_non_int_target_raises(self):
        matrix = [[1, 2, 3], [4, 5, 6]]
        target = "5"
        with self.assertRaises(TypeError):
            search_matrix(matrix, target)

    def test_non_list_matrix_raises(self):
        matrix = "not a matrix"
        target = 5
        with self.assertRaises(AttributeError):
            search_matrix(matrix, target)