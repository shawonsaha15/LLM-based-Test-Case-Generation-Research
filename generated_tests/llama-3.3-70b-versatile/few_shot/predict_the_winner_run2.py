class TestPredictTheWinner(unittest.TestCase):
    def test_win(self):
        result = predict_the_winner([1, 5, 2])
        self.assertTrue(result)

    def test_lose(self):
        result = predict_the_winner([1, 2, 5])
        self.assertFalse(result)

    def test_tie(self):
        result = predict_the_winner([1, 1, 1])
        self.assertTrue(result)

    def test_single_element(self):
        result = predict_the_winner([5])
        self.assertTrue(result)

    def test_empty_list(self):
        with self.assertRaises(IndexError):
            predict_the_winner([])

    def test_large_list(self):
        result = predict_the_winner([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertTrue(result)

    def test_negative_numbers(self):
        result = predict_the_winner([-1, -2, -3])
        self.assertFalse(result)

    def test_mixed_numbers(self):
        result = predict_the_winner([-1, 2, -3])
        self.assertFalse(result)