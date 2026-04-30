from typing import List


def predict_the_winner(nums: List[int]) -> bool:
    n = len(nums)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = nums[i]

    for diagonal in range(1, n):
        for i in range(n - diagonal):
            j = i + diagonal
            dp[i][j] = max(
                nums[i] - dp[i + 1][j],
                nums[j] - dp[i][j - 1]
            )

    return dp[0][n - 1] >= 0

import unittest
from typing import List

class TestPredictTheWinner(unittest.TestCase):

    def test_normal_cases(self):
        self.assertTrue(predict_the_winner([1, 2, 3, 4]))
        self.assertTrue(predict_the_winner([2, 2, 2, 2]))
        self.assertTrue(predict_the_winner([1, 1, 1, 1]))

    def test_edge_cases(self):
        self.assertTrue(predict_the_winner([1]))
        self.assertTrue(predict_the_winner([]))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            predict_the_winner("1234")
        with self.assertRaises(TypeError):
            predict_the_winner(1234)
        with self.assertRaises(TypeError):
            predict_the_winner([1, 2, 3, "4"])

if __name__ == "__main__":
    unittest.main()