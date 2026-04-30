class TestSearchMatrixFunction(unittest.TestCase):

    def test_empty_matrix(self):
        matrix = []
        target = 1
        self.assertFalse(search_matrix(matrix, target))

    def test_matrix_with_no_columns(self):
        matrix = [[]]
        target = 1
        self.assertFalse(search_matrix(matrix, target))

    def test_matrix_with_single_element_found(self):
        matrix = [[1]]
        target = 1
        self.assertTrue(search_matrix(matrix, target))

    def test_matrix_with_single_element_not_found(self):
        matrix = [[1]]
        target = 2
        self.assertFalse(search_matrix(matrix, target))

    def test_matrix_with_multiple_elements_found(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
        target = 3
        self.assertTrue(search_matrix(matrix, target))

    def test_matrix_with_multiple_elements_not_found(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
        target = 13
        self.assertFalse(search_matrix(matrix, target))

    def test_matrix_with_negative_numbers_found(self):
        matrix = [[-10, -8, -5, -3], [-2, 0, 2, 4], [6, 8, 10, 12]]
        target = -8
        self.assertTrue(search_matrix(matrix, target))

    def test_matrix_with_negative_numbers_not_found(self):
        matrix = [[-10, -8, -5, -3], [-2, 0, 2, 4], [6, 8, 10, 12]]
        target = -12
        self.assertFalse(search_matrix(matrix, target))