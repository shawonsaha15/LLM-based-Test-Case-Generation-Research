import unittest

class TestSearchMatrix(unittest.TestCase):
    # Normal case: target exists in the middle of the matrix
    def test_normal_target_found(self):
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

    # Normal case: target does not exist
    def test_normal_target_not_found(self):
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

    # Boundary case: target is the first element
    def test_boundary_first_element(self):
        # Arrange
        matrix = [
            [2, 4, 6],
            [8, 10, 12]
        ]
        target = 2
        # Act
        result = search_matrix(matrix, target)
        # Assert
        self.assertTrue(result)

    # Boundary case: target is the last element
    def test_boundary_last_element(self):
        # Arrange
        matrix = [
            [2, 4, 6],
            [8, 10, 12]
        ]
        target = 12
        # Act
        result = search_matrix(matrix, target)
        # Assert
        self.assertTrue(result)

    # Single-element matrix where target is present
    def test_single_element_found(self):
        # Arrange
        matrix = [[42]]
        target = 42
        # Act
        result = search_matrix(matrix, target)
        # Assert
        self.assertTrue(result)

    # Single-element matrix where target is absent
    def test_single_element_not_found(self):
        # Arrange
        matrix = [[42]]
        target = 7
        # Act
        result = search_matrix(matrix, target)
        # Assert
        self.assertFalse(result)

    # Empty matrix (no rows)
    def test_empty_matrix(self):
        # Arrange
        matrix = []
        target = 1
        # Act
        result = search_matrix(matrix, target)
        # Assert
        self.assertFalse(result)

    # Matrix with empty rows
    def test_matrix_with_empty_rows(self):
        # Arrange
        matrix = [[], []]
        target = 1
        # Act
        result = search_matrix(matrix, target)
        # Assert
        self.assertFalse(result)

    # Invalid input: matrix is None
    def test_none_matrix(self):
        # Arrange
        matrix = None
        target = 5
        # Act
        result = search_matrix(matrix, target)
        # Assert
        self.assertFalse(result)

    # Invalid input: target is not an integer (should safely return False)
    def test_non_integer_target(self):
        # Arrange
        matrix = [
            [1, 2, 3],
            [4, 5, 6]
        ]
        target = "5"
        # Act
        result = search_matrix(matrix, target)
        # Assert
        self.assertFalse(result)