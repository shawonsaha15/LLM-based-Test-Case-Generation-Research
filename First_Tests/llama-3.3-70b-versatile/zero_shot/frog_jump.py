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
    def test_normal_case(self):
        self.assertTrue(can_cross([0,1,3,5,6,8,12,17]))

    def test_edge_case_empty(self):
        self.assertFalse(can_cross([]))

    def test_edge_case_single(self):
        self.assertTrue(can_cross([0]))

    def test_edge_case_two(self):
        self.assertTrue(can_cross([0, 1]))

    def test_invalid_case_negative(self):
        with self.assertRaises(ValueError):
            can_cross([-1, 0, 1])

    def test_invalid_case_non_integer(self):
        with self.assertRaises(TypeError):
            can_cross([0, '1', 2])

    def test_invalid_case_non_list(self):
        with self.assertRaises(TypeError):
            can_cross('123')

    def test_large_input(self):
        self.assertTrue(can_cross([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

    def test_unreachable_stone(self):
        self.assertFalse(can_cross([0, 2, 4, 6, 8, 10, 100]))

if __name__ == "__main__":
    unittest.main()