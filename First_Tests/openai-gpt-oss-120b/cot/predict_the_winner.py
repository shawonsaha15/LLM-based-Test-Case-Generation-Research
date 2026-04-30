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

# Assume predict_the_winner is defined in the same module
# from your_module import predict_the_winner

class TestPredictTheWinner(unittest.TestCase):
    def test_single_element(self):
        self.assertTrue(predict_the_winner([10]))
        self.assertTrue(predict_the_winner([-5]))

    def test_two_elements(self):
        self.assertTrue(predict_the_winner([5, 3]))
        self.assertFalse(predict_the_winner([2, 7]))

    def test_example_cases(self):
        self.assertFalse(predict_the_winner([1, 5, 2]))
        self.assertTrue(predict_the_winner([1, 5, 233, 7]))
        self.assertTrue(predict_the_winner([0, 0]))
        self.assertTrue(predict_the_winner([7, 8, 8, 10]))

    def test_negative_numbers(self):
        self.assertFalse(predict_the_winner([-1, -2, -3]))
        self.assertTrue(predict_the_winner([-1, -1, -1, -1]))

    def test_large_numbers(self):
        nums = [10**9, 10**9 - 1, 10**9 - 2, 10**9 - 3]
        self.assertTrue(predict_the_winner(nums))

    def test_empty_list_raises(self):
        with self.assertRaises(IndexError):
            predict_the_winner([])

    def test_none_input_raises(self):
        with self.assertRaises(TypeError):
            predict_the_winner(None)

    def test_non_integer_elements(self):
        with self.assertRaises(TypeError):
            predict_the_winner([1, "a", 3])

if __name__ == "__main__":
    unittest.main()