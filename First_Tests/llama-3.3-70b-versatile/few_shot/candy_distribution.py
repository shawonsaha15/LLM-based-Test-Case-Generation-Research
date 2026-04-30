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
    def test_basic(self):
        self.assertEqual(candy_distribution([1, 0, 2]), 5)
        self.assertEqual(candy_distribution([1, 2, 2]), 4)

    def test_edge(self):
        self.assertEqual(candy_distribution([]), 0)
        self.assertEqual(candy_distribution([1]), 1)

    def test_equal_ratings(self):
        self.assertEqual(candy_distribution([1, 1, 1]), 3)

    def test_increasing_ratings(self):
        self.assertEqual(candy_distribution([1, 2, 3]), 6)

    def test_decreasing_ratings(self):
        self.assertEqual(candy_distribution([3, 2, 1]), 6)

if __name__ == "__main__":
    unittest.main()