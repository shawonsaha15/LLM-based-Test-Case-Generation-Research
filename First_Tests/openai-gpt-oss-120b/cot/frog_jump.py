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
    def test_example_true(self):
        self.assertTrue(can_cross([0, 1, 3, 5, 6, 8, 12, 17]))

    def test_example_false(self):
        self.assertFalse(can_cross([0, 1, 2, 3, 4, 8, 9, 11]))

    def test_single_stone(self):
        self.assertTrue(can_cross([0]))

    def test_two_stones_unreachable(self):
        self.assertFalse(can_cross([0, 2]))

    def test_two_stones_reachable(self):
        self.assertTrue(can_cross([0, 1]))

    def test_unsorted_input(self):
        self.assertFalse(can_cross([0, 2, 1]))

    def test_continuous_one_step(self):
        self.assertTrue(can_cross([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

    def test_large_gap_exceeds_n(self):
        self.assertFalse(can_cross([0, 1, 2, 3, 4, 5, 20]))

    def test_negative_positions(self):
        self.assertFalse(can_cross([-1, 0, 1, 3]))

if __name__ == "__main__":
    unittest.main()