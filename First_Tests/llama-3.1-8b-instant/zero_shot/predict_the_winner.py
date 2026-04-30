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

    def test_normal_case(self):
        self.assertTrue(predict_the_winner([1, 2, 3, 4]))

    def test_edge_case_single_element(self):
        self.assertTrue(predict_the_winner([5]))

    def test_edge_case_two_elements(self):
        self.assertTrue(predict_the_winner([1, 2]))

    def test_invalid_case_empty_list(self):
        with self.assertRaises(IndexError):
            predict_the_winner([])

    def test_invalid_case_non_list_input(self):
        with self.assertRaises(TypeError):
            predict_the_winner("1234")

    def test_invalid_case_non_integer_input(self):
        with self.assertRaises(TypeError):
            predict_the_winner([1, 2, "3", 4])

    def test_invalid_case_negative_numbers(self):
        self.assertTrue(predict_the_winner([-1, -2, -3, -4]))

    def test_invalid_case_zero(self):
        self.assertTrue(predict_the_winner([0, 0, 0, 0]))

if __name__ == "__main__":
    unittest.main()