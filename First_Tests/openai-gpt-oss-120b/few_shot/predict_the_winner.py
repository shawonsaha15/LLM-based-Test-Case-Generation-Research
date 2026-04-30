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
    def test_examples(self):
        self.assertFalse(predict_the_winner([1, 5, 2]))
        self.assertTrue(predict_the_winner([1, 5, 233, 7]))

    def test_single(self):
        self.assertTrue(predict_the_winner([0]))
        self.assertTrue(predict_the_winner([10]))

    def test_two(self):
        self.assertTrue(predict_the_winner([1, 1]))
        self.assertTrue(predict_the_winner([2, 1]))
        self.assertFalse(predict_the_winner([1, 2]))

    def test_all_equal(self):
        self.assertTrue(predict_the_winner([2, 2, 2, 2]))
        self.assertTrue(predict_the_winner([5, 5, 5, 5, 5]))

    def test_complex(self):
        self.assertTrue(predict_the_winner([3, 9, 1, 2]))
        self.assertFalse(predict_the_winner([1, 2, 3, 4, 5, 6, 7, 8, 9]))
        self.assertTrue(predict_the_winner([7, 8, 8, 10]))

if __name__ == "__main__":
    unittest.main()