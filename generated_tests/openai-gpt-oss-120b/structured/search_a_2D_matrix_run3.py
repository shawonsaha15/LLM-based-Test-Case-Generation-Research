import unittest

class TestSearchMatrix(unittest.TestCase):
    def test_normal_case_found(self):
        # Arrange
        matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]
        target = 16

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

    def test_boundary_first_element(self):
        # Arrange
        matrix = [
            [2, 4, 6],
            [8, 10, 12]
        ]
        target = 2  # first element

        # Act
        result = search_matrix(matrix, target)

        # Assert
        self.assertTrue(result)

    def test_boundary_last_element(self):
        # Arrange
        matrix = [
            [2, 4, 6],
            [8, 10, 12]
        ]
        target = 12  # last element

        # Act
        result = search_matrix(matrix, target)

        # Assert
        self.assertTrue(result)

    def test_single_element_matrix_found(self):
        # Arrange
        matrix = [[42]]
        target = 42

        # Act
        result = search_matrix(matrix, target)

        # Assert
        self.assertTrue(result)

    def test_single_element_matrix_not_found(self):
        # Arrange
        matrix = [[42]]
        target = 7

        # Act
        result = search_matrix(matrix, target)

        # Assert
        self.assertFalse(result)

    def test_one_row_multiple_columns_found(self):
        # Arrange
        matrix = [[1, 3, 5, 7, 9]]
        target = 7

        # Act
        result = search_matrix(matrix, target)

        # Assert
        self.assertTrue(result)

    def test_one_column_multiple_rows_not_found(self):
        # Arrange
        matrix = [
            [1],
            [3],
            [5],
            [7],
            [9]
        ]
        target = 4

        # Act
        result = search_matrix(matrix, target)

        # Assert
        self.assertFalse(result)

    def test_empty_matrix(self):
        # Arrange
        matrix = []
        target = 1

        # Act
        result = search_matrix(matrix, target)

        # Assert
        self.assertFalse(result)

    def test_matrix_with_empty_row(self):
        # Arrange
        matrix = [[]]
        target = 1

        # Act
        result = search_matrix(matrix, target)

        # Assert
        self.assertFalse(result)

    def test_large_matrix_boundary(self):
        # Arrange
        size = 1000
        matrix = [list(range(i * size, (i + 1) * size)) for i in range(size)]
        target = size * size - 1  # last element in the matrix

        # Act
        result = search_matrix(matrix, target)

        # Assert
        self.assertTrue(result)

    def test_invalid_target_type(self):
        # Arrange
        matrix = [
            [1, 2],
            [3, 4]
        ]
        target = "2"  # non‑int target

        # Act & Assert
        with self.assertRaises(TypeError):
            search_matrix(matrix, target)

    def test_invalid_matrix_type(self):
        # Arrange
        matrix = "not a matrix"
        target = 1

        # Act & Assert
        with self.assertRaises(TypeError):
            search_matrix(matrix, target)