import unittest

class TestPredictTheWinner(unittest.TestCase):
    def test_single_element(self):
        self.assertTrue(predict_the_winner([5]))

    def test_two_elements_first_larger(self):
        self.assertTrue(predict_the_winner([5, 3]))

    def test_two_elements_second_larger(self):
        self.assertTrue(predict_the_winner([3, 5]))

    def test_three_elements_first_loses(self):
        self.assertFalse(predict_the_winner([1, 5, 2]))

    def test_three_elements_first_wins(self):
        self.assertTrue(predict_the_winner([2, 2, 2]))

    def test_even_length_first_wins(self):
        self.assertTrue(predict_the_winner([1, 5, 233, 7]))

    def test_large_numbers(self):
        self.assertTrue(predict_the_winner([1000, 2000, 3000, 4000]))

    def test_negative_numbers(self):
        self.assertFalse(predict_the_winner([-1, -2, -3]))

    def test_empty_list_raises(self):
        with self.assertRaises(IndexError):
            predict_the_winner([])

    def test_none_input_raises(self):
        with self.assertRaises(TypeError):
            predict_the_winner(None)

    def test_non_integer_elements_raises(self):
        with self.assertRaises(TypeError):
            predict_the_winner([1, "a", 3])