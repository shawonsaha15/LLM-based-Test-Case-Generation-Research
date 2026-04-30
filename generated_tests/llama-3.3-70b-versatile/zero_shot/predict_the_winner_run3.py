class TestPredictTheWinner(unittest.TestCase):

    def test_predict_the_winner_empty_list(self):
        self.assertTrue(predict_the_winner([]))

    def test_predict_the_winner_single_element(self):
        self.assertTrue(predict_the_winner([1]))

    def test_predict_the_winner_two_elements_win(self):
        self.assertTrue(predict_the_winner([1, 2]))

    def test_predict_the_winner_two_elements_lose(self):
        self.assertFalse(predict_the_winner([-1, -2]))

    def test_predict_the_winner_multiple_elements_win(self):
        self.assertTrue(predict_the_winner([1, 2, 3]))

    def test_predict_the_winner_multiple_elements_lose(self):
        self.assertFalse(predict_the_winner([-1, -2, -3]))

    def test_predict_the_winner_large_list_win(self):
        self.assertTrue(predict_the_winner([1, 2, 3, 4, 5]))

    def test_predict_the_winner_large_list_lose(self):
        self.assertFalse(predict_the_winner([-1, -2, -3, -4, -5]))

    def test_predict_the_winner_list_with_zeros(self):
        self.assertTrue(predict_the_winner([0, 0, 0]))

    def test_predict_the_winner_list_with_negative_and_positive(self):
        self.assertTrue(predict_the_winner([-1, 2, -3, 4]))