import unittest
from typing import List

class TestPredictTheWinner(unittest.TestCase):
    # Normal cases
    def test_normal_case_simple_win(self):
        # Arrange
        nums: List[int] = [1, 5, 233, 7]

        # Act
        result = predict_the_winner(nums)

        # Assert
        self.assertTrue(result, "Player 1 should be able to win or tie with [1,5,233,7]")

    def test_normal_case_simple_loss(self):
        # Arrange
        nums: List[int] = [1, 5, 2]

        # Act
        result = predict_the_winner(nums)

        # Assert
        self.assertFalse(result, "Player 1 should lose with [1,5,2]")

    def test_normal_case_all_equal(self):
        # Arrange
        nums: List[int] = [4, 4, 4, 4]

        # Act
        result = predict_the_winner(nums)

        # Assert
        self.assertTrue(result, "Tie should be considered a win for player 1")

    # Boundary cases
    def test_boundary_single_element(self):
        # Arrange
        nums: List[int] = [42]

        # Act
        result = predict_the_winner(nums)

        # Assert
        self.assertTrue(result, "Single element list should always return True")

    def test_boundary_two_elements_first_larger(self):
        # Arrange
        nums: List[int] = [10, 1]

        # Act
        result = predict_the_winner(nums)

        # Assert
        self.assertTrue(result, "Player 1 picks the larger of two numbers and wins")

    def test_boundary_two_elements_second_larger(self):
        # Arrange
        nums: List[int] = [1, 10]

        # Act
        result = predict_the_winner(nums)

        # Assert
        self.assertTrue(result, "Player 1 picks the larger of two numbers and wins")

    def test_boundary_two_elements_equal(self):
        # Arrange
        nums: List[int] = [7, 7]

        # Act
        result = predict_the_winner(nums)

        # Assert
        self.assertTrue(result, "Equal numbers should result in a tie, which is a win for player 1")

    def test_boundary_large_numbers(self):
        # Arrange
        nums: List[int] = [10**12, 10**12 - 1, 10**12 - 2, 10**12 - 3]

        # Act
        result = predict_the_winner(nums)

        # Assert
        self.assertTrue(result, "Player 1 should win with optimal play even with large integer values")

    # Invalid inputs
    def test_invalid_input_empty_list(self):
        # Arrange
        nums: List[int] = []

        # Act & Assert
        with self.assertRaises(IndexError):
            predict_the_winner(nums)

    def test_invalid_input_non_integer(self):
        # Arrange
        nums: List[int] = [1, "two", 3]

        # Act & Assert
        with self.assertRaises(TypeError):
            predict_the_winner(nums)

    def test_invalid_input_none(self):
        # Arrange
        nums = None  # type: ignore

        # Act & Assert
        with self.assertRaises(TypeError):
            predict_the_winner(nums)