import unittest

class TestCandyDistribution(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(candy_distribution([]), 0)

    def test_single_child(self):
        self.assertEqual(candy_distribution([5]), 1)

    def test_all_equal_ratings(self):
        ratings = [3, 3, 3, 3, 3]
        self.assertEqual(candy_distribution(ratings), len(ratings))

    def test_strictly_increasing(self):
        ratings = [1, 2, 3, 4, 5]
        # Expected candies: 1,2,3,4,5 -> sum = 15
        self.assertEqual(candy_distribution(ratings), 15)

    def test_strictly_decreasing(self):
        ratings = [5, 4, 3, 2, 1]
        # Expected candies: 5,4,3,2,1 -> sum = 15
        self.assertEqual(candy_distribution(ratings), 15)

    def test_valley_pattern(self):
        ratings = [1, 0, 2]
        # Expected candies: 2,1,2 -> sum = 5
        self.assertEqual(candy_distribution(ratings), 5)

    def test_plateau_after_increase(self):
        ratings = [1, 2, 2]
        # Expected candies: 1,2,1 -> sum = 4
        self.assertEqual(candy_distribution(ratings), 4)

    def test_plateau_before_decrease(self):
        ratings = [2, 2, 1]
        # Expected candies: 1,2,1 -> sum = 4
        self.assertEqual(candy_distribution(ratings), 4)

    def test_complex_mixed_ratings(self):
        ratings = [1, 3, 4, 5, 2]
        # Expected candies: 1,2,3,4,1 -> sum = 11
        self.assertEqual(candy_distribution(ratings), 11)

    def test_multiple_peaks_and_valleys(self):
        ratings = [1, 2, 2, 1, 2, 3, 2, 1]
        # Expected candies: 1,2,1,1,2,3,2,1 -> sum = 13
        self.assertEqual(candy_distribution(ratings), 13)