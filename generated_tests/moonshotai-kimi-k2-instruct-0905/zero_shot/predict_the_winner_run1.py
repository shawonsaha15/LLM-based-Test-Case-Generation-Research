import unittest


class TestPredictTheWinner(unittest.TestCase):

    def test_single_element_player1_wins(self):
        self.assertTrue(predict_the_winner([5]))

    def test_two_elements_player1_can_win(self):
        self.assertTrue(predict_the_winner([1, 2]))

    def test_player1_cannot_win(self):
        self.assertFalse(predict_the_winner([1, 5, 2]))

    def test_player1_can_win_with_optimal_play(self):
        self.assertTrue(predict_the_winner([1, 5, 233, 7]))

    def test_all_equal_elements(self):
        self.assertTrue(predict_the_winner([3, 3, 3, 3]))

    def test_empty_list(self):
        self.assertTrue(predict_the_winner([]))

    def test_negative_numbers(self):
        self.assertTrue(predict_the_winner([-1, -2, -3]))

    def test_large_numbers(self):
        self.assertTrue(predict_the_winner([1000000, 1000000, 1000000]))

    def test_alternating_high_low(self):
        self.assertTrue(predict_the_winner([10, 1, 100, 1]))

    def test_odd_length_player1_wins(self):
        self.assertTrue(predict_the_winner([2, 4, 6, 8, 10]))

    def test_even_length_player1_wins(self):
        self.assertTrue(predict_the_winner([3, 9, 1, 2]))

    def test_strictly_decreasing(self):
        self.assertTrue(predict_the_winner([5, 4, 3, 2, 1]))

    def test_strictly_increasing(self):
        self.assertTrue(predict_the_winner([1, 2, 3, 4, 5]))

    def test_all_zeros(self):
        self.assertTrue(predict_the_winner([0, 0, 0, 0]))

    def test_two_same_one_large(self):
        self.assertFalse(predict_the_winner([1, 1, 100]))