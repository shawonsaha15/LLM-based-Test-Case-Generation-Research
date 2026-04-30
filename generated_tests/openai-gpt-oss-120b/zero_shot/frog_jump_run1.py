import unittest

class TestCanCross(unittest.TestCase):
    def test_example_true(self):
        stones = [0, 1, 3, 5, 6, 8, 12, 17]
        self.assertTrue(can_cross(stones))

    def test_example_false(self):
        stones = [0, 1, 2, 3, 4, 8, 9, 11]
        self.assertFalse(can_cross(stones))

    def test_single_stone(self):
        stones = [0]
        self.assertTrue(can_cross(stones))

    def test_two_stones_unreachable(self):
        stones = [0, 2]
        self.assertFalse(can_cross(stones))

    def test_consecutive_stones(self):
        stones = list(range(0, 11))  # [0, 1, 2, ..., 10]
        self.assertTrue(can_cross(stones))

    def test_large_gap_ignored(self):
        stones = [0, 1, 100]
        self.assertFalse(can_cross(stones))

    def test_gap_equal_to_n(self):
        # Gap exactly equal to number of stones should be considered
        stones = [0, 1, 3, 6, 10]  # n = 5, last gap = 4 (<= n)
        self.assertTrue(can_cross(stones))

    def test_complex_reachable(self):
        stones = [0, 1, 3, 4, 5, 7, 9, 10, 12, 14, 17, 21, 22]
        self.assertTrue(can_cross(stones))

    def test_complex_unreachable(self):
        stones = [0, 1, 2, 5, 6, 7, 11, 12, 13, 17, 18, 19, 23]
        self.assertFalse(can_cross(stones))