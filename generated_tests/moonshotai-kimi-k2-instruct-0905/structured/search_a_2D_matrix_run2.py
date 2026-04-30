import unittest

class TestSearchMatrix(unittest.TestCase):
    def test_target_present_in_middle(self):
        # Arrange
        matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
        target = 9
        # Act
        result = search_matrix(matrix, target)
        # Assert
        self.assertTrue(result)

    def test_target_present_at_start(self):
        # Arrange
        matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
        target = 1
        # Act
        result = search_matrix(matrix, target)
        # Assert
        self.assertTrue(result)

    def test_target_present_at_end(self):
        # Arrange
        matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
        target = 17
        # Act
        result = search_matrix(matrix, target)
        # Assert
        self.assertTrue(result)

    def test_target_not_present(self):
        # Arrange
        matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
        target = 6
        # Act
        result = search_matrix(matrix, target)
        # Assert
        self.assertFalse(result)

    def test_single_element_matrix_target_present(self):
        # Arrange
        matrix = [[5]]
        target = 5
        # Act
        result = search_matrix(matrix, target)
        # Assert
        self.assertTrue(result)

    def test_single_element_matrix_target_not_present(self):
        # Arrange
        matrix = [[5]]
        target = 3
        # Act
        result = search_matrix(matrix, target)
        # Assert
        self.assertFalse(result)

    def test_empty_matrix(self):
        # Arrange
        matrix = []
        target = 5
        # Act
        result = search_matrix(matrix, target)
        # Assert
        self.assertFalse(result)

    def test_empty_rows(self):
        # Arrange
        matrix = [[]]
        target = 5
        # Act
        result = search_matrix(matrix, target)
        # Assert
        self.assertFalse(result)

    def test_single_row_target_present(self):
        # Arrange
        matrix = [[2, 4, 6, 8]]
        target = 6
        # Act
        result = search_matrix(matrix, target)
        # Assert
        self.assertTrue(result)

    def test_single_row_target_not_present(self):
        # Arrange
        matrix = [[2, 4, 6, 8]]
        target = 5
        # Act
        result = search_matrix(matrix, target)
        # Assert
        self.assertFalse(result)

    def test_single_column_target_present(self):
        # Arrange
        matrix = [[1], [3], [5], [7]]
        target = 5
        # Act
        result = search_matrix(matrix, target)
        # Assert
        self.assertTrue(result)

    def test_single_column_target_not_present(self):
        # Arrange
        matrix = [[1], [3], [5], [7]]
        target = 4
        # Act
        result = search_matrix(matrix, target)
        # Assert
        self.assertFalse(result)

    def test_target_smaller_than_all_elements(self):
        # Arrange
        matrix = [[2, 4, 6], [8, 10, 12]]
        target = 1
        # Act
        result = search_matrix(matrix, target)
        # Assert
        self.assertFalse(result)

    def test_target_larger_than_all_elements(self):
        # Arrange
        matrix = [[2, 4, 6], [8, 10, 12]]
        target = 13
        # Act
        result = search_matrix(matrix, target)
        # Assert
        self.assertFalse(result)

    def test_matrix_with_negative_numbers(self):
        # Arrange
        matrix = [[-10, -5, -1], [0, 5, 10]]
        target = -5
        # Act
        result = search_matrix(matrix, target)
        # Assert
        self.assertTrue(result)

    def test_matrix_with_all_same_elements_target_present(self):
        # Arrange
        matrix = [[7, 7, 7], [7, 7, 7]]
        target = 7
        # Act
        result = search_matrix(matrix, target)
        # Assert
        self.assertTrue(result)

    def test_matrix_with_all_same_elements_target_not_present(self):
        # Arrange
        matrix = [[7, 7, 7], [7, 7, 7]]
        target = 8
        # Act
        result = search_matrix(matrix, target)
        # Assert
        self.assertFalse(result)