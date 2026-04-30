class TestSearchMatrix:
    def test_normal_input(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
        target = 3
        assert search_matrix(matrix, target) == True

    def test_empty_matrix(self):
        matrix = []
        target = 3
        assert search_matrix(matrix, target) == False

    def test_empty_row_matrix(self):
        matrix = [[]]
        target = 3
        assert search_matrix(matrix, target) == False

    def test_zero_matrix(self):
        matrix = [[0, 0, 0], [0, 0, 0]]
        target = 0
        assert search_matrix(matrix, target) == True

    def test_none_matrix(self):
        matrix = None
        target = 3
        assert search_matrix(matrix, target) == False

    def test_large_values(self):
        matrix = [[1, 1000, 5000], [10000, 20000, 30000]]
        target = 20000
        assert search_matrix(matrix, target) == True

    def test_target_not_in_matrix(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
        target = 13
        assert search_matrix(matrix, target) == False

    def test_target_at_first_position(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
        target = 1
        assert search_matrix(matrix, target) == True

    def test_target_at_last_position(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
        target = 50
        assert search_matrix(matrix, target) == True