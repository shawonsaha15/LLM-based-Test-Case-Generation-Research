import unittest

class TestCandyDistribution(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(candy_distribution([]), 0)

    def test_single_child(self):
        self.assertEqual(candy_distribution([5]), 1)

    def test_all_equal_ratings(self):
        self.assertEqual(candy_distribution([3, 3, 3]), 3)

    def test_increasing_ratings(self):
        self.assertEqual(candy_distribution([1, 2, 3]), 6)

    def test_decreasing_ratings(self):
        self.assertEqual(candy_distribution([3, 2, 1]), 6)

    def test_peak_in_middle(self):
        self.assertEqual(candy_distribution([1, 3, 2]), 5)

    def test_valley_in_middle(self):
        self.assertEqual(candy_distribution([3, 1, 2]), 4)

    def test_large_values(self):
        ratings = [1000000, 2000000, 3000000]
        self.assertEqual(candy_distribution(ratings), 6)

    def test_two_children_increasing(self):
        self.assertEqual(candy_distribution([1, 2]), 3)

    def test_two_children_decreasing(self):
        self.assertEqual(candy_distribution([2, 1]), 3)

    def test_two_children_equal(self):
        self.assertEqual(candy_distribution([2, 2]), 2)

    def test_alternating_high_low(self):
        self.assertEqual(candy_distribution([1, 5, 1, 5, 1]), 9)

    def test_long_increasing_sequence(self):
        ratings = list(range(1, 101))
        expected = sum(range(1, 101))
        self.assertEqual(candy_distribution(ratings), expected)

    def test_long_decreasing_sequence(self):
        ratings = list(range(100, 0, -1))
        expected = sum(range(1, 101))
        self.assertEqual(candy_distribution(ratings), expected)

    def test_mixed_sequence(self):
        ratings = [1, 2, 2, 3, 3, 3, 2, 1]
        self.assertEqual(candy_distribution(ratings), 12)

    def test_zero_ratings(self):
        self.assertEqual(candy_distribution([0, 0, 0]), 3)

    def test_negative_ratings(self):
        self.assertEqual(candy_distribution([-3, -2, -1]), 6)

    def test_all_same_negative(self):
        self.assertEqual(candy_distribution([-5, -5, -5]), 3)