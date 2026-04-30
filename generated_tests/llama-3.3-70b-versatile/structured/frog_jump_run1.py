class TestCanCross(unittest.TestCase):

    def test_normal_case(self):
        # Arrange
        stones = [0, 1, 3, 5, 6, 8, 12, 17]
        # Act
        result = can_cross(stones)
        # Assert
        self.assertTrue(result)

    def test_normal_case_false(self):
        # Arrange
        stones = [0, 1, 2, 3, 4, 8, 9, 10]
        # Act
        result = can_cross(stones)
        # Assert
        self.assertFalse(result)

    def test_boundary_case_empty(self):
        # Arrange
        stones = []
        # Act
        result = can_cross(stones)
        # Assert
        self.assertFalse(result)

    def test_boundary_case_single(self):
        # Arrange
        stones = [0]
        # Act
        result = can_cross(stones)
        # Assert
        self.assertFalse(result)

    def test_boundary_case_two(self):
        # Arrange
        stones = [0, 1]
        # Act
        result = can_cross(stones)
        # Assert
        self.assertTrue(result)

    def test_invalid_input_none(self):
        # Arrange
        stones = None
        # Act and Assert
        with self.assertRaises(TypeError):
            can_cross(stones)

    def test_invalid_input_not_list(self):
        # Arrange
        stones = "123"
        # Act and Assert
        with self.assertRaises(TypeError):
            can_cross(stones)

    def test_invalid_input_list_with_non_int(self):
        # Arrange
        stones = [0, 1, "2", 3]
        # Act and Assert
        with self.assertRaises(TypeError):
            can_cross(stones)

    def test_invalid_input_list_with_negative(self):
        # Arrange
        stones = [0, 1, -2, 3]
        # Act and Assert
        with self.assertRaises(TypeError):
            can_cross(stones)