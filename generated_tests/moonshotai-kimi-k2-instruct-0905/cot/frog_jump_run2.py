import unittest

class TestCanCross(unittest.TestCase):

    def test_basic_crossable(self):
        # Normal case: can cross with steps 0->1->3->5
        self.assertTrue(can_cross([0, 1, 3, 5]))

    def test_basic_not_crossable(self):
        # Normal case: cannot cross due to gap too large
        self.assertFalse(can_cross([0, 1, 10]))

    def test_single_stone(self):
        # Edge case: only one stone (start), already at end
        self.assertTrue(can_cross([0]))

    def test_two_stones_zero_gap(self):
        # Edge case: two stones at same position (invalid but handled)
        self.assertFalse(can_cross([0, 0]))

    def test_two_stones_unit_gap(self):
        # Normal case: two stones, unit gap
        self.assertTrue(can_cross([0, 1]))

    def test_empty_input(self):
        # Edge case: empty list
        self.assertFalse(can_cross([]))

    def test_large_gap(self):
        # Edge case: gap larger than n
        self.assertFalse(can_cross([0, 100]))

    def test_negative_stones(self):
        # Invalid input: negative stone positions
        with self.assertRaises((ValueError, IndexError)):
            can_cross([-1, 0, 1])

    def test_unsorted_stones(self):
        # Invalid input: unsorted stones
        with self.assertRaises((ValueError, IndexError)):
            can_cross([0, 3, 1])

    def test_none_input(self):
        # Invalid input: None instead of list
        with self.assertRaises((TypeError)):
            can_cross(None)

    def test_large_values(self):
        # Edge case: large stone values but still crossable
        self.assertTrue(can_cross([0, 1, 3, 6, 10, 15]))

    def test_all_same_stones(self):
        # Edge case: all stones same position
        self.assertFalse(can_cross([0, 0, 0, 0]))

    def test_max_steps_increase(self):
        # Normal case: steps increase by one each time
        self.assertTrue(can_cross([0, 1, 3, 6, 10]))

    def test_max_steps_decrease(self):
        # Normal case: steps can decrease
        self.assertTrue(can_cross([0, 2, 3, 5, 6]))

    def test_no_valid_moves_after_start(self):
        # Edge case: no valid moves from start
        self.assertFalse(can_cross([0, 5]))

    def test_mutant_skip_k_check(self):
        # Logical fault: mutant might skip k > n check
        # This test would fail if k > n check is removed
        self.assertFalse(can_cross([0, 1, 100]))

    def test_mutant_wrong_index_in_dp(self):
        # Logical fault: mutant might use wrong index in dp[i][k]
        # This test would fail if dp[i][k] is set incorrectly
        self.assertTrue(can_cross([0, 1, 3]))

    def test_mutant_missing_any_check(self):
        # Logical fault: mutant might return dp[-1][some_fixed_k]
        # This test would fail if any(dp[-1]) is replaced with single index
        self.assertTrue(can_cross([0, 1, 3, 4]))