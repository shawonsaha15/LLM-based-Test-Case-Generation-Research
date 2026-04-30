class TestSearchMatrix(unittest.TestCase):
    def test_found_in_first_row(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
        result = search_matrix(matrix, 3)
        self.assertTrue(result)

    def test_found_in_last_row(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
        result = search_matrix(matrix, 50)
        self.assertTrue(result)

    def test_not_found(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
        result = search_matrix(matrix, 13)
        self.assertFalse(result)

    def test_empty_matrix(self):
        matrix = []
        result = search_matrix(matrix, 5)
        self.assertFalse(result)

    def test_single_element_matrix_found(self):
        matrix = [[5]]
        result = search_matrix(matrix, 5)
        self.assertTrue(result)

    def test_single_element_matrix_not_found(self):
        matrix = [[5]]
        result = search_matrix(matrix, 3)
        self.assertFalse(result)

    def test_single_row_matrix_found(self):
        matrix = [[1, 3, 5, 7]]
        result = search_matrix(matrix, 3)
        self.assertTrue(result)

    def test_single_row_matrix_not_found(self):
        matrix = [[1, 3, 5, 7]]
        result = search_matrix(matrix, 9)
        self.assertFalse(result)