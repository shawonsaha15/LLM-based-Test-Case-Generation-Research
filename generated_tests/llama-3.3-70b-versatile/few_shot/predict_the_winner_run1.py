class TestPredictTheWinner(unittest.TestCase):
    def test_winning_game(self):
        result = predict_the_winner([1, 5, 2])
        self.assertTrue(result)

    def test_losing_game(self):
        result = predict_the_winner([1, 5, 100])
        self.assertFalse(result)

    def test_tied_game(self):
        result = predict_the_winner([1, 1])
        self.assertTrue(result)

    def test_single_element(self):
        result = predict_the_winner([5])
        self.assertTrue(result)

    def test_empty_list(self):
        with self.assertRaises(IndexError):
            predict_the_winner([])