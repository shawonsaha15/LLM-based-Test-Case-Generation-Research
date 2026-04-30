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

    def test_two_stones_possible(self):
        stones = [0, 1]
        self.assertTrue(can_cross(stones))

    def test_two_stones_impossible(self):
        stones = [0, 2]
        self.assertFalse(can_cross(stones))

    def test_consecutive_stones(self):
        stones = list(range(0, 11))  # [0, 1, 2, ..., 10]
        self.assertTrue(can_cross(stones))

    def test_triangular_numbers_possible(self):
        # Stones at positions of triangular numbers: 0,1,3,6,10,15,21,28,36,45,55
        stones = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
        self.assertTrue(can_cross(stones))

    def test_large_gap_impossible(self):
        stones = [0, 1, 3, 6, 10, 15, 21, 28, 36, 44]  # last gap is 8, too large to reach
        self.assertFalse(can_cross(stones))

    def test_return_type(self):
        stones = [0, 1, 3, 5, 6, 8, 12, 17]
        result = can_cross(stones)
        self.assertIsInstance(result, bool)