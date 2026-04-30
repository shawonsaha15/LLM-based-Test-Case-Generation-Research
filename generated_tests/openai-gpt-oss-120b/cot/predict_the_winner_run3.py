import unittest
import random
from typing import List

class TestPredictTheWinner(unittest.TestCase):
    def brute_force(self, nums: List[int]) -> bool:
        """Return True if the first player can achieve a non‑negative score difference."""
        from functools import lru_cache

        @lru_cache(None)
        def helper(i: int, j: int) -> int:
            if i == j:
                return nums[i]
            # player picks left
            left = nums[i] - helper(i + 1, j)
            # player picks right
            right = nums[j] - helper(i, j - 1)
            return max(left, right)

        if not nums:
            raise IndexError("empty list")
        return helper(0, len(nums) - 1) >= 0

    def test_single_element(self):
        self.assertTrue(predict_the_winner([42]))

    def test_two_elements(self):
        self.assertTrue(predict_the_winner([1, 2]))
        self.assertTrue(predict_the_winner([2, 1]))

    def test_example_true(self):
        self.assertTrue(predict_the_winner([1, 5, 233, 7]))

    def test_example_false(self):
        self.assertFalse(predict_the_winner([1, 5, 2]))

    def test_negative_numbers(self):
        self.assertTrue(predict_the_winner([-1, -2, -3]))
        self.assertFalse(predict_the_winner([-1, -5, -2]))

    def test_empty_list_raises(self):
        with self.assertRaises(IndexError):
            predict_the_winner([])

    def test_none_input_raises(self):
        with self.assertRaises(TypeError):
            predict_the_winner(None)  # type: ignore

    def test_random_small_vs_bruteforce(self):
        for _ in range(100):
            length = random.randint(1, 6)
            nums = [random.randint(-10, 10) for _ in range(length)]
            expected = self.brute_force(nums)
            result = predict_the_winner(nums)
            self.assertEqual(result, expected, f"Failed for input {nums}")

    def test_large_input_performance(self):
        # Not a strict performance test, just ensures it runs without error on larger input.
        large_nums = [random.randint(0, 1000) for _ in range(200)]
        result = predict_the_winner(large_nums)
        self.assertIsInstance(result, bool)