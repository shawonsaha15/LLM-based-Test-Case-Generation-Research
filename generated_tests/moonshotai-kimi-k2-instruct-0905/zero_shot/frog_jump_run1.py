import unittest

class TestCanCross(unittest.TestCase):
    def test_single_stone(self):
        stones = [0]
        self.assertTrue(can_cross(stones))

    def test_two_stones_no_jump_possible(self):
        stones = [0, 2]
        self.assertFalse(can_cross(stones))

    def test_two_stones_jump_possible(self):
        stones = [0, 1]
        self.assertTrue(can_cross(stones))

    def test_three_stones_valid_path(self):
        stones = [0, 1, 3]
        self.assertTrue(can_cross(stones))

    def test_three_stones_no_valid_path(self):
        stones = [0, 2, 5]
        self.assertFalse(can_cross(stones))

    def test_example_case(self):
        stones = [0, 1, 3, 5, 6, 8, 12, 17]
        self.assertTrue(can_cross(stones))

    def test_impossible_case(self):
        stones = [0, 1, 2, 3, 4, 8, 9, 11]
        self.assertFalse(can_cross(stones))

    def test_large_gaps(self):
        stones = [0, 10, 20, 30]
        self.assertFalse(can_cross(stones))

    def test_consecutive_stones(self):
        stones = [0, 1, 2, 3, 4, 5]
        self.assertTrue(can_cross(stones))

    def test_empty_list(self):
        stones = []
        self.assertFalse(can_cross(stones))