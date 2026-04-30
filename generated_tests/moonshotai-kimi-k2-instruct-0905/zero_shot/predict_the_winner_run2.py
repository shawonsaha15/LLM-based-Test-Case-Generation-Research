import unittest

class TestPredictTheWinner(unittest.TestCase):

    def test_single_element_player1_wins(self):
        self.assertTrue(predict_the_winner([5]))

    def test_two_elements_player1_can_win(self):
        self.assertTrue(predict_the_winner([1, 5]))

    def test_two_elements_player1_cannot_win(self):
        self.assertFalse(predict_the_winner([1, 2]))

    def test_three_elements_player1_wins(self):
        self.assertTrue(predict_the_winner([1, 5, 2]))

    def test_three_elements_player1_loses(self):
        self.assertFalse(predict_the_winner([1, 2, 3]))

    def test_four_elements_draw(self):
        self.assertTrue(predict_the_winner([1, 2, 2, 1]))

    def test_four_elements_player1_wins(self):
        self.assertTrue(predict_the_winner([2, 4, 1, 5]))

    def test_five_elements_player1_wins(self):
        self.assertTrue(predict_the_winner([3, 9, 1, 2, 7]))

    def test_five_elements_player1_loses(self):
        self.assertFalse(predict_the_winner([1, 1, 1, 2, 2]))

    def test_large_input_player1_wins(self):
        self.assertTrue(predict_the_winner([10, 15, 20, 5, 1, 8]))

    def test_large_input_player1_loses(self):
        self.assertFalse(predict_the_winner([1, 1, 1, 1, 1, 1, 1, 1, 1]))