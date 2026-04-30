class TestSearchMatrix(unittest.TestCase):
    def test_normal_case_found(self):
        # Arrange
        matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]
        target = 3

        # Act
        result = search_matrix(matrix, target)

        # Assert
        self.assertTrue(result)

    def test_normal_case_not_found(self):
        # Arrange
        matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]
        target = 13

        # Act
        result = search_matrix(matrix, target)

        # Assert
        self.assertFalse(result)

    def test_boundary_case_first_element(self):
        # Arrange
        matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]
        target = 1

        # Act
        result = search_matrix(matrix, target)

        # Assert
        self.assertTrue(result)

    def test_boundary_case_last_element(self):
        # Arrange
        matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]
        target = 50

        # Act
        result = search_matrix(matrix, target)

        # Assert
        self.assertTrue(result)

    def test_invalid_input_empty_matrix(self):
        # Arrange
        matrix = []
        target = 5

        # Act
        result = search_matrix(matrix, target)

        # Assert
        self.assertFalse(result)

    def test_invalid_input_matrix_with_empty_row(self):
        # Arrange
        matrix = [
            [],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]
        target = 5

        # Act
        result = search_matrix(matrix, target)

        # Assert
        self.assertFalse(result)

    def test_invalid_input_none_matrix(self):
        # Arrange
        matrix = None
        target = 5

        # Act
        with self.assertRaises(TypeError):
            search_matrix(matrix, target)

    def test_invalid_input_none_target(self):
        # Arrange
        matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]
        target = None

        # Act
        with self.assertRaises(TypeError):
            search_matrix(matrix, target)