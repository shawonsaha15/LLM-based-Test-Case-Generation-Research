import unittest

class TestCanCross(unittest.TestCase):
    def test_normal_true(self):
        # Arrange
        stones = [0, 1, 3, 5, 6, 8, 12, 17]
        # Act
        result = can_cross(stones)
        # Assert
        self.assertTrue(result)

    def test_normal_false(self):
        # Arrange
        stones = [0, 1, 2, 3, 4, 8, 9, 11]
        # Act
        result = can_cross(stones)
        # Assert
        self.assertFalse(result)

    def test_single_stone(self):
        # Arrange
        stones = [0]
        # Act
        result = can_cross(stones)
        # Assert
        self.assertTrue(result)

    def test_two_stones(self):
        # Arrange
        stones = [0, 1]
        # Act
        result = can_cross(stones)
        # Assert
        self.assertTrue(result)

    def test_boundary_max_jump(self):
        # Arrange
        # n = 5, maximum allowed jump length is 5; the last gap equals n
        stones = [0, 1, 2, 3, 4, 9]
        # Act
        result = can_cross(stones)
        # Assert
        self.assertTrue(result)

    def test_empty_list_raises(self):
        # Arrange
        stones = []
        # Act & Assert
        with self.assertRaises(IndexError):
            can_cross(stones)

    def test_negative_position_raises(self):
        # Arrange
        stones = [0, -1, 1]
        # Act & Assert
        with self.assertRaises(IndexError):
            can_cross(stones)

    def test_non_list_input_raises(self):
        # Arrange
        stones = "not a list"
        # Act & Assert
        with self.assertRaises(TypeError):
            can_cross(stones)