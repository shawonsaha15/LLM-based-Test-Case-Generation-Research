import unittest

class TestCandyDistribution(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(candy_distribution([]), 0)

    def test_single_element(self):
        self.assertEqual(candy_distribution([5]), 1)

    def test_all_equal_ratings(self):
        ratings = [3, 3, 3, 3, 3]
        self.assertEqual(candy_distribution(ratings), len(ratings))

    def test_strictly_increasing(self):
        ratings = [1, 2, 3, 4, 5]
        # Expected candies: 1,2,3,4,5 => sum = 15
        self.assertEqual(candy_distribution(ratings), 15)

    def test_strictly_decreasing(self):
        ratings = [5, 4, 3, 2, 1]
        # Expected candies: 5,4,3,2,1 => sum = 15
        self.assertEqual(candy_distribution(ratings), 15)

    def test_mixed_ratings(self):
        ratings = [1, 2, 2, 1, 0, 1, 2, 3, 2, 1]
        # Expected total from manual calculation = 21
        self.assertEqual(candy_distribution(ratings), 21)

    def test_alternating_peaks(self):
        ratings = [1, 3, 2, 2, 1]
        # Expected candies: [1,2,1,2,1] => sum = 7
        self.assertEqual(candy_distribution(ratings), 7)

    def test_large_input(self):
        # Create a long increasing then decreasing sequence
        inc = list(range(1, 51))          # 1..50
        dec = list(range(49, 0, -1))      # 49..1
        ratings = inc + dec
        # For a perfect mountain, total candies = sum(1..50) + sum(1..49)
        expected = sum(range(1, 51)) + sum(range(1, 50))
        self.assertEqual(candy_distribution(ratings), expected)

    def test_none_input_raises(self):
        with self.assertRaises(TypeError):
            candy_distribution(None)

    def test_non_iterable_input_raises(self):
        with self.assertRaises(TypeError):
            candy_distribution(42)

    def test_non_integer_elements_raises(self):
        with self.assertRaises(TypeError):
            candy_distribution([1, "a", 3])