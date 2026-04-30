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
    def test_normal_cases(self):
        self.assertTrue(can_cross([0, 1, 3, 5, 6, 8, 12, 17]))
        self.assertFalse(can_cross([0, 1, 2, 3, 4, 8, 9, 11]))
    def test_edge_cases(self):
        self.assertTrue(can_cross([0, 1]))
        self.assertFalse(can_cross([0]))
        self.assertFalse(can_cross([0, 2]))
        self.assertTrue(can_cross([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    def test_invalid_inputs(self):
        with self.assertRaises(Exception):
            can_cross(None)
        with self.assertRaises(Exception):
            can_cross("invalid")
        with self.assertRaises(Exception):
            can_cross([0, "a", 2])

if __name__ == "__main__":
    unittest.main()