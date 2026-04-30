import unittest

class TestCanCross(unittest.TestCase):
    def test_single_stone(self):
        stones = [0]
        self.assertTrue(can_cross(stones))

    def test_two_stones(self):
        stones = [0, 1]
        self.assertTrue(can_cross(stones))

    def test_impossible_jump(self):
        stones = [0, 2]
        self.assertFalse(can_cross(stones))

    def test_typical_case(self):
        stones = [0, 1, 3, 5, 6, 8, 12, 17]
        self.assertTrue(can_cross(stones))

    def test_impossible_case(self):
        stones = [0, 1, 2, 3, 4, 8, 9, 11]
        self.assertFalse(can_cross(stones))

    def test_large_gap(self):
        stones = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        self.assertTrue(can_cross(stones))

    def test_empty_list(self):
        stones = []
        self.assertFalse(can_cross(stones))

    def test_no_jump_needed(self):
        stones = [0, 1]
        self.assertTrue(can_cross(stones))

    def test_negative_stones(self):
        stones = [0, -1, -3]
        self.assertFalse(can_cross(stones))

    def test_non_sequential_stones(self):
        stones = [0, 1, 3, 6, 10, 15, 21, 28]
        self.assertTrue(can_cross(stones))