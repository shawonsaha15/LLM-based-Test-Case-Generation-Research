import unittest

class TestCanCross(unittest.TestCase):
    def test_single_stone(self):
        stones = [0]
        self.assertTrue(can_cross(stones))

    def test_two_stones_success(self):
        stones = [0, 1]
        self.assertTrue(can_cross(stones))

    def test_two_stones_failure(self):
        stones = [0, 2]
        self.assertFalse(can_cross(stones))

    def test_basic_success(self):
        stones = [0, 1, 3, 5, 6, 8, 12, 17]
        self.assertTrue(can_cross(stones))

    def test_basic_failure(self):
        stones = [0, 1, 2, 3, 4, 8, 9, 11]
        self.assertFalse(can_cross(stones))

    def test_unreachable_due_to_gap(self):
        stones = [0, 1, 3, 7, 12]
        self.assertFalse(can_cross(stones))

    def test_complex_success(self):
        stones = [0, 1, 2, 4, 7, 11, 16]
        self.assertTrue(can_cross(stones))

    def test_complex_failure(self):
        stones = [0, 1, 2, 5, 9, 14, 20, 27, 35, 44, 54, 65, 77, 90, 104, 119, 135]
        self.assertFalse(can_cross(stones))