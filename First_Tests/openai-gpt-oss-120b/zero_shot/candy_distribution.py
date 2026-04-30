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

class TestCandy_distribution(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(candy_distribution([]), 0)

    def test_single(self):
        self.assertEqual(candy_distribution([5]), 1)

    def test_all_equal(self):
        self.assertEqual(candy_distribution([3, 3, 3, 3]), 4)

    def test_increasing(self):
        self.assertEqual(candy_distribution([1, 2, 3, 4]), 10)

    def test_decreasing(self):
        self.assertEqual(candy_distribution([4, 3, 2, 1]), 10)

    def test_valley(self):
        self.assertEqual(candy_distribution([5, 4, 3, 2, 3, 4, 5]), 16)

    def test_peak(self):
        self.assertEqual(candy_distribution([1, 2, 3, 2, 1]), 9)

    def test_complex(self):
        self.assertEqual(candy_distribution([1, 0, 2]), 5)

    def test_invalid_input(self):
        with self.assertRaises(Exception):
            candy_distribution(None)

if __name__ == "__main__":
    unittest.main()