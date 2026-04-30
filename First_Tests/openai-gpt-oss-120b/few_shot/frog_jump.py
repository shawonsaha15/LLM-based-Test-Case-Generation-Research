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
    def test_single_stone(self):
        self.assertTrue(can_cross([0]))

    def test_two_stones_success(self):
        self.assertTrue(can_cross([0, 1]))

    def test_two_stones_failure(self):
        self.assertFalse(can_cross([0, 2]))

    def test_basic_success(self):
        self.assertTrue(can_cross([0, 1, 3, 5, 6, 8, 12, 17]))

    def test_basic_failure(self):
        self.assertFalse(can_cross([0, 1, 2, 3, 4, 8, 9, 11]))

    def test_no_possible_jumps(self):
        self.assertFalse(can_cross([0, 2, 5, 9, 14]))

    def test_long_sequence_success(self):
        self.assertTrue(can_cross([0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105]))

    def test_long_sequence_failure(self):
        self.assertFalse(can_cross([0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 106]))

if __name__ == "__main__":
    unittest.main()