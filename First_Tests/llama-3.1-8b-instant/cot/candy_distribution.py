def candy_distribution(ratings: list[int]) -> int:
    n = len(ratings)

    if n == 0:
        return 0

    left = [1] * n
    right = [1] * n

    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            left[i] = left[i - 1] + 1

    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            right[i] = right[i + 1] + 1

    total = 0
    for l_val, r_val in zip(left, right):
        total += max(l_val, r_val)

    return total

import unittest

class TestCandyDistribution(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(candy_distribution([]), 0)

    def test_single_element_list(self):
        self.assertEqual(candy_distribution([1]), 1)

    def test_increasing_ratings(self):
        self.assertEqual(candy_distribution([1, 2, 3, 4, 5]), 15)

    def test_decreasing_ratings(self):
        self.assertEqual(candy_distribution([5, 4, 3, 2, 1]), 5)

    def test_constant_ratings(self):
        self.assertEqual(candy_distribution([1, 1, 1, 1, 1]), 5)

    def test_mixed_ratings(self):
        self.assertEqual(candy_distribution([1, 2, 3, 2, 1]), 7)

    def test_negative_ratings(self):
        self.assertEqual(candy_distribution([1, -2, 3, -4, 5]), 9)

    def test_zero_ratings(self):
        self.assertEqual(candy_distribution([0, 0, 0, 0, 0]), 5)

    def test_large_ratings(self):
        self.assertEqual(candy_distribution([100, 200, 300, 400, 500]), 1500)

if __name__ == '__main__':
    unittest.main()