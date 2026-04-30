import unittest

class TestCandyDistribution(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(candy_distribution([]), 0)

    def test_single_child(self):
        self.assertEqual(candy_distribution([5]), 1)

    def test_all_equal_ratings(self):
        self.assertEqual(candy_distribution([3, 3, 3]), 3)

    def test_strictly_increasing(self):
        self.assertEqual(candy_distribution([1, 2, 3, 4]), 10)

    def test_strictly_decreasing(self):
        self.assertEqual(candy_distribution([4, 3, 2, 1]), 10)

    def test_valley_pattern(self):
        # Ratings: 1 < 2 == 2
        # Expected candies: [1, 2, 1] => total 4
        self.assertEqual(candy_distribution([1, 2, 2]), 4)

    def test_peak_pattern(self):
        # Ratings: 1 < 3 > 2 == 2 > 1
        # Expected candies: [1, 2, 1, 2, 1] => total 7
        self.assertEqual(candy_distribution([1, 3, 2, 2, 1]), 7)

    def test_classic_example(self):
        # Ratings: 1 > 0 < 2
        # Expected candies: [2, 1, 2] => total 5
        self.assertEqual(candy_distribution([1, 0, 2]), 5)

    def test_complex_mixed(self):
        # Mixed ratings to test both passes
        ratings = [1, 2, 2, 3, 2, 1, 2, 3, 2, 1]
        # Manually computed expected total = 19
        self.assertEqual(candy_distribution(ratings), 19)