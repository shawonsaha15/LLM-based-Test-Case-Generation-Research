import unittest

class TestCandyDistribution(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(candy_distribution([]), 0)

    def test_single_element(self):
        self.assertEqual(candy_distribution([5]), 1)

    def test_all_equal(self):
        self.assertEqual(candy_distribution([2, 2, 2, 2]), 4)

    def test_strictly_increasing(self):
        ratings = [1, 2, 3, 4, 5]
        expected = sum(range(1, len(ratings) + 1))  # 1+2+3+4+5 = 15
        self.assertEqual(candy_distribution(ratings), expected)

    def test_strictly_decreasing(self):
        ratings = [5, 4, 3, 2, 1]
        expected = sum(range(1, len(ratings) + 1))  # also 15
        self.assertEqual(candy_distribution(ratings), expected)

    def test_valley(self):
        ratings = [1, 2, 2, 1]
        # Expected distribution: [1,2,2,1] => total 6
        self.assertEqual(candy_distribution(ratings), 6)

    def test_peak(self):
        ratings = [1, 3, 4, 5, 2]
        # Expected distribution: [1,2,3,4,1] => total 11
        self.assertEqual(candy_distribution(ratings), 11)

    def test_negative_ratings(self):
        ratings = [-1, -2, -3]
        # Decreasing sequence, same as positive case
        self.assertEqual(candy_distribution(ratings), 6)

    def test_large_increasing(self):
        n = 1000
        ratings = list(range(n))
        expected = n * (n + 1) // 2  # sum of 1..n
        self.assertEqual(candy_distribution(ratings), expected)

    def test_large_decreasing(self):
        n = 1000
        ratings = list(range(n, 0, -1))
        expected = n * (n + 1) // 2
        self.assertEqual(candy_distribution(ratings), expected)

    def test_none_input_raises(self):
        with self.assertRaises(TypeError):
            candy_distribution(None)

    def test_non_integer_elements_raise(self):
        with self.assertRaises(TypeError):
            candy_distribution([1, "a", 3])