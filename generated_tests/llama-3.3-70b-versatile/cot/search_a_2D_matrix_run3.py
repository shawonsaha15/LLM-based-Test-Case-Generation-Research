class TestSearchMatrix:
    def test_normal_input(self):
        matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]
        target = 3
        assert search_matrix(matrix, target) is True

    def test_not_found(self):
        matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]
        target = 13
        assert search_matrix(matrix, target) is False

    def test_empty_matrix(self):
        matrix = []
        target = 1
        assert search_matrix(matrix, target) is False

    def test_empty_row_matrix(self):
        matrix = [[]]
        target = 1
        assert search_matrix(matrix, target) is False

    def test_single_element_matrix_found(self):
        matrix = [[1]]
        target = 1
        assert search_matrix(matrix, target) is True

    def test_single_element_matrix_not_found(self):
        matrix = [[1]]
        target = 2
        assert search_matrix(matrix, target) is False

    def test_large_matrix(self):
        matrix = [
            [i for i in range(1000)] for _ in range(1000)
        ]
        target = 500500
        assert search_matrix(matrix, target) is True

    def test_invalid_input_none(self):
        matrix = None
        target = 1
        assert search_matrix(matrix, target) is False

    def test_invalid_input_non_integer_target(self):
        matrix = [[1, 2, 3], [4, 5, 6]]
        target = 'a'
        try:
            search_matrix(matrix, target)
            assert False, "Expected TypeError"
        except TypeError:
            pass

    def test_invalid_input_non_list_matrix(self):
        matrix = 'a'
        target = 1
        try:
            search_matrix(matrix, target)
            assert False, "Expected TypeError"
        except TypeError:
            pass

    def test_invalid_input_non_integer_matrix_values(self):
        matrix = [[1, 'a', 3], [4, 5, 6]]
        target = 1
        try:
            search_matrix(matrix, target)
            assert False, "Expected TypeError"
        except TypeError:
            pass