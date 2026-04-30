class TestPredictTheWinner(unittest.TestCase):
    def test_predict_the_winner_base_case(self):
        nums = [5]
        self.assertTrue(predict_the_winner(nums))

    def test_predict_the_winner_two_elements(self):
        nums = [1, 2]
        self.assertTrue(predict_the_winner(nums))

    def test_predict_the_winner_three_elements(self):
        nums = [1, 5, 2]
        self.assertTrue(predict_the_winner(nums))

    def test_predict_the_winner_four_elements(self):
        nums = [1, 5, 233, 7]
        self.assertTrue(predict_the_winner(nums))

    def test_predict_the_winner_large_input(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertTrue(predict_the_winner(nums))

    def test_predict_the_winner_negative_numbers(self):
        nums = [-1, -2, -3]
        self.assertFalse(predict_the_winner(nums))

    def test_predict_the_winner_zero(self):
        nums = [0, 0, 0]
        self.assertTrue(predict_the_winner(nums))

    def test_predict_the_winner_empty_list(self):
        nums = []
        with self.assertRaises(IndexError):
            predict_the_winner(nums)