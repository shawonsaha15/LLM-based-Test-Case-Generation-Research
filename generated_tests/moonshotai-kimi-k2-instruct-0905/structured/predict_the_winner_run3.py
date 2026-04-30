import unittest


class TestPredictTheWinner(unittest.TestCase):

    def test_single_element_player1_wins(self):
        # Arrange
        nums = [5]
        # Act
        result = predict_the_winner(nums)
        # Assert
        self.assertTrue(result)

    def test_two_elements_player1_can_win(self):
        # Arrange
        nums = [1, 2]
        # Act
        result = predict_the_winner(nums)
        # Assert
        self.assertTrue(result)

    def test_two_elements_player1_can_lose(self):
        # Arrange
        nums = [2, 1]
        # Act
        result = predict_the_winner(nums)
        # Assert
        self.assertTrue(result)

    def test_even_length_player1_wins(self):
        # Arrange
        nums = [1, 5, 233, 7]
        # Act
        result = predict_the_winner(nums)
        # Assert
        self.assertTrue(result)

    def test_odd_length_player1_loses(self):
        # Arrange
        nums = [1, 5, 2]
        # Act
        result = predict_the_winner(nums)
        # Assert
        self.assertFalse(result)

    def test_all_equal_elements(self):
        # Arrange
        nums = [4, 4, 4, 4]
        # Act
        result = predict_the_winner(nums)
        # Assert
        self.assertTrue(result)

    def test_ascending_order(self):
        # Arrange
        nums = [1, 2, 3, 4, 5]
        # Act
        result = predict_the_winner(nums)
        # Assert
        self.assertFalse(result)

    def test_descending_order(self):
        # Arrange
        nums = [5, 4, 3, 2, 1]
        # Act
        result = predict_the_winner(nums)
        # Assert
        self.assertTrue(result)

    def test_large_numbers(self):
        # Arrange
        nums = [1000000, 1, 1, 1000000]
        # Act
        result = predict_the_winner(nums)
        # Assert
        self.assertTrue(result)

    def test_zeros_and_negatives(self):
        # Arrange
        nums = [0, -1, 0, -1]
        # Act
        result = predict_the_winner(nums)
        # Assert
        self.assertTrue(result)

    def test_empty_list(self):
        # Arrange
        nums = []
        # Act
        result = predict_the_winner(nums)
        # Assert
        self.assertTrue(result)

    def test_negative_numbers_only(self):
        # Arrange
        nums = [-3, -2, -5]
        # Act
        result = predict_the_winner(nums)
        # Assert
        self.assertFalse(result)