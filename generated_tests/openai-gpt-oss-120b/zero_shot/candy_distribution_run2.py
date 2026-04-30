import unittest

class TestCandyDistribution(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(candy_distribution([]), 0)

    def test_single(self):
        self.assertEqual(candy_distribution([10]), 1)

    def test_increasing(self):
        ratings = [1, 2, 3, 4, 5]
        # Expected candies: 1,2,3,4,5 => total 15
        self.assertEqual(candy_distribution(ratings), 15)

    def test_decreasing(self):
        ratings = [5, 4, 3, 2, 1]
        # Expected candies: 5,4,3,2,1 => total 15
        self.assertEqual(candy_distribution(ratings), 15)

    def test_equal(self):
        ratings = [7, 7, 7, 7]
        # All get 1 candy each
        self.assertEqual(candy_distribution(ratings), 4)

    def test_valley(self):
        ratings = [5, 1, 5]
        # Expected distribution: [2,1,2] => total 5
        self.assertEqual(candy_distribution(ratings), 5)

    def test_peak(self):
        ratings = [1, 5, 1]
        # Expected distribution: [1,2,1] => total 4
        self.assertEqual(candy_distribution(ratings), 4)

    def test_complex(self):
        ratings = [1, 0, 2]
        # Expected distribution: [2,1,2] => total 5
        self.assertEqual(candy_distribution(ratings), 5)

    def test_plateau(self):
        ratings = [1, 2, 2]
        # Expected distribution: [1,2,1] => total 4
        self.assertEqual(candy_distribution(ratings), 4)