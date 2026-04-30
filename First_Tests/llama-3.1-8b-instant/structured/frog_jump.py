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
from typing import List

class TestCanCross(unittest.TestCase):

    def test_normal_cases(self):
        self.assertTrue(can_cross([0, 2, 5, 10, 17, 20, 28, 35]))
        self.assertTrue(can_cross([0, 1, 2, 3, 4, 7, 10, 12, 19]))
        self.assertTrue(can_cross([0, 2, 5, 10, 17, 20, 28, 35, 42]))

    def test_edge_cases(self):
        self.assertTrue(can_cross([0]))
        self.assertTrue(can_cross([0, 0]))
        self.assertTrue(can_cross([0, 1, 0]))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            can_cross('hello')
        with self.assertRaises(TypeError):
            can_cross(123)
        with self.assertRaises(TypeError):
            can_cross([1, 2, 3, 'hello'])

if __name__ == "__main__":
    unittest.main()