class TestSearchMatrix:
    def test_normal_input(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 3
        assert search_matrix(matrix, target) is True

    def test_empty_matrix(self):
        matrix = []
        target = 3
        assert search_matrix(matrix, target) is False

    def test_empty_row_matrix(self):
        matrix = [[]]
        target = 3
        assert search_matrix(matrix, target) is False

    def test_zero_matrix(self):
        matrix = [[0, 0, 0], [0, 0, 0]]
        target = 0
        assert search_matrix(matrix, target) is True

    def test_none_matrix(self):
        matrix = None
        target = 3
        assert search_matrix(matrix, target) is False

    def test_large_matrix(self):
        matrix = [[i for i in range(100)] for _ in range(100)]
        target = 50
        assert search_matrix(matrix, target) is True

    def test_invalid_input_matrix(self):
        matrix = "string"
        target = 3
        try:
            search_matrix(matrix, target)
            assert False, "Expected TypeError"
        except TypeError:
            pass

    def test_invalid_input_target(self):
        matrix = [[1, 2, 3], [4, 5, 6]]
        target = "string"
        try:
            search_matrix(matrix, target)
            assert False, "Expected TypeError"
        except TypeError:
            pass

    def test_not_found_target(self):
        matrix = [[1, 2, 3], [4, 5, 6]]
        target = 7
        assert search_matrix(matrix, target) is False

    def test_edge_case_first_element(self):
        matrix = [[1, 2, 3], [4, 5, 6]]
        target = 1
        assert search_matrix(matrix, target) is True

    def test_edge_case_last_element(self):
        matrix = [[1, 2, 3], [4, 5, 6]]
        target = 6
        assert search_matrix(matrix, target) is True