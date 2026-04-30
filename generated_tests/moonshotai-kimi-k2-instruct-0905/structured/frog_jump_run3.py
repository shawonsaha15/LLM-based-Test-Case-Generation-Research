import unittest


class TestCanCross(unittest.TestCase):
    def test_normal_crossable_path(self):
        # Arrange
        stones = [0, 1, 3, 5, 6, 8, 12, 17]
        # Act
        result = can_cross(stones)
        # Assert
        self.assertTrue(result)

    def test_normal_uncrossable_gap(self):
        # Arrange
        stones = [0, 1, 2, 3, 4, 8, 9, 11]
        # Act
        result = can_cross(stones)
        # Assert
        self.assertFalse(result)

    def test_boundary_single_stone(self):
        # Arrange
        stones = [0]
        # Act
        result = can_cross(stones)
        # Assert
        self.assertTrue(result)

    def test_boundary_two_stones_reachable(self):
        # Arrange
        stones = [0, 1]
        # Act
        result = can_cross(stones)
        # Assert
        self.assertTrue(result)

    def test_boundary_two_stones_unreachable(self):
        # Arrange
        stones = [0, 2]
        # Act
        result = can_cross(stones)
        # Assert
        self.assertFalse(result)

    def test_boundary_large_gap_at_start(self):
        # Arrange
        stones = [0, 5, 10]
        # Act
        result = can_cross(stones)
        # Assert
        self.assertFalse(result)

    def test_invalid_empty_list(self):
        # Arrange
        stones = []
        # Act & Assert
        with self.assertRaises(IndexError):
            can_cross(stones)

    def test_normal_three_stones_valid_jump_sequence(self):
        # Arrange
        stones = [0, 1, 3]
        # Act
        result = can_cross(stones)
        # Assert
        self.assertTrue(result)

    def test_boundary_max_jumps_increasing(self):
        # Arrange
        stones = [0, 1, 3, 6, 10, 15, 21, 28]
        # Act
        result = can_cross(stones)
        # Assert
        self.assertTrue(result)

    def test_normal_duplicate_stones_not_possible(self):
        # Arrange
        stones = [0, 1, 1, 2]
        # Act
        result = can_cross(stones)
        # Assert
        self.assertFalse(result)