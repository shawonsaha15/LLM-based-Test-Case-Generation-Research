class TestSearchMatrix:
    def test_normal_case_found(self, search_matrix):
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
        assert result is True

    def test_normal_case_not_found(self, search_matrix):
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
        assert result is False

    def test_boundary_case_first_element(self, search_matrix):
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
        assert result is True

    def test_boundary_case_last_element(self, search_matrix):
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
        assert result is True

    def test_invalid_input_empty_matrix(self, search_matrix):
        # Arrange
        matrix = []
        target = 1

        # Act
        result = search_matrix(matrix, target)

        # Assert
        assert result is False

    def test_invalid_input_matrix_with_empty_rows(self, search_matrix):
        # Arrange
        matrix = [
            [],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]
        target = 1

        # Act
        result = search_matrix(matrix, target)

        # Assert
        assert result is False

    def test_invalid_input_none_matrix(self, search_matrix):
        # Arrange
        matrix = None
        target = 1

        # Act
        result = search_matrix(matrix, target)

        # Assert
        assert result is False

    def test_invalid_input_none_target(self, search_matrix):
        # Arrange
        matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]
        target = None

        # Act
        result = search_matrix(matrix, target)

        # Assert
        assert result is False