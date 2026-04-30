import unittest

class TestCandyDistribution(unittest.TestCase):

    def test_normal_case_ascending(self):
        self.assertEqual(candy_distribution([1, 2, 3]), 6)

    def test_normal_case_descending(self):
        self.assertEqual(candy_distribution([3, 2, 1]), 6)

    def test_normal_case_mixed(self):
        self.assertEqual(candy_distribution([1, 0, 2]), 5)

    def test_all_equal(self):
        self.assertEqual(candy_distribution([5, 5, 5]), 3)

    def test_single_element(self):
        self.assertEqual(candy_distribution([7]), 1)

    def test_two_increasing(self):
        self.assertEqual(candy_distribution([1, 2]), 3)

    def test_two_decreasing(self):
        self.assertEqual(candy_distribution([2, 1]), 3)

    def test_two_equal(self):
        self.assertEqual(candy_distribution([3, 3]), 2)

    def test_empty_list(self):
        self.assertEqual(candy_distribution([]), 0)

    def test_large_values(self):
        ratings = [1000000, 1000001, 1000002]
        self.assertEqual(candy_distribution(ratings), 6)

    def test_peak_in_middle(self):
        self.assertEqual(candy_distribution([1, 3, 2, 1]), 7)

    def test_valley_in_middle(self):
        self.assertEqual(candy_distribution([3, 2, 1, 2]), 7)

    def test_alternating_high_low(self):
        self.assertEqual(candy_distribution([1, 3, 1, 3, 1]), 9)

    def test_long_increasing(self):
        ratings = list(range(1, 101))
        expected = sum(range(1, 101))
        self.assertEqual(candy_distribution(ratings), expected)

    def test_long_decreasing(self):
        ratings = list(range(100, 0, -1))
        expected = sum(range(1, 101))
        self.assertEqual(candy_distribution(ratings), expected)

    def test_negative_ratings(self):
        self.assertEqual(candy_distribution([-3, -2, -1]), 6)

    def test_mixed_negative_positive(self):
        self.assertEqual(candy_distribution([-1, 0, 1]), 6)

    def test_zero_included(self):
        self.assertEqual(candy_distribution([0, 1, 0]), 5)

    def test_all_zeros(self):
        self.assertEqual(candy_distribution([0, 0, 0]), 3)

    def test_large_input_size(self):
        ratings = [1] * 10000
        self.assertEqual(candy_distribution(ratings), 10000)