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

    def test_normal_case(self):
        self.assertTrue(predict_the_winner([1, 5, 2]))

    def test_normal_case_false(self):
        self.assertFalse(predict_the_winner([1, 5, 233, 7]))

    def test_empty_list(self):
        with self.assertRaises(IndexError):
            predict_the_winner([])

    def test_single_element_list(self):
        self.assertTrue(predict_the_winner([5]))

    def test_two_element_list(self):
        self.assertTrue(predict_the_winner([5, 3]))

    def test_two_element_list_false(self):
        self.assertFalse(predict_the_winner([3, 5]))

    def test_large_list(self):
        self.assertTrue(predict_the_winner([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

    def test_list_with_zeros(self):
        self.assertTrue(predict_the_winner([0, 0, 0, 0, 0]))

    def test_list_with_negative_numbers(self):
        self.assertFalse(predict_the_winner([-1, -2, -3, -4, -5]))

if __name__ == "__main__":
    unittest.main()