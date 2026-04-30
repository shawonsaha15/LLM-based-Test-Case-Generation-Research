import unittest


class TestPredictTheWinner(unittest.TestCase):

    # Normal cases
    def test_player1_can_win(self):
        # Arrange
        nums = [1, 5, 2]
        # Act
        result = predict_the_winner(nums)
        # Assert
        self.assertTrue(result)

    def test_player1_cannot_win(self):
        # Arrange
        nums = [1, 5, 233, 7]
        # Act
        result = predict_the_winner(nums)
        # Assert
        self.assertFalse(result)

    def test_single_element_player1_wins(self):
        # Arrange
        nums = [5]
        # Act
        result = predict_the_winner(nums)
        # Assert
        self.assertTrue(result)

    def test_two_elements_player1_wins(self):
        # Arrange
        nums = [3, 9]
        # Act
        result = predict_the_winner(nums)
        # Assert
        self.assertTrue(result)

    def test_two_elements_player1_loses(self):
        # Arrange
        nums = [9, 3]
        # Act
        result = predict_the_winner(nums)
        # Assert
        self.assertTrue(result)

    # Boundary cases
    def test_empty_list(self):
        # Arrange
        nums = []
        # Act
        result = predict_the_winner(nums)
        # Assert
        self.assertTrue(result)

    def test_all_zeros(self):
        # Arrange
        nums = [0, 0, 0, 0]
        # Act
        result = predict_the_winner(nums)
        # Assert
        self.assertTrue(result)

    def test_large_numbers(self):
        # Arrange
        nums = [10**9, 10**9, 10**9]
        # Act
        result = predict_the_winner(nums)
        # Assert
        self.assertTrue(result)

    def test_alternating_high_low(self):
        # Arrange
        nums = [100, 1, 100, 1, 100]
        # Act
        result = predict_the_winner(nums)
        # Assert
        self.assertTrue(result)

    # Invalid inputs (not applicable due to type hints, but testing robustness)
    def test_negative_numbers(self):
        # Arrange
        nums = [-1, -5, -3]
        # Act
        result = predict_the_winner(nums)
        # Assert
        self.assertTrue(result)

    def test_mixed_negative_positive(self):
        # Arrange
        nums = [-1, 5, -3, 2]
        # Act
        result = predict_the_winner(nums)
        # Assert
        self.assertTrue(result)