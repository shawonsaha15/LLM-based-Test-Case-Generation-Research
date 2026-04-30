import unittest


class TestCanCross(unittest.TestCase):

    def test_normal_case_crossable(self):
        # Arrange
        stones = [0, 1, 3, 6, 10, 15, 21, 28]
        # Act
        result = can_cross(stones)
        # Assert
        self.assertTrue(result)

    def test_normal_case_not_crossable(self):
        # Arrange
        stones = [0, 1, 2, 3, 4, 8, 9, 11]
        # Act
        result = can_cross(stones)
        # Assert
        self.assertFalse(result)

    def test_boundary_case_single_stone(self):
        # Arrange
        stones = [0]
        # Act
        result = can_cross(stones)
        # Assert
        self.assertTrue(result)

    def test_boundary_case_two_stones_unit_gap(self):
        # Arrange
        stones = [0, 1]
        # Act
        result = can_cross(stones)
        # Assert
        self.assertTrue(result)

    def test_boundary_case_two_stones_large_gap(self):
        # Arrange
        stones = [0, 5]
        # Act
        result = can_cross(stones)
        # Assert
        self.assertFalse(result)

    def test_boundary_case_max_jump_exactly_n(self):
        # Arrange
        stones = [0, 1, 3, 6, 10, 15, 21, 28, 36]
        # Act
        result = can_cross(stones)
        # Assert
        self.assertTrue(result)

    def test_boundary_case_max_jump_n_plus_one(self):
        # Arrange
        stones = [0, 1, 3, 6, 10, 15, 21, 28, 37]
        # Act
        result = can_cross(stones)
        # Assert
        self.assertFalse(result)

    def test_invalid_input_empty_list(self):
        # Arrange
        stones = []
        # Act & Assert
        with self.assertRaises(IndexError):
            can_cross(stones)

    def test_invalid_input_non_sequential_stones(self):
        # Arrange
        stones = [0, 5, 3, 10]
        # Act
        result = can_cross(stones)
        # Assert
        self.assertFalse(result)

    def test_invalid_input_negative_stones(self):
        # Arrange
        stones = [-1, 0, 2, 5]
        # Act
        result = can_cross(stones)
        # Assert
        self.assertFalse(result)