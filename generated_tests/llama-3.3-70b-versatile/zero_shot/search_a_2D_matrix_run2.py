class TestSearchMatrixFunction(unittest.TestCase):

    def test_empty_matrix(self):
        matrix = []
        target = 5
        self.assertFalse(search_matrix(matrix, target))

    def test_single_element_matrix_found(self):
        matrix = [[5]]
        target = 5
        self.assertTrue(search_matrix(matrix, target))

    def test_single_element_matrix_not_found(self):
        matrix = [[5]]
        target = 10
        self.assertFalse(search_matrix(matrix, target))

    def test_multiple_elements_matrix_found(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
        target = 3
        self.assertTrue(search_matrix(matrix, target))

    def test_multiple_elements_matrix_not_found(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
        target = 13
        self.assertFalse(search_matrix(matrix, target))

    def test_matrix_with_single_row_found(self):
        matrix = [[1, 3, 5, 7]]
        target = 5
        self.assertTrue(search_matrix(matrix, target))

    def test_matrix_with_single_row_not_found(self):
        matrix = [[1, 3, 5, 7]]
        target = 10
        self.assertFalse(search_matrix(matrix, target))

    def test_matrix_with_single_column_found(self):
        matrix = [[1], [3], [5], [7]]
        target = 5
        self.assertTrue(search_matrix(matrix, target))

    def test_matrix_with_single_column_not_found(self):
        matrix = [[1], [3], [5], [7]]
        target = 10
        self.assertFalse(search_matrix(matrix, target))