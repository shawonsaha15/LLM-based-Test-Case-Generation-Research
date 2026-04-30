class TestSearchMatrix(unittest.TestCase):
    def test_target_found(self):
        matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 60]
        ]
        target = 3
        result = search_matrix(matrix, target)
        self.assertTrue(result)

    def test_target_not_found(self):
        matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 60]
        ]
        target = 13
        result = search_matrix(matrix, target)
        self.assertFalse(result)

    def test_empty_matrix(self):
        matrix = []
        target = 5
        result = search_matrix(matrix, target)
        self.assertFalse(result)

    def test_single_element_matrix(self):
        matrix = [[5]]
        target = 5
        result = search_matrix(matrix, target)
        self.assertTrue(result)

    def test_single_element_matrix_not_found(self):
        matrix = [[5]]
        target = 3
        result = search_matrix(matrix, target)
        self.assertFalse(result)

    def test_single_row_matrix(self):
        matrix = [[1, 3, 5, 7]]
        target = 3
        result = search_matrix(matrix, target)
        self.assertTrue(result)

    def test_single_row_matrix_not_found(self):
        matrix = [[1, 3, 5, 7]]
        target = 9
        result = search_matrix(matrix, target)
        self.assertFalse(result)

    def test_single_column_matrix(self):
        matrix = [
            [1],
            [3],
            [5],
            [7]
        ]
        target = 3
        result = search_matrix(matrix, target)
        self.assertTrue(result)

    def test_single_column_matrix_not_found(self):
        matrix = [
            [1],
            [3],
            [5],
            [7]
        ]
        target = 9
        result = search_matrix(matrix, target)
        self.assertFalse(result)