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
    def test_empty(self):
        self.assertEqual(candy_distribution([]), 0)

    def test_single(self):
        self.assertEqual(candy_distribution([5]), 1)

    def test_increasing(self):
        self.assertEqual(candy_distribution([1, 2, 3, 4]), 10)

    def test_decreasing(self):
        self.assertEqual(candy_distribution([4, 3, 2, 1]), 10)

    def test_equal_ratings(self):
        self.assertEqual(candy_distribution([2, 2, 2]), 3)

    def test_mixed(self):
        self.assertEqual(candy_distribution([1, 0, 2]), 5)

    def test_plateau(self):
        self.assertEqual(candy_distribution([1, 2, 2]), 4)

    def test_complex(self):
        self.assertEqual(candy_distribution([2, 4, 3, 5, 2, 1]), 10)

if __name__ == "__main__":
    unittest.main()