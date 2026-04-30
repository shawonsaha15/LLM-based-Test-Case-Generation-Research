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
    def test_empty_list(self):
        self.assertTrue(predict_the_winner([]))

    def test_single_element_list(self):
        self.assertTrue(predict_the_winner([1]))

    def test_two_element_list(self):
        self.assertTrue(predict_the_winner([1, 2]))
        self.assertTrue(predict_the_winner([2, 1]))

    def test_three_element_list(self):
        self.assertTrue(predict_the_winner([1, 2, 3]))
        self.assertTrue(predict_the_winner([3, 2, 1]))

    def test_negative_numbers(self):
        self.assertTrue(predict_the_winner([-1, 1]))
        self.assertTrue(predict_the_winner([1, -1]))

    def test_zero_sum(self):
        self.assertTrue(predict_the_winner([0, 0]))

if __name__ == "__main__":
    unittest.main()