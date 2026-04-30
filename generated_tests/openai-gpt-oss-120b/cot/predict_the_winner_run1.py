import unittest

class TestPredictTheWinner(unittest.TestCase):
    def test_single_element(self):
        self.assertTrue(predict_the_winner([5]), "Single element should always return True")

    def test_two_elements(self):
        cases = [
            ([1, 2], True),
            ([2, 1], True),
            ([0, 0], True),
            ([-1, -2], True),  # first can pick the larger (less negative) number
        ]
        for nums, expected in cases:
            with self.subTest(nums=nums):
                self.assertEqual(predict_the_winner(nums), expected)

    def test_known_outcomes(self):
        cases = [
            ([1, 5, 2], False),
            ([1, 5, 233, 7], True),
            ([1, 2, 3, 4], True),
            ([0, 0, 0], True),
            ([10, 100, 10, 100, 10], True),
            ([7, 8, 8, 10], True),
        ]
        for nums, expected in cases:
            with self.subTest(nums=nums):
                self.assertEqual(predict_the_winner(nums), expected)

    def test_large_values(self):
        large_nums = [10**12, 10**12 - 1, 10**12 - 2, 10**12 - 3]
        # First player can take the largest number and still win/tie
        self.assertTrue(predict_the_winner(large_nums))

    def test_empty_list_raises(self):
        with self.assertRaises(IndexError):
            predict_the_winner([])

    def test_none_input_raises(self):
        with self.assertRaises(TypeError):
            predict_the_winner(None)

    def test_non_integer_elements_raises(self):
        with self.assertRaises(TypeError):
            predict_the_winner(['a', 1, 2])

    def test_mixed_negative_and_positive(self):
        cases = [
            ([-1, 2, -3, 4], True),
            ([-5, -3, -2, -1], True),
            ([-10, 5, 2, 1], False),
        ]
        for nums, expected in cases:
            with self.subTest(nums=nums):
                self.assertEqual(predict_the_winner(nums), expected)