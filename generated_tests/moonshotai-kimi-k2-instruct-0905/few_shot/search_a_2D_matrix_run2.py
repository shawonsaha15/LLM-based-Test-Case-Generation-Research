class TestSearchMatrix(unittest.TestCase):
    def test_target_present(self):
        matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
        target = 9
        result = search_matrix(matrix, target)
        self.assertTrue(result)

    def test_target_not_present(self):
        matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
        target = 10
        result = search_matrix(matrix, target)
        self.assertFalse(result)

    def test_empty_matrix(self):
        matrix = []
        target = 5
        result = search_matrix(matrix, target)
        self.assertFalse(result)

    def test_empty_row(self):
        matrix = [[]]
        target = 5
        result = search_matrix(matrix, target)
        self.assertFalse(result)

    def test_single_element_found(self):
        matrix = [[5]]
        target = 5
        result = search_matrix(matrix, target)
        self.assertTrue(result)

    def test_single_element_not_found(self):
        matrix = [[5]]
        target = 3
        result = search_matrix(matrix, target)
        self.assertFalse(result)

    def test_target_in_first_row(self):
        matrix = [[1, 2, 3, 4]]
        target = 3
        result = search_matrix(matrix, target)
        self.assertTrue(result)

    def test_target_in_last_column(self):
        matrix = [[1], [2], [3], [4]]
        target = 3
        result = search_matrix(matrix, target)
        self.assertTrue(result)

    def test_large_matrix_target_present(self):
        matrix = [[i * 10 + j for j in range(10)] for i in range(10)]
        target = 55
        result = search_matrix(matrix, target)
        self.assertTrue(result)

    def test_large_matrix_target_not_present(self):
        matrix = [[i * 10 + j for j in range(10)] for i in range(10)]
        target = 105
        result = search_matrix(matrix, target)
        self.assertFalse(result)