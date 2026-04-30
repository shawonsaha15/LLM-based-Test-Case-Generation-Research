import unittest

class TestCandyDistribution(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(candy_distribution([]), 0)

    def test_single_element(self):
        self.assertEqual(candy_distribution([10]), 1)

    def test_all_equal_ratings(self):
        ratings = [5, 5, 5, 5]
        self.assertEqual(candy_distribution(ratings), len(ratings))

    def test_strictly_increasing(self):
        ratings = [1, 2, 3, 4, 5]
        # Expected candies: 1+2+3+4+5 = 15
        self.assertEqual(candy_distribution(ratings), 15)

    def test_strictly_decreasing(self):
        ratings = [5, 4, 3, 2, 1]
        # Expected candies: 5+4+3+2+1 = 15
        self.assertEqual(candy_distribution(ratings), 15)

    def test_simple_mixed(self):
        ratings = [1, 0, 2]
        # Expected candies: 2 + 1 + 2 = 5
        self.assertEqual(candy_distribution(ratings), 5)

    def test_plateau(self):
        ratings = [1, 2, 2]
        # Expected candies: 1 + 2 + 1 = 4
        self.assertEqual(candy_distribution(ratings), 4)

    def test_complex_case(self):
        ratings = [1, 3, 4, 5, 2]
        # Expected candies: 1 + 2 + 3 + 4 + 1 = 11
        self.assertEqual(candy_distribution(ratings), 11)

    def test_alternating_high_low(self):
        ratings = [1, 3, 2, 2, 1]
        # Expected candies: left = [1,2,1,1,1], right = [1,2,2,1,1] => max = [1,2,2,1,1] sum = 7
        self.assertEqual(candy_distribution(ratings), 7)