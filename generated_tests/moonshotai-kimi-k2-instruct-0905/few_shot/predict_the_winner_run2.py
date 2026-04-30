class TestPredictTheWinner(unittest.TestCase):
    def test_player1_wins(self):
        result = predict_the_winner([1, 5, 2])
        self.assertTrue(result)

    def test_player2_wins(self):
        result = predict_the_winner([1, 5, 233, 7])
        self.assertFalse(result)

    def test_single_element(self):
        result = predict_the_winner([5])
        self.assertTrue(result)

    def test_two_elements_player1_wins(self):
        result = predict_the_winner([3, 9])
        self.assertTrue(result)

    def test_all_equal(self):
        result = predict_the_winner([4, 4, 4, 4])
        self.assertTrue(result)

    def test_empty_list(self):
        result = predict_the_winner([])
        self.assertTrue(result)