class TestSearchMatrixFunction(unittest.TestCase):

    def test_empty_matrix(self):
        matrix = []
        target = 1
        self.assertFalse(search_matrix(matrix, target))

    def test_no_target_found(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 13
        self.assertFalse(search_matrix(matrix, target))

    def test_target_found(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 3
        self.assertTrue(search_matrix(matrix, target))

    def test_target_at_start(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 1
        self.assertTrue(search_matrix(matrix, target))

    def test_target_at_end(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 60
        self.assertTrue(search_matrix(matrix, target))

    def test_single_element_matrix(self):
        matrix = [[5]]
        target = 5
        self.assertTrue(search_matrix(matrix, target))

    def test_single_row_matrix(self):
        matrix = [[1, 3, 5, 7]]
        target = 3
        self.assertTrue(search_matrix(matrix, target))

    def test_single_column_matrix(self):
        matrix = [[1], [3], [5], [7]]
        target = 3
        self.assertTrue(search_matrix(matrix, target))