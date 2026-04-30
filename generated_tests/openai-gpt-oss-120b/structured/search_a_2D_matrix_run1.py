import unittest

class TestSearchMatrix(unittest.TestCase):
    def test_target_present_middle(self):
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

    def test_target_absent(self):
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

    def test_target_first_element(self):
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

    def test_target_last_element(self):
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

    def test_single_row(self):
        # Arrange
        matrix = [[-5, -3, 0, 2, 4]]
        target_present = 0
        target_absent = 1

        # Act
        result_present = search_matrix(matrix, target_present)
        result_absent = search_matrix(matrix, target_absent)

        # Assert
        self.assertTrue(result_present)
        self.assertFalse(result_absent)

    def test_single_column(self):
        # Arrange
        matrix = [
            [-10],
            [-5],
            [0],
            [5],
            [10]
        ]
        target_present = 5
        target_absent = 3

        # Act
        result_present = search_matrix(matrix, target_present)
        result_absent = search_matrix(matrix, target_absent)

        # Assert
        self.assertTrue(result_present)
        self.assertFalse(result_absent)

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

    def test_none_input(self):
        # Arrange
        matrix = None
        target = 1

        # Act
        result = search_matrix(matrix, target)

        # Assert
        self.assertFalse(result)

    def test_negative_numbers(self):
        # Arrange
        matrix = [
            [-20, -15, -10],
            [-5, 0, 5],
            [10, 15, 20]
        ]
        target_present = -5
        target_absent = -7

        # Act
        result_present = search_matrix(matrix, target_present)
        result_absent = search_matrix(matrix, target_absent)

        # Assert
        self.assertTrue(result_present)
        self.assertFalse(result_absent)