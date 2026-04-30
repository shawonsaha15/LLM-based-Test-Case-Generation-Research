import unittest

class TestCandyDistribution(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(candy_distribution([]), 0)

    def test_single_child(self):
        self.assertEqual(candy_distribution([5]), 1)

    def test_two_children_increasing(self):
        self.assertEqual(candy_distribution([1, 2]), 3)

    def test_two_children_decreasing(self):
        self.assertEqual(candy_distribution([2, 1]), 3)

    def test_all_equal_ratings(self):
        self.assertEqual(candy_distribution([3, 3, 3]), 3)

    def test_increasing_sequence(self):
        self.assertEqual(candy_distribution([1, 2, 3, 4, 5]), 15)

    def test_decreasing_sequence(self):
        self.assertEqual(candy_distribution([5, 4, 3, 2, 1]), 15)

    def test_peak_in_middle(self):
        self.assertEqual(candy_distribution([1, 3, 2, 2, 1]), 7)

    def test_valley_in_middle(self):
        self.assertEqual(candy_distribution([3, 2, 1, 2, 3]), 13)

    def test_alternating_high_low(self):
        self.assertEqual(candy_distribution([1, 5, 1, 5, 1]), 9)

    def test_large_peak(self):
        self.assertEqual(candy_distribution([1, 2, 5, 3, 2, 1]), 12)

    def test_all_same_except_one(self):
        self.assertEqual(candy_distribution([2, 2, 2, 5, 2]), 9)