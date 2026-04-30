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
import random
from typing import List

class TestPredictTheWinner(unittest.TestCase):
    def test_single_element(self):
        self.assertTrue(predict_the_winner([42]))

    def test_two_elements_first_wins(self):
        self.assertTrue(predict_the_winner([10, 5]))

    def test_two_elements_second_wins(self):
        self.assertFalse(predict_the_winner([3, 7]))

    def test_example_true(self):
        self.assertTrue(predict_the_winner([1, 5, 233, 7]))

    def test_example_false(self):
        self.assertFalse(predict_the_winner([1, 5, 2]))

    def test_random_small(self):
        def brute(nums: List[int]) -> bool:
            from functools import lru_cache
            @lru_cache(None)
            def dfs(i, j):
                if i == j:
                    return nums[i]
                return max(nums[i] - dfs(i + 1, j), nums[j] - dfs(i, j - 1))
            return dfs(0, len(nums) - 1) >= 0

        for _ in range(20):
            lst = [random.randint(0, 20) for _ in range(random.randint(1, 8))]
            self.assertEqual(predict_the_winner(lst), brute(lst))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            predict_the_winner(None)

    def test_empty_list_raises(self):
        with self.assertRaises(IndexError):
            predict_the_winner([])

if __name__ == "__main__":
    unittest.main()