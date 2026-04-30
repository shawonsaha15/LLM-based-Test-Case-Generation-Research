import unittest

class TestPredictTheWinner(unittest.TestCase):
    # Normal cases
    def test_normal_case_simple_true(self):
        # Arrange
        nums = [1, 5, 233, 7]
        expected = True
        # Act
        result = predict_the_winner(nums)
        # Assert
        self.assertEqual(result, expected)

    def test_normal_case_simple_false(self):
        # Arrange
        nums = [1, 5, 2]
        expected = False
        # Act
        result = predict_the_winner(nums)
        # Assert
        self.assertEqual(result, expected)

    def test_normal_case_all_equal(self):
        # Arrange
        nums = [3, 3, 3, 3]
        expected = True  # first player can tie or win
        # Act
        result = predict_the_winner(nums)
        # Assert
        self.assertEqual(result, expected)

    # Boundary cases
    def test_boundary_single_element(self):
        # Arrange
        nums = [42]
        expected = True  # only one move, first player gets the only number
        # Act
        result = predict_the_winner(nums)
        # Assert
        self.assertEqual(result, expected)

    def test_boundary_two_elements_first_larger(self):
        # Arrange
        nums = [10, 1]
        expected = True
        # Act
        result = predict_the_winner(nums)
        # Assert
        self.assertEqual(result, expected)

    def test_boundary_two_elements_second_larger(self):
        # Arrange
        nums = [1, 10]
        expected = True  # first player picks the larger one
        # Act
        result = predict_the_winner(nums)
        # Assert
        self.assertEqual(result, expected)

    def test_boundary_large_input(self):
        # Arrange
        nums = [i for i in range(1, 21)]  # 1..20
        # For a strictly increasing sequence of even length, first player can always win
        expected = True
        # Act
        result = predict_the_winner(nums)
        # Assert
        self.assertEqual(result, expected)

    def test_boundary_negative_numbers(self):
        # Arrange
        nums = [-1, -2, -3, -4]
        expected = True  # picking the least negative values leads to a non‑negative score difference
        # Act
        result = predict_the_winner(nums)
        # Assert
        self.assertEqual(result, expected)

    # Invalid inputs
    def test_invalid_empty_list_raises(self):
        # Arrange
        nums = []
        # Act & Assert
        with self.assertRaises(IndexError):
            predict_the_winner(nums)

    def test_invalid_non_integer_elements_raises(self):
        # Arrange
        nums = [1, "a", 3]
        # Act & Assert
        with self.assertRaises(TypeError):
            predict_the_winner(nums)