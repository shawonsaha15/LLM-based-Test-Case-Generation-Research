class TestPredictTheWinner(unittest.TestCase):
    def test_tied_game(self):
        result = predict_the_winner([1, -1])
        self.assertTrue(result)

    def test_winning_game(self):
        result = predict_the_winner([5, -3])
        self.assertTrue(result)

    def test_losing_game(self):
        result = predict_the_winner([-5, 3])
        self.assertFalse(result)

    def test_single_element(self):
        result = predict_the_winner([5])
        self.assertTrue(result)

    def test_empty_list(self):
        with self.assertRaises(IndexError):
            predict_the_winner([])

    def test_large_list(self):
        result = predict_the_winner([1, -1, 1, -1, 1])
        self.assertTrue(result)

    def test_all_positive(self):
        result = predict_the_winner([1, 2, 3, 4, 5])
        self.assertTrue(result)

    def test_all_negative(self):
        result = predict_the_winner([-1, -2, -3, -4, -5])
        self.assertFalse(result)