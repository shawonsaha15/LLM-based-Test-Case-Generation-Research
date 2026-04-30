import unittest


class TestCanCross(unittest.TestCase):

    # Normal Cases
    def test_normal_crossable(self):
        # Arrange
        stones = [0, 1, 3, 5, 6, 8, 12, 17]
        # Act
        result = can_cross(stones)
        # Assert
        self.assertTrue(result)

    def test_normal_not_crossable(self):
        # Arrange
        stones = [0, 1, 2, 3, 4, 8, 9, 11]
        # Act
        result = can_cross(stones)
        # Assert
        self.assertFalse(result)

    def test_minimal_crossable(self):
        # Arrange
        stones = [0, 1]
        # Act
        result = can_cross(stones)
        # Assert
        self.assertTrue(result)

    # Boundary Cases
    def test_single_stone(self):
        # Arrange
        stones = [0]
        # Act
        result = can_cross(stones)
        # Assert
        self.assertTrue(result)

    def test_two_stones_non_consecutive(self):
        # Arrange
        stones = [0, 2]
        # Act
        result = can_cross(stones)
        # Assert
        self.assertFalse(result)

    def test_large_gaps(self):
        # Arrange
        stones = [0, 100, 200]
        # Act
        result = can_cross(stones)
        # Assert
        self.assertFalse(result)

    # Invalid Inputs
    def test_empty_list(self):
        # Arrange
        stones = []
        # Act
        result = can_cross(stones)
        # Assert
        self.assertFalse(result)

    def test_negative_stones(self):
        # Arrange
        stones = [-1, 0, 1]
        # Act
        result = can_cross(stones)
        # Assert
        self.assertFalse(result)

    def test_non_increasing_stones(self):
        # Arrange
        stones = [0, 3, 2, 5]
        # Act
        result = can_cross(stones)
        # Assert
        self.assertFalse(result)