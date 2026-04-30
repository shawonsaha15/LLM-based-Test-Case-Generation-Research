import unittest

class TestPredictTheWinner(unittest.TestCase):
    def test_single_element(self):
        self.assertTrue(predict_the_winner([5]))

    def test_two_elements_first_wins(self):
        self.assertTrue(predict_the_winner([7, 3]))

    def test_two_elements_second_wins(self):
        self.assertFalse(predict_the_winner([2, 5]))

    def test_two_elements_equal(self):
        self.assertTrue(predict_the_winner([4, 4]))

    def test_three_elements_first_loses(self):
        self.assertFalse(predict_the_winner([1, 5, 2]))

    def test_complex_case_true(self):
        self.assertTrue(predict_the_winner([1, 5, 233, 7]))

    def test_complex_case_false(self):
        self.assertFalse(predict_the_winner([8, 15, 3, 7]))

    def test_all_negative_even_length(self):
        self.assertTrue(predict_the_winner([-5, -5]))

    def test_all_negative_odd_length(self):
        self.assertFalse(predict_the_winner([-1, -2, -3]))

    def test_return_type_is_bool(self):
        result = predict_the_winner([1, 2])
        self.assertIsInstance(result, bool)