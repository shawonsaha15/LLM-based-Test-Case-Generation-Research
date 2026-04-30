import unittest

class TestPredictTheWinner(unittest.TestCase):
    def test_single_element(self):
        self.assertTrue(predict_the_winner([1]))

    def test_two_elements_first_loses(self):
        self.assertFalse(predict_the_winner([1, 5]))

    def test_two_elements_tie(self):
        self.assertTrue(predict_the_winner([3, 3]))

    def test_three_elements_first_loses(self):
        self.assertFalse(predict_the_winner([1, 5, 2]))

    def test_four_elements_first_wins(self):
        self.assertTrue(predict_the_winner([1, 5, 233, 7]))

    def test_all_zeros(self):
        self.assertTrue(predict_the_winner([0, 0, 0]))

    def test_all_negative_numbers(self):
        self.assertFalse(predict_the_winner([-1, -2, -3]))

    def test_longer_sequence_first_wins(self):
        self.assertTrue(predict_the_winner([20, 30, 2, 2, 2, 10]))

    def test_alternating_high_low(self):
        self.assertTrue(predict_the_winner([5, 3, 4, 5, 3, 4, 5]))

    def test_large_numbers(self):
        self.assertTrue(predict_the_winner([1000, 2000, 3000, 4000, 5000]))