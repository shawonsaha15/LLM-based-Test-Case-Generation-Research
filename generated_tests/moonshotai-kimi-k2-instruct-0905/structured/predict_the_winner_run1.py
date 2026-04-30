import unittest


class TestPredictTheWinner(unittest.TestCase):

    # Normal cases
    def test_player1_can_win_with_simple_array(self):
        # Arrange
        nums = [1, 5, 2]
        # Act
        result = predict_the_winner(nums)
        # Assert
        self.assertTrue(result)

    def test_player2_wins_when_player1_cannot_force_win(self):
        # Arrange
        nums = [1, 5, 233, 7]
        # Act
        result = predict_the_winner(nums)
        # Assert
        self.assertFalse(result)

    def test_single_element_player1_wins_by_default(self):
        # Arrange
        nums = [10]
        # Act
        result = predict_the_winner(nums)
        # Assert
        self.assertTrue(result)

    def test_two_elements_player1_can_choose_max(self):
        # Arrange
        nums = [3, 9]
        # Act
        result = predict_the_winner(nums)
        # Assert
        self.assertTrue(result)

    # Boundary cases
    def test_empty_array_returns_true(self):
        # Arrange
        nums = []
        # Act
        result = predict_the_winner(nums)
        # Assert
        self.assertTrue(result)

    def test_all_equal_elements_even_length_draw(self):
        # Arrange
        nums = [4, 4, 4, 4]
        # Act
        result = predict_the_winner(nums)
        # Assert
        self.assertTrue(result)

    def test_all_equal_elements_odd_length_player1_wins(self):
        # Arrange
        nums = [7, 7, 7]
        # Act
        result = predict_the_winner(nums)
        # Assert
        self.assertTrue(result)

    def test_large_numbers_no_overflow(self):
        # Arrange
        nums = [10**9, 10**9, 10**9]
        # Act
        result = predict_the_winner(nums)
        # Assert
        self.assertTrue(result)

    # Invalid inputs (if applicable)
    def test_negative_numbers_allowed(self):
        # Arrange
        nums = [-1, -2, -3]
        # Act
        result = predict_the_winner(nums)
        # Assert
        self.assertTrue(result)

    def test_mixed_positive_negative(self):
        # Arrange
        nums = [5, -3, 2]
        # Act
        result = predict_the_winner(nums)
        # Assert
        self.assertTrue(result)

    def test_zeros_in_array(self):
        # Arrange
        nums = [0, 0, 0, 0]
        # Act
        result = predict_the_winner(nums)
        # Assert
        self.assertTrue(result)