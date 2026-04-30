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

    def test_normal_cases(self):
        self.assertEqual(candy_distribution([1, 0, 2]), 5)
        self.assertEqual(candy_distribution([1, 3, 2, 2, 1]), 7)
        self.assertEqual(candy_distribution([1, 2, 2]), 4)

    def test_edge_cases(self):
        self.assertEqual(candy_distribution([]), 0)
        self.assertEqual(candy_distribution([1]), 1)
        self.assertEqual(candy_distribution([1, 1]), 2)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            candy_distribution("123")
        with self.assertRaises(TypeError):
            candy_distribution([1, 2, '3'])
        with self.assertRaises(TypeError):
            candy_distribution([1, 2, 3.0])

if __name__ == "__main__":
    unittest.main()