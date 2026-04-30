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

    def test_normal_input(self):
        self.assertTrue(predict_the_winner([1, 5, 2]))
        self.assertFalse(predict_the_winner([1, 5, 233, 7]))

    def test_edge_case_empty_list(self):
        with self.assertRaises(IndexError):
            predict_the_winner([])

    def test_edge_case_single_element(self):
        self.assertTrue(predict_the_winner([5]))

    def test_edge_case_two_elements(self):
        self.assertTrue(predict_the_winner([5, 3]))
        self.assertFalse(predict_the_winner([3, 5]))

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            predict_the_winner(123)

    def test_invalid_input_list_with_non_integers(self):
        with self.assertRaises(TypeError):
            predict_the_winner([1, 'a', 3])

if __name__ == '__main__':
    unittest.main()