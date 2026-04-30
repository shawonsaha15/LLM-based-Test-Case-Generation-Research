class TestCanCross(unittest.TestCase):

    def test_normal_case(self):
        # Arrange
        stones = [0, 1, 3, 5, 6, 8, 12, 17]
        expected_result = True

        # Act
        result = can_cross(stones)

        # Assert
        self.assertEqual(result, expected_result)

    def test_normal_case_false(self):
        # Arrange
        stones = [0, 1, 2, 3, 4, 8, 9, 10]
        expected_result = False

        # Act
        result = can_cross(stones)

        # Assert
        self.assertEqual(result, expected_result)

    def test_boundary_case_single_stone(self):
        # Arrange
        stones = [0]
        expected_result = True

        # Act
        result = can_cross(stones)

        # Assert
        self.assertEqual(result, expected_result)

    def test_boundary_case_two_stones(self):
        # Arrange
        stones = [0, 1]
        expected_result = True

        # Act
        result = can_cross(stones)

        # Assert
        self.assertEqual(result, expected_result)

    def test_boundary_case_large_distance(self):
        # Arrange
        stones = [0, 1000]
        expected_result = False

        # Act
        result = can_cross(stones)

        # Assert
        self.assertEqual(result, expected_result)

    def test_invalid_input_empty_list(self):
        # Arrange
        stones = []
        expected_result = False

        # Act
        result = can_cross(stones)

        # Assert
        self.assertEqual(result, expected_result)

    def test_invalid_input_duplicate_stones(self):
        # Arrange
        stones = [0, 0, 1, 2, 3]
        expected_result = False

        # Act
        result = can_cross(stones)

        # Assert
        self.assertEqual(result, expected_result)

    def test_invalid_input_unsorted_stones(self):
        # Arrange
        stones = [3, 1, 0, 2]
        expected_result = False

        # Act
        result = can_cross(stones)

        # Assert
        self.assertEqual(result, expected_result)

    def test_invalid_input_negative_stones(self):
        # Arrange
        stones = [0, -1, 2, 3]
        with self.assertRaises(ValueError):
            can_cross(stones)

    def test_invalid_input_non_integer_stones(self):
        # Arrange
        stones = [0, 1.5, 2, 3]
        with self.assertRaises(TypeError):
            can_cross(stones)