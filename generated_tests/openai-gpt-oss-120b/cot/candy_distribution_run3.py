import unittest

class TestCandyDistribution(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(candy_distribution([]), 0)

    def test_single_element(self):
        self.assertEqual(candy_distribution([5]), 1)

    def test_increasing_ratings(self):
        ratings = [1, 2, 3, 4, 5]
        # Expected candies: 1+2+3+4+5 = 15
        self.assertEqual(candy_distribution(ratings), 15)

    def test_decreasing_ratings(self):
        ratings = [5, 4, 3, 2, 1]
        # Expected candies: 5+4+3+2+1 = 15
        self.assertEqual(candy_distribution(ratings), 15)

    def test_equal_ratings(self):
        ratings = [3, 3, 3, 3]
        # Each child gets exactly one candy
        self.assertEqual(candy_distribution(ratings), 4)

    def test_mixed_ratings(self):
        ratings = [1, 0, 2]
        # Expected distribution: [2,1,2] => total 5
        self.assertEqual(candy_distribution(ratings), 5)

        ratings = [1, 2, 2]
        # Expected distribution: [1,2,1] => total 4
        self.assertEqual(candy_distribution(ratings), 4)

        ratings = [2, 4, 3, 5, 2, 1, 2, 3]
        # Known answer from classic problem
        self.assertEqual(candy_distribution(ratings), 12)

    def test_large_increasing(self):
        n = 1000
        ratings = list(range(n))
        # Sum of first n natural numbers
        expected = n * (n + 1) // 2
        self.assertEqual(candy_distribution(ratings), expected)

    def test_invalid_none(self):
        with self.assertRaises(TypeError):
            candy_distribution(None)

    def test_invalid_non_iterable(self):
        with self.assertRaises(TypeError):
            candy_distribution(123)

    def test_invalid_non_comparable(self):
        # Mixing incomparable types should raise a TypeError during comparison
        with self.assertRaises(TypeError):
            candy_distribution([1, "a", 2])

    def test_return_type(self):
        result = candy_distribution([1, 2, 3])
        self.assertIsInstance(result, int)