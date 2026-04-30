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

    def test_normal_case(self):
        self.assertEqual(candy_distribution([1, 0, 2]), 5)

    def test_edge_case_empty_list(self):
        self.assertEqual(candy_distribution([]), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(candy_distribution([1]), 1)

    def test_edge_case_all_equal(self):
        self.assertEqual(candy_distribution([1, 1, 1]), 3)

    def test_edge_case_all_decreasing(self):
        self.assertEqual(candy_distribution([1, 2, 3]), 3)

    def test_edge_case_all_increasing(self):
        self.assertEqual(candy_distribution([3, 2, 1]), 3)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            candy_distribution("123")

    def test_invalid_input_value(self):
        with self.assertRaises(TypeError):
            candy_distribution([1, 2, '3'])

    def test_invalid_input_structure(self):
        with self.assertRaises(TypeError):
            candy_distribution(123)

    def test_large_input(self):
        ratings = [i for i in range(1000)]
        ratings[500] = 0
        self.assertEqual(candy_distribution(ratings), 500500)

if __name__ == "__main__":
    unittest.main()