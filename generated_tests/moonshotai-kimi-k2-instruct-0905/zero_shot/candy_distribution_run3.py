import unittest

class TestCandyDistribution(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(candy_distribution([]), 0)

    def test_single_child(self):
        self.assertEqual(candy_distribution([5]), 1)

    def test_two_equal_ratings(self):
        self.assertEqual(candy_distribution([3, 3]), 2)

    def test_increasing_ratings(self):
        self.assertEqual(candy_distribution([1, 2, 3]), 6)

    def test_decreasing_ratings(self):
        self.assertEqual(candy_distribution([3, 2, 1]), 6)

    def test_mixed_ratings(self):
        self.assertEqual(candy_distribution([1, 0, 2]), 5)

    def test_all_same_ratings(self):
        self.assertEqual(candy_distribution([4, 4, 4, 4]), 4)

    def test_peak_in_middle(self):
        self.assertEqual(candy_distribution([1, 3, 2, 2, 1]), 7)

    def test_large_increase_then_decrease(self):
        self.assertEqual(candy_distribution([1, 2, 3, 4, 5, 3, 2, 1]), 22)

    def test_alternating_high_low(self):
        self.assertEqual(candy_distribution([5, 3, 5, 3, 5]), 9)