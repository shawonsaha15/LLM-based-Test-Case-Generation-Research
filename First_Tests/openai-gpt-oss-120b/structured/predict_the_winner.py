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

class TestPredictTheWinner(unittest.TestCase):
    def test_normal_cases(self):
        self.assertFalse(predict_the_winner([1, 5, 2]))
        self.assertTrue(predict_the_winner([1, 5, 233, 7]))
        self.assertTrue(predict_the_winner([3, 9, 1, 2]))
        self.assertFalse(predict_the_winner([1, 2, 3, 4, 5, 6]))

    def test_edge_cases(self):
        self.assertTrue(predict_the_winner([0]))
        self.assertTrue(predict_the_winner([10]))
        self.assertTrue(predict_the_winner([5, 5]))
        self.assertFalse(predict_the_winner([5, 3, 4, 5]))
        self.assertTrue(predict_the_winner([7, 7, 7, 7, 7]))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            predict_the_winner(None)
        with self.assertRaises(TypeError):
            predict_the_winner("not a list")
        with self.assertRaises(TypeError):
            predict_the_winner([1, "two", 3])

if __name__ == "__main__":
    unittest.main()