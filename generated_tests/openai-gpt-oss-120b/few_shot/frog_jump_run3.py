import unittest

class TestCanCross(unittest.TestCase):
    def test_single_stone(self):
        # Only the starting stone; should be trivially reachable.
        self.assertTrue(can_cross([0]))

    def test_two_stones_reachable(self):
        # First jump of length 1 lands on the second stone.
        self.assertTrue(can_cross([0, 1]))

    def test_two_stones_unreachable(self):
        # First jump must be 1, but the next stone is at distance 2.
        self.assertFalse(can_cross([0, 2]))

    def test_classic_reachable_example(self):
        # Classic LeetCode example where the frog can cross.
        stones = [0, 1, 3, 5, 6, 8, 12, 17]
        self.assertTrue(can_cross(stones))

    def test_classic_unreachable_example(self):
        # Classic LeetCode example where the frog cannot cross.
        stones = [0, 1, 2, 3, 4, 8, 9, 11]
        self.assertFalse(can_cross(stones))

    def test_large_gap_prevents_crossing(self):
        # A gap larger than the number of stones makes crossing impossible.
        stones = [0, 1, 2, 3, 4, 20, 21, 22]
        self.assertFalse(can_cross(stones))

    def test_multiple_small_jumps(self):
        # Many small jumps that eventually allow reaching the last stone.
        stones = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertTrue(can_cross(stones))

    def test_no_initial_jump_possible(self):
        # The first stone after 0 is farther than 1, making the first jump impossible.
        stones = [0, 3, 4, 5, 6]
        self.assertFalse(can_cross(stones))