import unittest

class TestPredictTheWinner(unittest.TestCase):
    def test_single_element(self):
        # With one number, first player trivially wins
        self.assertTrue(predict_the_winner([5]))

    def test_two_elements_first_player_wins(self):
        # First player can pick the larger number
        self.assertTrue(predict_the_winner([7, 3]))

    def test_two_elements_first_player_loses(self):
        # No matter what first player picks, second player can match or exceed
        self.assertFalse(predict_the_winner([2, 3]))

    def test_three_elements_first_player_wins(self):
        # Example where optimal play leads to first player victory
        self.assertTrue(predict_the_winner([1, 5, 2]))

    def test_three_elements_first_player_loses(self):
        # Example where second player can force a win
        self.assertFalse(predict_the_winner([1, 5, 233, 7][:3]))  # [1,5,233]

    def test_even_length_first_player_wins(self):
        # Classic LeetCode example where first player can win
        self.assertTrue(predict_the_winner([1, 5, 2, 4, 6]))

    def test_even_length_first_player_loses(self):
        # Constructed case where second player can force a win
        self.assertFalse(predict_the_winner([20, 30, 2, 2, 2, 10]))

    def test_large_input_all_equal(self):
        # All numbers equal; first player should win or tie (>=0)
        nums = [10] * 50
        self.assertTrue(predict_the_winner(nums))

    def test_large_input_random(self):
        # Mixed values; verify function runs without error and returns a bool
        nums = [3, 9, 1, 2, 7, 5, 8, 4, 6, 10]
        result = predict_the_winner(nums)
        self.assertIsInstance(result, bool)
        # Known outcome for this specific list (computed externally)
        self.assertTrue(result)