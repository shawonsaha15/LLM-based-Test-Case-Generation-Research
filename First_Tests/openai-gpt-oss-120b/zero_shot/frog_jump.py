from typing import List


def can_cross(stones: List[int]) -> bool:
    n = len(stones)
    dp = [[False] * (n + 1) for _ in range(n)]
    dp[0][0] = True

    for i in range(1, n):
        for j in range(i):
            k = stones[i] - stones[j]
            if k > n:
                continue
            for x in (k - 1, k, k + 1):
                if 0 <= x <= n and dp[j][x]:
                    dp[i][k] = True

    return any(dp[-1])

import unittest

class TestCanCross(unittest.TestCase):
    def test_basic_true(self):
        stones = [0, 1, 3, 5, 6, 8, 12, 17]
        self.assertTrue(can_cross(stones))

    def test_basic_false(self):
        stones = [0, 1, 2, 3, 4, 8, 9, 11]
        self.assertFalse(can_cross(stones))

    def test_single_stone(self):
        stones = [0]
        self.assertTrue(can_cross(stones))

    def test_two_stones(self):
        stones = [0, 1]
        self.assertTrue(can_cross(stones))

    def test_large_gap(self):
        stones = [0, 2]
        self.assertFalse(can_cross(stones))

    def test_unsorted_input(self):
        stones = [0, 3, 1, 5, 6]
        self.assertFalse(can_cross(stones))

    def test_negative_positions(self):
        stones = [0, -1, 1, 2]
        self.assertFalse(can_cross(stones))

    def test_empty_list(self):
        stones = []
        with self.assertRaises(IndexError):
            can_cross(stones)

    def test_non_integer_elements(self):
        stones = [0, 1.5, 3]
        with self.assertRaises(TypeError):
            can_cross(stones)

if __name__ == "__main__":
    unittest.main()